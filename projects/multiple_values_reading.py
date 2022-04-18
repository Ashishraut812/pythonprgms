# How to read multiple values from the keyboard in a single line:


a,b = [int(x) for x in input("Enter 2 numbers: ").split()]
print("Product is : ",a*b)

# Write a program to read 3 float numbers from the keyboard with seperator and print their sum:

a,b,c = [float(x) for x in input("Enter 3 float numbers: ").split()]
print("The sum is : ",int(a+b+c))