# File Upload Attacks
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: File Upload Attacks
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 8 hours
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Absent Validation
### Question:
![](./attachments/Pasted%20image%2020220705125513.png)

*Hint: You may use the 'system()' PHP function to execute system commands*

**Answer:** ``

---
## Upload Exploitation
### Question:
![](./attachments/Pasted%20image%2020220705125814.png)


**Answer:** ``

---
## Client-Side Validation
### Question:
![](./attachments/Pasted%20image%2020220705125856.png)

*Hint: Try to locate the function responsible for validating the input type, then try to remove it without breaking the upload functionality*

**Answer:** ``

---
## Blacklist Filters
### Question:
![](./attachments/Pasted%20image%2020220705125935.png)

*Hint: When you fuzz for allowed extensions, change the content to a PHP 'hello world' script. Then, when you you check the uploaded file, you would know whether it can execute PHP code.*

**Answer:** ``

---
## Whitelist Filters
### Question:
![](./attachments/Pasted%20image%2020220705130035.png)

*Hint: You may use either of the last two techniques. If one extension is blocked, try another one that can execute PHP code.*

**Answer:** ``

---
## Type Filters
### Question:
![](./attachments/Pasted%20image%2020220705130135.png)

*Hint: Start with a request that can be uploaded (e.g. jpg image), then try to find an allowed PHP extension that doesn't get blocked, then utilize one of the whitelist filter bypasses to bypass both extension filters.*

**Answer:** ``

---
## Limited File Uploads
### Question 1:
![](./attachments/Pasted%20image%2020220705130232.png)

*Hint: Use an attack that can read files, and don't forget to check the page source!*

**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020220705130403.png)

*Hint: Use a different payload to read source code*

**Answer:** ``

---
## Skills Assessment
### Question:
![](./attachments/Pasted%20image%2020220705130538.png)

*Hint: Try to fuzz for non-blacklisted extensions, and for allowed content-type headers. If you are unable to locate the uploaded files, try to read the source code to find the uploads directory and the naming scheme.*

**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]