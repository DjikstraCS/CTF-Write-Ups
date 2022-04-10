# PW Crack 2
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: PW Crack 2
* Category: General Skills
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410114742.png)

---
## Hints:
1. Does that encoding look familiar?
2. The str_xor function does not need to be reverse engineered for this challenge.

---
## Solution:
We need do put the files in the same directory, fortunately this happens automatically if you just download them via the browser.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ ll
total 8
-rw-r--r-- 1 kali kali  30 Apr 10 05:33 level2.flag.txt.enc
-rw-r--r-- 1 kali kali 876 Apr 10 05:33 level2.py
```

Let's run the script and see what happens.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level2.py
Please enter correct password for flag: 1234
That password is incorrect
```

We need to find the password. If we open the script in a code friendly editor like `gedit` to have a closer look at how it validates the password, we can see that the password is hard-coded into the script. 

![](./attachments/Pasted%20image%2020220410115347.png)

We can see the password is a simple string of python `chr()`'s. We can simply pass it on to the python interpreter to get it decoded.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3
```

```py
Python 3.9.10
>>> chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) 
'4ec9'
```

And there we have the password in clear text. Let's try it out. 

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level2.py
Please enter correct password for flag: 4ec9
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_9701e681}
```

And we get the flag!

**Flag:** `picoCTF{tr45h_51ng1ng_9701e681}`

---
**Tags:** [[PicoCTF]] [[Python]]