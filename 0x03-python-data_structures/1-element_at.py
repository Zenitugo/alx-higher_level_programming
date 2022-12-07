#!/usr/bin/python3
def element_at(my_list, idx):
  for i in range(my_list):
    if idx < 0:
      return none
    elif idx > len(my_list):
      return none
    else:
      return my_list.pop(idx)
    print("Element at index {:d} is { }". format(idx, element_at(my_list, idx))
