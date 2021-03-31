import time
from win10toast import ToastNotifier

toast = ToastNotifier()

firval = 1
wait = time.sleep

print("How long do you want your timer to last?")
lasval = input()

# Firval is short for first value, and lasval is short for last value.

VOID_ILLUSION = ('''

































''')

#Gives the script everything it needs to run efficiently. ^^

print (VOID_ILLUSION)

toast.show_toast("PY-TIMER", "Timer Starting.", icon_path=None, duration=5)

#Tells the user their timer is starting. ^^

print(VOID_ILLUSION)

while int(firval) - int(lasval) - 1:
    print("")
    print(firval)
    firval = int(firval) + 1
    wait(1)

#The main components the script needs to be able to work. ^^

print(VOID_ILLUSION)

print("Your timer's done!")

toast.show_toast("PY-TIMER", "Your timer's done!",
icon_path=None, duration=5)

#Tells the user their timer is finished. ^^

while toast.notification_active():
    wait(5)

#Makes a delay so the user can see what's happened. ^^




#Script made by Bot_101 on Github, more projects coming soon!
# - Dylan
