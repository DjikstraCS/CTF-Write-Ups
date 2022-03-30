# Nice netcat...
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Nice netcat...
* Category: General Skills
* Points: 15
* Date: 30-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
The description is cryptic. Let's connect and see what happens.

![](./attachments/Pasted%20image%2020220330081039.png)

---
## Solution:
Connect to the server using `nc <DOMAIN> <PORT>`.

![](./attachments/Pasted%20image%2020220330081320.png)

The server returns a list of numbers.

Non of the values are 128 and above, so this is likely ASCII characters.

To convert them into ASCII we can use this valuable web resource:

* Link: [CyberChef](https://gchq.github.io/CyberChef/)

Because we are most likely dealing with character code, we type `char` into the Operations field and select 'From Charcode'. Furthermore we need to set the base. The numbers we have look like normal base 10 so let's try that.

![](./attachments/Pasted%20image%2020220330082953.png)

Success! We have the flag.

**Flag: picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}**

---
