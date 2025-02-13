# some of common modules in Python are: datetime random string os math browser(interacting with browsers)
# Following line shows by running it, I can run basic/normal commands in python
# <script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.7.0/brython.min.js"></script>
# the above and below line can be added to the index.html in my workspace
# <script type="text/javascript"
#      src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.7.0/brython_stdlib.js"></script>
# import platform
# The above shows standard library which is bigger and I can start importing things.

# if I am looking for a specific module I can check it in this URL:
# https://docs.python.org/3/py-modindex.html


import platform
# print(dir(platform)) # to check what it does, it gives me all the methods inside module.
print(platform.python_version()) # it shows the python version that I'm running.

# for importing more than one module, I can do that by separating them with a comma.
import platform, string, os
# to access any of these functions inside those modules, I would prefix them with the name
# to shorten our typing a bit, I can import them and give them an alias:
import platform as pl
print(pl.python_version()) #platform.python_version() it does not work anymore.

# I can even import just one function/method and there is no need to type it all the time:
# I can separate different functions by comma:
from platform import python_version, system
# to access them now, I don't need prefix:
print(python_version())
print(system())

# alias works here as well:
from platform import python_version as pv
print(pv())