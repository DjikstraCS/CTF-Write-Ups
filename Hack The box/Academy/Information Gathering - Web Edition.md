# Web Requests
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Information Gathering - Web Edition
* Tier: II
* Difficulty: Easy
* Category: Offensive
* Time estimate: 7 hours
* Date: 09-05-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## WHOIS
### Question 1:
![](./attachments/Pasted%20image%2020220509221547.png)

```bash
┌──(kali㉿kali)-[~]
└─$ whois paypal.com  
Domain Name: PAYPAL.COM
Registry Domain ID: 8017040_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.markmonitor.com
Registrar URL: http://www.markmonitor.com
Updated Date: 2021-06-13T09:21:55Z
Creation Date: 1999-07-15T05:32:11Z
Registry Expiry Date: 2022-07-15T05:32:11Z
Registrar: MarkMonitor Inc.
Registrar IANA ID: 292
Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
Registrar Abuse Contact Phone: +1.2086851750

(...)
```

**Answer:** `292`

### Question 2:
![](./attachments/Pasted%20image%2020220509221602.png)

```bash
┌──(kali㉿kali)-[~]
└─$ whois venmo.com | grep -E "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b"
Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
Registrant Email: hostmaster@paypal.com
Admin Email: hostmaster@paypal.com
your request and the reasons for your request to whoisrequest@markmonitor.com
```


**Answer:** `hostmaster@paypal.com`

---
## DNS
### Question 1:
![](./attachments/Pasted%20image%2020220509223616.png)

We can use `dig` to make DNS lookups.

```bash
┌──(kali㉿kali)-[~]
└─$ dig paydiant.com                                         

; <<>> DiG 9.18.0-2-Debian <<>> paydiant.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 760
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 4, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0x0005, udp: 4096
; COOKIE: a5bf18f0d23db725f087fa7a627980afe3167e543b3abd40 (good)
;; QUESTION SECTION:
;paydiant.com.                  IN      A

;; ANSWER SECTION:
paydiant.com.           5       IN      A       204.74.99.103

;; AUTHORITY SECTION:
paydiant.com.           5       IN      NS      edns3.ultradns.net.
paydiant.com.           5       IN      NS      edns3.ultradns.org.
paydiant.com.           5       IN      NS      edns3.ultradns.biz.
paydiant.com.           5       IN      NS      edns3.ultradns.com.

;; Query time: 163 msec
;; SERVER: 192.168.47.2#53(192.168.47.2) (UDP)
;; WHEN: Mon May 09 16:59:27 EDT 2022
;; MSG SIZE  rcvd: 210
```

**Answer:** `204.74.99.103`

### Question 2:
![](./attachments/Pasted%20image%2020220509223627.png)

PTR records can be collected with the `-x` flag.

```bash
┌──(kali㉿kali)-[~]
└─$ dig -x 173.0.87.51

; <<>> DiG 9.18.0-2-Debian <<>> -x 173.0.87.51
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 57964
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0x0005, udp: 4096
; COOKIE: fdbedda77a9cdb788ff9682c62798180f51e4f1d754b73ab (good)
;; QUESTION SECTION:
;51.87.0.173.in-addr.arpa.      IN      PTR

;; ANSWER SECTION:
51.87.0.173.in-addr.arpa. 5     IN      PTR     cloudmonitor30.paypal.com.

;; Query time: 353 msec
;; SERVER: 192.168.47.2#53(192.168.47.2) (UDP)
;; WHEN: Mon May 09 17:02:57 EDT 2022
;; MSG SIZE  rcvd: 120
```


**Answer:** `cloudmonitor30.paypal.com`

### Question 3:
![](./attachments/Pasted%20image%2020220509223635.png)

Use `mx` to get MX records.

```bash
┌──(kali㉿kali)-[~]
└─$ dig mx paypal.com 

; <<>> DiG 9.18.0-2-Debian <<>> mx paypal.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 29302
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 2, AUTHORITY: 4, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0x0005, udp: 4096
; COOKIE: e0a72694b8c04015b946db4562798235ba2115a69f4f6c1f (good)
;; QUESTION SECTION:
;paypal.com.                    IN      MX

;; ANSWER SECTION:
paypal.com.             5       IN      MX      10 mx1.paypalcorp.com.
paypal.com.             5       IN      MX      10 mx2.paypalcorp.com.

;; AUTHORITY SECTION:
paypal.com.             5       IN      NS      ns2.p57.dynect.net.
paypal.com.             5       IN      NS      pdns100.ultradns.com.
paypal.com.             5       IN      NS      ns1.p57.dynect.net.
paypal.com.             5       IN      NS      pdns100.ultradns.net.

;; Query time: 1301 msec
;; SERVER: 192.168.47.2#53(192.168.47.2) (UDP)
;; WHEN: Mon May 09 17:05:58 EDT 2022
;; MSG SIZE  rcvd: 230
```

**Answer:** `mx1.paypalcorp.com`

---
## Active Infrastructure Identification
### Question 1:
![](./attachments/Pasted%20image%2020220509234536.png)

```bash
┌──(kali㉿kali)-[~]
└─$ sudo nmap -n -sC -sV app.inlanefreight.local
[sudo] password for kali: 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-19 12:53 EDT
Nmap scan report for app.inlanefreight.local (10.129.94.191)
Host is up (0.041s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f:4c:8f:10:f1:ae:be:cd:31:24:7c:a1:4e:ab:84:6d (RSA)
|   256 7b:30:37:67:50:b9:ad:91:c0:8f:f7:02:78:3b:7c:02 (ECDSA)
|_  256 88:9e:0e:07:fe:ca:d0:5c:60:ab:cf:10:99:cd:6c:a7 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-robots.txt: 15 disallowed entries 
| /joomla/administrator/ /administrator/ /bin/ /cache/ 
| /cli/ /components/ /includes/ /installation/ /language/ 
|_/layouts/ /libraries/ /logs/ /modules/ /plugins/ /tmp/
|_http-generator: Joomla! - Open Source Content Management
|_http-title: Home
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.68 seconds
```

```bash
┌──(kali㉿kali)-[~]
└─$ curl -I app.inlanefreight.local               
HTTP/1.1 200 OK
Date: Thu, 19 May 2022 16:58:17 GMT
Server: Apache/2.4.41 (Ubuntu)
Set-Cookie: 72af8f2b24261272e581a49f5c56de40=67unee4eqth2shdqd62rfhb4q2; path=/; HttpOnly
Permissions-Policy: interest-cohort=()
Expires: Wed, 17 Aug 2005 00:00:00 GMT
Last-Modified: Thu, 19 May 2022 16:58:17 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Content-Type: text/html; charset=utf-8
```

Command: `whatweb -a3 app.inlanefreight.local -v`

`-a3`: Aggressiveness 1-5

`-v`: Verbose

```bash
┌──(kali㉿kali)-[~]
└─$ whatweb -a3 app.inlanefreight.local -v 
WhatWeb report for http://app.inlanefreight.local
Status    : 200 OK
Title     : Home
IP        : 10.129.94.191
Country   : RESERVED, ZZ

Summary   : Apache[2.4.41], Bootstrap, Cookies[72af8f2b24261272e581a49f5c56de40], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], HttpOnly[72af8f2b24261272e581a49f5c56de40], JQuery, MetaGenerator[Joomla! - Open Source Content Management], OpenSearch[http://app.inlanefreight.local/index.php/component/search/?layout=blog&amp;id=9&amp;Itemid=101&amp;format=opensearch], Script, UncommonHeaders[permissions-policy]

Detected Plugins:
[ Apache ]
        The Apache HTTP Server Project is an effort to develop and 
        maintain an open-source HTTP server for modern operating 
        systems including UNIX and Windows NT. The goal of this 
        project is to provide a secure, efficient and extensible 
        server that provides HTTP services in sync with the current 
        HTTP standards. 

        Version      : 2.4.41 (from HTTP Server Header)
        Google Dorks: (3)
        Website     : http://httpd.apache.org/

[ Bootstrap ]
        Bootstrap is an open source toolkit for developing with 
        HTML, CSS, and JS. 

        Website     : https://getbootstrap.com/

[ Cookies ]
        Display the names of cookies in the HTTP headers. The 
        values are not returned to save on space. 

        String       : 72af8f2b24261272e581a49f5c56de40

[ HTML5 ]
        HTML version 5, detected by the doctype declaration 


[ HTTPServer ]
        HTTP server header string. This plugin also attempts to 
        identify the operating system from the server header. 

        OS           : Ubuntu Linux
        String       : Apache/2.4.41 (Ubuntu) (from server string)

[ HttpOnly ]
        If the HttpOnly flag is included in the HTTP set-cookie 
        response header and the browser supports it then the cookie 
        cannot be accessed through client side script - More Info: 
        http://en.wikipedia.org/wiki/HTTP_cookie 

        String       : 72af8f2b24261272e581a49f5c56de40

[ JQuery ]
        A fast, concise, JavaScript that simplifies how to traverse 
        HTML documents, handle events, perform animations, and add 
        AJAX. 

        Website     : http://jquery.com/

[ MetaGenerator ]
        This plugin identifies meta generator tags and extracts its 
        value. 

        String       : Joomla! - Open Source Content Management

[ OpenSearch ]
        This plugin identifies open search and extracts the URL. 
        OpenSearch is a collection of simple formats for the 
        sharing of search results. 

        String       : http://app.inlanefreight.local/index.php/component/search/?layout=blog&amp;id=9&amp;Itemid=101&amp;format=opensearch

[ Script ]
        This plugin detects instances of script HTML elements and 
        returns the script language/type. 


[ UncommonHeaders ]
        Uncommon HTTP server headers. The blacklist includes all 
        the standard headers and many non standard but common ones. 
        Interesting but fairly common headers should have their own 
        plugins, eg. x-powered-by, server and x-aspnet-version. 
        Info about headers can be found at www.http-stats.com 

        String       : permissions-policy (from headers)

HTTP Headers:
        HTTP/1.1 200 OK
        Date: Thu, 19 May 2022 17:00:16 GMT
        Server: Apache/2.4.41 (Ubuntu)
        Set-Cookie: 72af8f2b24261272e581a49f5c56de40=dvvqpdnv6apl3ku89mfraebv4f; path=/; HttpOnly
        Permissions-Policy: interest-cohort=()
        Expires: Wed, 17 Aug 2005 00:00:00 GMT
        Last-Modified: Thu, 19 May 2022 17:00:16 GMT
        Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
        Pragma: no-cache
        Vary: Accept-Encoding
        Content-Encoding: gzip
        Content-Length: 4127
        Connection: close
        Content-Type: text/html; charset=utf-8
```

```bash
┌──(kali㉿kali)-[~]
└─$ wafw00f -v http://app.inlanefreight.local

                   ______
                  /      \
                 (  Woof! )
                  \  ____/                      )
                  ,,                           ) (_
             .-. -    _______                 ( |__|
            ()``; |==|_______)                .)|__|
            / ('        /|\                  (  |__|
        (  /  )        / | \                  . |__|
         \(_)_))      /  |  \                   |__|

                    ~ WAFW00F : v2.1.0 ~
    The Web Application Firewall Fingerprinting Toolkit

[*] Checking http://app.inlanefreight.local
[+] Generic Detection results:
[-] No WAF detected by the generic detection
[~] Number of requests: 7
```

`Aquatone` is another useful tool used for bulk lookup of domains.

```bash
cat facebook_aquatone.txt | aquatone -out ./aquatone -screenshot-timeout 1000
```

```bash
┌──(kali㉿kali)-[~]
└─$ curl -I app.inlanefreight.local
HTTP/1.1 200 OK
Date: Thu, 30 Jun 2022 11:51:17 GMT
Server: Apache/2.4.41 (Ubuntu)
```

**Answer:** `2.4.41`

### Question 2:
![](./attachments/Pasted%20image%2020220509234556.png)

The answer was collected in the previous question.

**Answer:** `Joomla!`

### Question 3:
![](./attachments/Pasted%20image%2020220509234610.png)

The answer was collected in the previous question.

**Answer:** `Ubuntu`

---
## Active Subdomain Enumeration
### Question 1:
![](./attachments/Pasted%20image%2020220509235251.png)


Manual zone transfer:
```
┌──(kali㉿kali)-[~]
└─$ nslookup -query=NS inlanefreight.htb 10.129.158.69
Server:         10.129.158.69
Address:        10.129.158.69#53

inlanefreight.htb       nameserver = ns.inlanefreight.htb.
```

```                                                
┌──(kali㉿kali)-[~]
└─$ dig ns inlanefreight.htb @10.129.158.69 

; <<>> DiG 9.18.1-1-Debian <<>> ns inlanefreight.htb @10.129.158.69
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 45091
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 2
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: 8e5057a54a858e9c0100000062beb92e2c06292e4fb836e1 (good)
;; QUESTION SECTION:
;inlanefreight.htb.             IN      NS

;; ANSWER SECTION:
inlanefreight.htb.      604800  IN      NS      ns.inlanefreight.htb.

;; ADDITIONAL SECTION:
ns.inlanefreight.htb.   604800  IN      A       127.0.0.1

;; Query time: 39 msec
;; SERVER: 10.129.158.69#53(10.129.158.69) (UDP)
;; WHEN: Fri Jul 01 05:06:54 EDT 2022
;; MSG SIZE  rcvd: 107
```

**Answer:** `ns.inlanefreight.htb`

### Question 2:
![](./attachments/Pasted%20image%2020220509235308.png)

*Hint: If the DNS is misconfigured and allows zone transfer, the individual zones for domains and subdomains can be queried accordingly.*

```
┌──(kali㉿kali)-[~]
└─$ nslookup -type=any -query=AXFR inlanefreight.htb 10.129.158.69       
Server:         10.129.158.69
Address:        10.129.158.69#53

inlanefreight.htb
        origin = inlanefreight.htb
        mail addr = root.inlanefreight.htb
        serial = 2
        refresh = 604800
        retry = 86400
        expire = 2419200
        minimum = 604800
inlanefreight.htb       nameserver = ns.inlanefreight.htb.
Name:   admin.inlanefreight.htb
Address: 10.10.34.2
Name:   ftp.admin.inlanefreight.htb
Address: 10.10.34.2
Name:   careers.inlanefreight.htb
Address: 10.10.34.50
Name:   dc1.inlanefreight.htb
Address: 10.10.34.16
Name:   dc2.inlanefreight.htb
Address: 10.10.34.11
Name:   internal.inlanefreight.htb
Address: 127.0.0.1
Name:   admin.internal.inlanefreight.htb
Address: 10.10.1.11
Name:   wsus.internal.inlanefreight.htb
Address: 10.10.1.240
Name:   ir.inlanefreight.htb
Address: 10.10.45.5
Name:   dev.ir.inlanefreight.htb
Address: 10.10.45.6
Name:   ns.inlanefreight.htb
Address: 127.0.0.1
Name:   resources.inlanefreight.htb
Address: 10.10.34.100
Name:   securemessaging.inlanefreight.htb
Address: 10.10.34.52
Name:   test1.inlanefreight.htb
Address: 10.10.34.101
Name:   us.inlanefreight.htb
Address: 10.10.200.5
Name:   cluster14.us.inlanefreight.htb
Address: 10.10.200.14
Name:   messagecenter.us.inlanefreight.htb
Address: 10.10.200.10
Name:   ww02.inlanefreight.htb
Address: 10.10.34.112
Name:   www1.inlanefreight.htb
Address: 10.10.34.111
inlanefreight.htb
        origin = inlanefreight.htb
        mail addr = root.inlanefreight.htb
        serial = 2
        refresh = 604800
        retry = 86400
        expire = 2419200
        minimum = 604800
```

```
┌──(kali㉿kali)-[~]
└─$ dig AXFR inlanefreight.htb @10.129.158.69

; <<>> DiG 9.18.1-1-Debian <<>> AXFR inlanefreight.htb @10.129.158.69
;; global options: +cmd
inlanefreight.htb.      604800  IN      SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
inlanefreight.htb.      604800  IN      NS      ns.inlanefreight.htb.
admin.inlanefreight.htb. 604800 IN      A       10.10.34.2
ftp.admin.inlanefreight.htb. 604800 IN  A       10.10.34.2
careers.inlanefreight.htb. 604800 IN    A       10.10.34.50
dc1.inlanefreight.htb.  604800  IN      A       10.10.34.16
dc2.inlanefreight.htb.  604800  IN      A       10.10.34.11
internal.inlanefreight.htb. 604800 IN   A       127.0.0.1
admin.internal.inlanefreight.htb. 604800 IN A   10.10.1.11
wsus.internal.inlanefreight.htb. 604800 IN A    10.10.1.240
ir.inlanefreight.htb.   604800  IN      A       10.10.45.5
dev.ir.inlanefreight.htb. 604800 IN     A       10.10.45.6
ns.inlanefreight.htb.   604800  IN      A       127.0.0.1
resources.inlanefreight.htb. 604800 IN  A       10.10.34.100
securemessaging.inlanefreight.htb. 604800 IN A  10.10.34.52
test1.inlanefreight.htb. 604800 IN      A       10.10.34.101
us.inlanefreight.htb.   604800  IN      A       10.10.200.5
cluster14.us.inlanefreight.htb. 604800 IN A     10.10.200.14
messagecenter.us.inlanefreight.htb. 604800 IN A 10.10.200.10
ww02.inlanefreight.htb. 604800  IN      A       10.10.34.112
www1.inlanefreight.htb. 604800  IN      A       10.10.34.111
inlanefreight.htb.      604800  IN      SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 40 msec
;; SERVER: 10.129.158.69#53(10.129.158.69) (TCP)
;; WHEN: Fri Jul 01 05:12:54 EDT 2022
;; XFR size: 22 records (messages 1, bytes 594)
```


**Answer:** `2`

### Question 3:
![](./attachments/Pasted%20image%2020220509235319.png)

*Hint: One of the existing zones contains a TXT record.*

```
┌──(kali㉿kali)-[~]
└─$ dig axfr internal.inlanefreight.htb @10.129.158.69      

; <<>> DiG 9.18.1-1-Debian <<>> axfr internal.inlanefreight.htb @10.129.158.69
;; global options: +cmd
internal.inlanefreight.htb. 604800 IN   SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
internal.inlanefreight.htb. 604800 IN   TXT     "ZONE_TRANSFER{87o2z3cno7zsoiedznxoi82z3o47xzhoi}"
internal.inlanefreight.htb. 604800 IN   NS      ns.inlanefreight.htb.
dev.admin.internal.inlanefreight.htb. 604800 IN A 10.10.1.2
panel.admin.internal.inlanefreight.htb. 604800 IN A 10.10.1.2
printer.admin.internal.inlanefreight.htb. 604800 IN A 10.10.1.3
dc3.internal.inlanefreight.htb. 604800 IN A     10.10.1.5
ns.internal.inlanefreight.htb. 604800 IN A      127.0.0.1
ns2.internal.inlanefreight.htb. 604800 IN A     10.10.34.136
ws1.internal.inlanefreight.htb. 604800 IN A     10.10.2.11
ws2.internal.inlanefreight.htb. 604800 IN A     10.10.3.12
internal.inlanefreight.htb. 604800 IN   SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 36 msec
;; SERVER: 10.129.158.69#53(10.129.158.69) (TCP)
;; WHEN: Fri Jul 01 05:59:41 EDT 2022
;; XFR size: 12 records (messages 1, bytes 435)
```


**Answer:** `ZONE_TRANSFER{87o2z3cno7zsoiedznxoi82z3o47xzhoi}`

### Question 4:
![](./attachments/Pasted%20image%2020220509235340.png)

The answer is under question 3.

**Answer:** `ns2.internal.inlanefreight.htb`

### Question 5:
![](./attachments/Pasted%20image%2020220509235351.png)

The answer is under question 3.

**Answer:** `dc3.internal.inlanefreight.htb`

### Question 6:
![](./attachments/Pasted%20image%2020220509235402.png)

The answer is under question 2.

**Answer:** `10.10.200.5`

### Question 7:
![](./attachments/Pasted%20image%2020220509235415.png)

*Hint: There are several zones.*

Adding the number of A records from question 2 and 3 together.

**Answer:** `27`

---
## Virtual Hosts
### Question 1:
![](./attachments/Pasted%20image%2020220509235436.png)

Using FFuF to enumerate virtual hosts with Fuzzing.

```
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/DNS/namelist.txt -u http://10.129.165.231 -H "HOST: FUZZ.inlanefreight.htb" -fs 10918

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://10.129.165.231
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/namelist.txt
 :: Header           : Host: FUZZ.inlanefreight.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 10918
________________________________________________

ap                      [Status: 200, Size: 102, Words: 3, Lines: 6, Duration: 74ms]
app                     [Status: 200, Size: 103, Words: 3, Lines: 6, Duration: 46ms]
citrix                  [Status: 200, Size: 100, Words: 3, Lines: 6, Duration: 118ms]
customers               [Status: 200, Size: 94, Words: 3, Lines: 6, Duration: 69ms]
dmz                     [Status: 200, Size: 95, Words: 2, Lines: 6, Duration: 60ms]
www2                    [Status: 200, Size: 96, Words: 2, Lines: 6, Duration: 50ms]
:: Progress: [151265/151265] :: Job [1/1] :: 725 req/sec :: Duration: [0:04:27] :: Errors: 0 ::
```

Adding the pages to the `/etc/hosts` file.

![](./attachments/Pasted%20image%2020220701141121.png)

Opening the pages one by one in the browser:

![](./attachments/Pasted%20image%2020220701141422.png)

**Answer:** `HTB{h8973hrpiusnzjoie7zrou23i4zhmsxi8732zjso}`

### Question 2:
![](./attachments/Pasted%20image%2020220509235445.png)

![](./attachments/Pasted%20image%2020220701141359.png)

**Answer:** `HTB{u23i4zhmsxi872z3rn98h7nh2sxnbgriusd32zjso}`

### Question 3:
![](./attachments/Pasted%20image%2020220509235455.png)

![](./attachments/Pasted%20image%2020220701141336.png)

**Answer:** `HTB{Fl4gF0uR_o8763tznb4xou7zhgsniud7gfi734}`

### Question 4:
![](./attachments/Pasted%20image%2020220509235507.png)

![](./attachments/Pasted%20image%2020220701141321.png)

**Answer:** `HTB{bzghi7tghin2u76x3ghdni62higz7x3s}`

### Question 5:
![](./attachments/Pasted%20image%2020220509235516.png)

![](./attachments/Pasted%20image%2020220701141302.png)

**Answer:** `HTB{7zbnr4i3n7zhrxn347zhh3dnrz4dh7zdjfbgn6d}`

---
## Skills Assessment
### Question 1:
![](./attachments/Pasted%20image%2020220509235537.png)



**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020220509235547.png)

*Hint: There is a 5 in the FQDN*



**Answer:** ``

### Question 3:
![](./attachments/Pasted%20image%2020220509235559.png)



**Answer:** ``

### Question 4:
![](./attachments/Pasted%20image%2020220509235613.png)

*Hint: Try to use a tool like 'sublist3r'*



**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]