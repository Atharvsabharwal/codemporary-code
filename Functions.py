#!/usr/bin/env python
# coding: utf-8

# In[2]:


def sum(x,y,z):
    return x + y +z

print(sum(25,50,75))


# In[3]:


def sum(x,y=5,z=9):
    return x + y +z
print(sum(35+10+10))


# In[12]:


def multiply(*x):
    total = 1
    for x in  x:
        total *= x
    return total

print(multiply(3,2,4))
    


# In[4]:


x=10
def cube(x):
    return x*x*x
print(cube(x))


# In[6]:


y=100
import math
math.sqrt(y)


# In[ ]:




