
# never name your script as threading.py
# [ERROR] threading module has no attribute 'Thread'

# module: thread object
import threading
# import _thread

import time


def do_sth():
    print('sleeping .1 sec')
    time.sleep(0.1)
    print('back from sleep')

# threading.Thread(target="function")
# just pass in the function itself

# arg=(5, None) takes arguments arg(5,)
t1 = threading.Thread(target=do_sth)
t2 = threading.Thread(target=do_sth) 



# # .start() will begin run the thread, executing the function which is passed in 
# t1.start()
# t2.start()


print(threading.active_count())

# t1.join()
# t2.join()


# *****************************************************************************************

import threading 
import time

def count(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(1)
for _ in range(2):
    x = threading.Thread(target=count, args=(5,))
    x.start()
    # print('Done')


# # this is main thread
# print("Done")


# to fix the main thread kick in befor threading end, use .join()
x.join()
print("done")

