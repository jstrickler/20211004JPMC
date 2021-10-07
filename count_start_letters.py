letter_counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        letter = word[0]
        if letter not in letter_counts:
            letter_counts[letter] = 0  # initialize element
        letter_counts[letter] += 1  # add 1 to previous value
        # letter_counts[letter] = letter_counts[letter] + 1

print(letter_counts)

