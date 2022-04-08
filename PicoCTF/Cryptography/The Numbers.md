# The Numbers
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: The Numbers
* Category: Cryptography
* Points: 50
* Date: 08-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220408194305.png)

---
## Hints:
1. The flag is in the format PICOCTF{}

---
## Solution:
'The numbers' are an image file with numbers, plus curly brackets, indicating it's a flag.

![](./attachments/Pasted%20image%2020220408194931.png)

Message in image: `16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }`

It's encrypted in a number substitution cipher. The number correlate to that letter in the alphabet. We can use this de decrypt it:

![](./attachments/Pasted%20image%2020220408200051.png)

**Flag:** `PICOCTF{thenumbersmason}`

---
**Tags:** [[PicoCTF]] [[number substitution]]