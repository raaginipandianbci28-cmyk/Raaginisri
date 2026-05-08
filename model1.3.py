sentence = input("Enter a sentence: ")
words = sentence.split()
if words:
    longest_word = max(words, key=len)
    print(longest_word)

