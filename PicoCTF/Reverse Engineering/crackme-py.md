# crackme-py
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: crackme-py
* Category: Reverse Engineering
* Points: 30
* Date: 29-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220411200258.png)

---
## Solution:
The script we need to crack:

```py
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0d_a3hgc3N"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def decode_secret(secret):
    """ROT47 decode
    NOTE: encode and decode are the same operation in the ROT cipher family.
    """
    # Encryption key
    rotate_const = 47
    # Storage for decoded secret
    decoded = ""
    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)

def choose_greatest():
    """Echo the largest of the two numbers given by the user to the program
    Warning: this function was written quickly and needs proper error handling
    """
    user_value_1 = input("What's your first number? ")
    user_value_2 = input("What's your second number? ")
    greatest_value = user_value_1 # need a value to return if 1 & 2 are equal

    if user_value_1 > user_value_2:
        greatest_value = user_value_1
    elif user_value_1 < user_value_2:
        greatest_value = user_value_2

    print( "The number with largest positive magnitude is "
        + str(greatest_value) )

choose_greatest()
```

This one is going to be easy, everything we need to decrypt is already here. We can simply add this line at the bottom part of the script.

`print(decode_secret(bezos_cc_secret))`

![](./attachments/Pasted%20image%2020220411200939.png)

Now if we run it:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 crackme.py
picoCTF{1|\/|_4_p34|\|ut_502b984b}
None
What's your first number? 
```

And we get the flag!

**Flag:** `picoCTF{1|\/|_4_p34|\|ut_502b984b}`

---
**Tags:** [[PicoCTF]]