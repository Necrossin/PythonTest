from time import process_time

# Default example
def isEven(value):
    return value % 2 == 0

# Alternative #1
even_numbers = {repr(i):True for i in range(0,9,2)}
def isEvenDict(value):
    last_num = repr(value)[-1]

    try:
        return even_numbers[last_num]
    except:
        return False
    
# Alternative #2
def isEvenSet(value):
    last_num = repr(value)[-1]
    
    return last_num in {repr(i) for i in range(0,9,2)}

# Examples
def showcase():
    print("Input any integer:")
    
    try:
        val = int(input())
    
        print("isEven result:",isEven(val))
        print("isEvenDict result:",isEvenDict(val))
        print("isEvenSet result:",isEvenSet(val))
    except:
        print("Input must be an integer!")

# Speed comparison
def speed_test():
    print("Executing isEven, isEvenDict and isEvenSet 1000000 times for speed comparison:\n")

    # isEven
    t_start = process_time()

    for i in range(1000000):
        isEven(i)
    
    t_finish = process_time()

    print("isEven (1000000 calls) elapsed time in seconds:", t_finish-t_start)

    # isEvenDict
    t_start = process_time()

    for i in range(1000000):
        isEvenDict(i)
    
    t_finish = process_time()

    print("isEvenDict (1000000 calls) elapsed time in seconds:", t_finish-t_start)

    # isEvenSet
    t_start = process_time()

    for i in range(1000000):
        isEvenSet(i)
    
    t_finish = process_time()

    print("isEvenSet (1000000 calls) elapsed time in seconds:", t_finish-t_start)

# Main
def main():
    print("Press Enter for the showcase or type 'test' to show speed comparison between isEven and it's variants:")

    match input().replace("'", ""):
        case "test":
            speed_test()
        case _:
            showcase()

if __name__ == "__main__":
    main()