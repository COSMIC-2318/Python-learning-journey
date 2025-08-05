# 1. Create a dictionary to store names and their favorite fruits of 4 friends.
fruits = {
    "Ankit": "Mango",
    "Sandeep": "Apple",
    "Ashis": "Orange",
    "Shubham": "Pineapple"
}
print(fruits)
print("\n")

# 2. Add a new friend and their favorite fruit to the dictionary.
fruits.update({"Roshan": "Banana"})
print(fruits)
print("\n")

# 3. Update the favorite fruit of one friend in the dictionary.
fruits.update({"Ankit": "Lime"})
print(fruits)
print("\n")

# 4. Remove one friend from the dictionary using del and another using pop().
del fruits["Roshan"]  # using del to remove Roshan
print(fruits)
fruits.pop("Shubham")  # using pop() to remove Shubham
print(fruits)
print("\n")

# 5. Check whether a friend exists in the dictionary and print an appropriate message.
print(f"Is Ankit Present in the Dictionary Fruits : {'Ankit' in fruits}")
print("\n")

# 6. Loop through the dictionary and print keys and values separately.
for key, value in fruits.items():
    print("Key:", key)        # printing friend name
    print("Value:", value)    # printing their favorite fruit
    print()

print("\n")

# 7. Create a dictionary using two lists: one of keys and one of values.
names = ['Ankit', 'Aditya', 'Ashis', 'Rohan', 'Ram', 'Mohan', 'Abhi', 'Vick', 'Ron', 'Ria']
print(f"List 1 is : {names}")
num_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List 2 is : {num_3}")
detail = dict(zip(names, num_3))  # combining both lists into a dictionary
print(f"Combined dictionary of list 1 and 2 is : {detail}")
print("\n")

# 8. Count the number of times each word appears in a given sentence using a dictionary.
sentence = "ankit loves python and ankit also loves coding in python"
words = sentence.split()  # split sentence into words

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1  # if word exists, increase count
    else:
        word_count[word] = 1   # if word not in dict, add it with count 1

print(word_count)
print("\n")

# 9. Create a set of numbers from 1 to 10. Remove even numbers from the set.
set_1 = {1,2,3,4,5,6,7,8,9,10}
print(set_1)

set_1 = {z for z in set_1 if z % 2 != 0}  # keep only odd numbers
print(set_1)
print("\n")

# 10. Create two sets: one for fruits and one for vegetables. Find their union and intersection.
fruit_set = {"mango", "apple", "pineapple", "dragonfruit", "banana", "lime", "tomato"}
print(fruit_set)
vegi_set = {"tomato ", "beans", "bitterground", "pumpkin", "lime"}
print(vegi_set)

print(fruit_set.union(vegi_set))        # union = all items from both sets
print(fruit_set.intersection(vegi_set)) # intersection = common items
print(vegi_set)
print("\n")

# 11. Find the difference and symmetric difference between two sets of programming languages.
h_1 = {"Python", "Java", "C++", "JavaScript", "C#", "Go", "Ruby", "PHP", "Swift", "Kotlin"}
print(h_1)
l_1 = {"C", "Assembly", "Rust", "VHDL", "Verilog"}
print(l_1)

print(h_1.difference(l_1))              # elements in h_1 but not in l_1
print(h_1.symmetric_difference(l_1))    # elements not common in both sets
print("\n")

# 12. Check if one set is a subset or superset of another set.
print(h_1.issubset(l_1))    # check if h_1 is subset of l_1
print(h_1.issuperset(l_1))  # check if h_1 is superset of l_1
print("\n")

# 13. Create an empty dictionary and an empty set. Use type() to confirm their types.
e_d = {}           # empty dictionary
print(type(e_d))

empty_s = set()    # empty set
print(type(empty_s))
print("\n")

# 14. Write a program that takes marks of students and prints only those who scored more than 75 using a dictionary.
marks = {
    "Ankit": 88,
    "Riya": 72,
    "John": 95,
    "Meena": 67,
    "Aarav": 78
}
print("Students who scored more than 75:")
for name, score in marks.items():
    if score > 75:
        print(name, ":", score)
