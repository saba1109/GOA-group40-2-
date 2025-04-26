def divide_by_sum():
    n = int(input("type a number: "))
    s = 0
    for d in str(n):
        s += int(d)
    print(n / s)
divide_by_sum()
