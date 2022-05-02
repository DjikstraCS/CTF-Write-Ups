# fixme1.py
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: fixme1.py
* Category: General Skills
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410004419.png)

---
## Hints:
1. Indentation is very meaningful in Python
2. To view the file in the webshell, do: $ nano fixme1.py
3. To exit nano, press Ctrl and x and follow the on-screen prompts.
4. The str_xor function does not need to be reverse engineered for this challenge.

---
## Solution:
When we run the script:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 fixme1.py
  File "/home/kali/Downloads/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
```

Looks like there is a indentation error. Let's open the script up in `nano` and have a look at line 20.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nano fixme1.py
```

The print line has a few spaces, we need to delete them like this:

![](./attachments/Pasted%20image%2020220410005046.png)

After saving by clicking `ctrl` + `x` -> `y` -> `Enter`, we can run the script again.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 fixme1.py
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}

```

And we get the flag!

**Flag:** `picoCTF{1nd3nt1ty_cr1515_09ee727a}`

---
**Tags:** [[PicoCTF]]