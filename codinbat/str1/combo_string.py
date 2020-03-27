def combo_string(a, b):
  if(len(a)<len(b)):
    short = a
    l=b
  else:
    short=b
    l=a
  return short+l+short
  