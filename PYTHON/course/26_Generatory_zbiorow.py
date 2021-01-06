
multiline_file = open('words.txt', encoding='utf-8')

words = [line.strip() for line in multiline_file if len(line) > 4]
#print(words)

rank = sorted([(words.count(word), word) for word in set(words)], reverse=True)[:10]

print(rank)






