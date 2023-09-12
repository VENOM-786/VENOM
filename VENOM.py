import os,platform
os.system('git pull')
exit('\n Wait Working On Tool..!')
VENOM=platform.architecture()[0]
if VENOM=="32bit":exit(' 32bit coming soon')#__import__("BSDK32")
elif VENOM=="64bit":__import__("BSDK")
