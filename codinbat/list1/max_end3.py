def max_end3(a):
  b=[]
  if(a[0]>a[len(a)-1]):
    b = [a[0], a[0],a[0] ]
  elif(a[0]<a[len(a)-1]):
    b = [a[len(a)-1], a[len(a)-1],a[len(a)-1] ]
  else:
    b=[a[0], a[0],a[0] ]
  return b
  
    