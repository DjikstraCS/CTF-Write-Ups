# Explosion
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Explosion
* Topic: Account Misconfiguration, xfreerdp
* Difficulty: Very easy
* Date: 15-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What does the 3-letter acronym RDP stand for?
 - **remote desktop protocol**
2. What is a 3-letter acronym that refers to interaction with the host through a command line interface?
- **cli**
3. What about graphical user interface interactions? 
- **gui**
4. What is the name of an old remote access tool that came without encryption by default? 
- **telnet**
5. What is the concept used to verify the identity of the remote host with SSH connections?
- **public-key cryptography**
6. What is the name of the tool that we can use to initiate a desktop projection to our host using the terminal?
- **rdesktop**
7. What is the name of the service running on port 3389 TCP? 
- **ms-wbt-server**
8. What is the switch used to specify the target host's IP address when using xfreerdp?
- **/v:**

---
## Flag:
First, we need to scan the target with `nmap`.

Command:

`nmap -n -sC -sV 10.129.92.232`

`-n`: No DNS look up (Good [OPSEC](https://en.wikipedia.org/wiki/Operations_security)).

`-sC`: Run scripts during scan.

`-sV`: Try to detect the version of running services.

```console
┌──(kali㉿kali)-[~]
└─$ nmap -n -sC -sV 10.129.92.232 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-15 13:50 EDT
Nmap scan report for 10.129.92.232
Host is up (0.069s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: EXPLOSION
|   NetBIOS_Domain_Name: EXPLOSION
|   NetBIOS_Computer_Name: EXPLOSION
|   DNS_Domain_Name: Explosion
|   DNS_Computer_Name: Explosion
|   Product_Version: 10.0.17763
|_  System_Time: 2022-04-15T17:50:27+00:00
| ssl-cert: Subject: commonName=Explosion
| Not valid before: 2022-04-14T17:49:40
|_Not valid after:  2022-10-14T17:49:40
|_ssl-date: 2022-04-15T17:50:35+00:00; 0s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-04-15T17:50:31
|_  start_date: N/A

Nmap done: 1 IP address (1 host up) scanned in 22.03 seconds
```

We can use [xfreerdp](https://linux.die.net/man/1/xfreerdp) to connect to the host.

Command:

`xfreerdp /v:10.129.92.232 /u:Administrator /cert:ignore`

`/v:`: The host we want to connect to.

`/u:`: The user we want to log in as.

`/cert:`: Ignore all kind of certificates.

```console
┌──(kali㉿kali)-[~]
└─$ xfreerdp /v:10.129.92.232 /u:Administrator /cert:ignore
Password: 
[10:18:16:687] [89007:89008] [INFO][com.freerdp.gdi] - Local framebuffer format  PIXEL_FORMAT_BGRX32
[10:18:16:687] [89007:89008] [INFO][com.freerdp.gdi] - Remote framebuffer format PIXEL_FORMAT_RGB16
[10:18:16:733] [89007:89008] [INFO][com.freerdp.channels.rdpsnd.client] - [static] Loaded fake backend for rdpsnd
[10:18:19:505] [89007:89008] [INFO][com.freerdp.client.x11] - Logon Error Info LOGON_FAILED_OTHER [LOGON_MSG_SESSION_CONTINUE]
^C[10:21:06:676] [89007:89007] [ERROR][com.freerdp.utils] - Caught signal 'Interrupt' [2]
[10:21:06:677] [89007:89007] [ERROR][com.freerdp.utils] - 0: /lib/x86_64-linux-gnu/libwinpr2.so.2(winpr_backtrace+0x50) [0x7f32435efc30]

(...)
```

A new window appears. We've connected to a computer running Windows Server 2019.

The flag is visible on the desktop.

![](./attachments/Pasted%20image%2020220415162356.png)

**Flag:** `951fa96d7830c451b536be5a6be008a0`

---
**Tags:** [[Hack The Box]]