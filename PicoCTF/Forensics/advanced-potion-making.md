# advanced-potion-making
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: advanced-potion-making
* Category: Forensics
* Points: 100
* Date: 10-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220410141312.png)

---
## Solution:
 Let's open the file with `less` and have a look around.
 
![](./attachments/Pasted%20image%2020220410151849.png)
 
 We can see the file contains what appears to be .png header.
 
 If we open the file as an image, we get an error.
 
![](./attachments/Pasted%20image%2020220410152534.png)
 
 Looks like the file is corrupted. We need to open it in a hex editor and compare in to another PNG file. The syntax of the header need to comply with the official [PNG header](https://github.com/corkami/formats/blob/master/image/png.md) scheme. 
 
 Something is wrong. We need to edit a few values in order to repair the PNG header.
 
![](./attachments/Pasted%20image%2020220410160048.png)

Great! Now we can actually open the image and see what it contains.

![](./attachments/Pasted%20image%2020220410160604.png)

Just red. We need to dig deeper. 

Maybe someone used [steganography](https://en.wikipedia.org/wiki/Steganography) to hide a message in the image. To find out, we can use a neat little program called [StegSolve](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install). After testing a few settings, we get:

![](./attachments/Pasted%20image%2020220410164328.png)

Nice!
 
 **Flag:** `picoCTF{w1z4rdry}`

---
**Tags:** [[PicoCTF]] [[hexeditor]] [[StegSolve]] [[PNG Header]]