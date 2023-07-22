import os,platform
os.system('git pull')
 
VENOM=platform.architecture()[0]
if VENOM=="32bit":
    __import__("BSDK")
elif VENOM=="64bit":
     __import__("BSDK")
