# Christian Guiang
# October 31, 2022
# More toast notification testing; checks if duration params bypass the Ease of
# Access setting.

# Doesn't look like the settings have much of a grip over it if you set the
# duration lower here. What about a higher duration?
# If the duration is higher than the Ease of Access settings, then the settings will take the notification down.
# HOWEVER, the timer duration will continue in the program, so this could be problematic if the notifications
# aren't threaded (i.e., threaded is set to False).
# Note: Higher duration here overpowers edited versions in registry... unless you did it wrong?

from win10toast import ToastNotifier

tst = ToastNotifier()

inp = 1;
count = 0
while (inp==1):
    inp=int(input("Continue? Yes=1, No=0"))
    count = count + 1
    tst.show_toast("Header", "Try #"+str(count), icon_path=None, duration=15, threaded=False)

print("Bypass testing ended after "+str(count)+" tries.\n")
    




