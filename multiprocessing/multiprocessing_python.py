import re
import time
# import multiprocessing
import concurrent.futures

def do_something(sec):
    print(f'Sleeping {sec} second(s)...')
    time.sleep(sec)

    return f'Done Sleeping...{sec }'


start = time.perf_counter()

# p_list=[]

# for _ in range(10):
#     p=multiprocessing.Process(target=do_something, args=(2,))
#     p.start()
#     p_list.append(p)

# for p in p_list:
#     p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    results=executor.map(do_something,secs)

    for result in results:
        print(result)


finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
