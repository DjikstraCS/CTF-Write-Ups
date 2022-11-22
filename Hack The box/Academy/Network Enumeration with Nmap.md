* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Network Enumeration with Nmap
* Tier: I
* Difficulty: Easy
* Category: Offensive
* Time estimate: 7 hours
* Date: 12-11-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)


---
## Host Discovery
### Question:
![](./attachments/Pasted%20image%2020221107111839.png)

*Hint: The information that gives us such an indication is Time-To-Live (TTL). There exist a lot of different overviews with different protocols giving us an overview of which systems work specific TTL values.*

Different opearting systems have different TTL's hardcoded intor their protocol, a list of TTL's can be found [here](https://ostechnix.com/identify-operating-system-ttl-ping/). In this case the TTL is 128 and our target is therefore likely a Windows machine.

**Answer:** `Windows`

---
## Host and Port Scanning
### Question:
![](./attachments/Pasted%20image%2020221107110623.png)

```
┌──(kali㉿kali)-[~]
└─$ sudo nmap 10.129.2.49 -n 
[sudo] password for kali: 
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-07 06:30 EST
Nmap scan report for 10.129.2.49
Host is up (0.16s latency).
Not shown: 993 closed tcp ports (reset)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
110/tcp   open  pop3
139/tcp   open  netbios-ssn
143/tcp   open  imap
445/tcp   open  microsoft-ds
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 5.26 seconds
```

7 TCP ports are open.

**Answer:** `7`

### Question:
![](./attachments/Pasted%20image%2020221107110831.png)

```
┌──(kali㉿kali)-[~]
└─$ sudo nmap 10.129.2.49 -n -sV
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-07 06:32 EST
Nmap scan report for 10.129.2.49
Host is up (0.046s latency).
Not shown: 993 closed tcp ports (reset)
PORT      STATE SERVICE     VERSION
22/tcp    open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http        Apache httpd 2.4.18 ((Ubuntu))
110/tcp   open  pop3        Dovecot pop3d
139/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp   open  imap        Dovecot imapd
445/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
31337/tcp open  Elite?
Service Info: Host: NIX-NMAP-DEFAULT; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 159.95 seconds
```

The hostname is: `NIX-NMAP-DEFAULT`

**Answer:** `nix-nmap-default`

---
## Saving the Results
### Question:
![](./attachments/Pasted%20image%2020221107111105.png)

```
┌──(kali㉿kali)-[~]
└─$ sudo nmap 10.129.2.49 -n -oX Downloads/target.xml
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-07 06:44 EST
Nmap scan report for 10.129.2.49
Host is up (0.046s latency).
Not shown: 993 closed tcp ports (reset)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
110/tcp   open  pop3
139/tcp   open  netbios-ssn
143/tcp   open  imap
445/tcp   open  microsoft-ds
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 0.88 seconds

┌──(kali㉿kali)-[~]
└─$ cd Downloads 

┌──(kali㉿kali)-[~/Downloads]
└─$ xsltproc target.xml -o target.html
```

![](./attachments/Pasted%20image%2020221107124946.png)

**Answer:** `31337`

---
## Service Enumeration
### Question:
![](./attachments/Pasted%20image%2020221107111221.png)
*Hint: Remember that Nmap does not always recognize all information by default.*

Connecting to the last service on port 31337 reveals the flag. nmap and tcpdump are not able to catch it.

```
┌──(kali㉿kali)-[~]
└─$ nc -nv 10.129.140.150 31337
(UNKNOWN) [10.129.140.150] 31337 (?) open
220 HTB{pr0F7pDv3r510nb4nn3r}
```

**Answer:** `HTB{pr0F7pDv3r510nb4nn3r`

---
## Nmap Scripting Engine
### Question:
![](./attachments/Pasted%20image%2020221108133824.png)
*Hint: Web servers are among the most attacked services because they are made accessible to users and present a high attack potential.*

The `http-enum` script returns the presence a robot.txt file.

```
┌──(kali㉿kali)-[~]
└─$ sudo nmap 10.129.2.49 -p 80 -sV --script http-enum
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-08 07:29 EST
Stats: 0:00:43 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 97.73% done; ETC: 07:30 (0:00:01 remaining)
Nmap scan report for 10.129.2.49
Host is up (0.038s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-enum: 
|_  /robots.txt: Robots file
|_http-server-header: Apache/2.4.18 (Ubuntu)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 245.44 seconds

┌──(kali㉿kali)-[~]
└─$ sudo curl 10.129.2.49/robots.txt
User-agent: *

Allow: /

HTB{873nniuc71bu6usbs1i96as6dsv26}
```

**Answer:** `HTB{873nniuc71bu6usbs1i96as6dsv26}`

---
## Firewall and IDS/IPS Evasion - Easy Lab
### Question:
![](./attachments/Pasted%20image%2020221108142618.png)
*Hint: Remember, you don't need to provide a version of it. Think about which services can give you information about the operating system. After interviewing the administrators, we found out that they want to prevent neighboring hosts of their /24 subnet mask from communicating with each other.*

```
┌──(kali㉿kali)-[~]
└─$ sudo nmap 10.129.102.62 -Pn -n --disable-arp-ping -p 22 -sV          
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-11 04:53 EST
Nmap scan report for 10.129.102.62
Host is up (0.036s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.54 seconds
```

**Answer:** `Ubuntu`

---
## Firewall and IDS/IPS Evasion - Medium Lab
### Question:
![](./attachments/Pasted%20image%2020221111112028.png)
*Hint: During the meeting, the administrators talked about the host we tested as a publicly accessible server that was not mentioned before.*

Script fundt [here](https://nmap.org/nsedoc/scripts/dns-nsid.html).

```
┌──(kali㉿kali)-[~]
└─$ sudo nmap 10.129.102.64 -sSU -p 53 --script dns-nsid                     
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-11 05:19 EST
Nmap scan report for 10.129.102.64
Host is up (0.031s latency).

PORT   STATE    SERVICE
53/tcp filtered domain
53/udp open     domain
| dns-nsid: 
|_  bind.version: HTB{GoTtgUnyze9Psw4vGjcuMpHRp}

Nmap done: 1 IP address (1 host up) scanned in 1.10 seconds

```

**Answer:** `HTB{GoTtgUnyze9Psw4vGjcuMpHRp}`

---
## Firewall and IDS/IPS Evasion - Hard Lab
### Question:
![](./attachments/Pasted%20image%2020221112102303.png)

```
┌──(kali㉿kali)-[~]
└─$ ncat -nv --source-port 53 10.129.100.71 50000
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Connected to 10.129.100.71:50000.
220 HTB{kjnsdf2n982n1827eh76238s98di1w6}
^Z
zsh: suspended  ncat -nv --source-port 53 10.129.100.71 50000
```

**Answer:** `HTB{kjnsdf2n982n1827eh76238s98di1w6}`

---
**Tags:** [[Hack The Box Academy]]