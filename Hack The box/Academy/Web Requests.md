# Web Requests
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Web Requests
* Tier: 0
* Difficulty: Fundamental
* Topic: General
* Time estimate: 4 hours
* Date: 02-05-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## HypeText Transfer Protocol (HTTP)
![](./attachments/url_structure.png)

### Question:
![](./attachments/Pasted%20image%2020220502124757.png)

Using curl to connect.

```
┌──(kali㉿kali)-[~]
└─$ curl 157.245.42.82:31023/download.php   
HTB{64$!c_cURL_u$3r} 
```

**Answer:** `HTB{64$!c_cURL_u$3r}`

---
## HTTP Requests and Responses
### Question 1:
![](./attachments/Pasted%20image%2020220502102001.png)

*Hint: The request method is mentioned at the beginning of the HTTP request*

Open the page in Firefox and open DevTools/Inspector. In `Network` section we can see the requests. 

![](./attachments/Pasted%20image%2020220502094923.png)

**Answer:** `GET`

### Question 2:
![](./attachments/Pasted%20image%2020220502102147.png)

*Hint: The version is shown in the 'Server' response header*

Using curl to send a GET request, `-v` flag is used to get more information about the server:

```bash
┌──(kali㉿kali)-[~]
└─$ curl http://167.71.139.140:31808/ -v                       
*   Trying 167.71.139.140:31808...
* Connected to 167.71.139.140 (167.71.139.140) port 31808 (#0)
> GET / HTTP/1.1
> Host: 167.71.139.140:31808
> User-Agent: curl/7.82.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Mon, 02 May 2022 07:51:09 GMT
< Server: Apache/2.4.41 (Ubuntu)
```

**2nd answer:** `2.4.41`

---
## HTTP Headers

### Question:
![](./attachments/Pasted%20image%2020220502102920.png)

*Hint: Look for a request to a file called 'flag_...'. If you can't find it, refresh the page and monitor new requests.*

In the Network tab, we can see that a request for a `.txt` file is made.

![](./attachments/Pasted%20image%2020220502100059.png)

Let's check it out.

![](./attachments/Pasted%20image%2020220502100307.png)

**Answer:** `HTB{p493_r3qu3$t$_m0n!t0r}`

---
## GET

### Question:
![](./attachments/Pasted%20image%2020220502103054.png)

*Hint: Don't forget to set the user credentials when you send the 'search' request*

Open the page in Firefox and a login box pops up.

User:pass `admin:admin`

![](./attachments/Pasted%20image%2020220502103324.png)

A page with a search box, if we search for "flag" we can see the request in DevTools.

![](./attachments/Pasted%20image%2020220502103713.png)

With that knowledge, we can use curl to get the answer.

```bash
┌──(kali㉿kali)-[~]
└─$ curl --user admin:admin http://167.71.139.140:32154/search.php?search=flag
flag: HTB{curl_g3773r}

```

**Answer:** `HTB{curl_g3773r}`

---
## POST
### Question:
![](./attachments/Pasted%20image%2020220502104631.png)

*Hint: You may login through a browser and collect the cookie from the Storage tab. You may also use the '-i' or '-v' flags with cURL to view the response header and get the cookie.*

Login like last time.

User:pass `admin:admin`

![](./attachments/Pasted%20image%2020220502112718.png)

It's a page containing a search box.

![](./attachments/Pasted%20image%2020220502112605.png)

In the network section, we find the raw input.

![](./attachments/Pasted%20image%2020220502112846.png)

Likewise, if we do a search, we can get the URL and raw data from that request.

![](./attachments/Pasted%20image%2020220502121005.png)

Now we can recreate everything using cURL.

```bash
┌──(kali㉿kali)-[~]
└─$ curl -X POST -d 'username=admin&password=admin' http://157.245.46.136:30403/ -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 157.245.46.136:30403...
* Connected to 157.245.46.136 (157.245.46.136) port 30403 (#0)
> POST / HTTP/1.1
> Host: 157.245.46.136:30403
> User-Agent: curl/7.82.0
> Accept: */*
> Content-Length: 29
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Mon, 02 May 2022 09:38:30 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Set-Cookie: PHPSESSID=iisc7ljn107huqf218fhddjr9t; path=/
(...)
```

Now grab the cookie and use i to access the logged-in session.

```bash
┌──(kali㉿kali)-[~]
└─$ curl -b 'PHPSESSID=iisc7ljn107huqf218fhddjr9t' http://157.245.46.136:30403/
(...)
<em>Type a city name and hit <strong>Enter</strong></em>
(...)
```

Now we can search for `flag` via cURL, using the HTTP POST Method.

```bash
┌──(kali㉿kali)-[~]
└─$ curl -X POST -b 'PHPSESSID=iisc7ljn107huqf218fhddjr9t' -d '{"search":"flag"}' -H 'Content-Type: application/json' http://157.245.46.136:30403/search.php   
["flag: HTB{p0$t_r3p34t3r}"] 
```

**Answer:** `HTB{p0$t_r3p34t3r}`

---
## CRUD API
### Question:
![](./attachments/Pasted%20image%2020220502125859.png)

*Make sure that the number of cities is less than when you started. If you added any new cities, you should delete them as well.*

First confirm connection, we can use `jq` to show the output in JSON format and `-s` to remove the irrelevant data. 

```bash
┌──(kali㉿kali)-[~]
└─$ curl http://157.245.42.82:30154/api.php/city/london | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    46  100    46    0     0    546      0 --:--:-- --:--:-- --:--:--   547
[
  {
    "city_name": "London",
    "country_name": "(UK)"
  }
]
```

Using the following query to edit the name of 'London' to 'flag'.

```bash
┌──(kali㉿kali)-[~]
└─$ curl -X PUT http://157.245.42.82:30154/api.php/city/london -d '{"city_name":"flag", "country_name":"(UK)"}' -H 'Content-Type: application/json'

┌──(kali㉿kali)-[~]
└─$ curl -s http://157.245.42.82:30154/api.php/city/Lyngby | jq
[
  {
    "city_name": "flag",
    "country_name": "(UK)"
  }
]  
```

Delete the city of Boston. 

```bash
┌──(kali㉿kali)-[~]
└─$ curl -X DELETE http://157.245.42.82:30154/api.php/city/boston
```

Search for flag.

```bash
┌──(kali㉿kali)-[~]
└─$ curl -s http://157.245.42.82:30154/api.php/city/flag | jq 
[
  {
    "city_name": "flag",
    "country_name": "HTB{crud_4p!_m4n!pul4t0r}"
  }
]
```

**Answer:** `HTB{crud_4p!_m4n!pul4t0r}`

---
**Tags:** [[Hack The Box Academy]]