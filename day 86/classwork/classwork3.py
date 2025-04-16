def remove_digits(text):
    for digit in "0123456789":
        text = text.replace(digit, "")
    return text
print(remove_digits("ale4qs6and3re"))