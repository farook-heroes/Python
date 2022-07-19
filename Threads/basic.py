import time 
import threading
import multiprocessing
s=time.perf_counter()
def do_something():
    print(f"start")
    time.sleep(1)
    print(f"end\n")

t1=threading.Thread(target=do_something)  
t2=threading.Thread(target=do_something)    
t1.start()
t2.start()
t1.join()
t2.join()
t=multiprocessing.Process(target=do_something)
t.start()
f=time.perf_counter()
print(round(f-s,2))
    