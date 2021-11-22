import win32event
import time

try:
    mutex = win32event.CreateMutex(None, 1, "ROBLOX_singletonMutex")
    print('Mutex created')
    while True:
       time.sleep(864000)
finally:
    win32event.ReleaseMutex(mutex)
    print('Closed mutex')