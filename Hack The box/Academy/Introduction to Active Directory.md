# Introduction to Active Directory
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Introduction to Active Directory
* Tier: 0
* Difficulty: Fundamental
* Category: General
* Time estimate: 7 hours
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Active Directory Structure
### Question 1:
![](./attachments/Pasted%20image%2020230224100420.png)
*Hint: The answer is the top tier of a hierarchal TREE.*

![image](https://academy.hackthebox.com/storage/modules/74/ad_forests.png)

**Answer:** `Forest`

### Question 2:
![](./attachments/Pasted%20image%2020230224100428.png)
*Hint: It can be easier and quicker to just trust the previous domain infrastructure instead of rebuilding after acquiring a company.*

![image](https://academy.hackthebox.com/storage/modules/74/ilflog2.png)

**Answer:** `True`

### Question 3:
![](./attachments/Pasted%20image%2020230224100436.png)
*Hint: It validates the identity of users and provides them with the RIGHTS to access services.*

"AD provides authentication and authorization..."

**Answer:** `Authorization`

---
## Active Directory Terminology
### Question 1:
![](./attachments/Pasted%20image%2020230224113002.png)
*Hint: *

"The Active Directory [schema](https://docs.microsoft.com/en-us/windows/win32/ad/schema) is essentially the blueprint..."

**Answer:** `schema`


### Question 2:
![](./attachments/Pasted%20image%2020230224113011.png)
*Hint: *

"A [Service Principal Name (SPN)](https://docs.microsoft.com/en-us/windows/win32/ad/service-principal-names) uniquely identifies a service instance."

**Answer:** `Service Principal Name`


### Question 3:
![](./attachments/Pasted%20image%2020230224113023.png)
*Hint: *

"GPO settings can be applied to both user and computer objects."

**Answer:** `True`


### Question 4:
![](./attachments/Pasted%20image%2020230224113035.png)
*Hint: *

"A [tombstone](https://ldapwiki.com/wiki/Tombstone) is a container object in AD that holds deleted AD objects."

**Answer:** `Tombstone`


### Question 5:
![](./attachments/Pasted%20image%2020230224113047.png)
*Hint: *

"The NTDS.DIT file can be considered the heart of Active Directory. It is stored on a Domain Controller at `C:\Windows\NTDS\` and is a database that stores AD data such as information about user and group objects, group membership, and, most important to attackers and penetration testers, the password hashes for all users in the domain."

**Answer:** `NTDS.DIT`

---
## Active Directory Objects
### Question 1:
![](./attachments/Pasted%20image%2020230224115450.png)
*Hint: Computers cannot contain other objects.*

"Users are considered `leaf objects`...."

**Answer:** `True`

### Question 2:
![](./attachments/Pasted%20image%2020230224115501.png)
*Hint: It is the primary object used for Organization within a domain.*

"An organizational unit, or OU from here on out, is a container that systems administrators can use to store similar objects for ease of administration."

**Answer:** `Organizational Units`

### Question 3:
![](./attachments/Pasted%20image%2020230224115515.png)
*Hint: It CONTROLS access to a domain and its resources.*

"They handle authentication requests, verify users on the network, and control who can access the various resources in the domain."

**Answer:** `Domain Controller`

---
## Active Directory Functionality
### Question 1:
![](./attachments/Pasted%20image%2020230224121147.png)

"The PDC Emulator also maintains time within the domain."

**Answer:** `PDC Emulator`

### Question 2:
![](./attachments/Pasted%20image%2020230224121200.png)

"Authentication mechanism assurance, Managed Service Accounts."

**Answer:** `Windows Server 2008 R2`

### Question 3:
![](./attachments/Pasted%20image%2020230224121219.png)
*Hint: It is used to speed up authentication.*

![image](https://academy.hackthebox.com/storage/modules/74/trusts-diagram.png)

**Answer:** `Cross-link`

### Question 4:
![](./attachments/Pasted%20image%2020230224121229.png)
*Hint: It makes sure names are Relative to each object.*

"The RID Master helps ensure that multiple objects are not assigned the same SID."

**Answer:** `Relative ID Master`

---
## Kerberos, DNS, LDAP, MSRPC
### Question 1:
![](./attachments/Pasted%20image%2020230224124114.png)
*Hint: It's the same port for both TCP & UDP.*

"The Kerberos protocol uses port 88 (both TCP and UDP)."

**Answer:** `88`

### Question 2:
![](./attachments/Pasted%20image%2020230224124121.png)
*Hint: It is the system for naming within a domain.*

"DNS is used to resolve hostnames to IP addresses and is broadly used across internal networks and the internet."

**Answer:** `DNS`

### Question 3:
![](./attachments/Pasted%20image%2020230224124129.png)
*Hint: It is an open source directory protocol.*

"The latest LDAP specification is [Version 3](https://tools.ietf.org/html/rfc4511), published as RFC 4511."

**Answer:** `LDAP`

---
## NTLM Authentication
### Question 1:
![](./attachments/Pasted%20image%2020230224124555.png)
*Hint: The only protocol this section is not about.*

"Kerberos: Symmetric key cryptography & asymmetric cryptography."

**Answer:** `Kerberos`

### Question 2:
![](./attachments/Pasted%20image%2020230224124604.png)
*Hint: The last message is the purpose of the protocol.*

"It is a challenge-response authentication protocol and uses three messages to authenticate: a client first sends a `NEGOTIATE_MESSAGE` to the server, whose response is a `CHALLENGE_MESSAGE` to verify the client's identity. Lastly, the client responds with an `AUTHENTICATE_MESSAGE`."

**Answer:** ``

### Question 3:
![](./attachments/Pasted%20image%2020230224124615.png)
*Hint: Type the number, not the word.*

"Hosts save the last `ten` hashes for any domain users that successfully log into the machine in the `HKEY_LOCAL_MACHINE\SECURITY\Cache` registry key."

**Answer:** `10`

---
## User and Machine Accounts
### Question 1:
![](./attachments/Pasted%20image%2020230224194806.png)
*Hint: Local accounts only work for the host they were created on.*

The hint is very useful.

**Answer:** ``

### Question 2:
![](./attachments/Pasted%20image%2020230224194815.png)
*Hint: It the boss of the host. The admin in charge if you will.*

"`Administrator`: this account has the SID `S-1-5-domain-500` and is the first account created with a new Windows installation."

**Answer:** `Administrator`

### Question 3:
![](./attachments/Pasted%20image%2020230224194823.png)
*Hint: It's the service account for the system.*

"A `SYSTEM` account is the highest permission level one can achieve on a Windows host and, by default, is granted Full Control permissions to all files on a Windows system."

**Answer:** `SYSTEM`

### Question 4:
![](./attachments/Pasted%20image%2020230224194835.png)
*Hint: It's not a SID*

"In AD, the ObjectGUID attribute name never changes and remains unique even if the user is removed."

**Answer:** `ObjectGUID`

---
## Active Directory Groups
### Question 1:
![](./attachments/Pasted%20image%2020230224201434.png)
*Hint: We are using this group type to secure resources.*

"The `Security groups` type is primarily for ease of assigning permissions and rights to a collection of users instead of one at a time."

**Answer:** `Security`

### Question 2:
![](./attachments/Pasted%20image%2020230224201509.png)

"A global group can only contain accounts from the domain where it was created."

**Answer:** `True`

### Question 3:
![](./attachments/Pasted%20image%2020230224201517.png)
*Hint: No restrictions exist for this conversion unlike the other groups.*

"A Universal Group can be converted to a Domain Local Group without any restrictions."

**Answer:** `Yes`

---
## Active Directory Rights and Privileges
### Question:
![](./attachments/Pasted%20image%2020230224203327.png)
*Hint: The admins get full access.

"Members have full and unrestricted access to a computer or an entire domain if they are in this group on a Domain Controller."

**Answer:** `Administrators`

### Question:
![](./attachments/Pasted%20image%2020230224203337.png)
*Hint: *

"This grants a user the ability to create system backups and could be used to obtain copies of sensitive system files that can be used to retrieve passwords such as the SAM and SYSTEM Registry hives and the NTDS.dit Active Directory database file."

**Answer:** `SeBackupPrivilege`

### Question:
![](./attachments/Pasted%20image%2020230224203350.png)
*Hint: whoami will show us about the user, what /command will specify privs.*

```
PS C:\htb> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== ========
SeShutdownPrivilege           Shut down the system           Disabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
```

**Answer:** `whoami /priv`

---
## Security in Active Directory
### Question:
![](./attachments/Pasted%20image%2020230224211144.png)
*Hint: *

![image](https://academy.hackthebox.com/storage/modules/74/CIA-triad-diag.png)

**Answer:** `Integrity`

### Question:
![](./attachments/Pasted%20image%2020230224211154.png)

"This may include blocking certain users from running all executables, Windows Installer files, scripts, etc."

**Answer:** `Application Control Policies`

---
## Examining Group Policy
### Question:
![](./attachments/Pasted%20image%2020230227103246.png)
*Hint: It's a bit more than an hour and can change after the initial settings pull so that every host on net doesn't pull at once.*

"Windows performs periodic Group Policy updates, which by default is done every 90 minutes with a randomized offset of +/- 30 minutes for users and computers."

**Answer:** `90`

### Question:
![](./attachments/Pasted%20image%2020230227103258.png)
*Hint: LSDOU*

"Say a specific building or `site` performs secret or restricted research and requires a higher level of authentication for access to resources. You could specify those settings at the site level and ensure they are linked so as not to be overwritten by domain policy."

**Answer:** `False`

### Question:
![](./attachments/Pasted%20image%2020230227103308.png)
*Hint: It is the default for the domain if nothing else is specified.*

"The Default Domain Policy is the default GPO that is automatically created and linked to the domain."

**Answer:** `Default Domain Policy`

---
**Tags:** [[Hack The Box Academy]]