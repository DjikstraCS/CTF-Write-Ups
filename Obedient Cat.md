# **Obedient Cat**
Host: PicoCTF 
Challenge:  Obedient Cat
Category: General Skills
Link: [PicoCTF.org](https://picoctf.org/)
Date: 29-03-2022

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

![[Pasted image 20220329130407.png]]

**Step 3**
Use `cat` bash command to show the content of the file:

`cat flag`

![[Pasted image 20220329130444.png]]

And there it is.

**Flag: picoCTF{s4n1ty_v3r1f13d_1a94e0f9}**

---
Tags: [[PicoCTF]] [[kali]] [[bash]] [[cat]] [[cd]] [[ll]]
