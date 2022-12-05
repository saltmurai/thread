import threading
import time
import random as rand
import psutil

# Create a lock object to use as a mutex
lock = threading.Lock()

# Define a function that will be run by each thread
def thread_function(name, delay):

  # Acquire the lock to access the shared resource
  start_time = time.perf_counter()
  lock.acquire()
  try:

    # Access the shared resource here
    print(f'Thread {name} is accessing the shared resource')
    count = 0
    while count < 5:
      time.sleep(delay)
      count += 1
      print(f'Thread {name}: {time.ctime(time.time())}')
    # Release the lock when you are done
  finally:
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    # Log the total execution time
    print(f'Thread {name} executed in {execution_time:.2f} seconds')
    thread_process = psutil.Process()
    ram_used = thread_process.memory_info().rss
    print(f'Thread {name} used {ram_used} bytes of RAM')
    lock.release()

# Create some threads and start them
threads = []
for i in range(5):
  threads.append(threading.Thread(target=thread_function, args=(i, 2)))
  threads[-1].start()

# Wait for all threads to complete
for thread in threads:
  thread.join()
