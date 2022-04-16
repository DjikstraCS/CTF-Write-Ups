# caesar
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: caesar
* Category: Cryptography
* Points: 100
* Date: 08-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220408202852.png)

---
## Hints:
caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)

---
## Solution:
This is the content of the message:

![](./attachments/Pasted%20image%2020220408203107.png)

We can decrypt it manually by pushing all letters in the massage by one place in the alphabet until we find something that makes sense.

Alternatively, we can use [dCode](https://www.dcode.fr/) to help us.

![](./attachments/Pasted%20image%2020220408203845.png)

'Crossing the rubicon' makes sense, it's a reference to Caesar crossing the river Rubicon back in 49 BCE on his way to Rome. We got the flag!

**Flag:** `picoCTF{crossingtherubiconzaqjsscr}`

---
**Tags:** [[PicoCTF]] [[dCode]]