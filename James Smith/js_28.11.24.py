import random as r
import searchsort as s
nums = []
while True:
    num = r.randint(1,50)
    if num not in nums:
        nums.append(num)
    else:
        pass
    if len(nums) == 50:
        break

print(f'{nums}\n')
s.merge_sort(nums, 0, len(nums)-1)
print(nums)
