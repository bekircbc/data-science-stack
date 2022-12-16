import matplotlib.pyplot as plt
import numpy as np


# first edition without numpy

# import matplotlib.pyplot as plt

# xs =[]
# for x in range(0,10):
#   xs.append(x)

# ys=[]
# for x in xs:
#   ys.append(x**2)
  
# plt.plot(xs,ys)
# plt.show()

# with numpy



# xs =np.arange(10)
# ys=xs**2
  
# plt.plot(xs,ys)
# plt.show()

# numpy

print(np.arange(10)*3)

print(np.array([1,2,3,4,5,10])**2)

print(np.zeros(10))

print(np.array([1,2,3,4,5,10]).mean())
print(np.array([1,2,3,4,5,10]).max())
print(np.array([1,2,3,4,5,10]).min())
print(np.array([1,2,3,4,5,10]).std())

# 

a = np.array([1,2,3,4])
b=np.array([False, True, True, False])

c = a[b]
print(c)

c= a>=3
print(c)
print(a[c])

print(a[a>=3])

# mehrdimensiole arrays

mehrdim=np.array([1,2,3,4,5,6,7,8])
arr2= mehrdim.reshape((2,4))

print(arr2[0])
print(arr2[1])

print(arr2.shape)

