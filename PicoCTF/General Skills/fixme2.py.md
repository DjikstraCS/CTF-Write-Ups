# fixme2.py
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: fixme2.py
* Category: General Skills
* Points: 100
* Date: 09-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220409224245.png)

---
## Hints:
1. Are equality and assignment the same symbol?
2. To view the file in the webshell, do: $ nano fixme2.py
3. To exit nano, press Ctrl and x and follow the on-screen prompts.
4. The str_xor function does not need to be reverse engineered for this challenge.

---
## Solution:
When we run the code:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 fixme2.py
  File "/home/kali/Downloads/fixme2.py", line 22
    if flag = "":
            ^
SyntaxError: invalid syntax
```

We get a syntax error because there is only one `=`. There needs to be two `==` if we want to check if something is equal to something else. We use one `=` when we are assigning a value. Let's open the file and fix the error. We can open and edit the file with `nano`:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nano fixme2.py
```

![](./attachments/Pasted%20image%2020220409225600.png)

After saving by clicking `ctrl` + `x` -> `y` -> `Enter`, we can run the script again:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}
```

And we get the flag!

**Flag:** `picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}`

---
**Tags:** [[PicoCTF]]