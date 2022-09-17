a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

max = 0

if a > b and a > c :
    max = a
elif b > c:
    max = b
else:
    max = c

print(max)