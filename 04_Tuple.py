# 🔸 TUPLE PRACTICE QUESTIONS

# 1. Create a tuple containing your name, age, and city. Print each element separately using indexing.
data = ("Ankit", 21, "Hazaribagh")
print(data[0])  # name
print(data[1])  # age
print(data[2])  # city
print("\n")

# 2. Try changing the age value in the tuple and observe what error you get. (Comment your observation)
# data[0] = "Bajpeyee"
#  Tuples are immutable, so this gives:
# TypeError: 'tuple' object does not support item assignment

# 3. Write a program to count the number of times a particular value appears in a tuple.
a = (1, 2, 3, 4, 5, 4, 2, 2, 1, 5, 6, 8)
print(a)
print(f"2 has appeared {a.count(2)} times.")  # count how many times 2 appears
print("\n")

# 4. Create a tuple of 5 numbers and find the index of a specific number.
num = (2, 3, 4, 5, 2)
print(num.index(3))  # index of number 3
print("\n")

# 5. Take user input of 3 values and store them in a tuple using tuple() function.
value = []
input_1 = input("Enter a value: ")
value.append(input_1)
input_2 = input("Enter a value: ")
value.append(input_2)
input_3 = input("Enter a value: ")
value.append(input_3)

print(value)  # list before converting
value_t = tuple(value)  # converting list to tuple
print(value_t) # list after converting to tuple
print("\n")

# 6. Unpack a tuple with values ('Ankit', 21, 'Python') into three variables and print them.
a, b, c = ("Ankit", 21, "Python") # tuple unpacking
print(a)
print(b)
print(c)
print("\n")

# 7. Create a nested tuple (a tuple containing tuples) and access an inner element.
nested = (1, 4, 23, (2, 3), 45)
print(nested[3])       # prints the inner tuple (2, 3)
print(nested[3][1])    # prints the value 3 inside the nested tuple
print("\n")

# 8. Concatenate two tuples and repeat the result twice.
x = (1, 2)
y = (3, 4)
z = tuple(x + y)  # concatenate
print(x)
print(y)
print(z)       # repeat the result
print(z * 2)       # repeat the result twice
print("\n")

# 9. Create a tuple with mixed data types and check if a specific item exists using `in`.
mida = (1, 34, "ankit", (4, 5, 6), "what")
print("mida = ", mida)
print(f"34 is present in the tuple mida: {34 in mida}")      # check number
print(f"raju is present in the tuple mida: {'raju' in mida}")  # check string
print("\n")
