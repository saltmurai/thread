import threading
import time
import psutil 

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))


def thread_time(target, threadName):
   def wrapper(*args, **kwargs):
       st = time.time()
       try:
           return target(*args, **kwargs)
       finally:
           et = time.time()
           print(f"Execution time of {threadName}: {et - st}")
           print(f"Finish {threadName} RAM useage {psutil.virtual_memory().percent}")
           threading.currentThread().duration = et - st
           print(f"Start time of {threadName}: {st}")
           print(f"End time of {threadName}: {et}")
   return wrapper

if __name__ =="__main__":
	# creating thread
	t1 = threading.Thread(target=thread_time(print_time, "thread 1"), args=("Thread 1", 2))
	t2 = threading.Thread(target=thread_time(print_time, "thread 2"), args=("Thread 2", 1))	
	# starting thread 1
	t1.start()
	# starting thread 2
	t2.start()
	# wait until thread 1 is completely executed
	t1.join()
	# wait until thread 2 is completely executed
	t2.join()
	# both threads completely executed
	print("Done!")
