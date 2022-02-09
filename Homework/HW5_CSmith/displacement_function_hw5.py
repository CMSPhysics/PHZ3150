#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Corine Smith, Homework 5, Feb 06 12:25:12 EST 2022


# In[2]:


#Problem 4- displacement function
print( 'Problem 4')


# In[3]:


import numpy as np 


# In[4]:


def displacement( u_init , a , t ):
    """Calculates displacement of a body as a function of initial speed[ u_init ] , constant acceleration[ a ] , and time[ t ]
    INPUT: initial speed[ u_init ] , acceleration[ a ] , time[ t ] 
    OUPUT: displacement[ s ]"""
    
    s = u_init * t + 0.5 * a * np.power( t , 2 )
    
    return s 


# In[ ]:




