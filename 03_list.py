# 🔹 LIST PRACTICE QUESTIONS

# 1. Create a list of your 6 favorite fruits and print the second and fourth item.
print("\n")
fruits = ["mango", "apple", "pineapple", "dragonfruit", "banana", "lime"]
print(fruits)  # print the original list of fruits
print("\n")

# 2. Add a new fruit to the end of the list using append() and another at the second position using insert().
fruits.append("Cherry")       # add Cherry at the end
print(fruits)
fruits.insert(1, "orange")    # insert orange at index 1 (second position)
print(fruits)
print("\n")

# 3. Remove the last fruit using pop() and remove the second fruit by value using pop(index).
fruits.pop()      # remove last item
print(fruits)
fruits.pop(2)     # remove the third item (index 2)
print(fruits)
print("\n")

# 4. Sort the list in alphabetical order and then reverse it.
order = "ankitbajpeyee"
print(order)
order_list = list(order)   # convert string to list of characters
print(order_list)
order_list.sort()          # sort the list alphabetically
print(order_list)
print("\n")

# 5. Write a program to take 5 numbers as input from the user and store them in a list.
num_list = []
z = 1
while True:
    item = int(input("Enter an item to add to the list: "))  # take input and convert to int
    num_list.append(item)  # add to list
    if z == 5:              # stop after 5 inputs
        break
    z = z + 1

print("num_list:", num_list)
print("\n")

# 6. From the above list, print the maximum, minimum, and average value.
print(f"Maximum value in the list is {max(num_list)}")
print(f"Minimum value in the list is {min(num_list)}")
print(f"Average value of the list is {sum(num_list)/5}")
print("\n")

# 7. Replace the third element in your list of numbers with 100.
print(num_list)
num_list[2] = 100  # index 2 = third element
print(num_list)
print("\n")

# 8. Write a program to create a list of squares of numbers from 1 to 10 using list comprehension.
squares = [x**2 for x in range(1, 11)]
print("Squares of numbers from 1 to 10:", squares)
print("\n")

# 9. Combine two lists: one with names and one with roll numbers using zip() and print them as pairs.
names = ['Ankit', 'Aditya', 'Ashis', 'Rohan', 'Ram', 'Mohan', 'Abhi', 'Vick', 'Ron', 'Ria']
num_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = zip(names, num_3)      # To zip names and numbers together
data_l = list(data)           # To convert zip object to list of tuples
print(data_l)
print("\n")

# 10. Create a nested list (2D list) representing a 3x3 matrix and print the second row and second column.
matrix = [
    [5, 2, 3],
    [4, 9, 6],
    [7, 8, 993]
]
print(matrix)
print(f"Second Row {matrix[1]}")  # second row (index 1)

print(f"Second Column {[row[1] for row in matrix]}")  # elements at column index 1 , just the coulumn 
