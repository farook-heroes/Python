import threading
import time
counter=1
class Threader(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id
    def run(self):
        global counter
        lock.acquire()
        printodd() 
        lock.release()
          
      
class Threader2(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id
    def run(self):
        global counter
        lock.acquire()
              
        lock.release()
        printeven()
        
def printodd():
    global counter
    for i in range(1,10,2):
        print(i)
        counter+=1
        time.sleep(1)
def printeven():
    global counter
    for i in range(2,10,2):
        print(i)
        counter+=1
        time.sleep(1) 
lock=threading.Lock()
thread1=Threader(1)
thread2=Threader2(2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('process finished')
          