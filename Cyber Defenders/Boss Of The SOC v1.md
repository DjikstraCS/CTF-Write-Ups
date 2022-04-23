# Boss Of The SOC v1
* Source: [Cyber Defenders](https://cyberdefenders.org/blueteam-ctf-challenges/15)
* Challenge: Boss Of The SOC v1
* Category: SIEM Case Investigation
* Date: 23-04-2022
* Authors: [DjikstraCS](https://github.com/DjikstraCS) & [Miqqcrow](https://github.com/Miqqcrow)

---

## Challenge:
![](./attachments/Pasted%20image%2020220421175617.png)

### Challenge details:
**Scenario 1 (APT)**:

The focus of this hands on lab will be an APT scenario and a ransomware scenario. You assume the persona of Alice Bluebird, the analyst who has recently been hired to protect and defend Wayne Enterprises against various forms of cyberattack.

In this scenario, reports of the below graphic come in from your user community when they visit the Wayne Enterprises website, and some of the reports reference "P01s0n1vy." In case you are unaware, P01s0n1vy is an APT group that has targeted Wayne Enterprises. Your goal, as Alice, is to investigate the defacement, with an eye towards reconstructing the attack via the Lockheed Martin Kill Chain.

![](./attachments/Pasted%20image%2020220422134628.png)

**Scenario 2 (Ransomware)**:

In the second scenario, one of your users is greeted by this image on a Windows desktop that is claiming that files on the system have been encrypted and payment must be made to get the files back. It appears that a machine has been infected with Cerber ransomware at Wayne Enterprises and your goal is to investigate the ransomware with an eye towards reconstructing the attack.

![](./attachments/Pasted%20image%2020220422134641.png)

---
## Question 1:
This is a simple question to get you familiar with submitting answers. What is the name of the company that makes the software that you are using for this competition? Just a six-letter word with no punctuation.

### Solution:
The software we will be using is made by Splunk, this is clear due to the logo of the challenge and the fact that [Splunk Team](https://twitter.com/splunk) is the author.

![](./attachments/Pasted%20image%2020220421175534.png)

**Answer:** `Splunk`

## Question 2:
What is the likely IP address of someone from the Po1s0n1vy group scanning imreallynotbatman.com for web application vulnerabilities?

### Hints:
```
1. Start your search with "sourcetype=stream:http" and review the rich data captured in these events.
2. You'll notice that source and destination IP addresses are stored in fields called src_ip and dest_ip respectively. Determine top-talkers for HTTP by combining : "sourcetype=stream:http | stats count by src_ip, dest_ip | sort -count"
```

### Solution:
First, we can use `sourcetype="stream:http"` to get all the HTTP traffic. Since we are looking for a scanner, we can also try `scan*` to get all derivations of 'scan' e.g. scanner, scanning etc.

**Search Query:**
```
sourcetype="stream:http" scan*
```

In the first result we find a source header containing a browser user-agent which reveals that the Acunetix Web Vulnerability Scanner has been used against `imreallynotbatman.com`. Also, we can see that it tried to do some kind of injection into the search field on the site. `40.80.148.42` must be the IP address we are looking for.

![](./attachments/Pasted%20image%2020220422142822.png)

**Answer:** `40.80.148.42`

## Question 3:
What company created the web vulnerability scanner used by Po1s0n1vy? Type the company name. (For example, "Microsoft" or "Oracle")

### Hints:
```
1. Many commercial web vulnerability scanners clearly identify themselves in the headers of the HTTP request. Inspect the HTTP source headers (src_headers) of requests from the IP identified in question 101.
```

### Solution:
This one is free. We already found the answer during our last search query.

Answer: `Acunetix`

## Question 4:
What content management system is imreallynotbatman.com likely using? (Please do not include punctuation such as . , ! ? in your answer. We are looking for alpha characters only.)

### Hints:
```
1. Look for successful (http status code of 200) GET requests from the scanning IP address (identified previously) and inspect the fields related to URL/URI for clues to the CMS in use.
```

### Solution:
During our last search, we also found that the request made by the attacker was made to a URL containing `/joomla/`. This means that `imreallynotbatman.com` is probably a Joomla! site.

![](./attachments/Pasted%20image%2020220421191202.png)

Let's confirm it.

**Search Query:**
```
imreallynotbatman.com
```

Under the `url` field, we can see that all the top URLs contain `/joomla/`.

![](./attachments/Pasted%20image%2020220422144314.png)

Answer: `joomla`

## Question 5:
What is the name of the file that defaced the imreallynotbatman.com website? Please submit only the name of the file with the extension (For example, "notepad.exe" or "favicon.ico").

### Hints:
```
1. First find the IP address of the web server hosting imreallynotbatman.com. You may have found this IP during the course of answering the previous few questions.
2. Revealing sourcetypes include stream:http, fgt_utm, and suricata
3. The key here is searching for events where the IP address of the web server is the source. Because it's a web server, we most often see it as a destination but in this case the intruder took control of the server and pulled the defacement file from an internet site.
```

### Solution:
After taking control of the server, the attacker has most likely made the server download the image file. Therefore, we need to set the `src_ip` to the server's IP address. In the first search we did, we found the IP address of `imreallynotbatman.com` to be `192.168.250.70`.

If the download was made using HTTP, we can see all the packets where `192.168.250.70` is the source by using the following query. Also, we can pipe the input and catch all the URLs in order to quickly get an overview of what files have been downloaded.

**Search Query:**
```
sourcetype="stream:http" src_ip="192.168.250.70"
| stats count by url
```

![](./attachments/Pasted%20image%2020220422162842.png)

That `.jpeg` file must be the one we are looking for.

Answer: `poisonivy-is-coming-for-you-batman.jpeg`

## Question 6:
This attack used dynamic DNS to resolve to the malicious IP. What is the fully qualified domain name (FQDN) associated with this attack?

### Hints:
```
1. The fully qualified domain name was recorded by Stream, Suricata, and the FortiGate firewall.
```

### Solution:
We found the answer to this question in the answer to question 5.

![](./attachments/Pasted%20image%2020220422175307.png)

Answer: `prankglassinebracket.jumpingcrab.com`

## Question 7:
What IP address has Po1s0n1vy tied to domains that are pre-staged to attack Wayne Enterprises?

### Hints:
```
1. The fully qualified domain name was recorded by Stream, Suricata, and the FortiGate firewall.
```

### Solution:
Since the deface image file was downloaded from `prankglassinebracket.jumpingcrab.com`, that is probably a pre-staged machine. We can use an online tool like [Threat Crowd](https://www.threatcrowd.org/domain.php?domain=prankglassinebracket.jumpingcrab.com) to help us find connections between IP addresses and domains.

Searching for `prankglassinebracket.jumpingcrab.com` shows us a connection to `po1son1vy.com` which further leads us to the IP address `23.22.63.114`.

![](./attachments/Pasted%20image%2020220422170029.png)

To confirm that this IP indeed has a connection to our current scenario, we can do a simple search returning all HTTP connections coming from that IP address.

**Search Query:**
```
sourcetype="stream:http" src_ip="23.22.63.114"
```

Apart from the fact that the search returns valid results, we can confirm by looking under `dest_ip` where we can see the connection to our web server at `192.168.250.70`.

![](./attachments/Pasted%20image%2020220422175200.png)

There is no doubt `23.22.63.114` has a connection to the attack. It must be the pre-staged IP address we are looking for.

Answer: `23.22.63.114`

## Question 8:
Based on the data gathered from this attack and common open-source intelligence sources for domain names, what is the email address most likely associated with the Po1s0n1vy APT group?

### Hints:
```
1. Malicious IP addresses, like the one in the last question are examples of attacker infrastructure. Infrastructure is often reused by the same group. Use a service like [www.robtex.com](www.robtex.com) to determine other domains that are or have been associated with this attacker infrastructure (IP address).
2. Use the whois lookup on domaintools.com to iterate through domains associated with this IP and visually search for suspicious email addresses. Your knowledge of Batman will help you here!
```

### Solution:
If we do a new search for `23.22.63.114` at [Threat Crowd](https://www.threatcrowd.org/ip.php?ip=23.22.63.114) we find a connection to an email address.

![](./attachments/Pasted%20image%2020220421210622.png)

Answer: `lillian.rose@po1s0n1vy.com`

## Question 9:
What IP address is likely attempting a brute force password attack against imreallynotbatman.com?

### Hints:
```
1. Login attempts will use the HTTP POST method, and they will include some obvious fields in the form_data field of stream:http events.
```

### Solution:
Because all login attempts are sent via the HTTP POST method, we can filter everything else away by using `http_method=POST`. Also, we will add the keyword `login`. Using `| stats count` to make a nice human-readable output.

**Search Query:**
```
sourcetype="stream:http" http_method=POST login
| stats count by src_ip, src_content
```

`23.22.63.114` is clearly performing some kind of brute force attack.

![](./attachments/Pasted%20image%2020220422174111.png)

Answer: `23.22.63.114`

## Question 10:
What is the name of the executable uploaded by Po1s0n1vy? Please include the file extension. (For example, "notepad.exe" or "favicon.ico")

### Hints:
```
1. File uploads to web forms use the HTTP POST method.
2. The question mentions and executable. Search for common executable filename extensions on Windows systems.
```

### Solution:
We need to set `dest_ip` to `192.168.250.70` because we are looking for something that was sent to the server. Also, `"*.exe"` will find all strings ending in '.exe'.

**Search Query:**
```
dest_ip="192.168.250.70" "*.exe"
```

Scrolling through the output, this event clearly looks out of place. Also, it contains an '.exe' file which doesn't look like a standard windows process.

![](./attachments/Pasted%20image%2020220422181001.png)

Answer: `3791.exe`

## Question 11:
What is the MD5 hash of the executable uploaded?

### Hints:
```
1. Search for the file name in a different data source to find evidence of execution, including file hash values.
2. This is an ideal use case for Microsoft Sysmon data. Determine the sourcetype for Sysmon events and search them for the executable.
```

### Solution:

First off, let's do a search query for the executable and `md5`.

**Search Query:**
```
3791.exe md5
```

Under the `MD5` field, we find a few different MD5 hashes. Let's take a closer look at the first one.

![](./attachments/Pasted%20image%2020220422185236.png)

Here we can see that the MD5 hash has been made by 'Windows Event Log' which is a system monitoring tool.

![](./attachments/Pasted%20image%2020220422183712.png)

If an execution has happened via `cmd.exe` it should have been logged in the `CommandLine` field.

**Search Query:**
```
sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" CommandLine="*3791.exe" md5
```

We get a single event and upon inspection we can confirm that this event must contain the MD5 hash we are looking for. Note the `ParentCommandLine` field, it looks like `3791.exe` was executed using a payload.

![](./attachments/Pasted%20image%2020220422200512.png)

Answer: `AAE3F5A29935E6ABCC2C2754D12A9AF0`

## Question 12:
GCPD reported that common TTP (Tactics, Techniques, Procedures) for the Po1s0n1vy APT group, if initial compromise fails, is to send a spear-phishing email with custom malware attached to their intended target. This malware is usually connected to Po1s0n1vy's initial attack infrastructure. Using research techniques, provide the SHA256 hash of this malware.

### Hints:
```
1. You need to pivot outside of Splunk to answer this question. Use the IP address discovered earlier to search for malware that has been associated with it in the past.
2. Experienced analysts know to use sites like www.threatminer.org to search for malware associated with the malicious IP address, but if all else fails, Google it!
```

### Solution:
Since `23.22.63.114` is clearly part of Po1s0n1vy's attack infrastructure, we will search for it using [Virus Total](https://www.virustotal.com/gui/ip-address/23.22.63.114/relations). Under relations, we find a few files. `MirandaTateScreensaver.scr.exe` is interesting, it looks like it's pretending to be a screensaver.

![](./attachments/Pasted%20image%2020220422205310.png)

If we click on it, we can see it's SHA256 hash under the details tab.

![](./attachments/Pasted%20image%2020220422205448.png)

Answer: `9709473ab351387aab9e816eff3910b9f28a7a70202e250ed46dba8f820f34a8`

## Question 13:
What is the special hex code associated with the customized malware discussed in question 12? (Hint: It's not in Splunk)

### Hints:
```
1. Do some further research on the hash discovered in the last question. Virustotal.com is a good starting place.
2. malwr.com might lead you astray
3. The hex codes we are after here will be formatted like this: 49 66 20 79 6f 75 20 64 65 63 6f 64 65 20 74 68 65 20 68 69 6e 74 2c 20 79 6f 75 20 64 6f 6e 27 74 20 6e 65 65 64 20 61 20 68 69 6e 74 21. Submit the hex codes, but decode them on the web for fun!
```

### Solution:
Continuing our search on [Virus Total](https://www.virustotal.com/gui/file/9709473ab351387aab9e816eff3910b9f28a7a70202e250ed46dba8f820f34a8/community), under the community tab, we find the hex value we are hex value we are looking for.

![](./attachments/Pasted%20image%2020220422211635.png)

![](./attachments/Pasted%20image%2020220422211703.png)

Giving it to [Cyber Chef](https://gchq.github.io/CyberChef/) reveals what it means in plain English.

"`Steve Brant's Beard is a powerful thing. Find this message and ask him to buy you a beer!!!`"

![](./attachments/Pasted%20image%2020220422211535.png)

Answer: `53 74 65 76 65 20 42 72 61 6e 74 27 73 20 42 65 61 72 64 20 69 73 20 61 20 70 6f 77 65 72 66 75 6c 20 74 68 69 6e 67 2e 20 46 69 6e 64 20 74 68 69 73 20 6d 65 73 73 61 67 65 20 61 6e 64 20 61 73 6b 20 68 69 6d 20 74 6f 20 62 75 79 20 79 6f 75 20 61 20 62 65 65 72 21 21 21`

## Question 14:
One of Po1s0n1vy's staged domains has some disjointed "unique" whois information. Concatenate the two codes together and submit them as a single answer.

### Hints:
```
1. Use a service like www.threatcrowd.org to determine other domains that are or have been associated with the attacker's infrastructure (IP address).
2. Use a high quality whois site like https://www.whoxy.com/whois-history/demo.php to perform whois lookups against these domains until you see a hex code where you were expecting text. Warning not all whois sites show you all fields!
3. Use https://www.whoxy.com/whois-history/demo.php with the "waynecorinc.com" domain. The answer is "31 73 74 32 66 69 6E 64 67 65 74 73 66 72 65 65 62 65 65 72 66 72 6F 6D 72 79 61 6E 66 69 6E 64 68 69 6D 74 6F 67 65 74"
```

### Solution:
Going back to our previous search at [Threat Crowd](https://www.threatcrowd.org/ip.php?ip=23.22.63.114) we can see all the domains connected to the IP. We need to do a whois lookup on them one at a time until we find the one who has some disjointed whois info. [Whoxy](https://www.whoxy.com/) is a great tool for that.

Due to the age of this challenge, the domains are no longer registered and therefore no whois info is live. We might be able to find some historical records, but they will most likely cost money. Since we are too stingy to pay for that, we pulled the answer from this [writeup](https://cybersecurityfreeresource.wordpress.com/2021/12/31/cyberdefenders-org-boss-of-the-soc-v1-walkthrough/) made by [Cyber Security Free Resource](https://www.youtube.com/channel/UCfNM9pG9eest1iHr9Tl5QdA/featured).

![](./attachments/Pasted%20image%2020220422221315.png)

![](./attachments/Pasted%20image%2020220422220102.png)

Feeding it to [Cyber Chef](https://gchq.github.io/CyberChef/) gives us:

"`1st (and) 2(nd) find gets free beer from ryan, find him to get (it)`"

![](./attachments/Pasted%20image%2020220422225523.png)

Answer: `31 73 74 32 66 69 6E 64 67 65 74 73 66 72 65 65 62 65 65 72 66 72 6F 6D 72 79 61 6E 66 69 6E 64 68 69 6D 74 6F 67 65 74`

## Question 15:
What was the first brute force password used?

### Hints:
```
1. Login attempts will use the HTTP POST method, and they will include some obvious fields that you can search for in the form_data field of stream:http events.
2. By default, Splunk will put the most recent events at the top of the list. You can use the "reverse" SPL command to show you least recent first.
```

### Solution:
We can use the search query from question 9 as a starting point. We need to add the attacker's IP address with `src_ip` and changed the count line into a table containing the username and password along with their time stamp. Lastly, we use `sort _time` to sort the list for earliest first (reverse order).

**Search Query:**
```
sourcetype="stream:http" http_method=POST src_ip="23.22.63.114" login
| table _time, src_content
| sort by _time
```

By clicking `_timeᐞ` once, we will get the earliest event shown as the top result. The Password seems to be `12345678`.

![](./attachments/Pasted%20image%2020220422231847.png)

Answer: `12345678`

## Question 16:
One of the passwords in the brute force attack is [James Brodsky's](https://twitter.com/james_brodsky) favorite Coldplay song. Hint: we are looking for a six-character word on this one. Which is it?

### Hints:
```
1. If you have not done so already, try to extract the attempted password into a new field using the "rex" SPL command and a regular expression. Having the password attempt in its own field will serve you well for the next several questions!
2. It's not hard to get a list of songs by the artist. Once you have that, use the "len()" function of the "eval" SPL command. For Splunk style points, use a lookup table to match the password attempts with songs.
```

### Solution:
In order to extract the username and password out of `src_content` we can utilize the `rex` SPL command.

**Search Query:**
```
sourcetype=stream:http http_method=POST src_ip=23.22.63.114 form_data=*username*passwd*
| rex field=form_data username=(?<user>\w+)
| rex field=form_data passwd=(?<pw>\w+)
| table _time, user, pw
| sort by _time
```

It returns a nice-looking table with the password and username extracted.

![](./attachments/Pasted%20image%2020220422233255.png)

Now we need to filter out all the passwords which is not six-letters long.

**Search Query:**
```
sourcetype=stream:http http_method=POST src_ip=23.22.63.114 form_data=*username*passwd*
| rex field=form_data username=(?<user>\w+)
| rex field=form_data passwd=(?<pw>\w+)
| eval passwordLen=len(pw)
| search passwordLen=6
| table _time, user, pw
| sort by _time
```

Next, we need to compare them to all the Coldplay songs that has six-letters. We can use the neat online tool [Crossword Clues](https://www.crosswordclues.com/clue/coldplay-song) to speed up the process a bit. 

![](./attachments/Pasted%20image%2020220422234912.png)

We can use Excel `VLOOKUP()` function to find passwords that appear in both lists.

Command:
`=VLOOKUP(D2:D6;C2:C214;1;FALSE)`

![](./attachments/Pasted%20image%2020220423005438.png)

Answer: `yellow`

## Question 17:
What was the correct password for admin access to the content management system running "imreallynotbatman.com"?

### Hints:
```
1. From the previous questions, you should know how to extract the password attempts. You should also know what IP is submitting passwords. Are any other IP addresses submitting passwords?
```

### Solution:
We can use the first query from the previous question, we just need to make one change. In this case, we want to find all login attempts from any other IP address than the brute forcer. To do this, we just need to change the `=` operator in `src_ip=23.22.63.114` to `!=`.

**Search Query:**
```
sourcetype=stream:http http_method=POST src_ip!=23.22.63.114 form_data=*username*passwd*
| rex field=form_data username=(?<user>\w+)
| rex field=form_data passwd=(?<pw>\w+)
| table _time, user, pw
| sort by _time
```

The admin password appears to be `batman`.

![](./attachments/Pasted%20image%2020220423010235.png)

Answer: `batman`

## Question 18:
What was the average password length used in the password brute-forcing attempt? (Round to a closest whole integer. For example, "5" not "5.23213")

### Hints:
```
1. Calculate the length of every password attempt and store the result in a new field. Then calulate the average of that new field with a stats command. Use eval to average, or just visually inspect.
2. Then calulate the average of that new length field with a stats command, and finally use eval to round, or just manually round.
```

### Solution:
We can use the `avg()` and `round()` functions to find the average and round it to an integer value.

**Search Query:**
```
sourcetype=stream:http http_method=POST src_ip=23.22.63.114 form_data=*username*passwd*
| rex field=form_data passwd=(?<pw>\w+)
| eval passwordLen=len(pw)
| stats avg(passwordLen) as averageLen
| eval result=round(averageLen,0)
| table result
```

The returned value is `6`.

![](./attachments/Pasted%20image%2020220423012523.png)

Answer: `6`

## Question 19:
How many seconds elapsed between the brute force password scan identified the correct password and the compromised login? Round to 2 decimal places.

### Hints:
```
1. You'll note from previous answers that one of the passwords was attempted twice. You need to calculate the duration of time between those two attempts.
2. Need more help? Write a search that returns only the two events in questions, then use either "| delta _time" or "| transaction <extracted-pword-attempt>" SPL commands.
```

### Solution:
The `transaction` SPL commands calculates and makes the duration variable available.

**Search Query:**
```
sourcetype=stream:http http_method=POST form_data=*username*passwd*
| rex field=form_data passwd=(?<pw>\w+)
| search pw=batman
| transaction pw
| eval result=round(duration,2)
| table result
```

We get `92.17` seconds in return.

![](./attachments/Pasted%20image%2020220423014514.png)

Answer: `92.17`

## Question 20:
How many unique passwords were attempted in the brute force attempt?

### Hints:
```
1. Be sure you are extracting the password attempts correctly, then use a stats function to count unique (not total) attempts.
```

### Solution:
We can use the `dedup` SPL command to remove all duplicates.

**Search Query:**
```
sourcetype=stream:http http_method=POST src_ip=23.22.63.114 form_data=*username*passwd*
| rex field=form_data passwd=(?<pw>\w+)
| dedup pw
| stats count
```

We get `412` in return.

![](./attachments/Pasted%20image%2020220423100138.png)

Answer: `412`

## Question 21:
What was the most likely IP address of we8105desk in 24AUG2016?

### Hints:
```
1. Keep it simple and just search for the hostname provided in the question. Try using the stats command to get a count of events by source ip address to point you in the right direction.
```

### Solution:
We can return the likely IP address of `we8105desk` by counting the number of times different `src_ip` addresses appear in our search results. Because the source IP address of a system will appear every time it communicates, it is likely the IP address with the highest count that is the IP address of the system. We can use `sort - count` to sort the output, so the highest number will de displayed at the top of the list.

**Search Query:**
```
we8105desk
| stats count by src_ip
| sort - count
```

We get a list in return, it appears that `192.168.250.100` is likely the IP address we are looking for.

![](./attachments/Pasted%20image%2020220423104628.png)

Answer: `192.168.250.100`

## Question 22:
Amongst the Suricata signatures that detected the Cerber malware, which one alerted the fewest number of times? Submit ONLY the signature ID value as the answer. (No punctuation, just 7 integers.)

### Hints:
```
1. Keep it simple and start your search by looking at only the sourcetype associated with Suricata and maybe even the name of the malware in question. The field containing the signature ID should be obvious. Use stats to create a count by the field containing the signature ID.
```

### Solution:
We will search for `sourcetype=suricata` so we only get Suricata events, combined with the name of the malware `cerber`.

**Search Query:**
```
sourcetype=suricata cerber
```

Looking through the fields available after the search, we find `alert.signature_id`. The alert with ID `2816763` has only been triggered once.

![](./attachments/Pasted%20image%2020220423105343.png)

Answer: `2816763`

## Question 23:
What fully qualified domain name (FQDN) makes the Cerber ransomware attempt to direct the user to at the end of its encryption phase?

### Hints:
```
1. Search stream:dns data for A queries coming from the infected workstation IP on the date in question. Try and narrow your search period.
2. Perform a shannon entropy analysis on the query{} field using URL toolbox by adding this to the end of the search: |`ut_shannon(query{})` | stats count by ut_shannon, query{} | sort -ut_shannon
```

### Solution:
We can use `ut_shannon` to order our list after string complexity. This will make it easier to group false positives and filter them out.

In order to make `ut_shannon` work, we need the URL Toolbox app extension. If not already installed, the easiest way to get it is via the in-product app browser (Manage Apps -> Browse More Apps).

We will start off with this simple search query and slowly filter out the wrong results.

**Search Query:**
```
sourcetype=stream:dns src_ip=192.168.250.100
|`ut_shannon(query{})`
| stats count by ut_shannon, query{}
| sort - ut_shannon
```

We get `1.297` results. One at a time, adding filers we end up with this query.

**Search Query:**
```
sourcetype=stream:dns src_ip=192.168.250.100
| where !match(query, "in-addr")
| where !match(query, "microsoft")
| where !match(query, ".arp")
| where !match(query, ".local")
| where !match(query, ".com")
|`ut_shannon(query{})`
| stats count by ut_shannon, query{}
| sort - ut_shannon
```

This narrows the search down to 20 results, `cerberhhyed5frqa.xmfir0.win` looks strange.

![](./attachments/Pasted%20image%2020220423141344.png)

If we compare it with the screenshot, we got from the computer hit by the ransomware, we can see that one of the addresses match. This must be the FQDN we are looking for.

![](./attachments/Pasted%20image%2020220423134456.png)

Answer: `cerberhhyed5frqa.xmfir0.win`

## Question 24:
What was the first suspicious domain visited by we8105desk in 24AUG2016?

### Hints:
```
1. Search stream:dns data for A queries coming from the infected workstation IP on the date in question.
2. Use the "| reverse" SPL command to show oldest events first.
3. Eliminate domain lookups that you can explain, question the first one you cannot.
4. Go and git some IOCs on Cerber. Then compare to the DNS Data
```

### Solution:
First, on the right side of the page, we need to set the date to 24AUG2016.

![](./attachments/Pasted%20image%2020220423143240.png)

Like last time, we start with a simple query and slowly filter out false positives.

**Search Query:**
```
sourcetype=stream:dns src_ip=192.168.250.100 query=*.*
| table _time, query
| reverse
```

We end up with this.

**Search Query:**
```
sourcetype=stream:dns src_ip=192.168.250.100 query=*.* NOT .local AND NOT .arpa AND NOT microsoft
| table _time, query
| reverse
```

`solidaritedeproximite.org` look out of place.

Answer: `solidaritedeproximite.org`

## Question 25:
During the initial Cerber infection, a VB script is run. The entire script from this execution, pre-pended by the name of the launching .exe, can be found in a field in Splunk. What is the length in characters of the value of this field?

### Hints:
```
1. Keep it simple. Start by looking at Sysmon data for the infected device on the date in question. Calculate the length of the command line using the "len()" function of the "eval" SPL command, and give your eyes a break by using the Splunk table command.
```

### Solution:
Initially, we start with this search query in order to locate the script in question. Since it has been executed, it must be in the `CommandLine` field.

**Search Query:**
```
sourcetype=XmlWinEventLog:Microsoft-Windows-Sysmon/Operational *.vbs
| table CommandLine
```

There is no doubt which one contains the script we are looking for.

![](./attachments/Pasted%20image%2020220423150946.png)

In order to get the length in character of the field, we will use this search query.

**Search Query:**
```
sourcetype=XmlWinEventLog:Microsoft-Windows-Sysmon/Operational *.vbs CommandLine=cmd.exe*
| eval length=len(CommandLine)
| table length
```

It returns `4490`.

![](./attachments/Pasted%20image%2020220423151504.png)

Answer: `4490`

## Question 26:
What is the name of the USB key inserted by Bob Smith?

### Hints:
```
1. Tough question. Perhaps you should give http://answers.splunk.com a try.
```

### Solution:
When USB devices are plugged in, their name is stored in the `friendlyname` key in Windows registry.

**Search Query:**
```
sourcetype=WinRegistry friendlyname
```

![](./attachments/Pasted%20image%2020220423161310.png)

Answer: `MIRANDA_PRI`

## Question 27:
Bob Smith's workstation (we8105desk) was connected to a file server during the ransomware outbreak. What is the IP address of the file server?

### Hints:
```
1. Search for SMB (Windows file sharing protocol) traffic from the infected device on the date in question. The "stats" SPL command can be used to count the most common destination IP for the SMB protocol.
```

### Solution:
This query will fetch all the SMB events from Bob's workstation (`192.168.250.100`).

**Search Query:**
```
src_ip=192.168.250.100 sourcetype=stream:smb
| stats count by path
```

It has been connecting to `192.168.250.20`.

![](./attachments/Pasted%20image%2020220423165316.png)

Answer: `192.168.250.20`

## Question 28:
How many distinct PDFs did the ransomware encrypt on the remote file server?

### Hints:
```
1. Don't use SMB this time - it's a trap! Windows event logs are the way to go for this one. Focus on the event types that deal with windows shares and narrow the search by looking for distinct filenames for the extension in question.
```

### Solution:
First, we need to know which sourcetypes contain `*.pdf`.

**Search Query:**
```
*.pdf
| stats count by sourcetype
| sort -count
```

There is quite a lot of 'Windows Event Logs'.

![](./attachments/Pasted%20image%2020220423173325.png)

Let's dig deeper. We will use `count by dest` in order to find the destination of the files.

**Search Query:**
```
*.pdf sourcetype=wineventlog
| stats count by dest
| sort -count
```

![](./attachments/Pasted%20image%2020220423173856.png)

We'll add `dest=we9041srv.waynecorpinc.local` to the search query in order to try and locate the source.

**Search Query:**
```
*.pdf sourcetype=wineventlog dest=we9041srv.waynecorpinc.local
```

In the field's section, we found the `Source_Address` field.

![](./attachments/Pasted%20image%2020220423175441.png)

The following query will give us the final answer. The `dedup` SPL command is used to remove all duplicates.

**Search Query:**
```
*.pdf sourcetype=wineventlog dest=we9041srv.waynecorpinc.local Source_Address="192.168.250.100"
| dedup Relative_Target_Name
| stats count as Relative_Target_Name
```

We get `257` in return.

![](./attachments/Pasted%20image%2020220423181347.png)

Answer: `257`

## Question 29:
The VBScript found in question 25 launches 121214.tmp. What is the ParentProcessId of this initial launch?

### Hints:
```
1. Embrace your Sysmon data. Search for a command issued by the infected device on the date in question referencing the filename in question, and use the process_id, ParentProcessId, CommandLine, and ParentCommandLine, to track down the parent process id of them all.
```

### Solution:
This is a quick one, we'll simply search for the `121214.tmp` and `*.vbs` file.

**Search Query:**
```
121214.tmp *.vbs
```

In the field's section under `parent_proccess_id` we can see that the ID is `3968`.

![](./attachments/Pasted%20image%2020220423182540.png)

Answer: `3968`

## Question 30:
The Cerber ransomware encrypts files located in Bob Smith's Windows profile. How many .txt files does it encrypt?

### Hints:
```
1. Sysmon to the rescue again. Focus on the infected machine as well as the user profile while searching for the filename extension in question.
2. In Sysmon events, EventCode=2 indicates file creation time has changed. Watch out for duplicates!
```

### Solution:
Since we know the target is Bob, we can set the `TargetFilename` to be his directory.

**Search Query:**
```
sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" TargetFilename="C:\\Users\\bob.smith.WAYNECORPINC*.txt"
| stats count as TargetFilename
```

We get `406` in return.

![](./attachments/Pasted%20image%2020220423191917.png)

Answer: `406`

## Question 31:
The malware downloads a file that contains the Cerber ransomware crypto code. What is the name of that file?

### Hints:
```
1. When looking for potentially malicious file, start your search with the Suricata data. Narrow your search by focusing on the infected device. Remember malware does not always have to begin as an executable file.
```

### Solution:
Since the malware is installed on `192.168.250.100` that will be the source IP address. The file is probably downloaded from one of the malicious domains we found in question 24.

**Search Query:**
```
src_ip="192.168.250.100" solidaritedeproximite.org http_method=GET
| table url
```

The malware has downloaded what appears to be an image file from `solidaritedeproximite.org`.

![](./attachments/Pasted%20image%2020220423190108.png)

Answer: `mhtr.jpg`

## Question 32:
Now that you know the name of the ransomware's encryptor file, what obfuscation technique does it likely use?

### Hints:
```
1. The enrcyptor file was an image!
```

### Solution:
When you try to hide the existence of something by encapsulating it in something else, it is called [Steganography](https://en.wikipedia.org/wiki/Steganography). In this case, the executable was made to look like an innocent image.

Answer: `Steganography`

![](./attachments/Pasted%20image%2020220423232646.png)

---
**Tags:** [[Cyber Defenders]]