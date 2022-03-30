# Static ain't always noise
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Static ain't always noise
* Category: General Skills
* Points: 20
* Date: 30-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
Looks like we have to disassemble a binary.

We've been given a BASH script to help us.

![](./attachments/Pasted%20image%2020220330085052.png)

---
## Solution:
First let's look at the BASH script.

![](./attachments/Pasted%20image%2020220330085850.png)

Looks like the script disassembles the binary and prints the ".text" section of it.

Now that we know the syntax of the script we can try it out.

![](./attachments/Pasted%20image%2020220330090714.png)

We get a lot of data, but no flag.

The `-j .text` argument limits the output to only ".text" section of the binary. Let's try and run the script again without it.

![](./attachments/Pasted%20image%2020220330101158.png)

![](./attachments/Pasted%20image%2020220330094515.png)

Looking at the output we can see that we have a section called `<flag>`. Let's see if anything is hiding in those hex values.

Using [CyberChef](https://gchq.github.io/CyberChef/) to bake the hex values gives us the flag!

![](./attachments/Pasted%20image%2020220330094550.png)

**Flag: picoCTF{d15a5m_t34s3r_f5aeda17}**

---
## Alternate solution:
The flag is visible in clear text in the static file so in stead of using the BASH script to disassmble the binary and baking the hex values, we can just get it directly from there.

Using `cat` to output the content of the file, `|` to pipe the output to grep and finally `grep -a` in order to search for the string 'pico'.

![](./attachments/Pasted%20image%2020220330095650.png)

`strings` will yield the same result:

![](./attachments/Pasted%20image%2020220330100715.png)

**Flag: picoCTF{d15a5m_t34s3r_f5aeda17}**

---
