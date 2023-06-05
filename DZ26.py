def step(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return (a * step(a, b - 1 ))
a = int(input("Введите первое число : "))
b = int(input("Введите второе число : "))
print(step(a, b))