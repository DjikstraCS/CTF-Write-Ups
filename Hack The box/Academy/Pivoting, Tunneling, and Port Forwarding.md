# Pivoting, Tunneling, and Port Forwarding
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Pivoting, Tunneling, and Port Forwarding
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 2 days
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## The Networking Behind Pivoting
### Question 1:
![](./attachments/Pasted%20image%2020221124112751.png)

```shell-session
DjikstraCS@htb[/htb]$ ifconfig

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 134.122.100.200  netmask 255.255.240.0  broadcast 134.122.111.255
        inet6 fe80::e973:b08d:7bdf:dc67  prefixlen 64  scopeid 0x20<link>
        ether 12:ed:13:35:68:f5  txqueuelen 1000  (Ethernet)
        RX packets 8844  bytes 803773 (784.9 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 5698  bytes 9713896 (9.2 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
(...)
```

`134.122.100.200` is a public IP-address

**Answer:** `eth0`

### Question 2:
![](./attachments/Pasted%20image%2020221124112801.png)
*Hint: Consider how a routing table is used to make routing decisions. Destination IP address is very important.*

```shell-session
DjikstraCS@htb[/htb]$ netstat -r

Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
default         178.62.64.1     0.0.0.0         UG        0 0          0 eth0
10.10.10.0      10.10.14.1      255.255.254.0   UG        0 0          0 tun0
10.10.14.0      0.0.0.0         255.255.254.0   U         0 0          0 tun0
10.106.0.0      0.0.0.0         255.255.240.0   U         0 0          0 eth1
10.129.0.0      10.10.14.1      255.255.0.0     UG        0 0          0 tun0
178.62.64.0     0.0.0.0         255.255.192.0   U         0 0          0 eth0
```

`10.129.x.x` is routed through interface `tun0`.

**Answer:** `tun0`

### Question 3:
![](./attachments/Pasted%20image%2020221124112809.png)
*Hint: Consider how a routing table is used if the destination IP network is not listed in the routing table.*

```shell-session
DjikstraCS@htb[/htb]$ netstat -r

Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
default         178.62.64.1     0.0.0.0         UG        0 0          0 eth0
10.10.10.0      10.10.14.1      255.255.254.0   UG        0 0          0 tun0
10.10.14.0      0.0.0.0         255.255.254.0   U         0 0          0 tun0
10.106.0.0      0.0.0.0         255.255.240.0   U         0 0          0 eth1
10.129.0.0      10.10.14.1      255.255.0.0     UG        0 0          0 tun0
178.62.64.0     0.0.0.0         255.255.192.0   U         0 0          0 eth0
```

The default gateway has IP address `178.62.64.1`.

**Answer:** `178.62.64.1`

---
## Dynamic Port Forwarding with SSH and SOCKS Tunneling
### Question 1:
![](./attachments/Pasted%20image%2020221124115924.png)
*Hint: Submit that answer as a digit.*

```
┌──(kali㉿kali)-[~]
└─$ ssh ubuntu@10.129.204.127
The authenticity of host '10.129.204.127 (10.129.204.127)' can't be established.
ED25519 key fingerprint is SHA256:AtNYHXCA7dVpi58LB+uuPe9xvc2lJwA6y7q82kZoBNM.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.204.127' (ED25519) to the list of known hosts.
ubuntu@10.129.204.127's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu 24 Nov 2022 11:07:46 AM UTC

  System load:             0.07
  Usage of /:              30.4% of 13.72GB
  Memory usage:            31%
  Swap usage:              0%
  Processes:               195
  Users logged in:         0
  IPv4 address for ens192: 10.129.204.127
  IPv6 address for ens192: dead:beef::250:56ff:feb9:34fd
  IPv4 address for ens224: 172.16.5.129

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

147 updates can be applied immediately.
108 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Thu May 12 17:27:41 2022
ubuntu@WEB01:~$ ifconfig
ens192: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.129.204.127  netmask 255.255.0.0  broadcast 10.129.255.255
        inet6 fe80::250:56ff:feb9:34fd  prefixlen 64  scopeid 0x20<link>
        inet6 dead:beef::250:56ff:feb9:34fd  prefixlen 64  scopeid 0x0<global>
        ether 00:50:56:b9:34:fd  txqueuelen 1000  (Ethernet)
        RX packets 5502  bytes 424000 (424.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 867  bytes 76244 (76.2 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

ens224: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.16.5.129  netmask 255.255.254.0  broadcast 172.16.5.255
        inet6 fe80::250:56ff:feb9:f170  prefixlen 64  scopeid 0x20<link>
        ether 00:50:56:b9:f1:70  txqueuelen 1000  (Ethernet)
        RX packets 238  bytes 17885 (17.8 KB)
        RX errors 0  dropped 14  overruns 0  frame 0
        TX packets 255  bytes 17339 (17.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 2184  bytes 171129 (171.1 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2184  bytes 171129 (171.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

There are three interfaces, incuding the loopback interface.

**Answer:** `3`

### Question 2:
![](./attachments/Pasted%20image%2020221124115933.png)
*Hint: Make sure your pivot is working successfully from your Attack host to the pivot host.*

```
┌──(kali㉿kali)-[~]
└─$ proxychains nmap -v -sn 172.16.5.1-200  
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.16
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-24 06:50 EST
Initiating Ping Scan at 06:50
Scanning 200 hosts [2 ports/host]
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.2:80 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.5:80 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.8:80 <--socket error or timeout!
(...)
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.7:80 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:80  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.21:80 <--socket error or timeout!
(...)
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.115:80 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.129:80  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.136:80 <--socket error or timeout!
(...)
Completed Ping Scan at 07:00, 624.50s elapsed (200 total hosts)
Initiating Parallel DNS resolution of 200 hosts. at 07:00
Completed Parallel DNS resolution of 200 hosts. at 07:00, 0.63s elapsed
Nmap scan report for 172.16.5.1
Host is up (3.1s latency).
Nmap scan report for 172.16.5.2
Host is up (3.2s latency).
Nmap scan report for 172.16.5.3
Host is up (3.1s latency).
(...)
Host is up (3.1s latency).
Nmap scan report for 172.16.5.14
Host is up (3.2s latency).
Nmap scan report for 172.16.5.15
Host is up (3.2s latency).
Nmap scan report for 172.16.5.16
Host is up (3.2s latency).
Nmap scan report for 172.16.5.17
Host is up (3.2s latency).
Nmap scan report for 172.16.5.18
Host is up (3.1s latency).
Nmap scan report for 172.16.5.19
Host is up (0.092s latency).
(...)
Nmap scan report for 172.16.5.128
Host is up (3.2s latency).
Nmap scan report for 172.16.5.129
Host is up (0.080s latency).
Nmap scan report for 172.16.5.130
Host is up (3.2s latency).
(...)
Nmap done: 200 IP addresses (200 hosts up) scanned in 625.13 seconds
```

`172.16.5.19` and `172.16.5.129` seems to be up.

```
┌──(kali㉿kali)-[~]
└─$ proxychains nmap -v -Pn -sT 172.16.5.19
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.16
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-24 07:05 EST
Initiating Parallel DNS resolution of 1 host. at 07:05
Completed Parallel DNS resolution of 1 host. at 07:05, 0.09s elapsed
Initiating Connect Scan at 07:05
Scanning 172.16.5.19 [1000 ports]
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:21 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:995 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:111 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:443 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:256 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:445  ...  OK
Discovered open port 445/tcp on 172.16.5.19
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:587 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:139  ...  OK
Discovered open port 139/tcp on 172.16.5.19
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:22 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:135  ...  OK
Discovered open port 135/tcp on 172.16.5.19
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:199 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:80  ...  OK
Discovered open port 80/tcp on 172.16.5.19

(...)

[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:3306 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:53  ...  OK
Discovered open port 53/tcp on 172.16.5.19
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:3389  ...  OK
Discovered open port 3389/tcp on 172.16.5.19
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:113 <--socket error or timeout!

(...)

Completed Connect Scan at 07:06, 91.77s elapsed (1000 total ports)
Nmap scan report for 172.16.5.19
Host is up (0.085s latency).
Not shown: 987 closed tcp ports (conn-refused)
PORT     STATE SERVICE
53/tcp   open  domain
80/tcp   open  http
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
3389/tcp open  ms-wbt-server

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 91.89 seconds

```

```
┌──(kali㉿kali)-[~]
└─$ proxychains msfconsole
   
 ______________________________________
/ it looks like you're trying to run a \                                                                   
\ module                               /                                                                   
 --------------------------------------                                                                    
 \                                                                                                         
  \                                                                                                        
     __                                                                                                    
    /  \                                                                                                   
    |  |                                                                                                   
    @  @                                                                                                   
    |  |                                                                                                   
    || |/                                                                                                  
    || ||                                                                                                  
    |\_/|                                                                                                  
    \___/                                                                                                  


       =[ metasploit v6.2.23-dev                          ]
+ -- --=[ 2259 exploits - 1188 auxiliary - 402 post       ]
+ -- --=[ 951 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: Save the current environment with the 
save command, future console restarts will use this 
environment again
Metasploit Documentation: https://docs.metasploit.com/
msf6 > search rdp_scanner

Matching Modules
================

   #  Name                               Disclosure Date  Rank    Check  Description
   -  ----                               ---------------  ----    -----  -----------
   0  auxiliary/scanner/rdp/rdp_scanner                   normal  No     Identify endpoints speaking the Remote Desktop Protocol (RDP)
<

Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/rdp/rdp_scanner

msf6 > use 0
msf6 auxiliary(scanner/rdp/rdp_scanner) > options

Module options (auxiliary/scanner/rdp/rdp_scanner):

   Name             Current Setting  Required  Description
   ----             ---------------  --------  -----------
   DETECT_NLA       true             yes       Detect Network Level Authentication (NLA)
   RDP_CLIENT_IP    192.168.0.100    yes       The client IPv4 address to report during connect
   RDP_CLIENT_NAME  rdesktop         no        The client computer name to report during connect, UNSET =
                                                random
   RDP_DOMAIN                        no        The client domain name to report during connect
   RDP_USER                          no        The username to report during connect, UNSET = random
   RHOSTS                            yes       The target host(s), see https://github.com/rapid7/metasplo
                                               it-framework/wiki/Using-Metasploit
   RPORT            3389             yes       The target port (TCP)
   THREADS          1                yes       The number of concurrent threads (max one per host)

msf6 auxiliary(scanner/rdp/rdp_scanner) > set RHOST 172.16.5.19
msf6 auxiliary(scanner/rdp/rdp_scanner) > run
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:3389  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:3389  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:3389  ...  OK

[*] 172.16.5.19:3389      - Detected RDP on 172.16.5.19:3389      (name:DC01) (domain:INLANEFREIGHT) (domain_fqdn:inlanefreight.local) (server_fqdn:DC01.inlanefreight.local) (os_version:10.0.17763) (Requires NLA: No)
[*] 172.16.5.19:3389      - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

```
┌──(kali㉿kali)-[~]
└─$ proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  172.16.5.19:3389  ...  OK
[07:11:42:375] [19774:19776] [WARN][com.freerdp.crypto] - Certificate verification failure 'self-signed certificate (18)' at stack position 0
[07:11:42:375] [19774:19776] [WARN][com.freerdp.crypto] - CN = DC01.inlanefreight.local
[07:11:44:687] [19774:19776] [INFO][com.freerdp.gdi] - Local framebuffer format  PIXEL_FORMAT_BGRX32
[07:11:44:687] [19774:19776] [INFO][com.freerdp.gdi] - Remote framebuffer format PIXEL_FORMAT_BGRA32
[07:11:44:703] [19774:19776] [INFO][com.freerdp.channels.rdpsnd.client] - [static] Loaded fake backend for rdpsnd
[07:11:44:703] [19774:19776] [INFO][com.freerdp.channels.drdynvc.client] - Loading Dynamic Virtual Channel rdpgfx
```

And a RDP window opens. The flag is located on the desktop.

![](./attachments/Pasted%20image%2020221124131349.png)

**Answer:** `N1c3Piv0t`

---
## 
### Question:


**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]