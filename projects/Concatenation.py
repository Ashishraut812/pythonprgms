# Input: a string of comma separated numbers. the numbers 5 and 8 are present in the list Assume that 8 always comes after 5.

#  Case 1: num1 = add all the numbers which do not lie between 5 and 8 in the input.
#  Case 2: num2 = numbers formed by concatenating all numbers from 5 to 8.
#  Output: sum of num1 and num2.

'''
Example: 1) 3,2,6,5,1,4,8,9
Num1: 3+2+6+9=20
Num2: 5148
Output: 5248+20=5168 
'''


# input the array
array = list(map(int,input().split(",")))


# add all numbers which do not lie between 5 and 8
number1 = sum(array[:array.index(5)])+sum(array[array.index(8)+1:])

print(number1)
# numbers lie between 5 and 8
l = array[array.index(5):array.index(8)+1]

# initialization the number2
number2 = ""

# concatenation all number present in array 1
for i in l:
    number2 += str(i)

# output: number1 + number2
print(int(number2)+number1)