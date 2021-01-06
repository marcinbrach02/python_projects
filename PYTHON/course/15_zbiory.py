
l = ['a', 'b', 'c', 'd', 'e', 'a', 'b']

l += 's'
print(l)

for e in l.copy():
    #for e in l[:]:
    if e == 'b':
        l += 'x'
    if e == 'x':
        l += 'y'
    #print(e)

#l[20] = 'y'
l.append('y')
del l[l.index('b')]
l.remove('a')
print(l.count('x'))
print(l)
print(l.pop())
l.sort()
l.reverse()

print(l)


s = {'a', 'a', 'b', 'c'}
print(s)

s2 = set(l)
print(s2)




