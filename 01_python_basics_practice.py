#This program includes the use of Input , Operators , Mapping , Spliting the multi input 
# type() , Typecasting , Operators 
import pandas as pd
Name=input("Enter your name : ")
Age=input("Enter your age : ")
print("Data type of Age before type casting is",type(Age))
A, B = map(float, input("Enter Two numbers and put a Space between them  : ").split())
Age=int(Age)
print("\nData type Of Name is", type(Name), "Data type of Age after type casting is",type(Age), "Data type of Number  is",type(A))
Prog=input("Enter your favorite programming language : ")
C=A+B
print("The Sum Of ",A," and ",B," is ",C )
print("Your Favorite Programing Language is ",Prog)
print("Hello",Name,". You will be ",Age+1,"next year")
#Average of Marks of three Subject
sub1=float(input("Enter the marks of subject 1 :")) 
sub2=float(input("Enter the marks of subject 2 :"))
sub3=float(input("Enter the marks of subject 3 :"))
Average_3= (sub1+sub2+sub3)/3
print("Average Marks of 3 subject is ", Average_3)
num1=23
num2=34
num3="33"
print(num1+num2) # here as the both the numbers are integer , it give there sum 
print(num1+int(num3)) # here num3 is being converted to a integer , so it give there sum 
print(str(num1)+num3) # here num1 is being converted to a string , so it will not give the but will give the concation of both numbers