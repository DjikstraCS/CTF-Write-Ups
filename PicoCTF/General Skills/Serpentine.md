# Serpentine
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Serpentine
* Category: General Skills
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410135353.png)

---
## Hints:
1. Try running the script and see what happens
2. In the webshell, try examining the script with a text editor like nano
3. To exit nano, press Ctrl and x and follow the on-screen prompts.
4. The str_xor function does not need to be reverse engineered for this challenge.

---
## Solution:
When running the script, we get an error when we try to use the print flag function.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 serpentine.py   
Welcome to the serpentine encourager!

a) Print encouragement
b) Print flag
c) Quit

What would you like to do? (a/b/c) b

Oops! I must have misplaced the print_flag function! Check my source code!
```

When looking at the script, using `gedit serpentine.py &`, we can see the encoded flag and a `print_flag()` function.

![](./attachments/Pasted%20image%2020220410140152.png)

Further down, we can see the line that caused the error.

![](./attachments/Pasted%20image%2020220410140423.png)

If we replace that line with `print_flag()` we should get the flag.

Let's run the script again.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 serpentine.py   
Welcome to the serpentine encourager!

a) Print encouragement
b) Print flag
c) Quit

What would you like to do? (a/b/c) b

picoCTF{7h3_r04d_l355_7r4v3l3d_aa2340b2}
```

And it's solved!

**Flag:** `picoCTF{7h3_r04d_l355_7r4v3l3d_aa2340b2}`

---
**Tags:** [[PicoCTF]] [[Python]]