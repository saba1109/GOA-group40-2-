def print_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)
    
number = int(input("type a number: "))
print_triangle(number)