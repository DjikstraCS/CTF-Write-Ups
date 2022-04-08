# information
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: information
* Category: Forensics
* Points: 10
* Date: 09-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220409002714.png)

---
## Hints:
1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}

---
## Solution:
The Image:

![](./attachments/Pasted%20image%2020220409002829.png)

The usual wonder command `cat -n cat.jpg | grep Pico` returns something on line `1` and `14`. There is something that looks like base64, let's see if it's the flag.

![](./attachments/Pasted%20image%2020220409011715.png)

Doesn't look like anything useful. Let's get a closer look at the file, we can use `less` to view it in an easy way.

![](./attachments/Pasted%20image%2020220409011339.png)

![](./attachments/Pasted%20image%2020220409011309.png)

Another base64 value, we need to try that one too.

![](./attachments/Pasted%20image%2020220409011529.png)

There we go!

**Flag:** `picoCTF{the_m3tadata_1s_modified}`

---
**Tags:** [[PicoCTF]] [[bash]] [[cat]] [[grep]] [[|]] [[less]] [[Base64]]