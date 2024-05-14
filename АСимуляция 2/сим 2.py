#2
#
# import itertools
# count = 0
#
# def check(x, y, z):
#     if str(x) + str(z) + str(y) == '010' or str(x) + str(z) + str(y) == '110':
#         return 1
#     elif str(x) + str(y) + str(z) == '010' or str(x) + str(y) + str(z) == '110':
#         return 1
#     elif str(z) + str(x) + str(y) == '010' or str(z) + str(x) + str(y) == '110':
#         return 1
#     elif str(z) + str(y) + str(x) == '010' or str(z) + str(y) + str(x) == '110':
#         return 1
#     elif str(y) + str(x) + str(z) == '010' or str(y) + str(x) + str(z) == '110':
#         return 1
#     elif str(y) + str(z) + str(x) == '010' or str(y) + str(z) + str(x) == '110':
#         return 1
#     else:
#         return 0
#
# for i in itertools.product('01', repeat=3):
#     x, y, z = int(i[0]), int(i[1]), int(i[2])
#
#     if (x <= y and z) == 0:
#         count += check(x, y, z)
# print(count)
#
# print('2: 2')



#5

# for n in range(1000):
#     r = bin(n)[2:]
#     if len(r) % 2 == 0:
#         r = r[:len(r) // 2] + '000' + r[len(r) // 2:]
#     else:
#         r = '1' + r + '01'
#     r = int(r, 2)
#     if r > 100:
#         print('5:', n)
#         break
#
# print('5: 16')



#9

# with open('9.txt') as f:
#     f = f.readlines()
# count = 0
# for i in f:
#     i = i.split()
#     a, b, c, d = int(i[0]), int(i[1]), int(i[2]), int(i[3])
#     if a == d and b == c and a + b +c +d == 360:
#         count += 1
# print('9:', count)



#12

# for x in range(101, 200):
#     s = '5' * x
#     while '555' in s or '888' in s:
#         s = s.replace('555', '8', 1).replace('888', '55', 1)
#     if s.count('8') == 0:
#         print('12:', x)
#         break



#13

# from ipaddress import *
#
# net = ip_network('136.36.240.16/255.255.255.248', 0)
# count = 0
# for ip in net:
#     ip = bin(int(ip))[2:]
#     if '101' not in ip:
#         count += 1
# print('13:', count)


#14

# x = 673 ** 7 + 67 ** 6 + 3 ** 3
# def from12(f):
#     s = ''
#     while f != 0:
#         if f % 12 == 10:
#             s = 'A' + s
#         elif f % 12 == 11:
#             s = 'B' + s
#         else:
#             s = str(f % 12) + s
#         f //= 12
#     return s
#
# sum_a = from12(x).count('A')
# sum_8 = from12(x).count('8')
# print('14:', sum_a * 10 - sum_8 * 8)



#15

# def deli(n, m):
#     if n % m == 0:
#         return True
#
# b = range(50, 71)
# for a in range(100, 0, -1):
#     for x in range(100, 0, -1):
#         f = deli(x, a) or ((x in b) <= (not deli(x, 16)))
#         if not f:
#             break
#     else:
#         print(a)
#         break


#16

# def f(n):
#     if n > 300:
#         return 1
#     if n <= 3000 and n % 2 == 0:
#         return f(n + 1) - n + 1
#     if n <= 3000 and n % 2 != 0:
#         return f(n + 2) - 2 * n + 2
# print('16:', 2 * f(39) - 2 * f(34))



#17

# with open('17.txt') as f:
#     f = f.readlines()
#
# count = 0
# max_s = 0
# del_5 = len([i for i in f if int(i) % 5 == 0])
# for i in range(len(f) - 1):
#     left, right = int(f[i]), int(f[i + 1])
#     summ = left + right
#     # noinspection PyTypeChecker
#     if ((left < 0 <= right) or (left >= 0 > right)) and (summ < del_5):
#         count += 1
#         max_s = max(max_s, summ)
# print('17:', count, max_s)


#19

# def turn(s, t):
#     return [play(s + 1, t),
#             play(s + 3, t),
#             play(s * 2, t)]
#
# def play(s, t):
#     if s >= 443 or t > 5:
#         return t == 2
#     t += 1
#
#     if t % 2 == 1:
#         return all(turn(s, t))
#     else:
#         return any(turn(s, t))
#
# for s in range(1, 443):
#     if play(s, 0):
#         print('19:', s)


#20

# def turn(s, t):
#     return [play(s + 1, t),
#             play(s + 3, t),
#             play(s * 2, t)]
#
# def play(s, t):
#     if s >= 443 or t > 5:
#         return t == 3
#     t += 1
#
#     if t % 2 == 1:
#         return any(turn(s, t))
#     else:
#         return all(turn(s, t))
#
# for s in range(1, 443):
#     if play(s, 0):
#         print('20:', s)


#21

# def turn(s, t):
#     return [play(s + 1, t),
#             play(s + 3, t),
#             play(s * 2, t)]
#
# def play(s, t):
#     if s >= 443 or t > 5:
#         return t == 2 or t == 4
#     t += 1
#
#     if t % 2 == 1:
#         return all(turn(s, t))
#     else:
#         return any(turn(s, t))
#
# for s in range(1, 443):
#     if play(s, 0):
#         print('21:', s)
#         break



#23

# def f(x, y):
#     if x < y:
#         return 0
#     if x == y:
#         return 1
#     if x > y:
#         return f(x - 1, y) + f(x // 2, y)
# print('23:', f(30, 9) * f(9, 1))


#24

with open('24.txt') as f:
    f = f.readline()


# for i in 'ABCDEF':
#     f = f.replace(f'{i}{i}{i}', '***')
# count = 0
# m_c = 0
# for i in f:
#
#     if i == '*':
#         count += 1
#     else:
#         m_c = max(count, m_c)
#         count = 0
# print('24:', m_c)


#25

# from fnmatch import fnmatch as fn
# for i in range(9112376, 10**10 + 1, 50068):
#     if fn(str(i), '9?979*8') and str(i).count('0') > 0:
#         print(i, i // 50068)