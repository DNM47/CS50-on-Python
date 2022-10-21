from string import punctuation

text = input('Text: ')

letter_count = 0
word_count = 0
sentence_count = 0

n_t = text.split()

for w in n_t:
    word_count += 1
    w.split()
    for l in w:
        if l not in punctuation:
            letter_count += 1
        elif l == '?' or l == '.' or l =='!':
            sentence_count += 1


L = int(letter_count) / int(word_count) * 100
S = int(sentence_count) / int(word_count) * 100

index = 0.0588 * L - 0.296 * S - 15.8
n_index = round(index)

if n_index < 1:
    print("Before Grade 1")
elif n_index >= 16:
    print("Grade 16+")
else: print(f"Grade {n_index}")

# print(sentence_count)
# print(letter_count)
# print(word_count)
# print(L)
# print(S)
# print(n_index)