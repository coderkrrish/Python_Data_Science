#A Python array is an collection of elements with same data type.An array is a collection of items stored at contiguous memory locations. Array can be handled in Python by a module named array. The process of assigining memory blocks to a process by the system is called as Contigeous Memory.Array in Python can be created by importing array module.


#When to use Array in Python? ----->An array is used to store more than one value at a time. It can hold multiple values in a single variable, and also helps you reduce the overall size of the code. Arrays save time. Python arrays are used when you need to use many variables which are of the same type. It can also be used to store a collection of data. The arrays are especially useful when you have to process the data dynamically. Python arrays are much faster than list as it uses less memory.



#Syntax of Array :---->  array(data_type, value_list)


#Creating An Array ----> 
from array import array 

New_array = array('i',  [1, 2, 3, 4, 5])  #Here 'i' denotes the type of data that is Integer
# print(New_array)  #array('i', [1, 2, 3, 4, 5])

# print(dir(New_array))  #Array is having some methods same as lists like append,pop,remove,extend,index,reverse,count,insert

# my_arr = array('i' ,[1, "B", 20, "d"])
# print(my_arr)  #TypeError: 'str' object cannot be interpreted as an integer This error is raised because array supports only homogeneous data types

arr1 = array('i', [10, 11, 7])
# print(arr1) #array('i', [10, 11, 7])

arr2 = array('f', [2, 10.11, 110.2 ,22.20])  #Here 'f' float data type
# print(arr2)  #array('f', [2.0, 10.109999656677246, 110.19999694824219, 22.200000762939453])


arr3 = array('d', [9.29, 10.22, 8.38, 39.30])
# print(arr3)  #array('d', [9.29, 10.22, 8.38, 39.3])

arr4 = array('B', [255, 0, 3]) #Here 'B' is bytes data type It Only Supports values upto 255
# print(arr4)  #array('B', [255, 0, 3]) 

arr5 = array('i', (10, 200, 300)) 
# print(arr5) #array('i', [10, 200, 300]) Tuple will be converted into list

# arr6 = array('i', {1:"A", 2:"B", 3:"C", 4:"D"})
# print(arr6)  #array('i', [1, 2, 3, 4]) Only keys will be considered

arr7 = array('i', [True, False]) 
# print(arr7)  ##array('i', [1, 0])

arr8 = array('i', range(1,10))
# print(arr8)  #array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

arr9 = array('u', ["A","V", "E", "N", "G", "E", "R"])
# print(arr9)

#--------------------Array Methods :------>

a = array('i', [10,20,30,40,50])
a[0] = 60
# print(a)  #array('i', [60, 20, 30, 40, 50])


#Array Append :--
a.append(9)
# print(a)  #array('i', [60, 20, 30, 40, 50, 9])

# a.append(ord("B"))
# print(a)  #array('i', [60, 20, 30, 40, 50, 9, 66])

b = array('d', [10.22, 9.99, 8.23, 8.2, 9.33])
b.extend([20, 10.22])
# print(b) #array('d', [10.22, 9.99, 8.23, 8.2, 9.33, 20.0, 10.22])


# print(b.count(10.22))  #1

# print(b.index(9.99))  #1

# b.reverse()
# print(b)  #array('d', [9.33, 8.2, 8.23, 9.99, 10.22])


b.insert(6, 100.22)
# print(b)  #array('d', [10.22, 9.99, 8.23, 8.2, 9.33, 100.22])

b.insert(19, 22.88)
# print(b)  #array('d', [10.22, 9.99, 8.23, 8.2, 9.33, 100.22, 22.88])


# res = b.pop()
# print(res)  #22.88
# print(b)  #array('d', [10.22, 9.99, 8.23, 8.2, 9.33, 100.22])


# res = b.pop(4)
# print(res)  #9.33
# print(b)  #array('d', [10.22, 9.99, 8.23, 8.2, 100.22])


# b.remove(9.99)
# print(b)  #array('d', [10.22, 8.23, 8.2, 9.33, 100.22, 22.88])

 
# print(b[::])  #array('d', [10.22, 9.99, 8.23, 8.2, 9.33, 100.22, 22.88])

# print(b[::-1])  #array('d', [22.88, 100.22, 9.33, 8.2, 8.23, 9.99, 10.22])

# print(b[1:5])  #array('d', [9.99, 8.23, 8.2, 9.33])


for i in b:
    # print(i, end = ",")  #10.22,9.99,8.23,8.2,9.33,100.22,22.88,
    pass


import numpy as np

a4 = np.array([[10,20,ord("A")], [22,33,44]])
# print(a4)
# print(type(a4))


a5 = np.array([["A", "Abhay", 10+100],[20, 20+4j, "Ram"]])
# print(a5)

a6 = np.zeros (8, dtype=np.int64)
# print(a6)




p_language = np.array(["Python", "Java", "CSS",  "HTML", "JavaScript", "MySQL", "JSON", "XML"])
print(p_language)