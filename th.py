import threading
import os
import time

def sqr_num(x):
    print("Thread Name {}".format(threading.current_thread().name))
    print(("process {}".format(os.getpid())))
    print("Saquare:", x*x)

    time.sleep(30)
    print("sqr fn completed")


def cub_num(x):
    print("Thread Name {}".format(threading.current_thread().name))
    print(("process {}".format(os.getpid())))
    print("Cube:", x * x * x)
    time.sleep(30)
    print("cube fn completed")



t1=threading.Thread(target=sqr_num,args=(10,))
t2=threading.Thread(target=cub_num,args=(10,))

t1.start()
t2.start()


t1.join()
t2.join()