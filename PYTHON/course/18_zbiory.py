
d = {'fname': 'Test', 'lname': 'test'}

print(d['lname'])

d['email'] = 'mm@bb.pl'

print(d)

del d['lname']


print(d)

for e in d.values():
    print(e)

for e in d.keys():
    print(e)

for k, e in d.items():
    print(f'{k}:{e}')

ld = []
ld += dict(fn='Krzysiek', ln='d')
ld += dict(fn='sss', ln='ddd')

print(ld)

ld = [
    {'fn': 'krzysiek', 'ln': 'malinowski', 'email':
        (
            'asd@wp.pl',
            'qwe@wp.pl'
        )
     },
    {'fn': 'ddd', 'ln': 'ddd'}
]

print(ld)

print(ld[0]['email'][1])

