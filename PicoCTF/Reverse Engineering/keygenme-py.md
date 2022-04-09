# keygenme-py
* Source: PicoCTF
* Link: [PicoCTF.org](https://picoctf.org/)
* Challenge: keygenme-py
* Category: Reverse Engineering
* Points: 30
* Date: 09-04-2022
* Author: [DjikstraCS](https://github.com/DjikstraCS)

---
## Problem:
![](./attachments/Pasted%20image%2020220409185530.png)

---
## Solution:
Not a lot of description or hints. 

In the top of the file we can see some of the flag.

```py
# GLOBALS --v
arcane_loop_trial = True
jump_into_full = False
full_version_code = ""

username_trial = "SCHOFIELD"
bUsername_trial = b"SCHOFIELD"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```

Further down, we can see how the authentication methods `enter_license()` and `check_key()` work.

```py
def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial
    
    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")


def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False



        return key
```

In the first section of the `check_key()` method, the program is simply checking if the first part of the license is the same as the global variable `key_part_static1_trial`, which is the beginning of our flag. This means that the flag = license.

```py
	if len(key) != len(key_full_template_trial):
			return False
		else:
			# Check static base key part --v
			i = 0
			for c in key_part_static1_trial:
				if key[i] != c:
					return False

				i += 1
```

In the second section of the `check_key()` method, the program is using SHA-2 to hash the hard-coded username `SCHOFIELD`, picking out seemingly random hard-coded values from it and comparing it to the rest of the license.

```py        
	if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
		return False
	else:
		i += 1

	if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
		return False
	else:
		i += 1
		
	if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
        return False
   	else:
        i += 1
    #(...)
```

If we can calculate those hashes, we will get the flag. 

We can copy the lines and calculate the last part of the flag/license earlier in the program. Make sure to also remove or comment out `global bUsername_trial`, otherwise it will prevent `bUsername_trial` from being initialized.

```py
def enter_license():
    sec = hashlib.sha256(bUsername_trial).hexdigest()[4]
    sec += hashlib.sha256(bUsername_trial).hexdigest()[5]
    sec += hashlib.sha256(bUsername_trial).hexdigest()[3]
    sec += hashlib.sha256(bUsername_trial).hexdigest()[6]
    sec += hashlib.sha256(bUsername_trial).hexdigest()[2]
    sec += hashlib.sha256(bUsername_trial).hexdigest()[7]
    sec += hashlib.sha256(bUsername_trial).hexdigest()[1]
    sec += hashlib.sha256(bUsername_trial).hexdigest()[8]
    print('\nThe activation key is: ' + key_part_static1_trial + sec + key_part_static2_trial + '\n\n')
    
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    #global bUsername_trial
```

Let's run it again and see what happens. 

![](./attachments/Pasted%20image%2020220409210716.png)

Now when we run the program we get the flag/license printed, right when we need it. 

**Flag:** `picoCTF{1n_7h3_|<3y_of_e584b363}`

---
**Tags:** [[PicoCTF]] [[Python]] [[SHA-2]]