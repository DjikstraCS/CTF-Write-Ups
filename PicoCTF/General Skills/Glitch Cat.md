# Glitch Cat
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Glitch Cat
* Category: General Skills
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:


---
## Hints:
1. ASCII is one of the most common encodings used in programming
2. We know that the glitch output is valid Python, somehow!
3. Press Ctrl and c on your keyboard to close your connection and return to the command prompt.

---
## Solution:
Connecting:

```console
┌──(kali㉿kali)-[~/pythonScripts]
└─$ nc saturn.picoctf.net 53933
'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
```

That output looks like python syntax. Let's give it to the Python3 interpreter.

```console
┌──(kali㉿kali)-[~/pythonScripts]
└─$ python3
Python 3.9.10
>>> 'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
'picoCTF{gl17ch_m3_n07_a4392d2e}'
```

And we got the flag!

**Flag:** `picoCTF{gl17ch_m3_n07_a4392d2e}`

---
**Tags:** [[PicoCTF]]