def make_ends(nums):
  a=[]
  if(len(nums)>2):
    a=[nums[0], nums[len(nums)-1]]
  elif(len(nums)==2):
    a=[nums[0], nums[1]]
  else:
    a=[nums[0], nums[0]]
  return a
