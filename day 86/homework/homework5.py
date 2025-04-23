def process_lists(list1, list2):
    even_numbers = []
    for number in list1:
        if number % 2 == 0:
            even_numbers.append(number)

    odd_numbers = []
    for number in list2:
        if number % 2 != 0:
            odd_numbers.append(number)

    merged = even_numbers + odd_numbers

    total = 0
    for i in range(len(merged)):
        if i % 2 != 0:
            total += merged[i]

    return total
