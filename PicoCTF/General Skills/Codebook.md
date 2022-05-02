# Codebook
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Codebook
* Category: General Skills
* Points: 100
* Date: 09-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220409223625.png)

---
## Hints:
1. On the webshell, use ls to see if both files are in the directory you are in
2. The str_xor function does not need to be reverse engineered for this challenge.

---
## Solution:
We need to download the two files to the same directory and execute the script.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ ll
total 8
-rw-r--r-- 1 kali kali   27 Apr  9 16:35 codebook.txt
-rw-r--r-- 1 kali kali 1278 Apr  9 16:35 code.py

┌──(kali㉿kali)-[~/Downloads]
└─$ python3 code.py
picoCTF{c0d3b00k_455157_7d102d7a}
```

We got the flag!

**Flag:** `picoCTF{c0d3b00k_455157_7d102d7a}`

---
**Tags:** [[PicoCTF]]