# Baby RE
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: Baby RE
* Topic: [[]]
* Difficulty: Easy
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Flag:
![](./attachments/Pasted%20image%2020220516124638.png)

Opening the file in IDA, we see a few interesting lines.

![](./attachments/Pasted%20image%2020220516124334.png)

Grabbing the hex and giving it to cybershef reveals that we have the flag. We just need to decode them, reverse the string and lastly join all four together.

![](./attachments/Pasted%20image%2020220516124734.png)

**Flag:** `HTB{B4BY_R3V_TH4TS_EZ}`

---
**Tags:** [[Hack The Box]]