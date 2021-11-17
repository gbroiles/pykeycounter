# copied from https://www.geeksforgeeks.org/design-a-keylogger-in-python/
import os
import pyxhook
import syslog

count = 0

#creating key pressing event and saving it into log file
def OnKeyPress(event):
    global count
    count += 1
    print(".",end='',flush=True)
    if count == 100:
        print("100!",flush=True)
        syslog.syslog("Got 100 keystrokes.")
        count = 0

# create a hook manager object
print("Running.")
new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
# set the hook
new_hook.HookKeyboard()
print("Things are set up.")
try:
    print("In the try loop")
    new_hook.start()		 # start the hook
    print("Past hook,start()")
except KeyboardInterrupt:
	# User cancelled from command line.
    pass
except Exception as ex:
    msg = 'Error while catching events: {}'.format(ex)
    syslog.syslog(msg)

