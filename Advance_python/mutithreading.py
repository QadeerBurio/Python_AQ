# 1st COde
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

# code 2
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


# code 3
