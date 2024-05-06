#2

# for f in range(2):
#     for e in range(2):
#         for l in range(2):
#             for a in range(2):
#                 g = ((not f) and e) <= (not(not(l) or a))
#                 if g == 0:
#                     print(l,a,e,f)



#5

# for n in range(10000, 100000):
#     n = str(n)
#     a = int(n[0]) + int(n[2]) + int(n[4])
#     b = int(n[1]) + int(n[3])
#     if a < b:
#         r = str(a) + str(b)
#     else:
#         r = str(b) + str(a)
#     if r == str(922):
#         print(n)
#         break


#7

# x = 1920 * 1080
# print((((2**23)/58)*100) / x)


#8

# import itertools
# a = 'сокта'
# count = 0
# for i in list(itertools.product(a, repeat=6)):
#     s = ''.join(i)
#     count += 1
#     if s[0] not in ['с', 'к', 'т'] and 'оа' in s:
#         print(count)
#         break



#9

# s = '2' * 19 + '5' + '3' * 10

# while '233' in s or '225' in s:
#     if '233' in s:
#         s = s.replace('233', '3', 1)
#     else:
#         s = s.replace('225', '52', 1)
# print(s) 


#10
# from ipaddress import *

# a = [128, 192, 224, 240, 248, 252, 254, 255]
# for x in a:
#     net = ip_network(f'175.122.80.13/255.255.255.{x}', 0)



#13

# print(bin(175)[2:].zfill(8))
# print(bin(122)[2:].zfill(8))
# print(bin(80)[2:].zfill(8))
# print(bin(13)[2:].zfill(8))


#14

# for x in range(22, 1, -1):
#     for y in range(2, 21):
#         a = 9 + x * 21 + y * 21**2 + 6 * 21**3 + 3 * 21**4
#         b = 9 + 9 * 21 + y * 21**2 + 2 * 21**3 + 1 * 21**4
#         c = a + b
#         if c % 18 != 0:
#             break
#     else:
#         y = 5
#         a = 9 + x * 21 + y * 21**2 + 6 * 21**3 + 3 * 21**4
#         b = 9 + 9 * 21 + y * 21**2 + 2 * 21**3 + 1 * 21**4
#         c = a + b
#         print(c / 18)
#         break


#15

#
# def tre(n, m, k):
#     n, m, k = sorted([n, m, k])
#     return n + m > k
#
# for a in range(1, 100):
#     for x in range(1, 100):
#         f = not(tre(x, a, 5) and (tre(x, 11, 18) == (not(max(x, 5) > 15))))
#         if not f:
#             break
#     else:
#         print(a)



#16

# import sys
# sys.setrecursionlimit(100000000)
# def f(n):
#     if n <= 6:
#         return n
#     if n > 6:
#         return 2*n + 4 + f(n - 1)
# print(f(6189) - f(6183))


#17

# with open('5 симуляция/17-8.txt') as f:
#     f = f.readlines()

# count_100 = 0
# for i in f:
#     if abs(int(i)) % 100 == 0:
#         count_100 += 1

# count = 0
# m_sum = 0
# for i in range(len(f) - 1):
#     left, right = int(f[i]), int(f[i + 1])
#     if (left < 0 or right < 0) and (left + right < count_100):
#         count += 1
#         m_sum = max(m_sum, abs(left + right))
# print(count, m_sum)


#23


# def f(x, y):
#     if x > y or x == 21:
#         return 0
#     if x == y:
#         return 1
#     if x < y:
#         return f(x + 3, y) + f(x * 2, y)
# print(f(6, 42))


#24

with open('24-4.txt') as f:
    f = f.readline()
m_c = 0
a = 'AE'
b = 'BCD'
count = 0
for i in range(len(f) - 1):
    left, right = f[i], f[i + 1]
    if (left in a and right in b) or (left in b and right in a):
        count += 1
        m_c = max(m_c, count)
    else:
        m_c = max(m_c, count)
        count = 0
print(m_c // 2)



#25

# from fnmatch import fnmatch as fn
# count = 0
# for i in range(199999968, 0, -42):
#     if (fn(str(i), '?2*4*0') and (not (fn(str(i), '1*7*'))) and (i % 42 == 0)):
#         if count == 5:
#             break
#         else:
#             print(i, i // 42)
#             count += 1


