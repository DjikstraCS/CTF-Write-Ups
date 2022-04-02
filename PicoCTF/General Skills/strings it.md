# strings it
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: strings it
* Category: General Skills
* Points: 100
* Date: 30-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
We need to find the flag in a file without running it.

![](./attachments/Pasted%20image%2020220330163647.png)

---
## Hints:
1. [strings](https://linux.die.net/man/1/strings)

---
## Solution:
We can use the `strings` BASH command to exstract all strings in a file. Here we are looking for a specific string, so we need to parse se output of `strings` on to `grep` so we can search for that specific string. In order to parse or pipe det output we use `|`.

![](./attachments/Pasted%20image%2020220330164418.png)

**Flag:** `picoCTF{5tRIng5_1T_827aee91}`

---
