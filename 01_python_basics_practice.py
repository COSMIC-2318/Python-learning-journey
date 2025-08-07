# This program demonstrates: input handling, typecasting, operators, and basic calculations

import pandas as pd  # Imported for potential data handling (not used in this code but okay to keep)

# Taking basic user input
Name = input("Enter your name : ")
Age = input("Enter your age : ")

# Displaying data type of Age before conversion
print("Data type of Age before type casting is", type(Age))

# Taking two float numbers in a single line using map and split
A, B = map(float, input("Enter Two numbers and put a Space between them  : ").split())

# Typecasting age to integer
Age = int(Age)

# Showing data types after typecasting
print("\nData type Of Name is", type(Name), 
      "Data type of Age after type casting is", type(Age), 
      "Data type of Number is", type(A))

# Taking user's favorite programming language
Prog = input("Enter your favorite programming language : ")

# Performing addition of A and B
C = A + B
print("The Sum Of ", A, " and ", B, " is ", C)

# Printing greeting and age for next year
print("Your Favorite Programing Language is ", Prog)
print("Hello", Name, ". You will be ", Age + 1, "next year")

# Taking marks of 3 subjects and calculating average
sub1 = float(input("Enter the marks of subject 1 :")) 
sub2 = float(input("Enter the marks of subject 2 :"))
sub3 = float(input("Enter the marks of subject 3 :"))

# Calculating average
Average_3 = (sub1 + sub2 + sub3) / 3
print("Average Marks of 3 subjects is ", Average_3)

# Demonstrating typecasting and operator behavior
num1 = 23
num2 = 34
num3 = "33"

# Addition of two integers
print(num1 + num2)  # 23 + 34 = 57

# num3 is a string, converting it to int for addition
print(num1 + int(num3))  # 23 + 33 = 56

# Converting num1 to string and concatenating with num3
print(str(num1) + num3)  # "23" + "33" = "2333"
