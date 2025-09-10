# PRACTICE SET: FUNCTIONS & RECURSION

# 1. Write a function that takes two numbers and returns both their sum and product.

print("\n ankit")

def sumpro(a, b):
    return a + b, a * b

a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))
s, p = sumpro(a, b) 
print(f"Sum of {a} and {b} is {s}")
print(f"Product of {a} and {b} is {p}")

# 2. Create a function that accepts a list of numbers and returns a new list with only even numbers.

print("\n")

def evenlist(nums):
    return [num for num in nums if num % 2 == 0]

nums = [3, 4, 5, 6, 2, 7, 9, 8]
new_list = evenlist(nums)

print(f"The new list containing just the even numbers is: {new_list}")


# 3. Write a function that checks if a string is a palindrome (using slicing, no loops).

print("\n")

def palindrome_check(palin_check):
    palin_check = str(palin_check)
    return palin_check == palin_check[::-1]

list_to_check = [123, 234, 456, 234, 123]
print(f"The given list is a palindrome list : {palindrome_check(list_to_check)}")


# 4. Implement a recursive function to calculate factorial of a number.

print("\n")
def factorial(digit):
    if digit==1 or digit==0 :
        return 1
    else:
        return digit * factorial(digit-1)

digit=int(input("Emter the digit for factorial : "))
print(f"factorial of {digit} is {factorial(digit)}")

# 5. Write a recursive function to generate Fibonacci series up to n terms.

print("\n")

def fibonacci_series(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci_series(n-1)
        series.append(series[-1] + series[-2])
        return series

print(f"Fibonacci series up to  terms is: {fibonacci_series(11)}")


# 6. Create a function that accepts any number of positional arguments (*args) and returns their average.

print("\n")
def argssum(*args):
    if len(args)==0:
        return 0
    return sum(args) / len(args)
print(argssum(10,34,56,86))


# 7. Create a function that accepts keyword arguments (**kwargs) and prints them in "key = value" format.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(name="Ankit", age=21, course="AIML")

print("\n")


# 8. Write a function that uses default arguments to calculate power: power(base, exp=2).

def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(2, 3))

print("\n")


# 9. Write a recursive function that finds the sum of digits of a number.

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))

print("\n")


# 10. Implement a lambda function to sort a list of tuples based on the second element.

tuples = [(1, 4), (3, 1), (2, 5), (7, 2)]
sorted_list = sorted(tuples, key=lambda x: x[1])
print(sorted_list)

print("\n")


# 11. Write a higher-order function that takes another function as input and applies it to a given list.

def apply_function(lst, func):
    return [func(x) for x in lst]

def square(x):
    return x * x

print(apply_function([1, 2, 3], square))

print("\n")


# 12. Demonstrate local, global, and nonlocal variables inside a nested function.

x = "global variable"

def outer():
    x = "outer variable"
    def inner():
        nonlocal x
        x = "modified by inner"
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("Global:", x)

print("\n")


# 13. Write a recursive function to flatten a nested list.

def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

print(flatten_list([1, [2, [3, 4], 5]]))

print("\n")


# 14. Write a decorator that logs the execution time of any function.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def example_function():
    time.sleep(1)
    return "Done!"

print(example_function())

print("\n")


# 15. Implement a recursive solution to the "Tower of Hanoi" problem for n disks.

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

tower_of_hanoi(3, "A", "C", "B")

print("\n")
