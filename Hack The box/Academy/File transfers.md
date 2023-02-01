# File transfers
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: File transfers
* Tier: Tier 0
* Difficulty: Medium
* Category: Offensive
* Time estimate: 3 hours
* Date: 30-01-2023
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Windows File Transfer Methods
### Question:
![](./attachments/Pasted%20image%2020230127185922.png)

```
┌──(kali㉿kali)-[~/HTB]
└─$ wget http://10.129.187.68/flag.txt
--2023-01-27 13:59:40--  http://10.129.187.68/flag.txt
Connecting to 10.129.187.68:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 32 [text/plain]
Saving to: ‘flag.txt’

flag.txt                                  100%[===================================================================================>]      32  --.-KB/s    in 0s      

2023-01-27 13:59:40 (4.51 MB/s) - ‘flag.txt’ saved [32/32]

                                                                                                                                                                      
┌──(kali㉿kali)-[~/HTB]
└─$ cat flag.txt
b1a4ca918282fcd96004565521944a3b
```

**Answer:** `b1a4ca918282fcd96004565521944a3b`

### Question:
![](./attachments/Pasted%20image%2020230127185932.png)

Download the `upload_win.zip` file.

Copy the file to server directory and start the Python server.

```
┌──(kali㉿kali)-[~/HTB]
└─$ mv ~/Downloads/upload_win.zip ~/HTB/FileTransfers/winFileTransferMethods

┌──(kali㉿kali)-[~/HTB/FileTransfers/winFileTransferMethods]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

Now download and hash the file on the Windows machine.

```
PS C:\Users\htb-student\Documents> wget http://10.10.15.74:8000/upload_win.zip -OutFile upload_win.zip
PS C:\Users\htb-student\Documents> dir


    Directory: C:\Users\htb-student\Documents


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        1/27/2023  11:29 AM            194 upload_win.zip
```

Unzip the file.

![](./attachments/Pasted%20image%2020230127204451.png)

Use `hasher` to get the hash of the file.

```
PS C:\Users\htb-student\Documents> dir
    Directory: C:\Users\htb-student\Documents

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        1/27/2023  11:29 AM                upload_win
-a----        1/27/2023  11:29 AM            194 upload_win.zip

PS C:\Users\htb-student\Documents> cd .\upload_win\
PS C:\Users\htb-student\Documents\upload_win> hasher upload_win.txt
f458303ea783c224c6b4e7ef7f17eb9d
```

**Answer:** `f458303ea783c224c6b4e7ef7f17eb9d`

---
## Linux File Transfer Methods
### Question 1:
![](./attachments/Pasted%20image%2020230130110116.png)

```
┌──(kali㉿kali)-[~/HTB]
└─$ curl 10.129.219.107/flag.txt                         
5d21cf3da9c0ccb94f709e2559f3ea50
```

**Answer:** `5d21cf3da9c0ccb94f709e2559f3ea50`

### Question 2:
![](./attachments/Pasted%20image%2020230130110207.png)
*Hint: You can use gunzip to extract the file with the command: gunzip -S .zip upload_nix.zip*


```
┌──(kali㉿kali)-[~/HTB/FileTransfers/linFileTransferMethods]
└─$ scp upload_nix.zip htb-student@10.129.219.107:/home/htb-student/
The authenticity of host '10.129.219.107 (10.129.219.107)' can't be established.
ED25519 key fingerprint is SHA256:z4rcb3qcf0IdRnoTBNEJ4i8TlDystDA4uOJFxVcb41E.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.219.107' (ED25519) to the list of known hosts.
htb-student@10.129.219.107's password: 
upload_nix.zip                                                                                                                      100%  194     6.4KB/s   00:00    
```

File uploadet.

```
┌──(kali㉿kali)-[~/HTB/FileTransfers/linFileTransferMethods]
└─$ sudo ssh htb-student@10.129.219.107                             
[sudo] password for kali: 
The authenticity of host '10.129.219.107 (10.129.219.107)' can't be established.
ED25519 key fingerprint is SHA256:z4rcb3qcf0IdRnoTBNEJ4i8TlDystDA4uOJFxVcb41E.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.219.107' (ED25519) to the list of known hosts.
htb-student@10.129.219.107's password: 
Welcome to Ubuntu 20.04 LTS (GNU/Linux 5.4.0-47-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon 30 Jan 2023 10:12:14 AM UTC

  System load:             0.0
  Usage of /:              26.5% of 15.68GB
  Memory usage:            10%
  Swap usage:              0%
  Processes:               141
  Users logged in:         0
  IPv4 address for ens192: 10.129.219.107
  IPv6 address for ens192: dead:beef::250:56ff:feb9:b572


74 updates can be installed immediately.
0 of these updates are security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Wed Sep  9 22:42:43 2020 from 10.10.14.4
htb-student@nix04:~$ ls
upload_nix.zip
htb-student@nix04:~$ unzip upload_nix.zip 

Command 'unzip' not found, but can be installed with:

apt install unzip
Please ask your administrator.

htb-student@nix04:~$ gunzip -S .zip upload_nix.zip
htb-student@nix04:~$ ls
upload_nix
htb-student@nix04:~$ hasher upload_nix
159cfe5c65054bbadb2761cfa359c8b0
```

**Answer:** `159cfe5c65054bbadb2761cfa359c8b0`

---
## 
### Question:


**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]