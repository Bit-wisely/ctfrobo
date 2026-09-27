# Arithmetic puzzle demonstrating integer division truncation vs float precision

a = 10
b = 3

# In integer division (// in python or int division in C):
int_result = (a // b) * b # (10 // 3) * 3 = 3 * 3 = 9 != 10

# Float representation quirk:
f_result = 0.1 + 0.2 # 0.30000000000000004 != 0.3

print(f"Calculated integer math: {int_result}")
print(f"Calculated float math: {f_result}")

if int_result != 10:
    print("Notice how integer division truncates the fractional part!")
    print("The flag key concept is: integer_division_precision")
    print("Flag: flag{integer_division_precision}")
