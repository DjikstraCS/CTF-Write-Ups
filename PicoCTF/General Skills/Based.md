# Based
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Based
* Category: General Skills
* Points: 200
* Date: 30-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
We are going to convert some encoding.

![](./attachments/Pasted%20image%2020220330172642.png)

---
## Hints:
1. I hear python can convert things.
2. It might help to have multiple windows open.

---
## Requirements:
- Python

---
## Solution:
Using `nc` (netcat) to connect:

![](./attachments/Pasted%20image%2020220330172954.png)

Ok, we need to convert some binary values into Unicode.

Let's make a Python script like the hints suggest.

During testing of the script it was revealed that we also need to convert Octal and Hex into Unicode. For that reson I've added two extra steps to the script, taking care of those conversions.

Python script:

>#!/usr/bin/python3
>
>#Binary to Unicode
>input_list = input("Binary: ").split(' ')
>print(''.join(map(chr,[int(i,2) for i in input_list])))
>
>
>#Octal to Unicode
>input_list = input("Octal: ").split(' ')
>print(''.join(map(chr,[int(i,8) for i in input_list])))
>
>
>#Hex to Unicode
>hex_input = input("Hex: ")
>print(bytes.fromhex(hex_input).decode('utf-8'))

The output of the script after pasting the values from the program:

![](./attachments/Pasted%20image%2020220330201441.png)

The output of the program:

![](./attachments/Pasted%20image%2020220330201655.png)

And got our flag!


**Flag:** `picoCTF{learning_about_converting_values_00a975ff}`

---
**Tags:** [[PicoCTF]]