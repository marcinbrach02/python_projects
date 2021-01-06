
data = [
    ('Krzysiek', 'Malinowski'),
    ('Alina', 'Moroz')
]

file = open('dane.dat', 'x', encoding='utf-8')

data_str = []

for row in data:
    data_str.append(''.join(row))

file.write('\r\n' .join(data_str))

# 'a b' .split(' ')


