#1
max_a = 0
for n in range(3, 10001):
    s = '1' + n * '9'
    while '19' in s or '49' in s or '999' in s:
        if '19' in s:
            s = s.replace('19', '9', 1)
        if '49' in s:
            s = s.replace('49', '91', 1)
        if '999' in s:
            s = s.replace('999', '4', 1)
    a = 0
    for i in s:
        a += int(i)
    max_a = max(max_a, a)
print('1:', max_a)


#2

for a in range(100):
    flag = True
    for b in range(100):
        for c in range(100):
            x = '0' + '1'  * a + '2' * b + '3' * c + '0'
            s = x
            while not '00' in x:
                x = x.replace('01', '220', 1)
                x = x.replace('02', '1013', 1)
                x = x.replace('03', '120', 1)
            if x.count('1') == 13 and x.count('2') == 18:
                print('2:', len(s))
                flag = False
                break
        if not flag:
            break
    if not flag:
        break



#3

import sys
sys.setrecursionlimit(10000)
def f(n):
    if n > 3000:
        return n
    if n <= 3000 and n % 2 == 0:
        return n + f(n + 1) + 1
    if n <= 3000 and n % 2 != 0:
        return f(n + 2) + 2
print('3:', f(40) - f(43))



#4


with open('h17_1.txt') as f:
    f = f.readlines()
    nums = [i for i in f if (len(str(int(i))) == 3 and int(i) % 10 == 5)]
    min_n = int(min(nums))


    count = 0
    min_s = 1000000000
    for i in range(len(f) - 1):
        left, right = int(f[i]), int(f[i + 1])
        if ((len(str(left)) == 3 and len(str(right)) != 3) or (len(str(left)) != 3 and len(str(right)) == 3)) and ((int(left) + int(right)) % min_n == 0):
            count += 1
            min_s = min(int(left) + int(right), min_s)
print('4:', count, min_s)



#5

def sr(x, y, z):
    return (x + y + z) / 3

def dva(x, y, z, w):
    c = 0
    if x < 0:
        c += 1
    if y < 0:
        c += 1
    if z < 0:
        c += 1
    if w < 0:
        c += 1
    if c >= 2:
        return 1

def pat(x, y, z, w):
    if (x + y + z + w) % 51 == 0:
        return 1


with open('h17_2.txt') as f:
    f = f.readlines()
    count_tri = 0
    count_chet = 0
    nums = [abs(int(i)) for i in f if int(i) % 670 == 0]
    max_n = max(nums)

    for i in range(len(f) - 2):
        left, middle, right = int(f[i]), int(f[i + 1]), int(f[i + 2])
        if sr(left, middle, right) > max_n:
            count_tri += 1

    for i in range(len(f) - 3):
        left, middle, right, plus = int(f[i]), int(f[i + 1]), int(f[i + 2]), int(f[i + 3])
        if dva(left, middle, right, plus) and pat(left, middle, right, plus):
            count_chet += 1
print('5:', count_chet, count_tri)


#6


from fnmatch import fnmatch as fn
for i in range(1200381, 10**8 + 1, 273):
    if fn(str(i), '12??36*1'):
        print(i, i // 273)

#7
import math
def ch_n(x):
    n = 0
    for i in range(1, math.ceil(math.sqrt(x)) + 1):
        # if x % i == 0 and i % 4 == 0:
        #     n += i
        #     if x % (x / i) == 0 and (x // i) % 4 == 0:
        #         n += (x // i)
        if x % i == 0:
            if i % 4 == 0:
                n += i
            if (x // i) % 4 == 0:
                n += (x // i)
    return n
count = 0
for i in range(1_331_566, 10**10):
    if count == 4:
        break
    if ch_n(i) % 423 == 8:
        count += 1
        print(i, ch_n(i))
