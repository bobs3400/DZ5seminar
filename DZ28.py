def sum(a, b):
    result = a
    if b > 0:
        result = sum(a + 1, b - 1)
    return result
print(sum(2, 9))