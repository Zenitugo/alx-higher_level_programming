#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
  for i in range(my_list):
    my_list.sort( )
    my_list.reverse( )
    print("{:d}".format(my_list))
