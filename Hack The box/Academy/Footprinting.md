# Web Requests
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Footprinting
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 2 days
* Date: DD-MM-YYYY
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

**Answer:** ``

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

**Answer:** ``

### Question 6:
![](./attachments/Pasted%20image%2020230125202114.png)

**Answer:** ``

---
## SNMP
### Question 1:


**Answer:** ``

---
## 
### Question:


**Answer:** ``

---

**Tags:** [[Hack The Box Academy]]