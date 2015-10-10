# Eve-Static-Reader
Encapsulates Eve Online sqlite database for its static data and provides some helper functions to access data within.

Example code:
~~~python
import esr

e = esr.ESR()
# Get name of Tritanium
# 'Tritanium'
name = e.name_from_typeid(34) 
# Get volume of Tritanium
# 0.01
vol = e.vol_from_typeid(34) 
~~~
