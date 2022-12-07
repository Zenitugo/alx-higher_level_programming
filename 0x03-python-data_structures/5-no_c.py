def no_c(my_string):
  for char in my_string:
    if 'c' is in my_string:
      my_string.remove(c)
    elif 'C' is in my_string:
      my_string.remove(C)
    else:
      return my_string
 
