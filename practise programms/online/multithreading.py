#multithreading
#beakdown of big task 
from time import sleep
from threading import *

class RCB(Thread):
    def run(self):
        for i in range(5):
            print("RCB WINS")
            sleep(1)

class CSK(Thread):
    def run(self):
        for i in range(5):
            print("CSK LOOSE")   
            sleep(1)

r1=RCB()
c1=CSK()        

r1.start()
sleep(0.2)
c1.start()
r1.join()
c1.join()


print("Match Ended")
