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
![](Pasted%20image%2020220409112521.png)

---
## Hints:
1. Bits are expensive, I used only a little bit over 100 to save money

---
## Solution:
The values given:

![](Pasted%20image%2020220409114333.png)

c: `964354128913912393938480857590969826308054462950561875638492039363373779803642185`

n: `1584586296183412107468474423529992275940096154074798537916936609523894209759157543`

e: `65537`

If we go to [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Decryption), we can find the decryption function of RSA:

![](Pasted%20image%2020220409163036.png)

In order to decrypt, we need to find the value of `d`.

Again, [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Decryption) can help us out:

![](Pasted%20image%2020220409114758.png)

`1 = (e * x) mod λ(n), solve for x`

We could find `d` by solving this equation using [WolframAlpha](https://www.wolframalpha.com), but the values we are dealing with are too big. Let's have a closer look at how to decrypt RSA.

![](Pasted%20image%2020220409145855.png)

We need to find the value of `λ(n)`, also known as 'phi'.  Since it is too much for [WolframAlpha](https://www.wolframalpha.com), the only way to do so is to find `p` and `q` and calculate it based on them.

Although the values are too big for [WolframAlpha](https://www.wolframalpha.com), they are still pretty small. We can either use [Aplertron's](https://www.alpertron.com.ar/ECM.HTM) Integer factorization calculator to factorize `p` and `q`, or we can look in a database like [factordb](http://factordb.com/) to see if someone else has already factorized it.

![](Pasted%20image%2020220409142802.png)

![](Pasted%20image%2020220409142841.png)

p: `2434792384523484381583634042478415057961`

q: `650809615742055581459820253356987396346063`

Great! Now we have all the values we need to make the final decoding using Python.

![](Pasted%20image%2020220409164327.png)

And we got the flag!

**Flag:** `picoCTF{sma11_N_n0_g0od_73918962}`

---
## Extra:
[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) is a helpful tool that can solve this problem instantly.

---
**Tags:** [[PicoCTF]] [[Aplertron]] [[WolframAlpha]] [[factordb]] [[RSA]] [[Python]]