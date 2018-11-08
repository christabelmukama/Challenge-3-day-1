#2018 is required to get the age
this_year=int (2018)
your_input=int(input("please enter your birth  year"))
this_is=int(this_year - your_input)
#The condition being satisfied
if this_is < 18:
   print("this is a minor")
elif this_is > 18 and this_is < 36:
  print("this is a youth")
else:
  print("this is an elder")