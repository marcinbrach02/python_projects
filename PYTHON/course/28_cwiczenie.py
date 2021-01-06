import json

plik = open('dane.csv', encoding='utf-8')


def get_value(value):
    value = value.strip().replace('zł', ' ').replace(',', '.')
    try:
        return float(value)
    except ValueError:
        return value

def get_line_values(line):
    return [get_value(value) for value in line.split(';')]


records = [
    get_line_values(line) for line in plik
]


print(json.dumps(records, indent=4, ensure_ascii=False))
print(json.dump(records, open('wynik.json', 'x', encoding='utf-8'), indent=4, ensure_ascii=False))









