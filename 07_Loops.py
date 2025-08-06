# 1. Find the factorial of a number without using recursion.
print("\n")
i = 1
num_factorial = int(input("Enter the number whose factorial you want : "))
storage_factorial = num_factorial

# Multiply i with each number from num_factorial down to 1
while num_factorial > 0:
    i = num_factorial * i
    num_factorial -= 1

print(f"Factorial of {storage_factorial} is : {i}")

# 2. Print the Fibonacci series up to the Nth term
print("\n")
num_fibonacci = int(input("Enter the number of terms for the Fibonacci series:  "))
n = 0
a = 1
n_1 = 0

# Print Fibonacci series using loop
while n_1 < num_fibonacci:
    if n_1 == 0:
        print(n)
        n_1 += 1
    if n_1 == 1:
        print(a)
        n_1 += 1
    else:
        z = n + a
        n = a
        a = z
        print(z)
        n_1 += 1

# 3. Print only the prime numbers from a given list
print("\n")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 24, 53]
print(f"List of numbers : {my_list}")

for elements in my_list:
    count = 0
    for x in range(2, elements - 1):
        if elements % x == 0:
            count += 1
    if count == 0 and elements > 1:
        print(elements)

# 4. Reverse a number using a while loop
print("\n")
number_reverse = int(input("Enter a number to reverse : "))
rever = 0

# Extract digits one by one from the end and build reversed number
while number_reverse > 0:
    digit = number_reverse % 10
    rever = rever * 10 + digit
    number_reverse = number_reverse // 10
else:
    print(f"The reversed number is : {rever} ")

# 5. Check whether a number is a palindrome
print("\n")
number_palindrome = int(input("Enter a number to check if it's palindrome or not : "))
number_palindrome_1 = number_palindrome
rever_p = 0

# Reverse the number
while number_palindrome > 0:
    digit = number_palindrome % 10
    rever_p = rever_p * 10 + digit
    number_palindrome = number_palindrome // 10
else:
    # Check if original number and reversed number are same
    print(f"{number_palindrome_1} is a palindrome number") if number_palindrome_1 == rever_p else print(f"{number_palindrome_1} is not a palindrome number")

# 6. Print a pyramid pattern using nested loops
print("\n")
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")  # Print leading spaces
    for j in range(1, i + 1):     # Print left side numbers
        print(j, end="")
    for j in range(i - 1, 0, -1): # Print right side numbers
        print(j, end="")
    print()  # Move to next line

# 7. Find the first number between 100 and 200 divisible by 7 and contains '7'
print("\n")
random_number = 0

for i in range(100, 200):
    if i % 7 == 0 and "7" in list(str(i)):
        random_number += 1
        print(f"The first number between 100 and 200 that is divisible by 7 and also contains the digit '7' is {i}")
        break  # Stop after first match

# 8. Keep accepting numbers and print their sum and average
print("\n")
sum_z = 0
times = 0

# Run until user types 'stop'
while True:
    number_z = input("Enter a number of your choice (or type 'stop' to end): ")
    if number_z.lower() == "stop":
        break
    else:
        sum_z += int(number_z)
        times += 1

# Print result
if times > 0:
    print(f"Sum of numbers entered is {sum_z}")
    print(f"Average of numbers entered is {sum_z / times}")
else:
    print("No numbers were entered.")

# 9. Multiplication tables from 1 to 10
print("\n")
for k in range(1, 11):
    for l in range(1, 11):
        print(f"{k} x {l} = {k * l}")
    print("\n")  # Blank line after each table

# 10. Count frequency of each character without collections
print("\n")
character = input("Enter the string of your choice : ")

for words in character:
    count_times = 0
    for counting in character:
        if words == counting:
            count_times += 1
    # Avoid duplicate print for same character
    if character.index(words) == character.find(words):
        print(f"Number of times the character '{words}' occurred: {count_times}")

# 11. Flatten a nested list using loops
print("\n")
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []

# Loop through each sublist and append elements to flat_list
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print(f"Flattened list: {flat_list}")

# 12. Triangle pattern of asterisks (user-defined lines)
print("\n")
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)

# 13. Number guessing game with limited chances and hints
print("\n")
import random
secret = random.randint(1, 50)
attempts = 5

while attempts > 0:
    guess = int(input("Guess the number (1–50): "))
    if guess == secret:
        print("Correct! You win!")
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")
    attempts -= 1

if attempts == 0:
    print(f"You lost. The number was {secret}.")

# 14. Print all Armstrong numbers between 100 and 999
print("\n")
print("Armstrong numbers between 100 and 999:")

for num_y in range(100, 1000):
    f = num_y // 100
    g = (num_y // 10) % 10
    h = num_y % 10

    # Check Armstrong condition: a^3 + b^3 + c^3 == abc
    if num_y == f**3 + g**3 + h**3:
        print(num_y)

# 15. Print the longest word from a given string using only loops and string ops
print("\n")
user_input_sentence = input("Enter a sentence: ")
word_list_split = user_input_sentence.split()
longest_found_word = ""

# Loop through each word and find the longest
for single_word in word_list_split:
    if len(single_word) > len(longest_found_word):
        longest_found_word = single_word

print(f"The longest word is: {longest_found_word}")
