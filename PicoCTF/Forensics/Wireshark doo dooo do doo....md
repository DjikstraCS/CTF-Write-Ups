# Wireshark doo dooo do doo...
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Wireshark doo dooo do doo...
* Category: Forensics
* Points: 50
* Date: 29-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220411215934.png)

---
## Solution:
The file in Wireshark:

![](./attachments/Pasted%20image%2020220411220148.png)

987 packets to look through... Let's make this a bit easier by grouping the packets into individual streams, it will be much easier to see what is important because we get the context of every connection.

![](./attachments/Pasted%20image%2020220411220341.png)

Here we can see the first stream, nothing interesting though.

![](./attachments/Pasted%20image%2020220411221030.png)

When we get to stream 5 we find something. Someone made a GET request and got an answer. It looks like an encrypted flag.

![](./attachments/Pasted%20image%2020220411221207.png)

[Dcode](https://www.dcode.fr/cipher-identifier) can help us identify the cipher used.

![](./attachments/Pasted%20image%2020220411222533.png)

It must be ROT-13.

![](./attachments/Pasted%20image%2020220411222641.png)

Correct! We got the flag.

**Flag:** `picoCTF{p33kab00_1_s33_u_deadbeef}`

---
**Tags:** [[PicoCTF]]