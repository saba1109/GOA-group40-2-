names = ["Nino", "Giorgi", "Ana", "Alexandre", "Saba"]

def name_length(name):
    return len(name)

names.sort(key=name_length, reverse=True)

print(names)
