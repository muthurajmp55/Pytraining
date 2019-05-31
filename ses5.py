import threading
import time 


def t1():
    for i in range(5):
       print('word')
       time.sleep(2)
def t2():   
    for i in range(5):
       print('hello')
       time.sleep(2)

tt1=threading.Thread(target=t1)
tt2=threading.Thread(target=t2)
x=time.time()
tt1.start()
tt2.start()

tt1.join()


y=time.time()

tt2.join()
print(y-x)
