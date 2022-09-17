a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

if a >= 10 and b >= 10 and c >= 10:
    if a % 3 == 0 and b % 3 == 0:
        print('YES')
    else:
        print('NO')
