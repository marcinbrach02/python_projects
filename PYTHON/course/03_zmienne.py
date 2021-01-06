z = 2

print(type(z))

z = 2.0

print(type(z))

print(z.__class__)
print(isinstance(z, float))
print(float.__class__)

z = bool(1)
print(type(z))

z = 32
z = 0o123
z = 0xABC
z = 0b101

print(z)

print(9 / 4)
print(9 // 4)

z = .2
z = 2.4
z = 2e3
print(z)

print(int('   2   '))

print(float('23.2'))
print(float('23,2'.replace(',' , '.')))



