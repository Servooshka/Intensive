#2

for a in range(1000):
    for x in range(1000):
        if not((x & 39 == 0) or ((x & 11 == 0) <= (not(x & a == 0)))):
            break
    else:
        print('2:', a)
        break


#3

def poz(n, m):
    return n - m > 0


for a in range(100, -1, -1):
    flag = True
    for x in range(100):
        for y in range(100):
            if ((not poz(y + x, 53)) or (not poz(29, x - y)) or poz(y, a)) == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        print('3:', a)
        break


#4


b = range(24, 90 + 1)
c = range(47, 115 + 1)

for l in range(1, 100):
    for a1 in range(20, 120):
        a = range(a1, a1 + l + 1)

        for x in range(1, 100):
            if ((x in c) <= (((x not in a) and (x in b)) <= (x not in c))) == 0:
                break
        else:
            print('4:', l, a)
            break
    else:
        continue
    break



#7

for x in range (149, -1, -1):
    n1 = 5 * 150 ** 4 + 1 * 150 ** 3 + x * 150 ** 2 + 2 * 150 + 9
    n2 = x * 150 ** 3 + 0 + 2 * 150 + 3
    summ = n1 + n2

    if summ % 149 == 0:
        print('7:', summ // 149)
        break

#9
def S(n):
    for d1 in range(2, int(n**0.5) + 1):
        if n % d1 == 0:
            d2 = n // d1
            return d1 + d2
    return 0


count = 0
num = 432_000 + 1
while count != 6:
    if str(num).count('5') >= 3:
        summ = 0
        for n in str(num):
            if int(n) % 2 == 0:
                summ += int(n)
        if summ > 22:
            s = S(num)
            if s % 51 == 0 and s != 0:
                print('9:', num, s)
                count += 1
    num += 1