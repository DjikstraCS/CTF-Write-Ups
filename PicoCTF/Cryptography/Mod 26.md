# Mod 26
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Mod 26
* Category: Cryptography
* Points: 10
* Date: 09-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220409012232.png)

---
## Hints:
1. This can be solved online if you don't want to do it by hand!

---
## Solution:
The flag is encrypted with ROT13, see [13](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/PicoCTF/Cryptography/13.md) for more detailed information about decoding it.

Encrypted flag: `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}`

Here we will just solve it quickly, giving it to [CyberChef](https://gchq.github.io/CyberChef/).

![](./attachments/Pasted%20image%2020220409012733.png)

**Flag:** `picoCTF{next_time_I'll_try_2_rounds_of_rot13_wqWOSBKW}`

---
**Tags:** [[PicoCTF]] [[CyberChef]] [[ROT13]]