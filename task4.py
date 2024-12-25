def word_frequency(sentence):
    
    words = sentence.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = input("Enter a sentence: ")

word_frequency = word_frequency(sentence)

print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")
