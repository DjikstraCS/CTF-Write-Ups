# Magikarp Ground Mission
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Magikarp Ground Mission
* Category: General Skills
* Points: 30
* Date: 30-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:

We have to connect to a remote instance and browse its dictionary for the flag.

![](./attachments/Pasted%20image%2020220330152605.png)

---
## Hints:
1. Finding a cheat sheet for bash would be really helpful!

---
## Solution:
First we need to connect to the remote instance. The `ssh` command is visible in the description.

Type 'yes' to continue connection and type in the password.

![](./attachments/Pasted%20image%2020220330153031.png)

Now let's have a look around, `ll` is usually the fastest way to get an overview over a folder but is not supported by all systems. A more basic command is `ls` often seen with some flags following it e.g. `ls -lah`.

Using `cat` we can view the content of any files we find.

![](./attachments/Pasted%20image%2020220330153935.png)

Great! We got part of the flag. 

The instruction file tells us to go to the root directory (/).

In order to change directory, we use `cd` followed by the path we want to go to.

![](./attachments/Pasted%20image%2020220330154408.png)

Nice, we got the second part of the flag.

Further instructions tell us to go to the home directory of the user (~).

![](./attachments/Pasted%20image%2020220330154938.png)

And there is the last part of the flag!

**Flag:** `picoCTF{xxsh_0ut_0f_\/\/4t3r_3ca613a1}`

---
**Tags:** [[PicoCTF]] [[ll]] [[ls]] [[cat]] [[ssh]] [[bash]] [[cd]]