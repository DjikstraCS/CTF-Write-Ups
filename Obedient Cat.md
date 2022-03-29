# **Obedient Cat**
* Source: PicoCTF 
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge:  Obedient Cat
* Category: General Skills
* Date: 29-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---

### **Problem:**
Looks like we need to download the flag file and open it in order to extract the flag.

![](./attachments/Pasted%20image%2020220329124831.png)

---

### **Solution:**

**Step 1**

Download the flag file using your browser.

**Step 2**

Open a terminal and navigate to the Downloads folder, using `cd`.

Use `ll` to view the content of the folder.

![](./attachments/Pasted%20image%2020220329130407.png)

**Step 3**

Use `cat` bash command to show the content of the file:

`cat flag`

![](./attachments/Pasted%20image%2020220329130444.png)

And there it is.

**Flag: picoCTF{s4n1ty_v3r1f13d_1a94e0f9}**


---
