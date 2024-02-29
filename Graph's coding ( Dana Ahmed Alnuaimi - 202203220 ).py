# Graphs coding:
# Task 1 graph:
import random
import time
import matplotlib.pyplot as plt

class Chocolate:
    def __init__(self, id, weight, price, type):
        self.id = id
        self.weight = weight
        self.price = price
        self.type = type

def dIterative(chocolates, students):
    distributed_chocolates = {}
    student_index = 0
    for chocolate in chocolates:
        if student_index >= len(students):
            student_index = 0
        student = students[student_index]
        if student not in distributed_chocolates:
            distributed_chocolates[student] = []
        distributed_chocolates[student].append(chocolate)
        student_index += 1
    return distributed_chocolates

def dRecursive(chocolates, students, distributed_chocolates=None, student_index=0):
    if distributed_chocolates is None:
        distributed_chocolates = {}
    if student_index >= len(students):
        return distributed_chocolates
    student = students[student_index]
    if student not in distributed_chocolates:
        distributed_chocolates[student] = []
    if chocolates:
        distributed_chocolates[student].append(chocolates[student_index % len(chocolates)])
    return dRecursive(chocolates, students, distributed_chocolates, student_index + 1)


if __name__ == "__main__":
    MAX_LEN = 200
    chocolates = [Chocolate("002", 5, 2, "Almond chocolate"), Chocolate("005", 7, 4, "Peanut butter chocolate"),
                  Chocolate("007", 6, 3, "Hazelnut chocolate"), Chocolate("010", 8, 5, "Mint chocolate"),
                  Chocolate("013", 4, 3, "Spicy chocolate"), Chocolate("016", 6, 4, "Orange chocolate")]
    students = ["Dana", "Jamila", "Shamma", "Shaikah", "Salama", "Asma"]

    lengths_iterative = []
    times_iterative = []
    lengths_recursive = []
    times_recursive = []

    for length in range(0, MAX_LEN, 10):
        random_chocolates = [random.choice(chocolates) for _ in range(length)]
        start = time.perf_counter()
        dIterative(random_chocolates, students)
        end = time.perf_counter()
        lengths_iterative.append(length)
        times_iterative.append(end - start)
        start = time.perf_counter()
        dRecursive(random_chocolates, students)
        end = time.perf_counter()

        lengths_recursive.append(length)
        times_recursive.append(end - start)

    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Chocolate Distribution Time Complexity")
    plt.xlabel("Number of Chocolates")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_iterative, times_iterative, label="Iterative Distribution")
    plt.plot(lengths_recursive, times_recursive, label="Recursive Distribution")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Task 2 graph:
import random
import time
import matplotlib.pyplot as plt

class Chocolate:
    def __init__(self, id, weight, price, type):
        self.id = id
        self.weight = weight
        self.price = price
        self.type = type

def sCWeight(chocolates):
    return sorted(chocolates, key=lambda x: x.weight)

def sCPrice(chocolates):
    return sorted(chocolates, key=lambda x: x.price)


chocolates = [ Chocolate("002", 5, 2, "Almond chocolate"), Chocolate("005", 7, 4, "Peanut butter chocolate"),
    Chocolate("007", 6, 3, "Hazelnut chocolate"), Chocolate("010", 8, 5, "Mint chocolate"),
    Chocolate("013", 4, 3, "Spicy chocolate"), Chocolate("016", 6, 4, "Orange chocolate")]

# Sort chocolates by weight
sorted_by_weight = sCWeight(chocolates)
print("Chocolates sorted by weight:")
for chocolate in sorted_by_weight:
    print(f"ID: {chocolate.id}, Weight: {chocolate.weight}, Price: {chocolate.price}, Type: {chocolate.type}")

# Sort chocolates by price
sPrice = sCPrice(chocolates)
print("\nChocolates sorted by price:")
for chocolate in sPrice:
    print(f"ID: {chocolate.id}, Weight: {chocolate.weight}, Price: {chocolate.price}, Type: {chocolate.type}")



if __name__ == "__main__":
    MAX_LEN = 200
    chocolates = [Chocolate("002", 5, 2, "Almond chocolate"), Chocolate("005", 7, 4, "Peanut butter chocolate"),
                  Chocolate("007", 6, 3, "Hazelnut chocolate"), Chocolate("010", 8, 5, "Mint chocolate"),
                  Chocolate("013", 4, 3, "Spicy chocolate"), Chocolate("016", 6, 4, "Orange chocolate")]

    lengths_weight = []
    times_weight = []
    lengths_price = []
    times_price = []

    for length in range(0, MAX_LEN, 10):
        random_chocolates = [random.choice(chocolates) for _ in range(length)]

        start = time.perf_counter()
        sCWeight(random_chocolates)
        end = time.perf_counter()

        lengths_weight.append(length)
        times_weight.append(end - start)

        start = time.perf_counter()
        sCPrice(random_chocolates)
        end = time.perf_counter()

        lengths_price.append(length)
        times_price.append(end - start)

    plt.style.use("default")
    plt.figure().canvas.manager.set_window_title("Chocolate Sorting Time Complexity")
    plt.xlabel("Number of Chocolates")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_weight, times_weight, label="Sort by Weight", color="blue")
    plt.plot(lengths_price, times_price, label="Sort by Price", color="red")
    plt.legend()
    plt.tight_layout()
    plt.show()

#Task 3 graph:
import random
import time
import matplotlib.pyplot as plt

class Chocolate:
    def __init__(self, id, weight, price, type):
        self.id = id
        self.weight = weight
        self.price = price
        self.type = type

def findSCprice(chocolates, price):
    for chocolate in chocolates:
        if chocolate.price == price:
            return chocolate
    return None

def findSCweight(chocolates, weight):
    for chocolate in chocolates:
        if chocolate.weight == weight:
            return chocolate
    return None

if __name__ == "__main__":
    MAX_LEN = 200
    lengths_price = []
    times_price = []
    lengths_weight = []
    times_weight = []

    for length in range(0, MAX_LEN, 10):
        chocolates = [Chocolate(id=i, weight=random.uniform(50, 200), price=random.uniform(1, 10), type='Dark') for i in range(length)]

        start = time.perf_counter()
        findSCprice(chocolates, random.uniform(1, 10))
        end = time.perf_counter()

        lengths_price.append(length)
        times_price.append(end - start)

        start = time.perf_counter()
        findSCweight(chocolates, random.uniform(50, 200))
        end = time.perf_counter()
        lengths_weight.append(length)
        times_weight.append(end - start)

    plt.figure()
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_price, times_price, label="find_student_by_chocolate_price()")
    plt.plot(lengths_weight, times_weight, label="find_student_by_chocolate_weight()")
    plt.legend()
    plt.title("Time Complexity Analysis")
    plt.show()

