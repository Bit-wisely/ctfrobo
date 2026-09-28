a = 10
b = 3

int_result = (a // b) * b

f_result = 0.1 + 0.2

print(f"Calculated integer math: {int_result}")
print(f"Calculated float math: {f_result}")

if int_result != 10:
    print("Notice how integer division truncates the fractional part!")
    print("The flag key concept is: integer division precision")
    print("Flag: flag{integer division precision}")
