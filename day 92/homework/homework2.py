def count_vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

def sort_by_vowel_count(lst):
    return sorted(lst, key=count_vowels, reverse=True)

print(sort_by_vowel_count(["apple", "banana", "grape", "orange"]))
