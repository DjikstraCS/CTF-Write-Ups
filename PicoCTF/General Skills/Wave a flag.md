# Wave a flag
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Wave a flag
* Category: General Skills
* Points: 10
* Date: 30-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:

We need to invoke the help `-h` or `--help` function of the given program.

![](./attachments/Pasted%20image%2020220330064136.png)

---
## Solution:

Download the file, open a terminal and navigate to the Downloads folder.

`ll` Command should give us a file called `warm`.

![](./attachments/Pasted%20image%2020220330064913.png)

On the left, marked in the red rectangle, we see the permissions we have for the file.

`-rw-r--r--` Means that we currently, as a user, have read and write access to the file.

In order to execute the file, we need to add `x` to the permissions. 

The tool `chmod` is made for this. By giving it the argument `+x` we will add execute permission.

![](./attachments/Pasted%20image%2020220330065941.png)

Now that we have permission, we can execute the program. Remember the `-h` flag.

![](./attachments/Pasted%20image%2020220330070902.png)

We got the flag!

**Flag:** `picoCTF{b1scu1ts_4nd_gr4vy_616f7182}`

---
**Tags:** [[PicoCTF]]