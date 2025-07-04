# # 1st COde
#
# import threading
#
# def print_numbers():
#     for i in range(5):
#         print(f"Thread: {i}")
#
# # Create thread
# t1 = threading.Thread(target=print_numbers)
#
# # Start thread
# t1.start()
#
# # Wait for the thread to finish
# t1.join()
#
# print("Main thread finished")
#
# # code 2
# import threading
# import time
#
# def task(name):
#     for i in range(3):
#         print(f"{name} is running {i}")
#         time.sleep(1)
#
# # Creating multiple threads
# t1 = threading.Thread(target=task, args=("Thread-1",))
# t2 = threading.Thread(target=task, args=("Thread-2",))
#
# # Starting threads
# t1.start()
# t2.start()
#
# # Wait for both threads to finish
# t1.join()
# t2.join()
#
# print("All threads completed")


import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(1)

# ✅ Start timer here
start_time = time.time()

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

# ✅ Calculate total time
print("Time taken:", round(time.time() - start_time, 2), "seconds")
print("Both threads completed.")

