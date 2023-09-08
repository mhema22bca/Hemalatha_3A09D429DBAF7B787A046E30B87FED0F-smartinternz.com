def  isLeapYear(year):   
 if("Year % 4 == 0 and Year % 100!= 0") or year %  400 == 0:
   return True
 else: 
   return False
   year = 2013
if isLeapYear(year):
  print("{} is a leap year.".format(year))
else:
  print ('{} is a leap year.'.format(year))




    

