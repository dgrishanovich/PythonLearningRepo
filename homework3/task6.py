def int_func(little_word):
    return little_word.capitalize()


capitalized_words = [int_func(word) for word in input('Input some little words: ').split()]
print(" ".join(capitalized_words))
