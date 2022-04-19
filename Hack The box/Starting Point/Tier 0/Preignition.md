# Preignition
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Preignition
* Topic: [[PHP]] [[Default Credentials]] [[gobuster]]
* Difficulty: Very easy
* Date: 15-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What is considered to be one of the most essential skills to possess as a Penetration Tester? 
 - **dir busting**
2. What switch do we use for nmap's scan to specify that we want to perform version detection 
- **-sV**
3. What service type is identified as running on port 80/tcp in our nmap scan? 
- **http**
4. What service name and version of service is running on port 80/tcp in our nmap scan? 
- **nginx 1.14.2**
5. What is a popular directory busting tool we can use to explore hidden web directories and resources? 
- **gobuster**
6. What switch do we use to specify to gobuster we want to perform dir busting specifically? 
- **dir**
7. What page is found during our dir busting activities? 
- **admin.php**
8. What is the status code reported by gobuster upon finding a successful page? 
- **200**

---
## Flag:
First, we need to scan the target with `nmap`.

Command:

`nmap -n -sC -sV 10.129.92.154`

`-n`: No DNS look up (Good [OPSEC](https://en.wikipedia.org/wiki/Operations_security)).

`-sC`: Run scripts during scan.

`-sV`: Try to detect the version of running services.

```console
┌──(kali㉿kali)-[~]
└─$ nmap -n -sC -sV 10.129.92.154
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-15 10:33 EDT
Nmap scan report for 10.129.92.154
Host is up (0.070s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.2
|_http-server-header: nginx/1.14.2
|_http-title: Welcome to nginx!

Nmap done: 1 IP address (1 host up) scanned in 9.94 seconds
```

It's a simple web sever hosting HTTP on port 80.

![](./attachments/Pasted%20image%2020220415165113.png)

Just a page confirming that the web server was installed correctly, so no interaction.

We can use gobuster to find out if there are any more "hidden" directories on this site.

Command:

`gobuster dir \ 10.129.92.154 --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php,html`

`dir`: Enumerate directories, not DNS ex.

`--wordlist`: Use this list (list of common directory names).

`-x`: Find files in .php and .html format.

```console
┌──(kali㉿kali)-[~]
└─$ gobuster dir --url 10.129.92.154 --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php,html
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.92.154
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,html
[+] Timeout:                 10s
===============================================================
2022/04/15 10:41:10 Starting gobuster in directory enumeration mode
===============================================================
/admin.php            (Status: 200) [Size: 999]
```

Like the name indicates, this is an admin login page.

![](./attachments/Pasted%20image%2020220415170642.png)

This is probably not very secure, we can try the most common login credential:

user:pass `admin:admin`

![](./attachments/Pasted%20image%2020220415171032.png)

We got the flag!

**Flag:** `6483bee07c1c1d57f14e5b0717503c73`

---
**Tags:** [[HackTheBox]]