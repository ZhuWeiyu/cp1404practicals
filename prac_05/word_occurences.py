"""
CP1404/CP5632 Practical
Word Occurrences

Estimate: 10 minutes
Actual:   8 minutes

"""

word_count = {}
user_input = input("Text: ")

words = user_input.split()

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = list(word_count.keys())
sorted_words.sort()

max_word_length = max([len(word) for word in sorted_words])

for word in sorted_words:
    print(f"{word:{max_word_length}} : {word_count[word]}")
