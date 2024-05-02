#первые 19-21

# def turns(s1, s2, s3, t):
#     return [play(s1 * 2, s2, s3, t),
#             play(s1, s2 * 2, s3, t),
#             play(s1, s2, s3 * 2, t),
#             play(s1 + 2, s2 + 2, s3 + 2, t)]
#
#
# def play(s1, s2, s3, t):
#     if s1 + s2 + s3 >= 25 or s1 >= 20 or s2 >= 20 or s3 >= 20 or t > 5:
#         return t == 3
#     t += 1
#     if t % 2 == 1:
#         return any(turns(s1, s2, s3, t))
#     else:
#         return all(turns(s1, s2, s3, t))
#
#
# for s in range(1, 20):
#     if play(2, 3, s, 0):
#         print(s)
#
#



#вторые 19-21

def turns(s, t):
    if s % 2 == 1:
        return [play(s + 1, t),
                play(s * 2, t)]
    else:
        return [play(s + 1, t),
                play(s * 1.5, t)]


def play(s, t):
    if s >= 84 or t > 5:
        return t == 2 or t == 4
    t += 1
    if t % 2 == 1:
        return all(turns(s, t))
    else:
        return any(turns(s, t))

for s in range(1, 100):
    if play(s, 0):
        print(s)
