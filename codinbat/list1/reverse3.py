def reverse3(nums):
  a =[]
  m= len(nums)-1
  for i in nums:
    a.append(nums[m])
    m=m-1
  return a