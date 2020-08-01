#!/usr/bin/env python
# coding: utf-8

# In[12]:


#!/usr/bin/python

def fiboEvenSum(number):
    value = 1
    mySum = 0
    s = 0
    while(value < number):
        f = value
        #print ("**START**")
        #print ("Value of F: ",f)
        #print ("Value of S: ",s)
        value = f + s
        #print ("Value of V: ",value)
        if (value % 2 == 0):
            mySum += value
        s = f
    print(mySum)
    return

fiboEvenSum(4000000)


# In[ ]:





# In[ ]:




