# create a function name remove_middle which has three parameters: lst, #start and end. The function should return a list where all elements in #lst with an index between start and end (inclusive) have been removed.
#For example, the following code should return [4, 23, 42] because #elements at indices 1, 2, and 3 have been removed:
#removeMiddle([4, 8 , 15, 16, 23, 42], 1, 3)

def remove_middle(lst, start, end):
  if start < len(lst) and end <= len(lst):
    del(lst[start:end+1])
  return lst

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

"""
Create a function named more_than_n that has three parameters named
 lst, item, and n.
The function should return True if item appears in the list more than 
n times. The function should return False otherwise.
"""

def more_than_n(lst, item, n):
  if (lst.count(item)) > n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

"""
Create a function named more_frequent_item that has three parameters named lst, item1, and item2.

Return either item1 or item2 depending on which item appears more often in lst.

If the two items appear the same number of times, return item1.
"""

def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item2) > lst.count(item1):
    return item2
  elif lst.count(item1) == lst.count(item2):
    return item1

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

"""
Create a function called middle_element that has one parameter named lst.

If there are an odd number of elements in lst, the function should return 
the middle element.  If there are an even number of elements, the function
 should return the average of the middle two elements.
 Practice this one more!

""" 

def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

"""
Write a function named append_sum that has one parameter named lst.

The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].
"""


def append_sum(lst):
  add_last_two_items_1 = lst[-1] + lst[-2]
  lst.append(add_last_two_items_1)
  add_last_two_items_2 = lst[-1] + lst[-2]
  lst.append(add_last_two_items_2)
  add_last_two_items_3 = lst[-1] + lst[-2]
  lst.append(add_last_two_items_3)
  
  return lst
  
  
  

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))


"""
Write a function named larger_list that has two parameters named lst1 and lst2.

The function should return the last element of the list that contains more elements.
 If both lists are the same size, then return the last element of lst1.

"""

def larger_list(lst1, lst2):
  if len(lst1) > len(lst2):
    return lst1[-1]
  elif len(lst2) > len(lst1):
    return lst2[-1]
  else:
    return lst1[-1]
#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

"""
Write a function named combine_sort that has two parameters named lst1 and lst2.

The function should combine these two lists into one new list and sort the result. 
Return the new sorted list.

"""

#Write your function here
def combine_sort(lst1, lst2):
  new_lst = lst1 + lst2
  return sorted(new_lst)

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

"""
***
Create a function called append_size that has one parameter named lst.

The function should append all of the numbers between 1 and the size of
lst (inclusive) to the end of lst. The function should then return this
 new list.

For example, if lst was [23, 42, 108], the function should return 
[23, 42, 108, 1, 2, 3] because the size of lst was originally 3.
"""

#Write your function here
def append_size(lst):
  to_extend = list(range(1, len(lst) + 1))
  #listifying the range beginning with 1, and accounting fgor len(lst)+1
  lst.extend(to_extend)
  #attaching the new list to old list by extend method above.
  return lst
  #returning the most revised list.

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))


"""
Create a function called every_three_nums that has one parameter named start.

The function should return a list of every third number between start and 100 (inclusive). 
For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater
 than 100, the function should return an empty list.

"""

#Write your function here
def every_three_nums(start):
  my_lst = []
  if start > 100:
    return []
  elif start == 100:
    return [100]
  elif start < 100:
    return list(range(start, 100+1, 3))
    

#Uncomment the line below when your function is done
print(every_three_nums(91))


"""
Scoops sold problem:

"""

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
    
print(scoops_sold)


"""
Using list comprehensions to convert an existing list of celsius temps to farhenheit.
Note: temperature_in_fahrenheit = temperature_in_celsius * 9/5 + 32
"""

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [cl * 9/5 + 32 for cl in celsius]
print(fahrenheit)


















