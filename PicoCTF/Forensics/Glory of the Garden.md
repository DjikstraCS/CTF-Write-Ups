# Glory of the Garden
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Glory of the Garden
* Category: Forensics
* Points: 50
* Date: 08-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220408222710.png)

---
## Hints:
1. What is a hex editor?

---
## Solution:
We need to find the flag in this image: 

![](./attachments/Pasted%20image%2020220408222922.png)

A simple `cat garden.jpg | grep -a pico` gives us the flag!

![](./attachments/Pasted%20image%2020220408223232.png)

**Flag:** `picoCTF{more_than_m33ts_the_3y3657BaB2C}`

---
**Tags:** [[PicoCTF]]