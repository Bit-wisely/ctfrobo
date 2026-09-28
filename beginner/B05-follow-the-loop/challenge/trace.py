x = 1337

for step in range(1, 25):
    if step % 3 == 0:
        x = (x + step * 11) ^ 0x5A
    elif step % 2 == 0:
        x = (x * 2 - step) % 10000
    else:
        x = (x + 47) % 10000
