import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
VENOM=platform.architecture()[0]
if VENOM=="32bit":__import__("BSDK32")
elif VENOM=="64bit":
     __import__("BSDK")
