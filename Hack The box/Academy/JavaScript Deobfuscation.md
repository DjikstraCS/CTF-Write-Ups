# JavaScript Deobfuscation
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: JavaScript Deobfuscation
* Tier: 0
* Difficulty: Easy
* Category: Defensive
* Time estimate: 4 hours
* Date: 03-07-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Source Code
### Question:
![](./attachments/Pasted%20image%2020220703103654.png)

*Hint: It is in this form: HTB{...}*

Webpage given:

![](./attachments/Pasted%20image%2020220703104506.png)

`[CTRL + U]` will show the source code fo the page.

```html
</html>
<!DOCTYPE html>

<head>
    <title>Secret Serial Generator</title>
    <style>
        *,
        html {
            margin: 0;
            padding: 0;
            border: 0;
        }

(...)
		
    </style>
    <script src="secret.js"></script>
    <!-- HTB{4lw4y5_r34d_7h3_50urc3} -->
</head>

<body>
    <div class="center">
        <h1>Secret Serial Generator</h1>
        <p>This page generates secret serials!</p>
    </div>
</body>

</html>
```

**Answer:** `HTB{4lw4y5_r34d_7h3_50urc3}`

---
## Deobfuscation
### Question:
![](./attachments/Pasted%20image%2020220703103903.png)

*Hint: Don't just beautify it, deobfuscate it!*

Copy the contents of the `secret.js` file.

![](./attachments/Pasted%20image%2020220703105241.png)

Insert into [jsnice.org](http://jsnice.org/) and hit the 'Nicify Javascript' button.

![](./attachments/Pasted%20image%2020220703105509.png)

**Answer:** `HTB{1_4m_7h3_53r14l_g3n3r470r!}`

---
## HTTP Requests
### Question:
![](./attachments/Pasted%20image%2020220703104003.png)

*Hint: It should start with 'N' and end with 'z'*

```
┌──(kali㉿kali)-[~]
└─$ curl -s 157.245.33.77:31130/serial.php -X POST                      
N2gxNV8xNV9hX3MzY3IzN19tMzU1NGcz
```

**Answer:** `N2gxNV8xNV9hX3MzY3IzN19tMzU1NGcz`

---
## Decoding
### Question:
![](./attachments/Pasted%20image%2020220703104103.png)

*Hint: Use on the decoding commands you learned in this section!*

![](./attachments/Pasted%20image%2020220703111128.png)

```bash
┌──(kali㉿kali)-[~]
└─$ curl -s 157.245.33.77:31130/serial.php -X POST -d "serial=7h15_15_a_s3cr37_m3554g3" 
HTB{ju57_4n07h3r_r4nd0m_53r14l}  
```

**Answer:** `HTB{ju57_4n07h3r_r4nd0m_53r14l}`

---
## Skills Assessment
### Question 1:
![](./attachments/Pasted%20image%2020220703104209.png)

Open the page and hit `[CTRL + U]`.

![](./attachments/Pasted%20image%2020220703111802.png)

**Answer:** `api.min.js`
 
### Question 2:
![](./attachments/Pasted%20image%2020220703104338.png)

*Hint: HTB{flag}*

Insert the JavaScript code into [jsnice.org](http://jsnice.org/) and watch the magic happen.

![](./attachments/Pasted%20image%2020220703111610.png)

**Answer:** `HTB{j4v45cr1p7_3num3r4710n_15_k3y}`

### Question 3:
![](./attachments/Pasted%20image%2020220703104348.png)

*Hint: Don't forget to stitch it together!*

Answer found in previous question.

**Answer:** `HTB{n3v3r_run_0bfu5c473d_c0d3!}`
 
### Question 4:
![](./attachments/Pasted%20image%2020220703104403.png)

The code is sending a POST request to "/keys.php".

```bash
┌──(kali㉿kali)-[~]
└─$ curl -s 206.189.25.173:30149/keys.php -X POST
4150495f70336e5f37333537316e365f31355f66756e
```

**Answer:** `4150495f70336e5f37333537316e365f31355f66756e`
### Question 5:
![](./attachments/Pasted%20image%2020220703104412.png)

First, decode the key.

![](./attachments/Pasted%20image%2020220703113036.png)

Then do the POST request with cURL.

```
┌──(kali㉿kali)-[~]
└─$ curl -s 206.189.25.173:30149/keys.php -X POST -d "key=API_p3n_73571n6_15_fun"
HTB{r34dy_70_h4ck_my_w4y_1n_2_HTB}
```

**Answer:** `HTB{r34dy_70_h4ck_my_w4y_1n_2_HTB}`

---
**Tags:** [[Hack The Box Academy]]