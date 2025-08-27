import array
num_array=array.array("i",[1, 3, 5, 3, 7, 9, 3])
print("Original array: ",num_array)
print("First occurrence of 3 at index: ",
 num_array.count(3 ))
num_array.reverse()
print("Array after reverse: ",
      num_array)

