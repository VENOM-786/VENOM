import os,platform
os.system('git pull')
#exit('\n Wait Working On Tool..!')
VENOM=platform.architecture()[0]
if VENOM=="32bit":__import__("VENOM32")
elif VENOM=="64bit":__import__("VENOM")
