def starts_with_g(word):
    return not word.lower().startswith('g')

def sort_starting_with_g(lst):
    return sorted(lst, key=starts_with_g)

print(sort_starting_with_g(["grape", "apple", "Giraffe", "banana", "goat"]))
