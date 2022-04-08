# Easy1
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Easy1
* Category: Cryptography
* Points: 100
* Date: 08-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](Pasted%20image%2020220408204942.png)

---
## Hints:
1. Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
2. Please use all caps for the message.

---
## Solution:
We need to decrypt the One-time pad:

Message: `UFJKXQZQUNB`

Key: `SOLVECRYPTO`

On [Wikipedia](https://en.wikipedia.org/wiki/One-time_pad#Example), we can see how to decrypt a one time pad using [modular addition](https://en.wikipedia.org/wiki/Modular_arithmetic). It's essentially the same as a standard [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

![](Pasted%20image%2020220408220014.png)

In our case, the calculations look like this:

26mod(`U = 20` - `S = 18`) = `C = 2` 
26mod(`F = 20` - `O = 14`) = `R = 17` 
26mod(`J = 9` - `L = 11`) = `Y = 24` 
(...)

Because we are lazy, we can use [dCode](https://www.dcode.fr/) or [CyberChef](https://gchq.github.io/CyberChef/) to solve the rest.

![](Pasted%20image%2020220408221029.png)

![](Pasted%20image%2020220408221216.png)

I have no idea what the table is for, if you know, please let me know.

**Flag:** `picoCTF{CRYPTOISFUN}`

---
**Tags:** [[PicoCTF]] [[One-time pad]] [[Vigenère]] [[mod26]]