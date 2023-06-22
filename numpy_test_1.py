import numpy as np #import as np
#import numpy - import directly
#numpy.array([1, 2, 3, 4, 5])
#print(np.__version__) display version
e = int()
simple = np.array([1, 2, 3, 4])
x = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 12]])
y = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 12]])
#x = np.array([1, 3, 4],ndim=2) -  It display as 2 dimensional array
#print(x+y) - It's work as matrix
#print(x.ndim) #the number of dimensions
#print(x)
#access elements in two dimensional - x = array: print(x[row_number,column_number])
#print(x[1, 2])
z = np.array([[[ 1, 2, 3],[4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
#print(z)
#print(z[0, 1, 1])
#one dimensional arrays data structure
# np.array([1=0/-4, 2=1/-3, 3=2/-2, 4=3/-1])
# array range - x =np.array([1, 2, 3, 4]) - print(x[1:]) / print(x[:3]) / print(x[1:3])
#print(simple[:3]) - work - 1D
#print(x[1,:3]) - work - 2D
#print(z[1,0,0:1]) - work - 3D - slicing
# x[start:end:step]
#print(simple[1::2]) - even numbers
#print(simple[::2]) - Odd numbers
#print(x[0:, -1]) - work - 2D

#  ------ DATA TYPE CHARACTER CODES -----------
# Integer - 'i' | Boolean - 'b' | float - 'f' | Complex - 'c' | Unicode string - 'U'
# Time delta - 'm' | Date time - 'M' | Object - 'O'
print(x.dtype) # show data types
#already adding data types :-
#simple = np.array([1, 2, 3, 4],dtype="character code")

# ------------ convert data type ----------------
convert = x.astype('f')
#var = variable.astype('character code')
# ***----- specialy boolean data type represent 'True' Except '0' value ---****

#------------------------view--------------------
view = simple.view()
simple[1] = 10
print(view)
print(view.base) #oraginal

#----------------------- copy --------------------

copy = simple.copy()
simple[1] = 20
print(copy)
print(view.base) #facke
