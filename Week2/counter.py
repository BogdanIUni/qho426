print("Enter the first whole number")

number1 = int(input())

print("Enter the second whole number")

number2 = int(input())

print("Enter the third whole number")

number3 = int(input())

even_no = 0
odd_no = 0

if number1  % 2 == 0:
    even_no =  even_no + 1
else:
    odd_no = odd_no + 1

if number2  % 2 == 0:
    even_no =  even_no + 1
else:
    odd_no = odd_no + 1

if number3 % 2 == 0:
    even_no = even_no + 1
else:
    odd_no = odd_no + 1

print(f"Total even numbers are {even_no} and odd numbers are {odd_no}")