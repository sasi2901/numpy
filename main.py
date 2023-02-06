import random
import numpy as np
a = np.array([3, 6, 9])
print(a/3)
"""a = list([2,4,6,8])
print(a/2)"""
a = np.array([1,2,3,4,5])
print(a)
print("*")
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
a = np.array([1,2,3],"complex")
print(a)
a = np.array([1,2,3,4],dtype = "complex")
print(a)
a = np.array((5,4,3,2,1))
print(a)
b = np.arange(1,10)
print(b)
b = np.arange(3.0)
print(b)
b = np.arange(1,10,2)
print(b)
b = np.arange(20,dtype = "complex")
print(b)
b =np.arange(1,10,2,"float")
print(b)
c = np.zeros(5)
print(c)
print("*")
c = np.zeros((2,3))
print(c)
print("*")
c = np.zeros(2,dtype = "int")
print(c)
print("*")
c = np.zeros([3,4])
print(c)
print("*")
c = np.zeros((2,3),order = "F")
print(c)
print("*")
d = np.ones(8)
print(d)
print("#")
d = np.ones(4,dtype = "int")
print(d)
print("#")
d = np.ones((2,3))
print(d)
print("#*")
e = np.empty(6)
print(e)
e = np.empty([3,4],dtype = "int")
print(e)
f =np.linspace(1,100,num=5)
print(f)
f =np.linspace(1,100,num=5,endpoint = False)
print(f)
f =np.linspace(1,100,num=4,retstep=True) # it will return step i.e,size or increment in each step
print(f)
f =np.linspace(1,100,num=5,dtype = int)
print(f)
f =np.linspace(1,100)
print(f)
g =np.eye(2,dtype ="int") # if we mention only one parameter it takes column as same parameter
print(g)
g = np.eye(3,k=1)  # it will give ones in uppper triangle
print(g)
g = np.eye(5)
print(g)
g = np.eye(2,3)
print(g)
g = np.eye(4,k=-1)
print(g)
g =np.eye(5,k=2)
print(g)
print("%")
g =np.identity(5)
print(g)
print("%")
g = np.identity(5,dtype = "int")
print(g)
h = np.random.rand(5)
print(h)
h = np.random.rand(2,3)
print(h)
h = np.random.randn(5)
print(h)
h = np.random.rand(2,3)
print(h)
h = np.random.ranf(5)
print(h)
"""h =random.randint(5,size =10)
print(h)"""
# ATTRIBUTES IN NUMPY
a = np.array([1,2,3])
print(a.ndim)
b = np.array([[1,2,3],[3,2,1]])
print(b.ndim)
print(a.size)
print(b.size)
print(a.shape)
print(b.shape)
print(a.dtype)
print(b.dtype)
print(a.itemsize) # size in bites i.e,32/8
# Datatypes in numpy
a = np.float64([1,2,3])
print(a.dtype)
a = np.array([1,2,3],dtype = "f")
print(a.dtype)
a=np.zeros(5)
a=a.astype(int)
print(a)
# indexing in numpy
a = np.array([1,10,45,67])
print(a[-1])
print(a[-1]+a[-3])
b = np.array([[23,45,67,89],[98,76,54,32]])
print(b)
print(b[0][0])
print(b[-2][-4])
print(b[-2][-4]+b[-2][-3])
print(b[0,1])
c = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(c)
print(c[0,1,2])
print(c[1,0,3])
print(c[-1,-2,-4])
# numpy slicing ///////////////////////////////////////////////////////////////////////////////////////////////////////
a= np.array([1,2,3,4,5])
print(a[1:3])
print(a[:])
print(a[1:])
print(a[1::2])
print(a[::2])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[1:,2:])
b = np.array([[1,2,3,4],[5,6,7,8],[20,30,40,50]])
print(b)
print(b[1:,1:])
print(b[::,::2])
# advance indexeineg
a = np.arange(1,10)
print(a)
index = np.array([1,4,5])
c = a[index]
print(c)
c = a[[1,4,5]]
print(c)
d = np.array([[1,2,3],[4,5,6],[7,8,9]]) # [[row1,row2],[column1,column2]]
print(d)
print(d[[0,2],[2,0]]) # [[row1,row2],[column1,column2]]
print(d[[1,1,2],[0,2,1]])
a = np.array([[1,-2,3],[4,-2,1]])
print(a)
print(a[a<0])
print(a[a>=1])
print(a[a>=1]*3)
print("#")
# arthimetic operations on arrays//////////////////////////////////////////////////////////////////////////////////////
x = np.arange(1,5)
print(x)
print(x+2)
print(x**3)
print(x%2)
print(x-1)
print(x**2)
print("#")
y = np.array([[1,4,5,6],[8,9,3,1]])
print(y)
print(y**2)
x = np.array([10,20,30,40])
y = np.arange(1,5)
print(x+y)
print(x**y)
a = np.array([[1,2,3,4],[5,6,7,8]])
b = np.array([[10,20,30,40],[50,60,70,80]])
print(a)
print(b)
print(a+b)
print(np.add(a,b))
print("*")
print(a*b)
print(np.multiply(a,b))
print("*")
print(a%b)
print(np.mod(a,b))
c = np.array([[1,2],[3,4],[5,6]])
print(c)
d = np.array([10,20])
print(d)
print(c+d)
# arrays reshape()/////////////////////////////////////////////////////////////////////////////////////////////////////
a = np.arange(10)
print(a)
print(a.shape)
b = np.reshape(a,(5,2))  # by default it is taking row wise reshape
print(b)
print()
b = np.reshape(a,(5,2),order = "F") # reshape the elements by column wise
print(b)
b =a.reshape((2,5))
print(b)
a = np.arange(5)
print(a)
b = np.resize(a,(2,3))
print(b)
b = np.resize(a,(5,2)) # this is a new array with resize and it won't affect the original array
print(b)
a = np.arange(10)
print("$",a)
a = a.resize((5,2))  # it will change the original array
print(a)
# order = "c" -->rowise operation,order = "F" -->columnwise operation
a = np.array([[[1,2,3],[3,4,5]],[[6,7,8],[9,10,11]]])
print(a)
b = a.flatten() # by default it is flatten in row wise
print(b)
b = a.flatten(order = "F") # column wise flatten
print(b)
b = np.array([[0,9,8,7],[8,5,4,3]])
print(b)
c = b.flatten()
print(c)
c = b.flatten(order = "F")
print(c)
print("#")
f = b.ravel()  # by default it is rowwise
print(f)
f = b.ravel(order = "F")
print(f)
f = np.ravel(b)
print(f)
a = np.arange(1,11).reshape(5,2)
print(a)
print(a.shape)
b = np.transpose(a)
print(b)
print(b.shape)
b = np.transpose(a,axes = (1,0))  # rowwise
print(b)
b = np.transpose(a,axes = (0,1)) # column wise
print(b)

c = np.arange(1,25).reshape(3,4,2)
print(c)
print(c.shape)
"""d= np.transpose(c,axes = (0,1))
print(d)
print("#")
d= np.transpose(c,axes = (1,0))
print(d)"""
d = np.transpose(c)
print(d)
print(d.shape)
d = a.transpose()
print(d)
d = a.T
print(d)
print("#")
a = np.array([[1,2,3],[4,5,6]])
print(a)
b = np.swapaxes(a,0,1)
print(b)
print("$")
b = np.swapaxes(a,1,0)
print(b)
a = np.array([[2,3,6]])
print(a)
b = np.swapaxes(a,1,0)
print(b)
a = np.arange(1,25).reshape(2,3,4)
print(a)
b = np.swapaxes(a,1,2)
print(b)
# splitting and joining arrays/////////////////////////////////////////////////////////////////////////////////
a = np.arange(1,5)
b = np.arange(6)
c = np.arange(1,10,2)
print(a)
print(b)
print(c)
d = np.concatenate((a,b,c))
print(d)
a = np.array([[1,2],[3,4]])
print(a)
b = np.array([[5,6]])
print(b)
c = np.concatenate((a,b),axis = 0) # by default axis = 0
print(c)
"""c = np.concatenate((a,b),axis = 1)
print(c)"""
b = b.transpose()
c = np.concatenate((a,b),axis =1)
print(c)
a = np.arange(6)
b = np.arange(5)
c = np.arange(5)
d = np.vstack((b,c))
print(d)
d =np.stack((b,c),axis = 0)
print(d)
# array splitting /////////////////////////////////////////////////////
a = np.arange(1,10)
print(a)
b = np.split(a,3)
print(b)
a = np.arange(1,13).reshape(2,6)
b = np.split(a,2)
print(b)
# array insert and delete ////////////////////////////////////////////////
a = np.arange(1,11)
print(a)
b= np.insert(a,1,50)
print(b)
b = np.insert(a,1,50.5) # it will convert float into integer
print(b)
b = np.insert(a,(1,3),50)
print(b)
a = np.array([[2,3,4,5],[6,7,8,9,]])
print(a)
b= np.insert(a,1,300,axis = 0)
print(b)
b= np.insert(a,1,300,axis = 1)
print(b)
a = np.arange(1,11)
print(a)
b = np.append(a,30)
print(b)
a = np.array([[1,2,3],[4,5,6]])
print(a)
b = np.append(a,[[8,9,0]],axis =0)
print(b)
b = np.delete(a,2)
print(b)
c = np.delete(b,2)
print(c)
# matrix in numpy ////////////////////////////////////////
print("$")
a = np.array([[1,2,3],[4,5,6]])
print(a)
b = np.array([[10,20,30],[40,50,60]])
print(b)
c = a+b
print(c)
d =a*b
print(d)
print("#")
"""e = a.dot(b)
print(e)"""
e = np.transpose(a)
print(e)
a = np.matrix("1 2; 3 4")
print(a)
b = np.matrix([[1,2],[5,6]])
print(b)
print("$")
c = a+b
print(c)
d =a*b
print(d)
e =a.T
print(e)
# inverse of a matrix
a  = np.array([[1,2],[4,5]])
print(a)
b = np.linalg.inv(a)
print(b)
# power of a matrix
a = np.array([[1,2],[3,4]])
print(a)
b = np.linalg.matrix_power(a,2)
print(b)
b = np.dot(a,a)
print(b)
c = np.linalg.matrix_power(a,3)
print(c)
b = np.linalg.matrix_power(a,0)
print(b)
b = np.linalg.matrix_power(a,-2)
print(b)
# linear equation using numpy
# 3x+y = 9 and x+2y = 8
a = np.array([[3,1],[1,2]])
b = np.array([9,8])
c = np.linalg.solve(a,b)
print(c)
# 6x+2y-5z = 13
# 3x+3y-2z = 13
# 7x+5y -3z = 26
a = np.array([[6,2,5],[3,3,-2],[7,5,-3]])
b = np.array([13,13,26])
c = np.linalg.solve(a,b)
print(c)
# determinant of a matrix
a = np.array([[1,2],[3,4]])
print(a)
b = np.linalg.det(a)
print(b)
print(round(b))
c = np.array([[1,2,3],[5,6,7],[9,10,11]])
d = np.linalg.det(c)
print(d)
