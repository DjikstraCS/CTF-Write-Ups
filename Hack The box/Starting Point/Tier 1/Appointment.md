# Appointment
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Appointment
* Topic: [[SQL Injection]]
* Difficulty: Very easy
* Date: 12-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What does the acronym SQL stand for? 
 - **Structured Query Language**
2. What is one of the most common type of SQL vulnerabilities?
- **SQL Injection**
3. What does PII stand for? 
- **Personally Identifiable Information**
4. What does the OWASP Top 10 list name the classification for this vulnerability? 
- **A03:2021-Injection**
5. What service and version are running on port 80 of the target?
- **Apache httpd 2.4.38 ((Debian))**
6. What is the standard port used for the HTTPS protocol? 
- **443**
7. What is one luck-based method of exploiting login pages? 
- **Brute-forcing**
8. What is a folder called in web-application terminology? 
- **Directory**
9. What response code is given for "Not Found" errors? 
- **404**
10. What switch do we use with Gobuster to specify we're looking to discover directories, and not subdomains? 
 - **dir**
11. What symbol do we use to comment out parts of the code? 
 - **#**

---
## Flag:
Since the questions asked about how to comment out code, we'll try that.

Username: `admin'#`

Password: `1`

![](./attachments/Pasted%20image%2020220412155331.png)

![](./attachments/Pasted%20image%2020220412155534.png)

**Flag:** `e3d0796d002a446c0e622226f42e9672`

---
**Tags:** [[HackTheBox]] [[gobuster]] [[SQL]] [[SQLi]] [[MariaDB]]