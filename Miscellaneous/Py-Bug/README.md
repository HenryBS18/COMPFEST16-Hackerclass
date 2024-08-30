# Title
Py-Bug (500 points)

# Flag
COMPFEST16{belajar_debug_pake_python_yekan_8691c490f1}

# Description
I don't think that someone know my random password for admin credential.

```bash
nc challenges.ctf.compfest.id 20010
```

# Author
Zanark

# Solution
first of all we that everytime we start the program, it will automatically register a user named **cf-min** with role **admin**,

we can register a new user with name **"cf-min "** (with space), because first the register function will check if username is already registered, so we add space at the end of cf-min, then if not it will remove the space and store it into the accounts array. then we retrieve a session key.

then we can login with session key method

in login function, it will check the account[0] (which this account is registered automatically) and the name of our username that we made,
if same it will return the username and role **admin**

then we are in administrator menu now.

then i choose debug menu, and the program ask to input command but it limited only max 15 characters and we cant use **_** which we cant use dunder's too.

so i try to look at python builtin functions, and since the menu is named **debug**, i got 1 function that is related with **debug** things, its **breakpoint()** function.

and yes we are in python debugging mode right now, and i can make any commands without any restrictions.

so this is what i do
```python
import os

os.system('ls')

os.system('ls / ')

print(open('/flag').read())
```