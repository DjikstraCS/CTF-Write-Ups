# convertme.py
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: convertme.py
* Category: General Skills
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410001753.png)

---
## Hints:
1. Look up a decimal to binary number conversion app on the web or use your computer's calculator!
2. The str_xor function does not need to be reverse engineered for this challenge.
3. If you have Python on your computer, you can download the script normally and run it. Otherwise, use the wget command in the webshell.
4. To use wget in the webshell, first right click on the download link and select 'Copy Link' or 'Copy Link Address'
5. Type everything after the dollar sign in the webshell: $ wget , then paste the link after the space after wget and press enter. This will download the script for you in the webshell so you can run it!
6. Finally, to run the script, type everything after the dollar sign and then press enter: $ python3 convertme.py

---
## Solution:
When we run the script, it asks what the binary value of 95 is. 

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 convertme.py
If 95 is in decimal base, what is it in binary base?
Answer: 
```

We can use [CyberChef](https://gchq.github.io/CyberChef) to solve this problem.

![](./attachments/Pasted%20image%2020220410003618.png)

Type the result into the script.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 convertme.py
If 95 is in decimal base, what is it in binary base?
Answer: 1011111
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_762f748e}
```

And we are presented with a flag.

**Flag:** `picoCTF{4ll_y0ur_b4535_762f748e}`

---
**Tags:** [[PicoCTF]] [[CyberChef]]