# Introduction to Web Applications
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Introduction to Web Applications
* Tier: 0
* Difficulty: Fundamental
* Topic: General
* Time estimate: 3 hours
* Date: 02-05-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## HTML
[OWASP Web Security Testing Guide](https://github.com/OWASP/wstg/tree/master/document/4-Web_Application_Security_Testing)

### Question:
![](./attachments/Pasted%20image%2020220502135026.png)

*Hint: Google is your friend. Only put the opening tag 'i.e. <...>'*

**Answer:** `<img>`

---
## CSS
### Question:
![](./attachments/Pasted%20image%2020220502135738.png)

*Hint: Don't forget the semi-colon ';'*

**Answer:** `text-align: left;`

---
## Sensitive Data Exposure
### Question:
![](./attachments/Pasted%20image%2020220502140922.png)

*Hint: Use ctrl+u to show source in Firefox, or right click > View Page Source*

The page contains a login screen. 

Upon inspection of the site, we find some login credentials in a comment in the page source code. 

![](./attachments/Pasted%20image%2020220502140846.png)

**Answer:** `HiddenInPlainSight`

---
## HTML Injection
### Question:
![](./attachments/Pasted%20image%2020220502141242.png)

*Hint: Use the full text displayed on the page as the answer "Your ..."*

The page has a button, if clicked a window pops up asking for a name.

![](./attachments/Pasted%20image%2020220502142150.png)

The given name will be reflected back at the user.

![](./attachments/Pasted%20image%2020220502141942.png)

We can try and see if the page i vulnerable to HTML injection. 

Injection: `<a href="http://www.hackthebox.com">Click Me</a>`

![](./attachments/Pasted%20image%2020220502142047.png)

It is vulnerable!

**Answer:** `Your name is Click Me`

---
## Cross-Site Scripting (XSS)
### Question:
![](./attachments/Pasted%20image%2020220502142357.png)

We can use the following injection to exploit the XXS vulnerability in order to get the cookie value.

Injection: `#"><img src=/ onerror=alert(document.cookie)>`

![](./attachments/Pasted%20image%2020220502143219.png)

![](./attachments/Pasted%20image%2020220502143327.png)

**Answer:** `XSSisFun`

---
## Back End Servers
### Question:
![](./attachments/Pasted%20image%2020220502144032.png)

**Answer:** `Windows`

---
## # Web Servers
![](./attachments/Pasted%20image%2020220502144447.png)

### Question:
![](./attachments/Pasted%20image%2020220502144149.png)

*Hint: Submit just the code name, without the code number. For example, for the code (200 OK), the answer would be just 'OK'.*

Answer is found here: [HTTP Response Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

**Answer:** `Created`

---
## Databases
### Question:
![](./attachments/Pasted%20image%2020220502144724.png)

*Isn't Google still your friend?*

**Answer:** `NoSQL`

---
## # Development Frameworks & APIs
### Question:
![](./attachments/Pasted%20image%2020220502145414.png)

*Hint: Remember: GET request parameters go in the URL, after the website name `http://example.com`*

In Firefox, insert path and query string:

`/index.php?id=1`

![](./attachments/Pasted%20image%2020220502145814.png)


**Answer:** ``

---
## Common Web Vulnerabilities
### Question:
![](./attachments/Pasted%20image%2020220502151309.png)

*Hint: It's one of the above! Simply search for the vulnerability description and read about it, and you'll know the answer.*

Answer can be found here: [nvd.nist.gov](https://nvd.nist.gov/vuln/detail/cve-2014-6271)

**Answer:** `Command Injection`

---
## Public Vulnerabilities
### Question:
![](./attachments/Pasted%20image%2020220502151533.png)

*Hint: Use CVSS v2.0 score, not CVSS v3.X*

![](./attachments/Pasted%20image%2020220502154019.png)

[nvd.nist.gov](https://nvd.nist.gov/vuln/detail/cve-2014-6271)

**Answer:** `9.3`

---
**Tags:** [[HackTheBox]] [[Academy]]