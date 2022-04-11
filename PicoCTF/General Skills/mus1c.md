# mus1c
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: mus1c
* Category: General Skills
* Points: 300
* Date: 11-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220411230507.png)

---
## Hints:
1. Do you think you can master rockstar?

---
## Solution:
Someone wrote a song about picoCTF.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ cat lyrics.txt
Pico's a CTFFFFFFF
my mind is waitin
It's waitin

Put my mind of Pico into This
my flag is not found
put This into my flag
put my flag into Pico


shout Pico
shout Pico
shout Pico

My song's something
put Pico into This

Knock This down, down, down
put This into CTF

shout CTF
my lyric is nothing
Put This without my song into my lyric
Knock my lyric down, down, down

shout my lyric

Put my lyric into This
Put my song with This into my lyric
Knock my lyric down

shout my lyric

Build my lyric up, up ,up

shout my lyric
shout Pico
shout It

Pico CTF is fun
security is important
Fun is fun
Put security with fun into Pico CTF
Build Fun up
shout fun times Pico CTF
put fun times Pico CTF into my song

build it up

shout it
shout it

build it up, up
shout it
shout Pico
```

Let's find out what this is about. After a bit of searching, I found this, Rockstar is a programming language made to "(...) give the programmer an unprecedented degree of poetic license when it comes to the composition and structure of their programs."

![](./attachments/Pasted%20image%2020220411230900.png)

We could look in the docs for more information about syntax and then revers engender it all from scratch. Luckily we dont have to, because there is an online interpreter on the site if we click on "try it". All we need to do now is paste the song into the interpreter and click "Rock!".

![](./attachments/Pasted%20image%2020220411231533.png)

We get some numbers in return, looks like they might be ASCII.

`114 114 114 111 99 107 110 114 110 48 49 49 51 114`

[CyberChef](https://gchq.github.io/CyberChef) can help us out!

![](./attachments/Pasted%20image%2020220411232312.png)

We got it the flag.

**Flag:** `picoCTF{rrrocknrn0113r}`

---
**Tags:** [[PicoCTF]]