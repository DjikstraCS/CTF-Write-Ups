# Warmed up
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Warmed up
* Category: General Skills
* Points: 50
* Date: 30-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
We need to convert a value from hex to decimal.

Note the hint that we need to construct the flag ourselves this time.

![](./attachments/Pasted%20image%2020220330160507.png)

---
## Hints:
1. Submit your answer in our flag format. For example, if your answer was '22', you would submit 'picoCTF{22}' as the flag.

---

## Solution:
A hex (base 16) value can easily be converted into a int (base 10) in Python with `int(hex, 16)`. 

![](./attachments/Pasted%20image%2020220330160805.png)

And that is our flag value!

**Flag:** `picoCTF{61}`

---
