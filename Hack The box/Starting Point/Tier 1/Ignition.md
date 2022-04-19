# Ignition
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Ignition
* Topic: [[PHP]] [[Web Fussing]] [[DNS]]
* Difficulty: Very easy
* Date: 15-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. Which service version is found to be running on port 80? 
 - **nginx 1.14.2**
2. What is the 3-digit HTTP status code returned when you visit http://{machine IP}/? 
- **302**
3. What is the virtual host name the webpage expects to be accessed by? 
- **/etc/hosts**
4. What is the full path to the file on a Linux computer that holds a local list of domain name to IP address pairs? 
- **/etc/hosts**
5. What is the full URL to the Magento login page? 
- **http://ignition.htb/admin**
6. What password provides access as admin to Magento? 
- **qwerty123**

---
## Flag:
Nmap:

```console
┌──(kali㉿kali)-[~]
└─$ nmap -n -sC -sV 10.129.94.130
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-15 11:15 EDT
Nmap scan report for 10.129.94.130
Host is up (0.069s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.2
|_http-title: Did not follow redirect to http://ignition.htb/
|_http-server-header: nginx/1.14.2

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.68 seconds
```

It's a simple web sever hosting HTTP on port 80. When we visit it, we get an error. 

We typed in the IP, and we are being redirected to a domain name like expected, but it can't be found.

![](./attachments/Pasted%20image%2020220415173436.png)

This is a sign that 'Virtual Hosting' technology is being used. If we type the domain name of the page provided into the URL, we get the same error. The host must be isolated, which means there are no larger DNS servers referring to it.

What the browser is trying to do is find out what IP address is connected to the domain `ignition.htb`. But we already know the IP, so in order to solve this connection issue, we just have to tell the browser.

Before we do that we can confirm with a simple `curl` request.

```
┌──(kali㉿kali)-[~]
└─$ curl -v 10.129.1.27  
*   Trying 10.129.1.27:80...
* Connected to 10.129.1.27 (10.129.1.27) port 80 (#0)
> GET / HTTP/1.1
> Host: 10.129.1.27
> User-Agent: curl/7.82.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 302 Found
< Server: nginx/1.14.2
< Date: Fri, 15 Apr 2022 18:40:09 GMT
< Content-Type: text/html; charset=UTF-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< Set-Cookie: PHPSESSID=l8d8f1j49hbirs1ms2hj1062id; expires=Fri, 15-Apr-2022 19:40:09 GMT; Max-Age=3600; path=/; domain=10.129.1.27; HttpOnly; SameSite=Lax
< Location: http://ignition.htb/
< Pragma: no-cache
< Cache-Control: max-age=0, must-revalidate, no-cache, no-store
< Expires: Thu, 15 Apr 2021 18:40:09 GMT

```

As expected, we can see that the host field is the IP and the location is the domain, it should have been the other way around.  

In order to make the browser create the connection between IP and domain name, we need to make an entry into our local DNS file located in `/etc/hosts`. This can be done with a simple command.

Command:

`echo "10.129.94.130 ignition.htb" | sudo tee -a /etc/hosts`

`echo`: Print this "x".

`|`: Take the output from cmd 1 and give it to cmd 2.

`tee`: Duplicate the output. Print one output in the console and in this case, append the other.

`-a`: Append the input into file.

```console
┌──(kali㉿kali)-[~]
└─$ echo "10.129.94.130 ignition.htb" | sudo tee -a /etc/hosts
[sudo] password for kali: 
10.129.94.130 ignition.htb
 
┌──(kali㉿kali)-[~]
└─$ cat /etc/hosts
127.0.0.1       localhost
127.0.1.1       kali

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

10.129.94.130 ignition.htb
```

The line has been added. Now we should be able to access the site.

![](./attachments/Pasted%20image%2020220415182317.png)

A simple site without much interaction. Let's use gobuster to enumerate the directories, so we can see if there are any other interesting URLs we can visit.

```console
┌──(kali㉿kali)-[~]
└─$ gobuster dir --url http://ignition.htb/ --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php,html
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://ignition.htb/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,html
[+] Timeout:                 10s
===============================================================
2022/04/15 12:32:07 Starting gobuster in directory enumeration mode
===============================================================
/index.php            (Status: 200) [Size: 25815]
/contact              (Status: 200) [Size: 28673]
/home                 (Status: 200) [Size: 25802]
/media                (Status: 301) [Size: 185] [--> http://ignition.htb/media/]
/0                    (Status: 200) [Size: 25803]                               
/catalog              (Status: 302) [Size: 0] [--> http://ignition.htb/]        
/admin                (Status: 200) [Size: 7095]                                
/static               (Status: 301) [Size: 185] [--> http://ignition.htb/static/]
/Home                 (Status: 301) [Size: 0] [--> http://ignition.htb/home]
```

We found `/admin`, it's probably a login page for the administration portal.

![](./attachments/Pasted%20image%2020220415183636.png)

A Magento site. We can't brute force it, since Magento has anti-bruteforce measures implemented.

All we can do from here is manually trying random usernames and passwords. This sounds like a huge amount of work, but by combining the [10 currently most used passwords](https://cybernews.com/best-password-managers/most-common-passwords/) with the default username "admin", we can greatly improve our chances and maybe get a lucky match.
 
 ![](Pasted%20image%2020220415185952.png)
 
User:pass `admin:qwerty123`

We got in, and the flag is in plain sight.

**Flag:** `797d6c988d9dc5865e010b9410f247e0`

---
**Tags:** [[HackTheBox]]