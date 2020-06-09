#Program to swap two variable without using 3rd variable....
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
print("Before swaping")
print("num1 = ",num1)
print("num2 = ",num2)
print("After swapping")
#LOGIC 1:- of swapping
# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2
#LOGIC 2:- of swapping
num1,num2 = num2,num1
print("num1 = ",num1)
print("num2 = ",num2)