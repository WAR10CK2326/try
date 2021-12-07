num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))
num3 = int(input("Enter 3rd integer: "))
num4 = int(input("Enter 4th integer: "))
num5 = int(input("Enter 5th integer: "))
total = num1 + num2 + num3 + num4 + num5

if num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5:
print("Least is ", num1)
elif num2 <= num1 and num2 <= num3 and num2 <= num4 and num2 <= num5:
print("Least is ", num2)
elif num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5:
print("Least is ", num3)
elif num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5:
print("Least is ", num4)
elif num5 <= num1 and num5 <= num2 and num5 <= num3 and num5 <= num4:
print("Least is ", num5)

if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
print("Least is ", num1)
elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
print("Least is ", num2)
elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
print("Least is ", num3)
elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
print("Least is ", num4)
elif num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4:
print("Least is ", num5)
average = total / 5
print("Average is ", average)
