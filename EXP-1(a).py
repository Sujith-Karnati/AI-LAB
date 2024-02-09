#nested list
nested_list=[[1,2,3,],[4,5,6],[7,8,9]]

#length of a list
length_of_list = len(nested_list)

#concatenation of lists
list1 = [1,2,3]
list2 = [4,5,6]
concatenated_list = list1 + list2

#membership test
element_to_check = 3
is_member = element_to_check in list1

#indexing
first_element = list1[0]

#slicing
sliced_list = list1[1:3]
  
#displaying result 
print("nested list:",nested_list)
print("length of the list:",length_of_list)
print("concatenated lists:",concatenated_list)
print(f"is {element_to_check} a member of list1? {is_member}")
print("first element in list1:",first_element)
print("sliced list:", sliced_list)  