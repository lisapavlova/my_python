def histogram(s):
    word_count = {}
    for word in s:
        word_count.setdefault(word, 0)
        word_count[word] += 1     
    return word_count
with open('moby_clean.txt', 'r') as input_file:
    freq = histogram(input_file)
sorted_freq = sorted(freq, key=freq.get, reverse=True)
print('5 самых часто встречающихся слов:')
for i in range(0, 5):
    print(sorted_freq[i])
sorted_freq = sorted(freq, key=freq.get, reverse=False)
print('5 самых редко встречающихся слов:')
for i in range(0, 5):
    print(sorted_freq[i])
