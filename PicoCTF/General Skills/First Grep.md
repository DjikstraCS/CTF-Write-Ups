# First Grep
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: First Grep
* Category: General Skills
* Points: 100
* Date: 30-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
We need to find the flag in the file.

![](./attachments/Pasted%20image%2020220330171825.png)

---
## Hints:
1. grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

---
## Solution:
The string we are looking for can be found by `grep`. But first we need to parse/pipe the content of the file to it by using a combination of `cat` and `|`.

![](./attachments/Pasted%20image%2020220330172010.png)

**Flag:** `picoCTF{grep_is_good_to_find_things_dba08a45}`

---
