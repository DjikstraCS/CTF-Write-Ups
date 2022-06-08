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

Zone Transfer:

[hackertarget.com](https://hackertarget.com/zone-transfer/)

Manual zone transfer:

```bash
DjikstraCS@htb[/htb]$ nslookup -type=NS zonetransfer.me

Server:		10.100.0.1
Address:	10.100.0.1#53

Non-authoritative answer:
zonetransfer.me	nameserver = nsztm2.digi.ninja.
zonetransfer.me	nameserver = nsztm1.digi.ninja.
```

```bash
DjikstraCS@htb[/htb]$ nslookup -type=any -query=AXFR zonetransfer.me nsztm1.digi.ninja

Server:		nsztm1.digi.ninja
Address:	81.4.108.41#53

zonetransfer.me
	origin = nsztm1.digi.ninja
	mail addr = robin.digi.ninja
	serial = 2019100801
	refresh = 172800
	retry = 900
	expire = 1209600
	minimum = 3600
zonetransfer.me	hinfo = "Casio fx-700G" "Windows XP"
zonetransfer.me	text = "google-site-verification=tyP28J7JAUHA9fw2sHXMgcCC0I6XBmmoVi04VlMewxA"
zonetransfer.me	mail exchanger = 0 ASPMX.L.GOOGLE.COM.
zonetransfer.me	mail exchanger = 10 ALT1.ASPMX.L.GOOGLE.COM.
zonetransfer.me	mail exchanger = 10 ALT2.ASPMX.L.GOOGLE.COM.
zonetransfer.me	mail exchanger = 20 ASPMX2.GOOGLEMAIL.COM.
zonetransfer.me	mail exchanger = 20 ASPMX3.GOOGLEMAIL.COM.
zonetransfer.me	mail exchanger = 20 ASPMX4.GOOGLEMAIL.COM.
zonetransfer.me	mail exchanger = 20 ASPMX5.GOOGLEMAIL.COM.
Name:	zonetransfer.me
Address: 5.196.105.14
zonetransfer.me	nameserver = nsztm1.digi.ninja.
zonetransfer.me	nameserver = nsztm2.digi.ninja.
_acme-challenge.zonetransfer.me	text = "6Oa05hbUJ9xSsvYy7pApQvwCUSSGgxvrbdizjePEsZI"
_sip._tcp.zonetransfer.me	service = 0 0 5060 www.zonetransfer.me.
14.105.196.5.IN-ADDR.ARPA.zonetransfer.me	name = www.zonetransfer.me.
asfdbauthdns.zonetransfer.me	afsdb = 1 asfdbbox.zonetransfer.me.
Name:	asfdbbox.zonetransfer.me
Address: 127.0.0.1
asfdbvolume.zonetransfer.me	afsdb = 1 asfdbbox.zonetransfer.me.
Name:	canberra-office.zonetransfer.me
Address: 202.14.81.230
cmdexec.zonetransfer.me	text = "; ls"
contact.zonetransfer.me	text = "Remember to call or email Pippa on +44 123 4567890 or pippa@zonetransfer.me when making DNS changes"
Name:	dc-office.zonetransfer.me
Address: 143.228.181.132
Name:	deadbeef.zonetransfer.me
Address: dead:beaf::
dr.zonetransfer.me	loc = 53 20 56.558 N 1 38 33.526 W 0.00m 1m 10000m 10m
DZC.zonetransfer.me	text = "AbCdEfG"
email.zonetransfer.me	naptr = 1 1 "P" "E2U+email" "" email.zonetransfer.me.zonetransfer.me.
Name:	email.zonetransfer.me
Address: 74.125.206.26
Hello.zonetransfer.me	text = "Hi to Josh and all his class"
Name:	home.zonetransfer.me
Address: 127.0.0.1
Info.zonetransfer.me	text = "ZoneTransfer.me service provided by Robin Wood - robin@digi.ninja. See http://digi.ninja/projects/zonetransferme.php for more information."
internal.zonetransfer.me	nameserver = intns1.zonetransfer.me.
internal.zonetransfer.me	nameserver = intns2.zonetransfer.me.
Name:	intns1.zonetransfer.me
Address: 81.4.108.41
Name:	intns2.zonetransfer.me
Address: 167.88.42.94
Name:	office.zonetransfer.me
Address: 4.23.39.254
Name:	ipv6actnow.org.zonetransfer.me
Address: 2001:67c:2e8:11::c100:1332
Name:	owa.zonetransfer.me
Address: 207.46.197.32
robinwood.zonetransfer.me	text = "Robin Wood"
rp.zonetransfer.me	rp = robin.zonetransfer.me. robinwood.zonetransfer.me.
sip.zonetransfer.me	naptr = 2 3 "P" "E2U+sip" "!^.*$!sip:customer-service@zonetransfer.me!" .
sqli.zonetransfer.me	text = "' or 1=1 --"
sshock.zonetransfer.me	text = "() { :]}; echo ShellShocked"
staging.zonetransfer.me	canonical name = www.sydneyoperahouse.com.
Name:	alltcpportsopen.firewall.test.zonetransfer.me
Address: 127.0.0.1
testing.zonetransfer.me	canonical name = www.zonetransfer.me.
Name:	vpn.zonetransfer.me
Address: 174.36.59.154
Name:	www.zonetransfer.me
Address: 5.196.105.14
xss.zonetransfer.me	text = "'><script>alert('Boo')</script>"
zonetransfer.me
	origin = nsztm1.digi.ninja
	mail addr = robin.digi.ninja
	serial = 2019100801
	refresh = 172800
	retry = 900
	expire = 1209600
	minimum = 3600
```

**Answer:** ``

# TO BE CONTINUED...

### Question 2:
![](./attachments/Pasted%20image%2020220509235308.png)

*Hint: If the DNS is misconfigured and allows zone transfer, the individual zones for domains and subdomains can be queried accordingly.*



**Answer:** ``

### Question 3:
![](./attachments/Pasted%20image%2020220509235319.png)

*Hint: One of the existing zones contains a TXT record.*



**Answer:** ``

### Question 4:
![](./attachments/Pasted%20image%2020220509235340.png)



**Answer:** ``

### Question 5:
![](./attachments/Pasted%20image%2020220509235351.png)



**Answer:** ``

### Question 6:
![](./attachments/Pasted%20image%2020220509235402.png)



**Answer:** ``

### Question 7:
![](./attachments/Pasted%20image%2020220509235415.png)

*Hint: There are several zones.*



**Answer:** ``

---
## Virtual Hosts
### Question 1:
![](./attachments/Pasted%20image%2020220509235436.png)



**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020220509235445.png)



**Answer:** ``

### Question 3:
![](./attachments/Pasted%20image%2020220509235455.png)



**Answer:** ``

### Question 4:
![](./attachments/Pasted%20image%2020220509235507.png)



**Answer:** ``

### Question 5:
![](./attachments/Pasted%20image%2020220509235516.png)



**Answer:** ``

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