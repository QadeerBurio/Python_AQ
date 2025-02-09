# import multiprocessing
#
# def square(n):
#     return n * n
#
# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5]
#     with multiprocessing.Pool(processes=4) as pool:
#         results = pool.map(square, numbers)
#     print("Squares:", results)

# code2
# import multiprocessing
#
# def cube(n):
#     return n ** 3
#
# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5]
#     with multiprocessing.Pool(processes=4) as pool:
#         for result in pool.imap(cube, numbers):
#             print(result)


# code 3
