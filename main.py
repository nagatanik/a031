bases = [2, 3, 5]

n = 7

def check_factor(value, bases):
    is_factor = False
    for b in bases:
        if value % b == 0:
            is_factor = True
            break
    return is_factor
            

value = 1
k = 1
while k < n:
    value += 1
    if check_factor(value, bases):
        k += 1

print(value)