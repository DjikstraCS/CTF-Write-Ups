# Fawn
* Source:  [Hack the Box](https://hackthebox.com/)
* Challenge: Dancing
* Topic: [[FTP]]
* Difficulty: Very easy
* Date: 12-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What does the 3-letter acronym FTP stand for? 
 - **File Transfer Protocol**
2. What communication model does FTP use, architecturally speaking? 
- **Client-Server model**
3. What is the name of one popular GUI FTP program? 
- **FileZilla**
4. Which port is the FTP service active on usually?
- **21 TCP**
5. What acronym is used for the secure version of FTP? 
- **SFTP**
6. What is the command we can use to test our connection to the target? 
- **ping**
7. From your scans, what version is FTP running on the target? 
- **vsftpd 3.0.3**
8. From your scans, what OS type is running on the target?
- **Unix**

---
## Solution:
Get the flag from FTP Server:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo nmap -sV -p T:20,21 10.129.87.103
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-12 07:47 EDT
Nmap scan report for 10.129.87.103
Host is up (0.063s latency).

PORT   STATE  SERVICE  VERSION
20/tcp closed ftp-data
21/tcp open   ftp      vsftpd 3.0.3
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1.18 seconds

┌──(kali㉿kali)-[~/Downloads]
└─$ ftp 10.129.87.103
Connected to 10.129.87.103.
220 (vsFTPd 3.0.3)
Name (10.129.87.103:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||36440|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
226 Directory send OK.
ftp> get flag.txt
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||36066|)
150 Opening BINARY mode data connection for flag.txt (32 bytes).
100% |*************************************************|    32      416.66 KiB/s    00:00 ETA
226 Transfer complete.
32 bytes received in 00:00 (0.44 KiB/s)
ftp> exit
221 Goodbye.
                           
┌──(kali㉿kali)-[~/Downloads]
└─$ cat flag.txt
035db21c881520061c53e0536e44f815
```

**Flag:** `035db21c881520061c53e0536e44f815`

---
**Tags:** [[HackTheBox]]