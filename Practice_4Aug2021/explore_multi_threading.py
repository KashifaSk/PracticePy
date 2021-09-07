from time import sleep
import threading

class Hello(threading.Thread):
    def run(self):
        for i in range(5):
         print("hello")
         sleep(1)

class Hi(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
t1 = Hello()
t2 = Hi()

t1.start()
sleep(.2)
t2.start()

t1.join()
t2.join()

print("Bye")
