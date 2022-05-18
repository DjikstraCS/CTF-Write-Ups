# REM Mandatory
## Part 1
### Problem 1
We are given a file, `bomb.exe`. When executed, it asks for a password. 

![](./attachments/Pasted%20image%2020220506222444.png)

Opening the file in IDA, we first try to get an overview.

![](./attachments/Pasted%20image%2020220506223206.png)

It looks like a lot of if statements. If not true, the program terminates.

Looking at the first section, we can see a compare is made between `eax` and `0DEADBABEh`. This i likely the imputed password and a hard-coded string being compared. Decoding `0DEADBABEh` will reveal the password.

![](./attachments/Pasted%20image%2020220506225716.png)

First we tried feeding it to [CyberChefs](https://gchq.github.io/CyberChef) magic operation which correctly identified it as a HEX value. Otherwise, no useful information was revealed.

Looking closer at the value, we realize that it is readable in clear text as 'DEAD BABE'. Upon searching for `DEADBABE` on Google we find a Wikipedia article on [Hexspeak](https://en.wikipedia.org/wiki/Hexspeak) In the 'Notable magic numbers' section of the page we find a table entry for `0xDEADBABE` with a decimal value of `3735927486`.

![](./attachments/Pasted%20image%2020220506225222.png)

Even though Cyberchef refused to help us, other online converters like [RapidTables](https://www.rapidtables.com/convert/number/hex-to-decimal.html) are more helpful.

![](./attachments/Pasted%20image%2020220509152324.png)

Testing `3735927486` as the password:

![](./attachments/Pasted%20image%2020220509153805.png)

### Problem 2

Looking at section number two, we find another compare. 

![](./attachments/Pasted%20image%2020220509154239.png)

This time [CyberChef](https://gchq.github.io/CyberChef) is much more helpful.

![](./attachments/Pasted%20image%2020220506230351.png)

We try `k` as password number two:

![](./attachments/Pasted%20image%2020220509153902.png)

### Problem 3

This section is not as simple as the previous two.

We have to look back through the assembly to get the value of `[ebp+var_C]`, which is being compared before the jump.

Going thought the code, we realize that we know the value of `al` from the previous problem. It is being moved around and modified by one subtraction and added upon twice, lastly it ends up in `[ebp+var_C]`.

![](./attachments/Pasted%20image%2020220509154448.png)

The calculation:
```
al = 1O7
107 - 98 = 9
9 + 9 = 18
18 + 9 = 27
27 + 16 = 43
```

Testing `43` as the password:

![](./attachments/Pasted%20image%2020220509154048.png)


## Part 2
### Static analysis
Upon opening the `corona.exe` in `x32dbg` we first check imports.

We can see that the executable is able to edit registry vales.

![](./attachments/Pasted%20image%2020220509160534.png)

Write to the console, manage internet connections, among other things.

![](./attachments/Pasted%20image%2020220509160349.png)

Then we have a closer look at Strings.

We discover that an HTTP request is made to get `ncat.exe`.

Netcat will be able to call home, thus making a backdoor into our system.

![](./attachments/Pasted%20image%2020220509160056.png)

On the last line we see a message.

![](./attachments/Pasted%20image%2020220509160730.png)

### Manual code review

Now that we have a rough idea about what the program is doing, we will have a closer look at the assembly code.

We first noticed that there are a lot of if statements. Having a closer look at them, we can see that they are a result of trying to obfuscate the code. Many of them are comparing the same values, resulting in jumping to the same location in all cases.

![](./attachments/Pasted%20image%2020220509162307.png)

If not comparing the same values, the values are carefully handled in such a way that they will always execute the same way. 

The following image shows the path through the code.

![](./attachments/Pasted%20image%2020220509164121.png)

We have now reached in interesting block.

Looking through the calls, we find that `sub_4014E0` contains a lot of interesting code.

![](./attachments/Pasted%20image%2020220509164450.png)

We take special note of the`ds:IsDebuggerPresent` call.

This is probably the beginning of the malicious part of the code. Exactly what we are looking for.

If a debugger is present, the code will not execute whatever is in the block marked with red.

Also, there is a `ds:ShowWindow` call, this is likely a window being opened by the malware.

![](./attachments/Pasted%20image%2020220518112155.png)

In the next block, we can see how the massage we discovered earlier is being displayed.

Furthermore, a Windows Registry value is likely being changed to `corona`.

![](./attachments/Pasted%20image%2020220517122906.png)

Going back to the malicious code block and diving into `sub_241010`, we discover what appears to be the download and execution of a netcat listener.

First, we see that the malware is trying to make it look like a Windows update.

![](./attachments/Pasted%20image%2020220517123900.png)

Then it creates an HTTP request for `ncat.exe`.

![](./attachments/Pasted%20image%2020220517124045.png)

Double clicking `aHttpSNcatExe` will lead us to where the value is stored. 

There are two interesting values here.

![](./attachments/Pasted%20image%2020220509165851.png)

The netcat line confirms our hypothesis about netcat being set up as a listener.

Next, we try to decode `xmmword_256BFC`, it turns out it to be `cmd.exe` in clear text.

![](./attachments/Pasted%20image%2020220518121859.png)

Using `CTRL + X` we will try and find where they are used in the malware. It leads us to this block where we can see that first `cmd.exe` is run, then the command line is used to set up the netcat listener. 

![](./attachments/Pasted%20image%2020220518125813.png)

Going a step back, we will have a look at the rest of the code.

Creates a file and downloads the content to it.

![](./attachments/Pasted%20image%2020220517124720.png)

In order to login with netcat, a username needs to be provided. Therefore, the malware will get the current username and send it to the attacker.

![](./attachments/Pasted%20image%2020220517125143.png)

It will try to make itself appear like a Google Chrome updater.

![](./attachments/Pasted%20image%2020220517125239.png)

Now that we have a basic understanding of how the malware works, we will try to actually run it and see how it behaves in practice.

## Dynamic Analysis
Lets fire up the debugger and set a few break points.

First, we need to make a breakpoint at `ds:IsDebuggerPresent` in order to manipulate the malware to run even though we have a debugger present. Secondly, we would like to see if we can extract the IP address of the attackers' server, therefore we will set at breakpoint at `"http://%s/ncat.exe"` in order to search for it.

Register value.

![](./attachments/Pasted%20image%2020220518104756.png)

Then execute the malware.

A window appears on our screen, its only content is an image of a coronavirus.

![](./attachments/Pasted%20image%2020220518111905.png)

As we have reached the first break point we need to edit the value of `EAX` in order to trick the malware into believing there is no debugger present, we will do this by changing the value of it from `1` to `0`. Then continue executing the program.

![](./attachments/Pasted%20image%2020220518110149.png)

When we click run again and hit the next breakpoint, the window updates with text.

![](./attachments/Pasted%20image%2020220518113315.png)

Now we will try to find the IP address of the attackers' pre-staged machine. 

We stop at `"http://%s/ncat.exe"` and do one step-over at a time, until we find the value which is supposed to be inserted into the URL.

The IP address of the attackers' pre-staged machine: `207.154.194.47`

![](./attachments/Pasted%20image%2020220518112816.png)

When we execute the rest of the program, a button appears in the windows.

![](./attachments/Pasted%20image%2020220518113850.png)

### Behavioral analysis
#### Regshot
![](./attachments/Pasted%20image%2020220518134105.png)

After running it, we get a lot of logs.

We found two edited lines containing `corona`.

```
HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-3176667959-2031769853-1735657949-1000\\Device\HarddiskVolume3\Users\admin\Desktop\Malware\Mandatory\part2\corona.exe:  DB C0 07 D5 9E 6A D8 01 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00
```

```
HKU\S-1-5-21-3176667959-2031769853-1735657949-1000\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Corona:  43 3A 5C 55 73 65 72 73 5C 61 64 6D 69 6E 5C 44 65 73 6B 74 6F 70 5C 4D 61 6C 77 61 72 65 5C 4D 61 6E 64 61 74 6F 72 79 5C 70 61 72 74 32 5C 63 6F 72 6F 6E 61 2E 65 78 65 00 00 00 08 08 00 00 00 00 00 00 A8 F7 D6 00 44 76 24 00 00 00 F5 00 30 00 00 00 C4 F7 D6 00 FD 78 95 77 64 F8 D6 00 20 AD 94 77 A6 A0 1C 5A FE FF FF FF DC F7 D6 00 FD 78 95 77 38 57 F6 00 08 08 00 00 40 57 F6 00 00 00 F5 00 00 B0 AB 00 00 00 00 00 B9 FC 92 77 00 00 F5 00 04 00 00 00 00 00 00 00 01 01 00 00 CE 5D 91 77 15 5D F6 00 68 00 00 40 00 08 00 00 00 00 00 00 24 00 00 00 00 00 F5 00 E8 F7 D6 00 8A 95 57 2D F8 F7 D6 00 F0 F7 D6 00 C4 39 EE 75 44 94 25 00 00 00 00 00 00 B0 AB 00 10 F8 D6 00 B8 8B 24 00 00 00 00 00 82 35 F5 00 44 1D F5 00 08 81 25 00 F8 48 F6 00 00 00 00 00 28 F8 D6 00 0E 8C 24 00
```

#### Process Monitor
Shows a lot of activity from `corona.exe`

![](./attachments/Pasted%20image%2020220518134655.png)

#### Process Hacker
Gave us no interesting results.

![](./attachments/Pasted%20image%2020220518140744.png)

#### Network
The network analysis confirms our assumption about netcat being downloaded and sending the username of the victims' machine back to the attacker. Even though there is en encoding issue, the number of characters correlate with `Admin`.

![](./attachments/Pasted%20image%2020220518140003.png)

# Spørgsmål:
Hvor meget er der vægt på de små programmer vs IDA og dbg?

Hvad er Statisk analyse vs manuel kode analyse og er der en bestemt rækkefølge?

LIFO, hvad betyder det helt præcist?

Gennemgå stack function calls igen?


# Mangler:
Forstå stack, fx push.
Læs sider igen

![](Pasted%20image%2020220518151211.png)

![](Pasted%20image%2020220518151547.png)

![](Pasted%20image%2020220518152059.png)

![](Pasted%20image%2020220518152111.png)

![](Pasted%20image%2020220518152938.png)

![](Pasted%20image%2020220518154203.png)

![](Pasted%20image%2020220518154537.png)

![](Pasted%20image%2020220518155212.png)

https://www.youtube.com/watch?v=7ZBAVsRQk-o

https://www.youtube.com/watch?v=A5lB3nEazc0