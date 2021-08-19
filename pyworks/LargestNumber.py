# This program finds the largest one out of provided numbers.

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))

# Logic to find the largest number
if(num1 > num2) and (num1 > num3):
    largest = num1
elif(num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3

print("The largest number between",num1,",",num2,"and",num3, "is",largest)

