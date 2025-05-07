words = []
word = ""

while word != "enough":
    word = input("Type a word (or 'enough' to stop): ")
    if word != "enough":
        words.append(word)

def get_length(w):
    return len(w)

words.sort(key=get_length)

print(words)
