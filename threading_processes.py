from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
    time.sleep(0.1)


processes = []
# Set processes limits
num_processes = os.cpu_count()

# Create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# Start processes
for p in processes:
    p.start()

# join processes
for p in processes:
    p.join()

print('All processes are done')