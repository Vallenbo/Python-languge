nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

j = 0
for i in range(m, len(nums1)):
    nums1[i] = nums2[j]
    j = j + 1
nums1.sort()


# for i in nums1:
#     nums1.remove(0)
#
# for y in nums2:
#     if y != 0:
#         nums1.append(y)
#
#
# nums1.sort()
print(nums1)
