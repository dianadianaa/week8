def date_fashion(you, date):
  if((you >= 8 or date>=8) and not( you<3 or date<3)):
    return 2
  elif(you <= 2 or date<=2):
    return 0
  else: 
    return 1
