import json

records = [
    {'login': row[0], 'email': row[1]}
    for row in
    [line.strip(' ').split(' ') for line in open('rekordy.dat', encoding='utf-8')]
]


print(json.dumps(records, indent=4))
print(json.dump(records, open('rekordy1.json', 'x', encoding='utf-8'), indent=4))




