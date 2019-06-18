def f(x):
    count = x
    for i in range(1,x+1):
        if i % 15 == 0:
            continue
        elif i % 3 == 0 or i % 5 == 0:
            count -= 1
    return count

print(f(15))
