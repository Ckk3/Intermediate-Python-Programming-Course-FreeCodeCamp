from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i
    time.sleep(0.1)


threads = []
num_threads = 20

# Create thread
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# Start processes
for t in threads:
    t.start()

# join processes
for t in threads:
    t.join()

print('All processes are done')