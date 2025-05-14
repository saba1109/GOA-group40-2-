def sort_sentence_by_length(sentence):
    words = sentence.split()
    return sorted(words, key=len, reverse=True)

print(sort_sentence_by_length("long sentence"))
