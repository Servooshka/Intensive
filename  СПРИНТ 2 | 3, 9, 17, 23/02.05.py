#4


# count = 0
# for line in open("9_3.txt"):
#     l = line.split()
#     nums = sorted([int(num) for num in l])
#
#     n1, n2 = [], []
#     for num in nums:
#         if nums.count(num) == 2:
#             n2.append(num)
#         elif nums.count(num) == 1:
#             n1.append(num)
#     c1 = len(n1) == 3 and len(n2) == 4
#
#     c2 = sum(n2) / 4 < sum(nums) / 7
#
#     if c1 * c2:
#         count += 1
# print(count)



#
# count = 0
# for line in open("9_3.txt"):
#     nums = sorted(int(num) for num in line.split())
#
#     n1 = [n for n in nums if nums.count(n) == 1]
#     n2 = [n for n in nums if nums.count(n) == 2]
#
#     if (len(n1) == 3 and len(n2) == 4) and (sum(n2) / 4 < sum(nums) / 7):
#         count += 1
#
# print(count)
#


#5

count = 0
for line in open("9_4.txt"):
    nums = sorted(int(num) for num in line.split())

    c1 = nums.count(nums[0]) == 1
    c2 = [i for i in nums[1:] if nums[1:].count(i) >= 2]
    c3 = max(nums) + min(nums) < sum(c2)
    if c1 and len(c2) != 0 and c3:
        count += 1
print(count)
