#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Write a program to accept user input and display it.
num = int(input('Enter a number'))
print('Your input: ', num)


# In[6]:


str1, str2 = input('Enter strings: ').split()
print('Input Strings: ', str1, str2)


# In[2]:


arr = [10, 11, 12, 13, 14]


# In[3]:


print('First Element: ', arr[0])
print('Last Eelement: ', arr[-1])


# In[4]:


sublist1 = [item for item in arr if item >=12]
print('Original list: ', arr)
print('Sublist: ', sublist1)


# In[ ]:




