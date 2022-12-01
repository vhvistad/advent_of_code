dictionary = {}
shona_words = []
with open('knowit/2022/1/dictionary.txt') as f:
    for line in f:
        shona, english = line.split(',')
        dictionary[shona] = english.strip()
        shona_words.append(shona)

shona_words.sort(key=len, reverse=True)

with open('knowit/2022/1/letter.txt') as f:
    letter = f.read()

result = ''
while len(letter) > 0:
    for word in shona_words:
        if letter[0:len(word)] == word:
            result += dictionary[word] + ' '
            letter = letter[len(word):]
            break

print(f'Translated: {result}\nLength: {len(result.strip())}')