# plumbing
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: plumbing
* Category: General Skills
* Points: 200
* Date: 31-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:

![](./attachments/Pasted%20image%2020220331003640.png)

---
## Hints:
1. Remember the flag format is picoCTF{XXXX}
2. What's a pipe? No not that kind of pipe... [This kind](http://www.linfo.org/pipes.html)

---
## Solution:
First we need to connect to the service.

![](./attachments/Pasted%20image%2020220331004216.png)

We get a very long output.

![](./attachments/Pasted%20image%2020220331004302.png)

Let's `|` the output to `grep` so we can search for the flag.

![](./attachments/Pasted%20image%2020220331004506.png)



**Flag:** `picoCTF{digital_plumb3r_06e9d954}`

---
