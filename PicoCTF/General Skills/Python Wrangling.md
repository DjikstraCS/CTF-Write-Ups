# **Python Wrangling**
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: Python Wrangling
* Category: General Skills
* Date: 29-03-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---

## **Problem:**

We need to run a Python script to decrypt the flag using a seperate password file.

![](./attachments/Pasted%20image%2020220329134632.png)


Let's do this via the terminal.

---

## **Solution:**

**Step 1**

Use `cd` to navigate to a suitable directory.
Then, for each of the three links do a `wget <URL>` to download the files.

![](./attachments/Pasted%20image%2020220329142042.png)

We should now be able to see the files with `ll`:

![](./attachments/Pasted%20image%2020220329142014.png)

**Step 2**
Let't have a look a the `pw.txt` file:

![](./attachments/Pasted%20image%2020220330000430.png)

Great, looks like a password.

**Step 3**
Now let's try to run the Python script.

![](./attachments/Pasted%20image%2020220330000720.png)


**Step 4**
use the `-d` flag to specify decryptio and provide the encrypted flag.

![](./attachments/Pasted%20image%2020220330001443.png)

The flag is decrypted!

**Flag: picoCTF{4p0110_1n_7h3_h0us3_192ee2db}**

---
