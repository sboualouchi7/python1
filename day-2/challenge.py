word = input("Enter a word: ")

letter_indexes = {}

for i, l in enumerate(word):
    if l in letter_indexes:
        letter_indexes[l].append(i)
    else:
        letter_indexes[l] = [i]

print(letter_indexes)