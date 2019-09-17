import numpy as np

z=np.zeros((2,4),np.uint8)
print("print type of z is ",type(z))
print("print z is\n",z)

o=np.ones((2,4),np.uint8)
print("print o is\n",o)

#initial a array and configurate the content for float data type.
m=np.array(([4,12,3,1],[10,12,14,29]),np.float32)
print("print m is \n",m)

# get the row and column size
print("Array m's shape is \n",m.shape)

