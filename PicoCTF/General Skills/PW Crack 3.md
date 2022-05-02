# PW Crack 3
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: PW Crack 3
* Category: General Skills
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410124713.png)

---
## Hints:
1. To view the level3.hash.bin file in the webshell, do: $ bvi level3.hash.bin
2. To exit bvi type :q and press enter.
3. The str_xor function does not need to be reverse engineered for this challenge.

---
## Solution:
We need do put the files in the same directory, fortunately this happens automatically if you just download them via the browser.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ ll
total 12
-rw-r--r-- 1 kali kali   31 Apr 10 06:05 level3.flag.txt.enc
-rw-r--r-- 1 kali kali   16 Apr 10 06:05 level3.hash.bin
-rw-r--r-- 1 kali kali 1337 Apr 10 06:05 level3.py
```

Let's run the script and see what happens.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level3.py
Please enter correct password for flag: 1234
That password is incorrect
```

We need to find the password. If we open the script in a code friendly editor like `gedit` to have a closer look at how it validates the password, we can see that the password is checked agains a hash. We also get a list of 7 possible passwords.

```py
flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

level_3_pw_check()

# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]
```

After moving the `pos_pw_list` and adding a few lines of code we can make the script leak the information we need, like this:

![](./attachments/Pasted%20image%2020220410123459.png)

Now all we need to do is observe the output in order to get the correct password:

![](./attachments/Pasted%20image%2020220410123929.png)

And we get the flag!

**Flag:** `picoCTF{m45h_fl1ng1ng_cd6ed2eb}`

---
**Tags:** [[PicoCTF]]