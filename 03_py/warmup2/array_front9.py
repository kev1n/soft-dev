def array_front9(nums):
  if len(nums) >= 4: #edge case
    for i in nums[0:4]:
      if i == 9:
        return True
  else:
    for i in nums:
      if i == 9:
        return True
  return False

print(array_front9([1, 2, 9, 3, 4])) # → True
print(array_front9([1, 2, 3, 4, 9])) # → False
print(array_front9([1, 2, 3, 4, 5])) # → False
print(array_front9([9, 2, 3])) # → True
print(array_front9([1, 9, 9])) # → True
print(array_front9([1, 2, 3])) # → False
print(array_front9([1, 9])) # → True
print(array_front9([5, 5])) # → False
print(array_front9([2])) # → False
print(array_front9([9])) # → True
print(array_front9([])) # → False
print(array_front9([3, 9, 2, 3, 3])) # → True