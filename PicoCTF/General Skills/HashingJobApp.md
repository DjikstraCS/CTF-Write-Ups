# HashingJobApp
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: HashingJobApp
* Category: General Skills
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410105553.png)

---
## Hints:
1. You can use a commandline tool or web app to hash text
2. Press Ctrl and c on your keyboard to close your connection and return to the command prompt.

---
## Solution:
Connect to the service:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nc saturn.picoctf.net 63116
Please md5 hash the text between quotes, excluding the quotes: 'Joan of Arc'
Answer:
```

We need to hash the string the service is giving us, using MD5.

We can use a simple bash command for that.

```console
──(kali㉿kali)-[~/pythonScripts]
└─$ echo -n "Joan of Arc" | md5sum
19ba425a542946fcf13228d9ddd53139  -
```

And if we paste that into the web service. 

```console
Answer: 
1c5d1684ae8cd2f62a070044e5fc40c7
1c5d1684ae8cd2f62a070044e5fc40c7
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'Corvettes'
Answer: 
```

Another one, looks like we have repeat.

```console
┌──(kali㉿kali)-[~/pythonScripts]
└─$ echo -n "Corvettes" | md5sum
0d18e8c9500eebd5748b6ad225652080  -
           
┌──(kali㉿kali)-[~/pythonScripts]
└─$ echo -n "gravity" | md5sum
67f2a835697e7c9c2c5146c76eca6038  -
```

And here, the web service:

```console
Answer: 
0d18e8c9500eebd5748b6ad225652080
0d18e8c9500eebd5748b6ad225652080
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'gravity'
Answer: 
67f2a835697e7c9c2c5146c76eca6038
67f2a835697e7c9c2c5146c76eca6038
Correct.

picoCTF{4ppl1c4710n_r3c31v3d_bf2ceb02}
```

And we get the flag.

**Flag:** `picoCTF{}`

---
**Tags:** [[PicoCTF]] [[MD5]] [[echo]]