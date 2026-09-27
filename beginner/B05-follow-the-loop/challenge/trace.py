# Trace the loop to determine the final value of x

x = 1337

for step in range(1, 25):
    if step % 3 == 0:
        x = (x + step * 11) ^ 0x5A
    elif step % 2 == 0:
        x = (x * 2 - step) % 10000
    else:
        x = (x + 47) % 10000

# When you find the final value of x, the flag is:
# flag{loop_trace_<value>}
# Example: if x is 1234, the flag is flag{loop_trace_1234}
