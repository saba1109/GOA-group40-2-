def count_threes(number):
    return str(number).count('3')

def sort_by_three_count(lst):
    return sorted(lst, key=count_threes, reverse=True)

print(sort_by_three_count([3, 3123, 121423, 301345, 30093]))
