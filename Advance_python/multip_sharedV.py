# import time
# import multiprocessing
#
# def cal_sqr(numbers,result,v):
#     v.value=5.67
#     for idx, n in enumerate(numbers):
#         result[idx]=n*n
#
#
#
# if __name__=="__main__":
#     numbers=[2,3,4]
#     result=multiprocessing.Array("i",3)
#     v=multiprocessing.Value("d",0.0)
#     p1=multiprocessing.Process(target=cal_sqr, args=(numbers,result,v))
#
#     p1.start()
#
#     p1.join()
#
#     print(v.value)



import multiprocessing

def increment(shared_value):
    shared_value.value += 1

if __name__ == "__main__":
    value = multiprocessing.Value('i', 0)  # 'i' stands for integer
    processes = [multiprocessing.Process(target=increment, args=(value,)) for _ in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("Final value:", value.value)
