import time 
import threading

s=time.perf_counter()
def do_something():
    print(f"start")
    time.sleep(1)
    print(f"end\n")
if __name__ == '__main__':
    do_something()

