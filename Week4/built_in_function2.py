print("Program Started!")
print("Please enter an ASCII code:")
ascii = int(input())

if abs(ascii) in range(32, 126):
    char = chr(ascii)
    print(f"The character represented by ASCII code {ascii} is {char}")
else:
    print("The input is outside the range")

print("Program Ended!")
