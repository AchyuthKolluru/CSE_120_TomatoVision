# Christian Guiang
# October 18, 2022
# Shamelessly copying the example from the Github, good for you (jk it's alright)

# Original code
#from win10toast import ToastNotifier
#toaster = ToastNotifier()
#toaster.show_toast("Hello World!!!",
#"Python is 10 seconds awsm!",
#icon_path="custom.ico",
#duration=10)

#toaster.show_toast("Example two",
#3"This notification is in it's own thread!",
#icon_path=None,
#duration=5,
#threaded=True)
# Wait for threaded notification to finish
#while toaster.notification_active(): time.sleep(0.1)
# End original code

# Ok, you can uncomment that if you want, but the premise seems to be as follows:
# You import ToastNotifier first, since that's the library you need to make Toast notifications.
# Make a ToastNotifier object.
# "objectName.show_toast("message1", "message2", icon_path="img", duration=10, threaded=True)" will call that object an display a notification with the following params:
#	- message1, which is the header message (This isn't necessary, you can leave it as "". It'll bold message2 too.)
# 	- message2, which is the body message (This is necessary, you can't leave it as "")
# 	- img, which is the image shown. You can use "None" for no image. Super plain toast, huh.
# 	- duration, which is TTL in seconds
#	- threaded, which denotes whether or not a program is allowed to continue running while the Toast notification is up.
#		- Think of it like a wait timer in OW workshop, or a sleep() that affects everything.
# Speaking of which, sleep(time) can be used to wait time seconds before executing the code that follows.

# Necessary imports: toastNotifier is the notification system, time is for sleep, keyboard is for key presses
from win10toast import ToastNotifier
import time

# Initialize Toast object
toaster = ToastNotifier()

# Set up notifications
# Oh I forgot that Python loops don't have an end. Also range goes to stop-1, so if you put range(1,10), it goes 1-9.
for a in range (1,10):
    if (not(a==9)):
        toaster.show_toast(str(a), "ALERT?", icon_path=None, duration=1.5, threaded=False)
        print(str(a) + " triggered!\n")
    else:
        toaster.show_toast("Test to make lasting?", "This message is customizable", icon_path=None, duration=10, threaded=False)
        print(str(a) + " triggered!\n")


# Ctrl+C breaks sleep like it does with terminal commands.
time.sleep(5);