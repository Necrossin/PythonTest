from FIFOList import FIFOList
from FIFODeque import FIFODeque

from time import process_time

# FIFO example
def showcase():
    print("\nCreating empty FIFOList and FIFODeque with the max capacity of 10:\n")
    
    fifo_list = FIFOList(10)
    fifo_deque = FIFODeque(10)

    print(fifo_list)
    print(fifo_deque)

    print("\n\nAdding a range of 10 into each:\n")

    for i in range(10):
        fifo_list.push(i)
        fifo_deque.push(i)

    print(fifo_list)
    print(fifo_deque)

    print("\n\nAdding [ 20, 21, 22 ] into each:\n")

    for i in range(20,23):
        fifo_list.push(i)
        fifo_deque.push(i)

    print(fifo_list)
    print(fifo_deque)

    print("\n\nPop 5 values from each:\n")

    for i in range(5):
        fifo_list.pop()
        fifo_deque.pop()

    print(fifo_list)
    print(fifo_deque)

# Speed comparison
def speed_test():
    
    print("Max capacity (10000 and more is recommended):")

    capacity = int(input())
    
    print("Creating FIFOList and FIFODeque with the max capacity of", capacity)
    
    fifo_list = FIFOList(capacity)
    fifo_deque = FIFODeque(capacity)

    # Push speed test
    print("Measuring time that it takes to fully fill each of them:\n")

    t1_start = process_time()

    for i in range(capacity):
        fifo_list.push(i)

    t1_finish = process_time()

    t2_start = process_time()

    for i in range(capacity):
        fifo_deque.push(i)
        
    t2_finish = process_time()

    print("FIFOList (push operations) elapsed time in seconds:", t1_finish-t1_start)
    print("FIFODeque (push operations) elapsed time in seconds:", t2_finish-t2_start)

    # Pop speed test
    print("\nMeasuring time that it takes to fully empty out each of them:\n")

    t1_start = process_time()

    for i in range(capacity):
        fifo_list.pop()

    t1_finish = process_time()

    t2_start = process_time()

    for i in range(capacity):
        fifo_deque.pop()
        
    t2_finish = process_time()

    print("FIFOList (pop operations) elapsed time in seconds:", t1_finish-t1_start) 
    print("FIFODeque (pop operations) elapsed time in seconds:", t2_finish-t2_start) 

# Main
def main():
    print("Press Enter for the FIFO showcase or type 'test' to show speed comparison between FIFOList and FIFODeque:")
    
    match input().replace("'", ""):
        case "test":
            speed_test()
        case _:
            showcase()

if __name__ == "__main__":
    main()
