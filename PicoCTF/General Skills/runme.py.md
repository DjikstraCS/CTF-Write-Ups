# runme.py
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: runme.py
* Category: General Skills
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410134708.png)

---
## Hints:
1. If you have Python on your computer, you can download the script normally and run it. Otherwise, use the wget command in the webshell.
2. To use wget in the webshell, first right click on the download link and select 'Copy Link' or 'Copy Link Address'
3. Type everything after the dollar sign in the webshell: $ wget , then paste the link after the space after wget and press enter. This will download the script for you in the webshell so you can run it!
4. Finally, to run the script, type everything after the dollar sign and then press enter: $ python3 runme.py You should have the flag now!

---
## Solution:
Download the file and use `cd` to navigate to the Downloads folder. Use `ll` to confirm that we indeed have the file.

```console
┌──(kali㉿kali)-[~]
└─$ cd Downloads

┌──(kali㉿kali)-[~/Downloads]
└─$ ll
total 4
-rw-r--r-- 1 kali kali 270 Apr 10 07:46 runme.py
```

Lastly, execute it using Python3.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 runme.py

picoCTF{run_s4n1ty_run}
```

We got the flag!

**Flag:** `picoCTF{run_s4n1ty_run}`

---
**Tags:** [[PicoCTF]]