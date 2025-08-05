# 1. Check if a number is even or odd using a conditional expression.
number = 13
# Your code here
print("The number is Even" if number%2==0 else "The number is odd")

print("\n")


# 2. Assign "Adult" if age >= 18, otherwise "Minor", using a conditional expression.
age = 16
# Your code here
print("Adult" if age >= 18 else "Minor")

print("\n")


# 3. Find the maximum of two numbers using a conditional expression.
a = 45
b = 78
# Your code here
print("a is greater than b" if a>b else "b ia greater than a")
print("\n")


# 4. Print "Positive", "Negative", or "Zero" using nested conditional expressions.
num = 0
# Your code here
if num>0:
    print("num is positive")
elif num<0:
    print("num is negative")
else:
    print("num is zero")
print("\n")


# 5. Assign grade using nested conditional expressions:
# 90+: A, 80+: B, 70+: C, else: F
marks = 72
# Your code here
print(f"Your marks is {marks} so your grade is : ")
print("A" if marks>90 else "B" if marks>80 else "C" if marks>70 else "F")
print("\n")


# 6. Using a conditional expression inside a list comprehension:
# Replace odd numbers with "Odd", even numbers with "Even".
nums = [1, 2, 3, 4, 5, 6]
# Your code here
print("Before :",nums)
nums=["EVEN" if num%2==0 else "Odd" for num in nums ]
print("After :",nums)
print("\n")


# 7. Use conditional expression to return “Pass” if score >= 40 and “Fail” otherwise.
score = 39
# Your code here
print("Score :",score)
print("PASS") if score>=40 else print("FAIL")
print("\n")


# 8. Use a lambda function with conditional expression to check if a number is divisible by 3.
check = lambda x: x%3==0# Your code here
print(check(9))  # Should return "Yes"
print(check(9))
print(check(10)) # Should return "No"
print(check(10))

print("\n")


# 9. Rewrite this logic using a conditional expression:
# if flag is True, set result = "Enabled", else "Disabled"
flag = False
# Your code here
result="Enabled" if flag is True else "Disabled"
print(result)

print("\n")


# 10. Create a one-liner function that takes two numbers and returns their difference if the first is greater, else their sum.
def compute(x, y):
    # Your code here
    if x>y :
        return x-y
    else :
        return x+y

print(compute(5, 2))  # Should return 3
print(compute(2, 5))  # Should return 7

print("\n")
