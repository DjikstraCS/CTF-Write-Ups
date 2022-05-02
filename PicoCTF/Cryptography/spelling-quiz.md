# spelling-quiz
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: spelling-quiz
* Category: Cryptography
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410220351.png)

---
## Solution:
The files unzipped:

```console
┌──(kali㉿kali)-[~/Downloads/public]
└─$ ll
total 3112
-rw-r--r-- 1 kali kali     510 Feb 21  2021 encrypt.py
-rw-r--r-- 1 kali kali      43 Feb 21  2021 flag.txt
-rw-r--r-- 1 kali kali 3178399 Feb 21  2021 study-guide.txt
```

It looks a bit complicated, reverse engineering it could take a long time. Letter substitution is used though. 

```py
import random
import os

files = [
    os.path.join(path, file)
    for path, dirs, files in os.walk('.')
    for file in files
    if file.split('.')[-1] == 'txt'
]

alphabet = list('abcdefghijklmnopqrstuvwxyz')
random.shuffle(shuffled := alphabet[:])
dictionary = dict(zip(alphabet, shuffled))

for filename in files:
    text = open(filename, 'r').read()
    encrypted = ''.join([
        dictionary[c]
        if c in dictionary else c
        for c in text
    ])
    open(filename, 'w').write(encrypted)
```

And we can use that knowledge to our advantage. Letter substitution is a really weak form of encryption. First, let's run a frequency analysis on `flag.txt` via [dCode](https://www.dcode.fr/en).

![](./attachments/Pasted%20image%2020220410221732.png)

And compare that to the letter frequency in the English language.

![](./attachments/Pasted%20image%2020220410224709.png)

Now we might have a clue as to what `r` in the encrypted text corresponds to.

`R = E`

We can use [quipquip](https://www.quipqiup.com/) to try and solve it.

![](./attachments/Pasted%20image%2020220410223045.png)

Just to be sure, we can remove the clue and paste 50 lines from the encrypted `study-guide.txt` into [quipquip](https://www.quipqiup.com/) alongside the flag. Then run it again to see if it gets to the same result.

![](./attachments/Pasted%20image%2020220410224046.png)

Yes! We got the flag.

**Flag:** `picoCTF{perhaps_the_dog_jumped_over_was_just_tired}`

---
**Tags:** [[PicoCTF]]