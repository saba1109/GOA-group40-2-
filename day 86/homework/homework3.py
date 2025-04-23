def sum_of_odd_index_numbers(numbers):
    total = 0
    for i in range(1, len(numbers), 2):
        total += numbers[i]
    return total
