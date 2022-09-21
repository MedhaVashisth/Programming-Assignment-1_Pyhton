#!/usr/bin/env python
# coding: utf-8

# In[3]:


print('Hello Python')


# In[5]:


a = 10
b = 5


# In[6]:


a+b


# In[7]:


a/b


# In[17]:


a = 5
b = 6
c = 7


# In[24]:


a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))


# In[25]:


s = (a + b + c) / 2


# In[26]:


area = (s*(s-a)*(s-b)*(s-c)) ** 0.5


# In[27]:


print('The area of the triangle is %0.2f' %area)


# In[28]:


x = 5
y = 10


# In[29]:


x = input('Enter value of x: ')
y = input('Enter value of y: ')


# In[30]:


temp = x
x = y
y = temp


# In[31]:


print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# In[32]:


import random


# In[33]:


print(random.randint(0,9))


# In[ ]:




