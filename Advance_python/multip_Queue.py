import multiprocessing

def calc_square(numbers, q):
    for n in numbers:
        q.put(n * n)  # Add the square of each number to the queue

if __name__ == "__main__":
    numbers = [2, 3, 4]
    q = multiprocessing.Queue()  # Create a multiprocessing queue
    p = multiprocessing.Process(target=calc_square, args=(numbers, q))  # Create a process
    p.start()  # Start the process
    p.join()  # Wait for the process to finish

    # Retrieve all data from the queue
    while not q.empty():
        print(q.get())
