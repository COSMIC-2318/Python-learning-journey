# 1. Take user's name as input and print a greeting message like:
#    "Good Afternoon, <name>!"
name=input("Enter Your name : ")
print(f"Good Afternoon {name}")
print("\n")
# 2. Take name and date as input and fill the following letter template using string formatting:
# '''Dear <|Name|>,
#       You are selected!
# <|Date|>'''

message= '''Dear <|Name|>,
     You are selected!
<|Date|>'''
print(message.replace("<|Name|>",name).replace("<|Date|>","02\\08\\2025"))
print("\n")

# 3. Write a program to detect and replace all double spaces in a given string with single spaces.
str_1="Hey  I am learning  Python "
print(str_1.replace("  "," "))
print("\n")

# 4. Format the following string using escape sequences to make it more readable:
#    "Dear Ankit, this python course is nice. Thanks!"
str_2="Dear Ankit, \n\tThis python course is nice. \nThanks!"
print(str_2)
print("\n")

# 5.  Given a string s = "PythonForBeginners", perform the following using slicing:
# a) Extract "Python"
# b) Extract "Beginners"
# c) Extract every second character from the entire string
# d) Reverse the entire string
# e) Extract "For" using negative indexing
s="PythonForBeginners"
print(len(s))
print(s[:6])
print(s[9:])
print(s[::2])
print("REversed : ",s[::-1])
print(s[-12:-9])