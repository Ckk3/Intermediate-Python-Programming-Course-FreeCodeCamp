from threading import Thread, Lock



database_value = 0

def increase(lock:Lock):
    global database_value

    # Open lock with lock.acquire() and close lock with lock.release(), same that we do in files like open() and close()
    with lock:
        local_copy = database_value

        local_copy += 1
        print(local_copy)

        database_value = local_copy
    


if __name__ == '__main__':
    print('Start value:', database_value)
    # Use lock 
    lock = Lock()

    thread_1 = Thread(target=increase, args=(lock,))
    thread_2 = Thread(target=increase, args=(lock,))

    thread_1.start()
    thread_2.start()


    thread_1.join()
    thread_2.join()


    print(database_value)
    print('end main')