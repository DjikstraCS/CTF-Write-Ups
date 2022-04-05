# Obedient Cat
* Source: PicoCTF 
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge:  Obedient Cat
* Category: General Skills
* Points: 5
* Date: 29-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:

Looks like we need to download the flag file and open it in order to extract the flag.

![](./attachments/Pasted%20image%2020220329124831.png)

---
## Solution:

Download the flag file using your browser.

Open a terminal and navigate to the Downloads folder, using `cd`.

Use `ll` to view the content of the folder.

![](./attachments/Pasted%20image%2020220329130407.png)

Use `cat` to show the content of the file:

![](./attachments/Pasted%20image%2020220329130444.png)

And there it is.

**Flag:** `picoCTF{s4n1ty_v3r1f13d_1a94e0f9}`


---
**Tags:** [[PicoCTF]] [[bash]] [[cat]] [[cd]] [[ll]]