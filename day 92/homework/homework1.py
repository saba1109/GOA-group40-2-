def count_a(word):
    return word.count('a')
def sort_by_a_count(lst):
    return sorted(lst, key=count_a)

print(sort_by_a_count(["apple", "banana", "grape", "avocado"]))