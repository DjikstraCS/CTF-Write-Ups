# Cross-site scripting
* Source: [PortSwigger](https://portswigger.net)
* Number of labs: 30
* Completion date:  DD-MM-YYYY (**IN PROGRESS...**)
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Reflected XSS into HTML context with nothing encoded
* Difficulty: Apprentice

### Question:
 This lab contains a simple [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that calls the `alert` function. 

### Solution:
The page:

![](./attachments/Pasted%20image%2020220807120524.png)

Insert payload:

```html
<script>alert(1)</script>
```

![](./attachments/Pasted%20image%2020220807120725.png)

Click 'Search'.

![](./attachments/Pasted%20image%2020220807120737.png)

---
## Stored XSS into HTML context with nothing encoded
* Difficulty: Apprentice

### Question:
 This lab contains a [stored cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability in the comment functionality.

To solve this lab, submit a comment that calls the `alert` function when the blog post is viewed. 

### Solution:
The page:

![](./attachments/Pasted%20image%2020220807121529.png)

Click 'View post' and scroll down to the comment section.

Insert the payload in the 'Comment' field. 

```html
<script>alert(1)</script>
```

Put dummy values in the remaining fields.

![](./attachments/Pasted%20image%2020220807122244.png)

Click 'Post Comment'.

![](./attachments/Pasted%20image%2020220807122334.png)

Click '< Back to the blog'.

![](./attachments/Pasted%20image%2020220807122411.png)

---
## 
* Difficulty: 

### Question:

### Solution:

---
## 
* Difficulty: 

### Question:

### Solution:

---
**Tags:** [[PortSwigger Web Security Academy]]