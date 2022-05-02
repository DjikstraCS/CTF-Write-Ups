# Matryoshka doll
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Matryoshka doll
* Category: Forensics
* Points: 30
* Date: 11-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220411191207.png)

---
## Hints:
1. Wait, you can hide files inside files? But how do you find them?
2. Make sure to submit the flag as picoCTF{XXXXX}

---
## Solution:
The image:

![](./attachments/Pasted%20image%2020220411191850.png)

First we will try the standard stuff, `cat | grep`and `strings | grep` but it gives us nothing. `file` and `identify -verbose` likewise doesn't return anything useful. Everything looks normal.

Binwalk gives us some useful information though. Looks like there's a Zip archive hidden in the image.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ binwalk dolls.jpg
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378942, uncompressed size: 383937, name: base_images/2_c.jpg
651600        0x9F150         End of Zip archive, footer length: 22
```

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ unzip dolls.jpg
Archive:  dolls.jpg
warning [dolls.jpg]:  272492 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/2_c.jpg  
  
┌──(kali㉿kali)-[~/Downloads]
└─$ ll
total 644
drwxr-xr-x 2 kali kali   4096 Apr 11 13:33 base_images
-rw-r--r-- 1 kali kali 651622 Apr 11 12:38 dolls.jpg

┌──(kali㉿kali)-[~/Downloads]
└─$ cd base_images 

┌──(kali㉿kali)-[~/Downloads/base_images]
└─$ ll
total 376
-rw-r--r-- 1 kali kali 383937 Mar 15  2021 2_c.jpg
```

Another image. Same as the first one. Is it also hiding something?

```console
┌──(kali㉿kali)-[~/Downloads/base_images]
└─$ binwalk 2_c.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196042, uncompressed size: 201444, name: base_images/3_c.jpg
383804        0x5DB3C         End of Zip archive, footer length: 22
383915        0x5DBAB         End of Zip archive, footer length: 22
```

Yes it is, I wonder how far this will take us...

```console
┌──(kali㉿kali)-[~/Downloads/base_images]
└─$ unzip 2_c.jpg
Archive:  2_c.jpg
warning [2_c.jpg]:  187707 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/3_c.jpg

┌──(kali㉿kali)-[~/Downloads/base_images]
└─$ ll
total 380
-rw-r--r-- 1 kali kali 383937 Mar 15  2021 2_c.jpg
drwxr-xr-x 2 kali kali   4096 Apr 11 13:43 base_images

┌──(kali㉿kali)-[~/Downloads/base_images]
└─$ cd base_images

┌──(kali㉿kali)-[~/Downloads/base_images/base_images]
└─$ ll
total 200
-rw-r--r-- 1 kali kali 201444 Mar 15  2021 3_c.jpg

┌──(kali㉿kali)-[~/Downloads/base_images/base_images]
└─$ unzip 3_c.jpg
Archive:  3_c.jpg
warning [3_c.jpg]:  123606 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/4_c.jpg
  
┌──(kali㉿kali)-[~/Downloads/base_images]
└─$ ll
total 380
-rw-r--r-- 1 kali kali 383937 Mar 15  2021 3_c.jpg
drwxr-xr-x 2 kali kali   4096 Apr 11 13:43 base_images
  
┌──(kali㉿kali)-[~/Downloads/base_images/base_images]
└─$ cd base_images

┌──(kali㉿kali)-[~/Downloads/base_images/base_images/base_images]
└─$ ll
total 80
-rw-r--r-- 1 kali kali 79806 Mar 15  2021 4_c.jpg

┌──(kali㉿kali)-[~/Downloads/base_images/base_images/base_images]
└─$ unzip 4_c.jpg
Archive:  4_c.jpg
warning [4_c.jpg]:  79578 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: flag.txt 
  
┌──(kali㉿kali)-[~/Downloads/base_images/base_images/base_images]
└─$ ll
total 84
-rw-r--r-- 1 kali kali 79806 Mar 15  2021 4_c.jpg
-rw-r--r-- 1 kali kali    81 Mar 15  2021 flag.txt

┌──(kali㉿kali)-[~/Downloads/base_images/base_images/base_images]
└─$ cat flag.txt
picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32} 
```

Finally, the flag!

**Flag:** `picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}`

---
**Tags:** [[PicoCTF]]