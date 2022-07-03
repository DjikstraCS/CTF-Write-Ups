# Attacking Web Applications with Ffuf
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Attacking Web Applications with Ffuf
* Tier: 0
* Difficulty: Easy
* Category: Offensive
* Time estimate: 5 hours
* Date: 02-07-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Directory Fuzzing
### Question:
![](./attachments/Pasted%20image%2020220702112151.png)

*Hint: All lowercase!*

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://134.209.17.29:30097/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://134.209.17.29:30097/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

# directory-list-2.3-small.txt [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 62ms]
forum                   [Status: 301, Size: 323, Words: 20, Lines: 10, Duration: 59ms]
(...)
```

**Answer:** `forum`

---
## Page Fuzzing
### Question:
![](./attachments/Pasted%20image%2020220702112306.png)

*Hint: Don't forget to remove copyrights from the wordlist, they clutter the results!*

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://134.209.17.29:30097/blog/FUZZ.php

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://134.209.17.29:30097/blog/FUZZ.php
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

# Priority-ordered case-sensitive list, where entries were found [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 67ms]
# Attribution-Share Alike 3.0 License. To view a copy of this [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 67ms]
# Suite 300, San Francisco, California, 94105, USA. [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 68ms]
#                       [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 68ms]
# Copyright 2007 James Fisher [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 984ms]
index                   [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 1986ms]
home                    [Status: 200, Size: 1046, Words: 438, Lines: 58, Duration: 2983ms]
(...)
```

![](./attachments/Pasted%20image%2020220702114317.png)

TIP: The comments in the word list can be removed with:
```bash
sudo sed -i 's/^\#.*$//g' /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt && sudo sed -i '/^$/d' /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
```

**Answer:** `HTB{bru73_f0r_c0mm0n_p455w0rd5}`

---
## Recursive Fuzzing
### Question:
![](./attachments/Pasted%20image%2020220702112438.png)

*Hint: Be recursive!*

```
──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://206.189.26.97:31390/FUZZ -recursion -recursion-depth 1 -e .php -v

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://206.189.26.97:31390/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
 :: Extensions       : .php 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

[Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 66ms]
| URL | http://206.189.26.97:31390/# on at least 3 different hosts
    * FUZZ: # on at least 3 different hosts
(...)
```

![](./attachments/Pasted%20image%2020220702115220.png)

**Answer:** `HTB{fuzz1n6_7h3_w3b!}`

---
## Sub-domain Fuzzing
### Question:
![](./attachments/Pasted%20image%2020220702112530.png)

*Hint: Write the answer as '*.hackthebox.eu'*

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://FUZZ.hackthebox.eu/

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://FUZZ.hackthebox.eu/
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

dev                     [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 75ms]
forum                   [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 76ms]
www                     [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 91ms]
mail                    [Status: 301, Size: 236, Words: 9, Lines: 7, Duration: 76ms]
forums                  [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 66ms]
api                     [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 135ms]
app                     [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 76ms]
store                   [Status: 301, Size: 91, Words: 5, Lines: 1, Duration: 217ms]
(...)
```

**Answer:** `store.hackthebox.eu`

---
## Filtering Results
### Question:
![](./attachments/Pasted%20image%2020220702112616.png)

*Hint: Make sure you are filtering correctly! Write the answer as '*.academy.htb'.*

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://206.189.26.97:31844/ -H 'Host: FUZZ.academy.htb' -fs 986

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://206.189.26.97:31844/
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Header           : Host: FUZZ.academy.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 986
________________________________________________

test                    [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 3683ms]
admin                   [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 4687ms]
:: Progress: [4989/4989] :: Job [1/1] :: 622 req/sec :: Duration: [0:00:11] :: Errors: 0 ::
```

**Answer:** `test.academy.htb`

---
## Parameter Fuzzing - GET
### Question:
![](./attachments/Pasted%20image%2020220702112705.png)

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:30006/admin/admin.php?FUZZ=key -fs 798

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://admin.academy.htb:30006/admin/admin.php?FUZZ=key
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 798
________________________________________________

user                    [Status: 200, Size: 783, Words: 221, Lines: 54, Duration: 65ms]
:: Progress: [6453/6453] :: Job [1/1] :: 638 req/sec :: Duration: [0:00:10] :: Errors: 0 ::
```

**Answer:** `user`

---
## Value Fuzzing
### Question:
![](./attachments/Pasted%20image%2020220702112731.png)

*Hint: It is in the form of HTB{flag},*

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w ids.txt:FUZZ -u http://admin.academy.htb:31005/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs 768

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : POST
 :: URL              : http://admin.academy.htb:31005/admin/admin.php
 :: Wordlist         : FUZZ: ids.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : id=FUZZ
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 768
________________________________________________

73                      [Status: 200, Size: 787, Words: 218, Lines: 54, Duration: 69ms]
:: Progress: [1000/1000] :: Job [1/1] :: 607 req/sec :: Duration: [0:00:01] :: Errors: 0 ::
```

```
┌──(kali㉿kali)-[~]
└─$ curl http://admin.academy.htb:31005/admin/admin.php -X POST -d 'id=73' -H 'Content-Type: application/x-www-form-urlencoded'
<div class='center'><p>HTB{p4r4m373r_fuzz1n6_15_k3y!}</p></div>
<html>
(...)
```

**Answer:** `HTB{p4r4m373r_fuzz1n6_15_k3y!}`

---
## Skills Assessment - Web Fuzzing
### Question 1:
![](./attachments/Pasted%20image%2020220702112830.png)

Sub-domain scan:
```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://FUZZ.academy.htb:30795/

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://FUZZ.academy.htb:30795/
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

:: Progress: [4989/4989] :: Job [1/1] :: 98 req/sec :: Duration: [0:00:34] :: Errors: 4989 ::
```

Nothing.

Vhost scan:
```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:30795/ -H 'Host: FUZZ.academy.htb' -fs 985

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://academy.htb:30795/
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Header           : Host: FUZZ.academy.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 985
________________________________________________

test                    [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 72ms]
archive                 [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 66ms]
faculty                 [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 63ms]
:: Progress: [4989/4989] :: Job [1/1] :: 609 req/sec :: Duration: [0:00:08] :: Errors: 0 ::
```

**Answer:** `test archive faculty`

### Question 2:
![](./attachments/Pasted%20image%2020220702112854.png)

*Hint: Don't forget to add the sub-domains you found to your hosts file, and then run the scan on all of them.*

PHP it is.

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://faculty.academy.htb:31361/indexFUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://faculty.academy.htb:31361/indexFUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

.php                    [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 63ms]
.php7                   [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 3702ms]
.phps                   [Status: 403, Size: 287, Words: 20, Lines: 10, Duration: 4709ms]
:: Progress: [39/39] :: Job [1/1] :: 13 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
```


**Answer:** ``

### Question 3:
![](./attachments/Pasted%20image%2020220702112950.png)

*Hint: Run a recursive scan on all sub-domains you found, and use all of the extensions you found. Use 'PORT' instead of the port shown above, like http://xxxxx.academy.htb:PORT/xxxxxxx ..etc*

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://faculty.academy.htb:31361/courses/FUZZ -recursion -recursion-depth 5 -e .php7,.php,.phps -v -fs 287

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://faculty.academy.htb:31361/courses/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
 :: Extensions       : .php7 .php .phps 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 287
________________________________________________

[Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 63ms]
| URL | http://faculty.academy.htb:31361/courses/index.php
    * FUZZ: index.php

[Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 67ms]
| URL | http://faculty.academy.htb:31361/courses/index.php7
    * FUZZ: index.php7

[Status: 200, Size: 774, Words: 223, Lines: 53, Duration: 72ms]
| URL | http://faculty.academy.htb:31361/courses/linux-security.php7
    * FUZZ: linux-security.php7
```

![](./attachments/Pasted%20image%2020220702141921.png)

**Answer:** `http://faculty.academy.htb:PORT/courses/linux-security.php7`

### Question 4:
![](./attachments/Pasted%20image%2020220702113023.png)

*Hint: Don't forget to try out both parameter fuzzing methods we learned! Also, don't forget to set the appropriate header flags for 'ffuf'.*

GET method:
```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://faculty.academy.htb:30666/courses/linux-security.php7?FUZZ=key -fs 774

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://faculty.academy.htb:30666/courses/linux-security.php7?FUZZ=key
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 774
________________________________________________

user                    [Status: 200, Size: 780, Words: 223, Lines: 53, Duration: 61ms]
:: Progress: [6453/6453] :: Job [1/1] :: 618 req/sec :: Duration: [0:00:10] :: Errors: 0 ::
```

POST method:
```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://faculty.academy.htb:30666/courses/linux-security.php7 -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs 774

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : POST
 :: URL              : http://faculty.academy.htb:30666/courses/linux-security.php7
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : FUZZ=key
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 774
________________________________________________

user                    [Status: 200, Size: 780, Words: 223, Lines: 53, Duration: 64ms]
username                [Status: 200, Size: 781, Words: 223, Lines: 53, Duration: 66ms]
:: Progress: [6453/6453] :: Job [1/1] :: 622 req/sec :: Duration: [0:00:10] :: Errors: 0 ::
```

**Answer:** `user username`

### Question 5:
![](./attachments/Pasted%20image%2020220702113035.png)

*Hint: Try to find a good wordlist from 'seclists'. Once you find a working value, use 'curl' to send a POST request with the value to get the flag.*

```
┌──(kali㉿kali)-[~]
└─$ curl http://faculty.academy.htb:30666/courses/linux-security.php7 -X POST -d 'username=harry' -H 'Content-Type: application/x-www-form-urlencoded'
<div class='center'><p>HTB{w3b_fuzz1n6_m4573r}</p></div>
<html>
(...)
```

**Answer:** `HTB{w3b_fuzz1n6_m4573r}`

---
**Tags:** [[Hack The Box Academy]]