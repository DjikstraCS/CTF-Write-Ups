# PW Crack 5
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: PW Crack 5
* Category: General Skills
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410130911.png)

---
## Hints:
1. Opening a file in Python is crucial to using the provided dictionary.
2. You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, strip
3. The str_xor function does not need to be reverse engineered for this challenge.

---
## Solution:
We need to put the files in the same directory, fortunately this happens automatically if you just download them via the browser.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ ll
total 332
-rw-r--r-- 1 kali kali 327680 Apr 10 07:07 dictionary.txt
-rw-r--r-- 1 kali kali     31 Apr 10 07:07 level5.flag.txt.enc
-rw-r--r-- 1 kali kali     16 Apr 10 07:07 level5.hash.bin
-rw-r--r-- 1 kali kali   1168 Apr 10 07:07 level5.py
```

Let's run the script and see what happens.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level5.py
Please enter correct password for flag: 1234
That password is incorrect
```

We need to find the password. If we open the script in a code friendly editor like `gedit` to have a closer look at how it validates the password, we can see that the password is checked against a hash. We also get a list of 7 possible passwords in a text file called `dictionary.txt`.

```py
flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_5_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
    
level_5_pw_check()
```

After adding a few lines of code, we can make the script leak the information we need.

```py
with open('dictionary.txt', 'r') as f: # Open file.
    lines = f.readlines() # Read lines in file.
    for i in lines: # For every line.
        if hash_pw(i.strip('\n')) == correct_pw_hash: # If dictionary hash matches correct_pw_hash we have found the correct password.
            print(i) # Print the password.
```

![](./attachments/Pasted%20image%2020220410134134.png)

Now all we need to do is run the script and type the password.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 level5.py
9581

Please enter correct password for flag: 9581        
Welcome back... your flag, user:
picoCTF{h45h_sl1ng1ng_36e992a6}
```

**Flag:** `picoCTF{m45h_fl1ng1ng_cd6ed2eb}`

---
**Tags:** [[PicoCTF]]