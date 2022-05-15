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

# TO BE CONTINUED...

---
## Active Infrastructure Identification
### Question 1:
![](./attachments/Pasted%20image%2020220509234536.png)



**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020220509234556.png)



**Answer:** ``

### Question 3:
![](./attachments/Pasted%20image%2020220509234610.png)



**Answer:** ``

---
## Active Subdomain Enumeration
### Question 1:
![](./attachments/Pasted%20image%2020220509235251.png)



**Answer:** ``

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