# Tab, Tab, Attack
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Tab, Tab, Attack
* Category: General Skills
* Points: 20
* Date: 30-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
We need to find a flag that is burried in folders.

Using 'Tab' to auto-complete is going to be crucial if we don't want to waste our life away.

![](./attachments/Pasted%20image%2020220330103742.png)

---
## Hints:
 1. After unzip'ing, this problem can be solved with 11 button-presses...(mostly Tab)...

---
## Solution:

First we need to unzip the compressed folders.

![](./attachments/Pasted%20image%2020220330104431.png)

We need to open the file to see it's content.

There is a lot of ways to do this, the shortest I found using basic BASH commands is the following combination which requires luck to hit:

`'c'` + `'a'` + `'t'` + `SPACE` +`'A'` + `Tab(HOLD)` + `ENTER` + `Tab(HOLD)` + `ENTER` = 7 clicks

![](./attachments/Pasted%20image%2020220330150739.png)

And there is the flag.

**Flag: picoCTF{l3v3l_up!_t4k3_4_r35t!_6f332f10}**

---
## Extra:
If you ever encounter unmanageable file structures `tree` is a really useful tool.

![](./attachments/Pasted%20image%2020220330151715.png)

---
