# import time
# import multiprocessing
#
# def cal_sqr(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print("Square "+str(n*n))
#
# def cal_cube(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print("Cube "+str(n*n*n))
# if __name__=="__main__":
#     arr=[1,2,3,4]
#     p1=multiprocessing.Process(target=cal_sqr, args=(arr,))
#     p2 = multiprocessing.Process(target=cal_cube, args=(arr,))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     print("Done")



# code 2

import multiprocessing

def worker(number):
    print(f"Worker {number} is running")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed")
