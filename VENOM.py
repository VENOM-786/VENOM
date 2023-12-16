import os,platform
os.system('git pull')
#exit('\n Update Soon...!')
print(' \n\n[1] File Cloning \n [2] Main Menu ')
g = input(' choose :- ')
if g == '1':
    VENOM=platform.architecture()[0]
    if VENOM=="32bit":__import__("BSDK32")
    elif VENOM=="64bit":__import__("BSDK")
elif g == '2':
    VENOM=platform.architecture()[0]
    if VENOM=="32bit":__import__("LPC32")
    elif VENOM=="64bit":__import__("LPC")
else:exit(' choose wrong ')
