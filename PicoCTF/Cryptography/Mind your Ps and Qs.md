# Mind your Ps and Qs
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Mind your Ps and Qs
* Category: Cryptography
* Points: 20
* Date: 09-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220409112521.png)

---
## Hints:
1. Bits are expensive, I used only a little bit over 100 to save money

---
## Solution:
The values given:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ cat values
Decrypt my super sick RSA:
c: 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n: 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e: 65537  
```

If we go to [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Decryption), we can find the decryption function of RSA:

![](./attachments/Pasted%20image%2020220409163036.png)

In order to decrypt, we need to find the value of `d`.

Again, [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Decryption) can help us out:

![](./attachments/Pasted%20image%2020220409114758.png)

We could find it by solving `1 = (e * d) mod λ(n)` for `d` using [WolframAlpha](https://www.wolframalpha.com), but the values we are dealing with are too big. Let's have a closer look at how to decrypt RSA.

![](./attachments/Pasted%20image%2020220409145855.png)

We need to find the value of `λ(n)`, also known as `phi` in order to calculate `d`. The only way to do this is to find `p` and `q` and calculate `λ(n)` based on them.

Although the values are too big for [WolframAlpha](https://www.wolframalpha.com), they are still pretty small. We can either use [Aplertron's Integer factorization calculator](https://www.alpertron.com.ar/ECM.HTM) to factorize `p` and `q`, or we can look in a database like [factordb](http://factordb.com/) to see if someone else has already factorized it.

![](./attachments/Pasted%20image%2020220409142802.png)

![](./attachments/Pasted%20image%2020220409142841.png)

Great! Now we have all the values we need to make the final decoding using Python.

```py
Python 3.9.10
>>> import math
>>> p = 2434792384523484381583634042478415057961
>>> q = 650809615742055581459820253356987396346063
>>> c = 964354128913912393938480857590969826308054462950561875638492039363373779803642185
>>> n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
>>> e = 65537
>>> phi = math.lcm(p-1,q-1) # Same as phi = (p-1)*(q-1)
>>> d = pow(e,-1,phi) # Inverse pow
>>> m = pow(c,d,n) # Same as m = c^d % n
>>> bytes.fromhex(hex(m)[2:]) # Convert message to bytes

b'picoCTF{sma11_N_n0_g0od_73918962}' # Flag!
```

And there we have it, the decrypted message containing our flag.

**Flag:** `picoCTF{sma11_N_n0_g0od_73918962}`

---
## Extra:
[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) is a helpful tool that can solve this problem instantly.

---
**Tags:** [[PicoCTF]]