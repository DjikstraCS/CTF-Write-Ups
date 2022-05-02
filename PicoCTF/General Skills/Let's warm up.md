# Let's warm up
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Let's warm up
* Category: General Skills
* Points: 50
* Date: 30-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
We need to convert a value from hex to ASCII.

Note the hint that we need to construct the flag ourselves this time.

![](./attachments/Pasted%20image%2020220330073925.png)

---
## Solution:
Unicode is ASCII compatible, so this is easily solved with the `chr()` function in Python.

![](./attachments/Pasted%20image%2020220330074257.png)

And that is our flag value!

**Flag:** `picoCTF{p}`

---
**Tags:** [[PicoCTF]]