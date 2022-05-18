# You Cant C Me
* Source: [Hack the Box](https://hackthebox.com/)
* Challenge: You Cant C Me
* Topic: [[]]
* Difficulty: Easy
* Date: DD-MM-YYYY
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Flag:
![](./attachments/Pasted%20image%2020220516125824.png)

Opening the file in IDA, look at the strings section for somthing interesting.

![](./attachments/Pasted%20image%2020220516125946.png)

Double clicking it reveals what appears to be the flag.

![](./attachments/Pasted%20image%2020220516130049.png)

Grabbing the hex and giving it to cybershef reveals that we have the flag. We just need to decode them, reverse the string and lastly join all four together.

![](./attachments/Pasted%20image%2020220516124734.png)

![](./attachments/Pasted%20image%2020220516132120.png)

`this_is_the_password`

![](./attachments/Pasted%20image%2020220516132152.png)

`æebb.vQo&kUZ'ZUYUc)`

# TO BE CONTINUED...

**Flag:** ``

---
**Tags:** [[Hack The Box]]