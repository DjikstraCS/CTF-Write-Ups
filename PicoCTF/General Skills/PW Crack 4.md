# PW Crack 4
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: PW Crack 4
* Category: General Skills
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410130846.png)

---
## Hints:
1. A for loop can help you do many things very quickly.
2. The str_xor function does not need to be reverse engineered for this challenge.

---
## Solution:
We need do put the files in the same directory, fortunately this happens automatically if you just download them via the browser.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ ll
total 12
-rw-r--r-- 1 kali kali   33 Apr 10 06:05 level4.flag.txt.enc
-rw-r--r-- 1 kali kali   16 Apr 10 06:05 level4.hash.bin
-rw-r--r-- 1 kali kali 2085 Apr 10 06:05 level4.py
```

Let's run the script and see what happens.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level4.py
Please enter correct password for flag: 1234
That password is incorrect
```

We need to find the password. If we open the script in a code friendly editor like `gedit` to have a closer look at how it validates the password, we can see that the password is checked agains a hash. We also get a list of 100 possible passwords.

```py
lag_enc = open('level4.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level4.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_4_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

level_4_pw_check()

# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8c86", "7692", "a519", "3e61", "7dd6", "8919", "aaea", "f34b", "d9a2", "39f7", "626b", "dc78", "2a98", "7a85", "cd15", "80fa", "8571", "2f8a", "2ca6", "7e6b", "9c52", "7423", "a42c", "7da0", "95ab", "7de8", "6537", "ba1e", "4fd4", "20a0", "8a28", "2801", "2c9a", "4eb1", "22a5", "c07b", "1f39", "72bd", "97e9", "affc", "4e41", "d039", "5d30", "d13f", "c264", "c8be", "2221", "37ea", "ca5f", "fa6b", "5ada", "607a", "e469", "5681", "e0a4", "60aa", "d8f8", "8f35", "9474", "be73", "ef80", "ea43", "9f9e", "77d7", "d766", "55a0", "dc2d", "a970", "df5d", "e747", "dc69", "cc89", "e59a", "4f68", "14ff", "7928", "36b9", "eac6", "5c87", "da48", "5c1d", "9f63", "8b30", "5534", "2434", "4a82", "d72c", "9b6b", "73c5", "1bcf", "c739", "6c31", "e138", "9e77", "ace1", "2ede", "32e0", "3694", "fc92", "a7e2"]
```

After moving the `pos_pw_list` and adding a few lines of code we can make the script leak the information we need like this:

![](./attachments/Pasted%20image%2020220410130346.png)

Now all we need to do is observe the output in order to get the correct password:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level4.py
607a
Please enter correct password for flag: 607a
Welcome back... your flag, user:
picoCTF{fl45h_5pr1ng1ng_d770d48c}
```

And we get the flag!

**Flag:** `picoCTF{fl45h_5pr1ng1ng_d770d48c}`

---
**Tags:** [[PicoCTF]] [[Python]]