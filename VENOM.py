import os,platform
os.system('git pull')
 
VENOM=platform.architecture()[0]
if VENOM=="32bit":
    print(' [•] 32Bit Coming Soon..!')
elif VENOM=="64bit":
     __import__("BSDK")
