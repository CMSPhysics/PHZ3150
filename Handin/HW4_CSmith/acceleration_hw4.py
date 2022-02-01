#!/usr/bin/env python
# coding: utf-8

# In[1]:


print( 'Problem 3' )


# In[2]:


#acceleration function written to be included in the solution for hw4 problem 3


# In[3]:


def acceleration( u1, u2, t1, t2 ):
    """Function for acceleration using the change in speed over the change in time.
    INPUT: initial speed u1[m/s], final speed u2[m/s], initial time t1[s], final time t2[s]
    OUTPUT: acceleration a[m/s^2]"""
    
    a = (u2-u1) / (t2-t1)
    
    return a 


# In[ ]:





# In[ ]:




