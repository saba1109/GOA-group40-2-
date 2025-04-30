def countss(number):
    count = 0
    for num in number:
        if number.count(num) > count:
            count = number.count(num)
        return count
    
save = [1, 23, 5, 67, 89, 55, 55, 2]