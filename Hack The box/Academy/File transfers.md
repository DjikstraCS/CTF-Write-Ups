# File transfers
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: File transfers
* Tier: Tier 0
* Difficulty: Medium
* Category: Offensive
* Time estimate: 3 hours
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Windows File Transfer Methods
### Question:
![](./attachments/Pasted%20image%2020230127185922.png)

```
┌──(kali㉿kali)-[~/HTB]
└─$ wget http://10.129.187.68/flag.txt
--2023-01-27 13:59:40--  http://10.129.187.68/flag.txt
Connecting to 10.129.187.68:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 32 [text/plain]
Saving to: ‘flag.txt’

flag.txt                                  100%[===================================================================================>]      32  --.-KB/s    in 0s      

2023-01-27 13:59:40 (4.51 MB/s) - ‘flag.txt’ saved [32/32]

                                                                                                                                                                      
┌──(kali㉿kali)-[~/HTB]
└─$ cat flag.txt
b1a4ca918282fcd96004565521944a3b
```

**Answer:** `b1a4ca918282fcd96004565521944a3b`

### Question:
![](./attachments/Pasted%20image%2020230127185932.png)

Download the `upload_win.zip` file.

Copy the file to server directory and start the Python server.

```
┌──(kali㉿kali)-[~/HTB]
└─$ mv ~/Downloads/upload_win.zip ~/HTB/FileTransfers/winFileTransferMethods

┌──(kali㉿kali)-[~/HTB/FileTransfers/winFileTransferMethods]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

Now download and hash the file on the Windows machine.

```
PS C:\Users\htb-student\Documents> wget http://10.10.15.74:8000/upload_win.zip -OutFile upload_win.zip
PS C:\Users\htb-student\Documents> dir


    Directory: C:\Users\htb-student\Documents


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        1/27/2023  11:29 AM            194 upload_win.zip
```

Unzip the file.

![](./attachments/Pasted%20image%2020230127204451.png)

Use `hasher` to get the hash of the file.

```
PS C:\Users\htb-student\Documents> dir
    Directory: C:\Users\htb-student\Documents

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        1/27/2023  11:29 AM                upload_win
-a----        1/27/2023  11:29 AM            194 upload_win.zip

PS C:\Users\htb-student\Documents> cd .\upload_win\
PS C:\Users\htb-student\Documents\upload_win> hasher upload_win.txt
f458303ea783c224c6b4e7ef7f17eb9d
```

**Answer:** `f458303ea783c224c6b4e7ef7f17eb9d`

---
## Linux File Transfer Methods
### Question:


**Answer:** ``

---
## 
### Question:


**Answer:** ``

---
## 
### Question:


**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]