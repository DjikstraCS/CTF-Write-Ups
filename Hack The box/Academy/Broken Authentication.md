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
## 
### Question 1:
![](./attachments/Pasted%20image%2020220714094738.png)

*Hint: Try to generate some failed login attempts.*

**Answer:** `40`

### Question 2:
![](./attachments/Pasted%20image%2020220714094940.png)

*Hint: This web server doesn't trust your IP!*

![](Pasted%20image%2020220724155629.png)

**Answer:** `HTB{127001>31337}`

---
## Bruteforcing Usernames
### Question 1:
![](./attachments/Pasted%20image%2020220714095111.png)

*Hint: Try a short username wordlist from a resource covered in this section.*

**Answer:** `puppet`

### Question 2:
![](./attachments/Pasted%20image%2020220714095158.png)

*Hint: Read the source of every response.*

**Answer:** `ansible`

### Question 3:
![](./attachments/Pasted%20image%2020220714095208.png)

*Hint: The timing.py script is a good starting point!*

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

**Answer:** ``

---
## Predictable Reset Token
### Question 1:
![](./attachments/Pasted%20image%2020220714095614.png)

*Hint: Convert the displayed date to epoch time in milliseconds and use it in the script you will create.*

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