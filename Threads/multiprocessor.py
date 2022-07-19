
import concurrent.futures
import time
import threading 
import multiprocessing
start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

#with concurrent.futures.ThreadPoolExecutor() as executor:
#    secs = [5, 4, 3, 2, 1]
#    results = executor.map(do_something, secs)
#
#    for result in results:
#         print(result)

if __name__ == '__main__':
    threads = []

    for _ in range(10):
        t = multiprocessing.Process(target=do_something, args=[1.5])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')