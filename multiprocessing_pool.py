from multiprocessing.pool import Pool

def cube(number):
    return number**3

if __name__ == '__main__':
    # Using Pool
    numbers = range(11)
    pool = Pool()

    result = pool.map(cube, numbers)
    pool.close()
    pool.join()

    print(result)
