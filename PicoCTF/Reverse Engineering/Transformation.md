# Transformation
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Transformation
* Category: Reverse Engineering
* Points: 20
* Date: 09-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220409000204.png)

---
## Hints:
1. You may find some decoders online

---
## Solution:
We need to decode the text.

![](./attachments/Pasted%20image%2020220409000311.png)

We can use [CyberChef's](https://gchq.github.io/CyberChef) magic function to detect the encoding.

![](./attachments/Pasted%20image%2020220409001854.png)

Alternatively, we can use [Universal Cyrillic decoder](https://2cyr.com/decode/?lang=en) to decode the text.

![](./attachments/Pasted%20image%2020220409000603.png)

**Flag:** `picoCTF{16_bits_inst34d_of_8_75d4898b}`

---
**Tags:** [[PicoCTF]]