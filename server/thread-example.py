import threading
import time

def task1():
    for i in range(15):
        print(i)
        time.sleep(0.3)

def task2():
    for i in range(100, 115):
        print(i)
        time.sleep(0.3)

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
