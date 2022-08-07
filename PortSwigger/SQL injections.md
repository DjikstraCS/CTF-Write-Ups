# SQL injections
* Source: [PortSwigger](https://portswigger.net)
* Number of labs: 16
* Completion date:  DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
* Difficulty: Appretice

### Question:
 This lab contains an SQL injection vulnerability in the product category filter. When the user selects a category, the application carries out an SQL query like the following:
 
```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

To solve the lab, perform an SQL injection attack that causes the application to display details of all products in any category, both released and unreleased. 

A webshop:

![](./attachments/Pasted%20image%2020220807102652.png)

Click on 'Gifts'.

Inject `' OR 1=1--` after the parameter value on each page in order to retrieve hidden data.

![](./attachments/Pasted%20image%2020220807102752.png)

Final executed query:

```
SELECT * FROM products WHERE category = 'Pets' OR 1=1--
```

---
## SQL injection vulnerability allowing login bypass
* Difficulty: Appretice

### Question:
This lab contains an SQL injection vulnerability in the login function.

To solve the lab, perform an SQL injection attack that logs in to the application as the `administrator` user. 

Find the login form and inject `' OR 1=1--` after the username `administrator`.

A dummy character is inserted in the password field, in this case `a`.

![](./attachments/Pasted%20image%2020220807103809.png)

Log in.

![](./attachments/Pasted%20image%2020220807104200.png)

---
## SQL injection UNION attack, determining the number of columns returned by the query
* Difficulty: Practitioner

### Question:
 This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing an SQL injection UNION attack that returns an additional row containing null values. 

The Page:

![](./attachments/Pasted%20image%2020220807110244.png)

Change the category's parameter value to `'+UNION+SELECT+NULL--` in order to try and determine how many collums are being returned by the query.

Insert additional `NULL` values untill the query executes without errors.

Payload `' UNION SELECT NULL,NULL,NULL--` returns no errors along with additional output.

![](./attachments/Pasted%20image%2020220807111010.png)

---
## 
* Difficulty: 

### Question:


**Answer:** ``

---
## 
* Difficulty: 

### Question:


**Answer:** ``

---
## 
* Difficulty: 

### Question:


**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]