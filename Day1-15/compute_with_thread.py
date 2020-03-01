from time import time
from multiprocessing import Queue, Process
from random import randint


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def add_all(up_limit, with_thread):
    total = 0
    number_list = [i for i in range(1, up_limit + 1)]
    if not with_thread:
        start = time()
        for i in number_list:
            total += i
        end = time()
    else:
        process = []
        result_queue = Queue()
        index = 0
        for _ in range(8):
            p = Process(target=task_handler,
                        args=(number_list[index:index + 12500000],
                              result_queue))
            index += 12500000
            process.append(p)
            p.start()
        start = time()
        for p in process:
            p.join()
        total = 0
        while not result_queue.empty():
            total += result_queue.get()
        end = time()
    return total, end - start


def main():
    upper_number = 100000000
    total1, time1 = add_all(upper_number, with_thread=False)
    total2, time2 = add_all(upper_number, with_thread=True)
    print(f"without multiprocess, it costs {time1}, the sum is {total1}"
          f"\nwith multiprocess, it costs {time2}, the sum is {total2}")


if __name__ == '__main__':
    main()
