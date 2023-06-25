#!/usr/bin/env python
# coding: utf-8

# # Numpy Tutorial 

# In[5]:


import numpy as np


# In[6]:


myarray = np.array([[1,2,4,5]],np.int8)  # int8 -> its store 8 bytes of integer data 


# In[7]:


myarray 


# In[8]:


print(type(myarray))


# In[9]:


myarray[0,1]


# In[10]:


myarray.shape  # shape ->define the structure of the array  output say 1 row and 4 columns


# In[11]:


myarray[0,1]=7


# In[12]:


myarray


# # Array Creation : Conversion from other python data structure

# In[14]:


import numpy as np


# In[15]:


listarray=np.array([[12,23,4],[2,8,9],[92,54,24]])


# In[16]:


listarray


# In[17]:


listarray.dtype


# In[18]:


listarray.shape


# In[20]:


listarray.size  #size -> it will print all the element of the array


# In[21]:


np.array({34,78})


# # Array Creation : Intrinsic Numpy array creation objects

# In[22]:


import numpy as np


# In[23]:


zeros=np.zeros((2,5))


# In[24]:


zeros


# In[25]:


rng=np.arange(15)  #arange->It print range betwen nos


# In[26]:


rng


# In[27]:


lspace=np.linspace(1,20,3)


# In[28]:


lspace


# In[30]:


emp=np.empty((4,6))


# In[31]:


emp


# In[32]:


emp_like=np.empty_like(lspace)


# In[33]:


emp_like


# In[34]:


ide=np.identity(20)


# In[35]:


ide


# In[36]:


ide.shape


# In[37]:


arr=np.arange(99)


# In[38]:


arr


# In[40]:


arr=arr.reshape(3,33)


# In[41]:


arr


# In[44]:


arr=arr.ravel()


# In[45]:


arr


# In[48]:


arr.shape


# In[49]:


x=[[1,2,3],[4,5,6],[7,1,0]]


# In[50]:


ar=np.array(x)


# In[51]:


ar


# In[52]:


ar.sum(axis=0)


# In[53]:


ar.sum(axis=1)


# In[54]:


ar.T # transpose matrix


# In[55]:


ar.flat


# In[56]:


for item in ar.flat:
    print(item)


# In[57]:


ar.ndim # 2 dimensional


# In[58]:


ar.size


# In[59]:


ar.nbytes


# In[60]:


one=np.array([1,2,3,5])


# In[61]:


one.argmax() # it return the index value of max elements


# In[62]:


one.argmin()  # it return the index value of min elements


# In[63]:


one.argsort()


# In[64]:


ar


# In[65]:


ar.argsort()


# In[66]:


ar.argmin()


# In[67]:


ar.argmax()


# In[68]:


ar.argmax(axis=0)


# In[69]:


ar.argmax(axis=1)


# In[70]:


ar.argmin(axis=0)


# In[71]:


ar.argmin(axis=1)


# In[72]:


ar.ravel()


# In[74]:


ar.reshape((3,3))


# In[75]:


ar


# In[76]:


ar2=np.array([[1, 2, 1],
       [4, 0, 6],
       [8, 1, 0]])


# In[77]:


ar2


# In[79]:


ar_sum=ar + ar2


# In[80]:


ar_sum


# In[81]:


ar_multipli=ar * ar2


# In[82]:


ar_multipli


# In[83]:


ar_sub=ar - ar2


# In[84]:


ar_sub


# In[85]:


ar_div=ar / ar2


# In[86]:


ar_div


# In[87]:


ar_squareroot=np.sqrt(ar) # print squareroot of each element of arr


# In[88]:


ar_squareroot


# In[89]:


ar_sum=ar.sum() # print sum of element in array


# In[90]:


ar_sum


# In[91]:


ar_max=ar.max()  # print max element in array


# In[92]:


ar_max


# In[93]:


ar_min=ar.min()  # print min element in array


# In[94]:


ar_min


# In[95]:


np.where(ar>5)


# In[96]:


ar


# In[98]:


np.count_nonzero(ar) # its count the non zero element in array


# In[99]:


np.nonzero(ar)


# In[100]:


import sys


# In[102]:


py_ar=[2,4,56,3]


# In[103]:


np_ar=np.array(py_ar)


# In[104]:


sys.getsizeof(1)*len(py_ar)


# In[108]:


np_ar.itemsize * np_ar.size


# In[ ]:




