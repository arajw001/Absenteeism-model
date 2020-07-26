#!/usr/bin/env python
# coding: utf-8

# In[7]:


from absenteeism_module import *


# In[8]:


model= absenteeism_model('model','scalar')


# In[9]:


model.load_and_clean_data('Absenteeism_new_data.csv')


# In[10]:


model.predicted_outputs()


# In[ ]:




