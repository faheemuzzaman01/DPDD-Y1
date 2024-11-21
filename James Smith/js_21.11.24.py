import search as s
nums = [15, 9, 27, 34, 6, 12]
nums1 = [2, 4, 6, 8, 10, 12, 14]

print(s.linear_search(nums, 27))
print(s.binary_search(sorted(nums), 27))
print(s.recursive_binary_search(sorted(nums), 27, 0, len(nums) -1))
print(s.for_loop_binary_search(nums1, 10))