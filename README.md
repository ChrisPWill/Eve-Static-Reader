# Eve-Static-Reader
Encapsulates Eve Online sqlite database for its static data and provides some helper functions to access data within.

Copy settings_example.ini to settings.ini before use.

The use_mem option, when changed to "yes" will load the DB into memory for faster lookups. Note that the act of loading the database may take 1-5 minutes and consume 1.5GB of RAM temporarily (~400-500MB once loaded). As such, use_mem should be disabled except if needed for a larger scale use (in which case you probably shouldn't be using my script anyway...)

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
