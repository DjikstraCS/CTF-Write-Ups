# File Upload Attacks
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: File Upload Attacks
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 8 hours
* Date: 11-07-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Absent Validation
### Question:
![](./attachments/Pasted%20image%2020220705125513.png)

*Hint: You may use the 'system()' PHP function to execute system commands*

The page:

![](./attachments/Pasted%20image%2020220705133533.png)

Making a .php file which executes `hostname` command.

```
┌──(kali㉿kali)-[~]
└─$ echo "<?php system('hostname');?>" > test.php
```

Upload the file.

![](./attachments/Pasted%20image%2020220705133407.png)

Click 'Download File' to open the file in the browser.

![](./attachments/Pasted%20image%2020220705133428.png)

**Answer:** `fileuploadsabsentverification`

---
## Upload Exploitation
### Question:
![](./attachments/Pasted%20image%2020220705125814.png)

Same page as previous question.

We will use [phpbash](https://github.com/Arrexel/phpbash) as the payload.

After upload and subsequent download, we get a web shell:

![](./attachments/Pasted%20image%2020220706113517.png)

**Answer:** `HTB{g07_my_f1r57_w3b_5h3ll}`

---
## Client-Side Validation
### Question:
![](./attachments/Pasted%20image%2020220705125856.png)

*Hint: Try to locate the function responsible for validating the input type, then try to remove it without breaking the upload functionality*

Make and upload dummy `.png` file to catch POST request.

```
┌──(kali㉿kali)-[~]
└─$ echo "image" > test.png
```

The POST request.

![](./attachments/Pasted%20image%2020220706123244.png)

We need to insert our `phpbash.php` payload here.

![](./attachments/Pasted%20image%2020220706123652.png)

The file is uploaded, we can now see the file in the source code in the browser after refreshing.

![](./attachments/Pasted%20image%2020220706121701.png)

Upon visiting the URL:

![](./attachments/Pasted%20image%2020220706121925.png)


Disabling front-end validation:

![](./attachments/Pasted%20image%2020220706121226.png)

Edit the page source code.

![](./attachments/Pasted%20image%2020220706121357.png)

Now we can upload [phpbash](https://github.com/Arrexel/phpbash).

![](./attachments/Pasted%20image%2020220706121701.png)

Our uploaded file is now visible as the source of the image.

![](./attachments/Pasted%20image%2020220706121925.png)

**Answer:** `HTB{cl13n7_51d3_v4l1d4710n_w0n7_570p_m3}`

---
## Blacklist Filters
### Question:
![](./attachments/Pasted%20image%2020220705125935.png)

*Hint: When you fuzz for allowed extensions, change the content to a PHP 'hello world' script. Then, when you check the uploaded file, you would know whether it can execute PHP code.*

Fuzzing reveals the blacklisted extensions.

![](./attachments/Pasted%20image%2020220709174921.png)

Trying `.phar` from [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/Extension%20PHP/extensions.lst) PHP list.

![](./attachments/Pasted%20image%2020220709175244.png)

The page:

![](./attachments/Pasted%20image%2020220709175132.png)

**Answer:** `HTB{1_c4n_n3v3r_b3_bl4ckl1573d}`

---
## Whitelist Filters
### Question:
![](./attachments/Pasted%20image%2020220705130035.png)

*Hint: You may use either of the last two techniques. If one extension is blocked, try another one that can execute PHP code.*

First fuzz file extensions. [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/Extension%20PHP/extensions.lst) PHP list point us in the direction of a reverse double extension.

Fuzzing for that reveals a few successful uploads, we will have to try them one by one until we find the one that executes.

![](./attachments/Pasted%20image%2020220710111701.png)

![](./attachments/Pasted%20image%2020220710111959.png)


**Answer:** `HTB{1_wh173l157_my53lf}`

---
## Type Filters
### Question:
![](./attachments/Pasted%20image%2020220705130135.png)

*Hint: Start with a request that can be uploaded (e.g. jpg image), then try to find an allowed PHP extension that doesn't get blocked, then utilize one of the whitelist filter bypasses to bypass both extension filters.*

[File Magick Numbers](https://en.wikipedia.org/wiki/List_of_file_signatures)

![](./attachments/Pasted%20image%2020220710174834.png)

![](./attachments/Pasted%20image%2020220710174711.png)

**Answer:** `HTB{m461c4l_c0n73n7_3xpl0174710n}`

---
## Limited File Uploads
### Question 1:
![](./attachments/Pasted%20image%2020220705130232.png)

*Hint: Use an attack that can read files, and don't forget to check the page source!*

![](./attachments/Pasted%20image%2020220711111707.png)

![](./attachments/Pasted%20image%2020220711111929.png)

**Answer:** `HTB{my_1m4635_4r3_l37h4l}`

### Question 2:
![](./attachments/Pasted%20image%2020220705130403.png)

*Hint: Use a different payload to read source code*

![](./attachments/Pasted%20image%2020220711112735.png)

![](./attachments/Pasted%20image%2020220711112841.png)

![](./attachments/Pasted%20image%2020220711112920.png)

**Answer:** `./images/`

---
## Skills Assessment
### Question:
![](./attachments/Pasted%20image%2020220705130538.png)

*Hint: Try to fuzz for non-blacklisted extensions, and for allowed content-type headers. If you are unable to locate the uploaded files, try to read the source code to find the uploads directory and the naming scheme.*

**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]