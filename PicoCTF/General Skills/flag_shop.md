# flag_shop
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: flag_shop
* Category: General Skills
* Points: 300
* Date: 31-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220331004941.png)

---
## Hints:
1. Two's complement can do some weird things when numbers get really big!

---
## Solution:
Connect to the service.

![](./attachments/Pasted%20image%2020220331005045.png)

We get presented with a shop selling flags, wonderful!

Let's check the different menus.

![](./attachments/Pasted%20image%2020220331005212.png)

Returns balance, currently `1100`.

![](./attachments/Pasted%20image%2020220331005529.png)

Two flags for sale. Sadly, the 1337 flag is too expensive.

Let's look at the other flag.

![](./attachments/Pasted%20image%2020220331005715.png)

Having the hints in mind, we might be able to break this with a really big number.

![](./attachments/Pasted%20image%2020220331010227.png)

We now have plenty of money to buy the 1337 flag.

![](./attachments/Pasted%20image%2020220331010444.png)

The 1337 flag is ours!

**Flag:** `picoCTF{m0n3y_bag5_9c5fac9b}`

---
**Tags:** [[PicoCTF]]