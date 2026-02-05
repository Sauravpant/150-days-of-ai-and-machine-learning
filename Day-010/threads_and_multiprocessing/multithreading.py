import threading
import time


# Without multithreading
def print_numbers():
    for i in range(6):
        time.sleep(1)
        print(f"Number: {i}")


word = "abcde"


def print_letters():
    for letter in word:
        time.sleep(1)
        print(f"Letter: {letter} \n")


t = time.time()
print_numbers()
print_letters()
print("Time taken without threading:", time.time() - t)


# With multithreading
def print_numbers():
    for i in range(6):
        time.sleep(1)
        print(f"Number: {i}")


word = "abcde"


def print_letters():
    for letter in word:
        time.sleep(1)
        print(f"Letter: {letter}")


t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
print("Time taken with threading:", time.time() - t)


#Output:
# Number: 0
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5
# Letter: a 
# Letter: b 
# Letter: c 
# Letter: d 
# Letter: e 

# Time taken without threading: 11.012967348098755

# Number: 0
# Letter: a
# Number: 1
# Letter: b
# Number: 2
# Letter: c
# Number: 3
# Letter: d
# Number: 4
# Letter: e
# Number: 5

# Time taken with threading: 6.010240077972412