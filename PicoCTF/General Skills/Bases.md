# Bases
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Bases
* Category: General Skills
* Points: 100
* Date: 30-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
We need to decode a string which is encoded in an unknown base.

![](./attachments/Pasted%20image%2020220330170134.png)

---
## Hints:
1. Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

---
## Solution:
Bases can quickly be decoded in bash by using `echo` to pipe the base encoded string on to either `Base32` or `Base64`. We'll try base 32 first.

![](./attachments/Pasted%20image%2020220330170814.png)

That didn't work. Let's try base 64.

![](./attachments/Pasted%20image%2020220330170900.png)

That's better, we got the flag.

**Flag:** `picoCTF{l3arn_th3_r0p35}`

---
## Alternate solution/Exstra:
 [CyberChef](https://gchq.github.io/CyberChef/) can also quickly solve this problem.
 
![](./attachments/Pasted%20image%2020220330171501.png)

**Flag:** `picoCTF{l3arn_th3_r0p35}`

---
**Tags:** [[PicoCTF]] [[Base64]] [[Base32]] [[echo]] [[bash]] [[|]]