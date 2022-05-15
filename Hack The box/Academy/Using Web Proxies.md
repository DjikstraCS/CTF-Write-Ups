# Using Web Proxies
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Using Web Proxies
* Tier: II
* Difficulty: Easy
* Category: Offensive
* Time estimate: 8 hours
* Date: 04-05-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Intercepting Web Requests
### Question:
![](./attachments/Pasted%20image%2020220502183409.png)

*Hint: You can inject the 'cat flag.txt' command.*

A simple website that can ping its own loop back addresses.

![](./attachments/Pasted%20image%2020220502185333.png)

We might be able to inject something with ZAP. Use the round red/green button to turn interception on and off, and the arrow next to it to forward the request. 

Let's try and inject `;ls`.

![](./attachments/Pasted%20image%2020220502190703.png)

Both ZAP returns a list of files, `flag.txt` looks interesting.

![](./attachments/Pasted%20image%2020220502185618.png)

We can try and inject `;cat flag.txt`.

![](./attachments/Pasted%20image%2020220502185832.png)

ZAP receives the flag in response!

![](./attachments/Pasted%20image%2020220502190311.png)


**Answer:** `HTB{1n73rc3p73d_1n_7h3_m1ddl3}`

---
## Repeating Requests
### Question:
![](./attachments/Pasted%20image%2020220502201501.png)

*Hint: It's not in the same directory!*

Open the build in Firefox browser in ZAP and enable capture. Insert `1` in the input field and hit the 'ping' button.

![](./attachments/Pasted%20image%2020220503211130.png)

The generated request will now appear in ZAP. By right-clicking, we can send it to the 'Request Editor'.

![](./attachments/Pasted%20image%2020220503211929.png)

By injecting `;cat /flag.txt` we get the flag.

![](./attachments/Pasted%20image%2020220503212247.png)

**Answer:** `HTB{qu1ckly_r3p3471n6_r3qu3575}`

---
## Encoding/Decoding
### Question:
![](./attachments/Pasted%20image%2020220503214303.png)

Inserting the given Base64 encoded value in the decoder tab in Burp, we can do multiple decodes in a row.

It was encoded with Base64 multiple times, and lastly URL encoded.

![](./attachments/Pasted%20image%2020220503214213.png)

**Answer:** `HTB{3nc0d1n6_n1nj4}`

---
## Proxying Tools
### Question:
![](./attachments/Pasted%20image%2020220503215021.png)

*Hint: It starts with 'msf'.*

Open Metasploit and find the `auxiliary/scanner/http/http_put` auxiliary. Set `RHOST` to `45.33.32.156` ([scanme.nmap.org](https://mxtoolbox.com/SuperTool.aspx?action=http%3a%2f%2fscanme.nmap.org%2f&run=toolpage#)) and `Proxies` to `http:127.0.0.1:8080`.

![](./attachments/Pasted%20image%2020220503234058.png)

**Answer:** `msf test file`

---
## Burp Intruder
### Question:
![](./attachments/Pasted%20image%2020220503234208.png)

*Hint: You can add .html after the position pointer (i.e., §1§.html), or you can use a Payload Processing rule to append .html to each line of payload.*

It will be too painful to solve this problem using Burp due to its speed limitations, `gobuster` is a much better tool for the job.

```bash
┌──(kali㉿kali)-[~]
└─$ gobuster dir --url http://157.245.40.78:30846/admin --wordlist /usr/share/seclists/Discovery/Web-Content/common.txt  -x html
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://157.245.40.78:30846/admin
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              html
[+] Timeout:                 10s
===============================================================
2022/05/08 08:10:05 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 281]
/.htpasswd            (Status: 403) [Size: 281]
/.hta.html            (Status: 403) [Size: 281]
/.htpasswd.html       (Status: 403) [Size: 281]
/.htaccess            (Status: 403) [Size: 281]
/.hta.txt             (Status: 403) [Size: 281]
/.htaccess.html       (Status: 403) [Size: 281]
/2010.html            (Status: 200) [Size: 987]
/index.html           (Status: 200) [Size: 0]

===============================================================
2022/05/08 08:11:52 Finished
===============================================================
```

We find a HTML file called `2010.html`, accessing it via `curl` reveals the flag. 

```bash
┌──(kali㉿kali)-[~]
└─$ curl http://157.245.40.78:30846/admin/2010.html                     
</html>
<!DOCTYPE html>
<head>
    (...)
</head>
<body>
    <div class="center">
        <p>HTB{burp_1n7rud3r_fuzz3r!}</p>
    </div>
</body>
</html>
```

**Answer:** `HTB{burp_1n7rud3r_fuzz3r!}`

---
## ZAP Fuzzer
### Question:
![](./attachments/Pasted%20image%2020220508143034.png)

*Hint: Use the 'MD5 Hash' processor and look for the page with a different content-length.*

Upon visiting `157.245.42.82:32348/skills/` we get a cookie in the form of an MD5 hash. When we refresh the page, we can see that the cookie is connected to the user `guest`.

![](./attachments/Pasted%20image%2020220508154608.png)

Finding the latest request in ZAP containing the cookie, we can right-click it and select `Fuzz...` under `Attack`.

![](./attachments/Pasted%20image%2020220508203322.png)

Select the cookie and click `Add...` -> `Add...` -> Type: `File` -> Select list.

![](./attachments/Pasted%20image%2020220508203903.png)

Next, we need to process the usernames into MD5 hashes, and then we can start fuzzing.

![](./attachments/Pasted%20image%2020220508204119.png)

In the results, one entry sticks out with a content-length of 450 bytes. Upon inspection of the response, we get the flag.

![](./attachments/Pasted%20image%2020220508204757.png)

**Answer:** `HTB{fuzz1n6_my_f1r57_c00k13}`

---
## ZAP Scanner
### Question:
![](./attachments/Pasted%20image%2020220508212022.png)

After doing a `Spider`, `Ajax Spider` and `Active` scan, we find four high-level vulnerabilities, all 'Remote OS Command Injections'.

![](./attachments/Pasted%20image%2020220508215555.png)

Clicking on the first one, we can see the payload.

![](./attachments/Pasted%20image%2020220508220618.png)

Using ZAP's Encode/Decode tool, we can construct a new payload. 

![](./attachments/Pasted%20image%2020220508220841.png)

Executing the payload, we get the flag.

![](./attachments/Pasted%20image%2020220508221127.png)

**Answer:** `HTB{5c4nn3r5_f1nd_vuln5_w3_m155}`

---
## Skills Assessment
### Question 1:
![](./attachments/Pasted%20image%2020220508222919.png)

*Hint: The button does not always give the flag from the first click, so try to make it easy to click it many times until you get the flag.*

The button is disabled, we need to delete `disabled=""`.

![](./attachments/Pasted%20image%2020220508225223.png)

When done, we can click the button and catch the request. To make it easier to repeat the request, we will right-click it and send it to the Request Editor.

![](./attachments/Pasted%20image%2020220508225554.png)

After sending the request a few times, we get a response with a size of `875` instead of `808`. Looking closer at the response, we get the flag.

**Answer:** `HTB{d154bl3d_bu770n5_w0n7_570p_m3}`

### Question 2:
![](./attachments/Pasted%20image%2020220508222932.png)

*Hint: For the first value, try multiple encoders until you get a clear text value.*

First we need to decode as `ASCII Hex`, then `Base64`.

![](./attachments/Pasted%20image%2020220508233850.png)

**Answer:** `3dac93b8cd250aa8c1a36fffc79a17a`

### Question 3:
![](./attachments/Pasted%20image%2020220508222944.png)

*Hint: With payload processing in Burp Intruder, first add the decoded cookie as a prefix to the payload, then encode the entire payload with the same encoding methods you identified earlier (in reverse order). The final payload should be 88 characters long, similar to the one from the previous question.*

First, we will use `alphanum-case.txt` from Seclist as our payloads.

![](./attachments/Pasted%20image%2020220509011045.png)

Then, we also need to add a few payload processing rules. 

First, add the MD5 hash with the missing last character as a prefix to the payload. Then we need to add the encoding in the reverse order of when we decoded it. So, first `Base64`, then `ASCII Hex`.

![](./attachments/Pasted%20image%2020220509011621.png)

Now we can start the attack.

In the first response, we get the flag.

![](./attachments/Pasted%20image%2020220509012115.png)

**Answer:** `HTB{burp_1n7rud3r_n1nj4!}`

### Question 4:
![](./attachments/Pasted%20image%2020220508222958.png)

*Hint: You may set any website as your RHOST.*

First, we need to launch Metasploit and find the scanner in question.

```bash
┌──(kali㉿kali)-[~]
└─$ sudo msfdb init && msfconsole
[sudo] password for kali: 
[+] Starting database
[i] The database appears to be already configured, skipping initialization

(...)

       =[ metasploit v6.1.37-dev                          ]
+ -- --=[ 2212 exploits - 1171 auxiliary - 396 post       ]
+ -- --=[ 615 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: Start commands with a space to avoid saving 
them to history


msf6 > search scanner coldfusion

Matching Modules
================

   #  Name                                                Disclosure Date  Rank    Check  Description
   -  ----                                                ---------------  ----    -----  -----------
   0  auxiliary/scanner/http/adobe_xml_inject                              normal  No     Adobe XML External Entity Injection
   1  auxiliary/scanner/http/coldfusion_locale_traversal                   normal  No     ColdFusion Server Check
   2  auxiliary/scanner/http/coldfusion_version                            normal  No     ColdFusion Version Scanner


Interact with a module by name or index. For example info 2, use 2 or use auxiliary/scanner/http/coldfusion_version

msf6 > use 1
msf6 auxiliary(scanner/http/coldfusion_locale_traversal) > options

Module options (auxiliary/scanner/http/coldfusion_locale_traversal):

   Name         Current Setting  Required  Description
   ----         ---------------  --------  -----------
   FILE                          no        File to retrieve
   FINGERPRINT  false            yes       Only fingerprint endpoints
   Proxies                       no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                        yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT        80               yes       The target port (TCP)
   SSL          false            no        Negotiate SSL/TLS for outgoing connections
   THREADS      1                yes       The number of concurrent threads (max one per host)
   VHOST                         no        HTTP server virtual host
```

We will set `RHOST` to `45.33.32.156` ([scanme.nmap.org](https://mxtoolbox.com/SuperTool.aspx?action=http%3a%2f%2fscanme.nmap.org%2f&run=toolpage#)) and `Proxies` to `http:127.0.0.1:8080`. When both are set, we can execute the exploit.

```bash
msf6 auxiliary(scanner/http/coldfusion_locale_traversal) > set RHOST 45.33.32.156
RHOST => 45.33.32.156
msf6 auxiliary(scanner/http/coldfusion_locale_traversal) > set Proxies http:127.0.0.1:8080
Proxies => http:127.0.0.1:8080
msf6 auxiliary(scanner/http/coldfusion_locale_traversal) > exploit
```

Looking at the intercepted request, we get the answer.

![](./attachments/Pasted%20image%2020220509003835.png)

**Answer:** `CFIDE`

---
**Tags:** [[Hack The Box Academy]]