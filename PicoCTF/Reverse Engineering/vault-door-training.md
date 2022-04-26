# vault-door-training
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: vault-door-training
* Category: Reverse Engineering
* Points: 50
* Date: 08-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220408193215.png)

---
## Hints:
1. The password is revealed in the program's source code.

---
## Solution:
Ok, let's download the .java file and `cat | grep` it to see if the flag is clearly visible.

![](./attachments/Pasted%20image%2020220408193521.png)

Part of the flag is in there for sure, let's open the file in a friendly editor like gedit.

![](./attachments/Pasted%20image%2020220408193634.png)

![](./attachments/Pasted%20image%2020220408193730.png)

And there we have it!

**Flag:** `picoCTF{w4rm1ng_Up_w1tH_jAv4_eec0716b713}`

---
**Tags:** [[PicoCTF]] [[Bash]] [[cat]] [[|]] [[grep]] [[gedit]]