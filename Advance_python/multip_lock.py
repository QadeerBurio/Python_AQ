import multiprocessing
import time

def print_numbers(numbers, lock):
    lock.acquire()  # Acquire the lock
    try:
        for n in numbers:
            print(f"Processing number: {n}")
            time.sleep(0.5)  # Simulate work
    finally:
        lock.release()  # Ensure the lock is released even if an error occurs

if __name__ == "__main__":
    lock = multiprocessing.Lock()  # Create a Lock
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]

    # Create two processes that share the lock
    p1 = multiprocessing.Process(target=print_numbers, args=(numbers1, lock))
    p2 = multiprocessing.Process(target=print_numbers, args=(numbers2, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Both processes are done.")


# Lock Creation:
#
# A Lock object is created using multiprocessing.Lock().
# This lock is shared between both processes.
# Acquire and Release:
#
# Before printing numbers, the process acquires the lock using lock.acquire().
# After printing, the lock is released using lock.release().
# Process Synchronization:
#
# The lock ensures that only one process can print numbers at a time, preventing overlapping outputs.
# When to Use:
# Use multiprocessing.Lock whenever multiple processes need controlled access to shared resources (e.g.,
# files, variables, or other critical sections).