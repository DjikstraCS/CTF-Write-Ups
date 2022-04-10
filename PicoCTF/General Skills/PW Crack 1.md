# PW Crack 1
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: PW Crack 2
* Category: General Skills
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410113216.png)

---
## Hints:
1. To view the file in the webshell, do: $ nano level1.py
2. To exit nano, press Ctrl and x and follow the on-screen prompts.
3. The str_xor function does not need to be reverse engineered for this challenge.

---
## Solution:
We need do put the files in the same directory, fortunately this happens automatically if you just download them via the browser.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ ll
total 8
-rw-r--r-- 1 kali kali  30 Apr 10 05:33 level1.flag.txt.enc
-rw-r--r-- 1 kali kali 876 Apr 10 05:33 level1.py
```

Let's run the script and see what happens.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level1.py
Please enter correct password for flag: 1234
That password is incorrect
```

We need to find the password. If we open the script in a code friendly editor like `gedit` to have a closer look at how it validates the password, we can see that the password is hard-coded into the script in plain text. 

The password is `691d`.

![](./attachments/Pasted%20image%2020220410114001.png)

Let's try it out. 

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level1.py
Please enter correct password for flag: 691d
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_56891419}
```

And we get the flag!


**Flag:** `picoCTF{545h_r1ng1ng_56891419}`

---
**Tags:** [[PicoCTF]] [[Python]]