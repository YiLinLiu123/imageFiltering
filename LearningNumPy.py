#trying things out 
import numpy as np # used to import numpy library, as... assigns a local name
import matplotlib as mpl
import scipy as sp

print ("hello world")

a = np.array( [[1,2],[3,4]], dtype = complex) #example call to the np.array method to create arrays
print (a)

# first create structured data type
dt = np.dtype([('age',np.int8)]) #describes how bytes is fixed, ordering and interpretation
    #essentially allows yout ot define your own data type

print(dt)
b = np.array([(10,),(20,),(30,)],dtype=dt)
print(b)

#Better example of dtype:

#A structured data type containing a 16-character string (in field ‘name’)
# and a sub-array of two 64-bit floating-point number (in field ‘grades’):

dt = np.dtype([('name',np.unicode_,16), ('grades', np.float64, (2,))]) 
x = np.array([('John', (6.0, 7.0)),('Sarah', (8.0, 7.0))], dtype=dt)
print(x[1]) #MSD goes into least memort address
print (x[1]['grades'])
print (type(x[1]))
print (type(x[1]['grades']))


# Shape function

# displays the matrix information
a = np.array([[1,2,3],[4,5,6]])
print (a.shape)

# resizing the array
a.shape = (3,2)
print (a.shape)

#array.ndim

# one dimensional array:
a = np.arange(24)
a.ndim

#now reshape the array
b=a.reshape(2,4,3)
print (b)


#.itemsize: length of each element of array in bytes
x = np.array([1,2,3,4,5], dtype = np.float32) 
print (x.itemsize)

#numpy.flags gives osmeflags regarding objects, kinda cool 
