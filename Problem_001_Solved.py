#!/usr/bin/env python
# coding: utf-8

# In[19]:


#!/usr/bin/python

def multiplesOf3and5(number):
    mySum = 0
    for x in range(1, number):
        if (x % 3 == 0) or (x % 5 == 0):
            mySum += x
        else:
            continue
            break
    print(mySum)
    return

multiplesOf3and5(1000)


# In[ ]:





# In[ ]:




