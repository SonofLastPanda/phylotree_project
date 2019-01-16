
# coding: utf-8

# In[14]:


import pandas as pd
from scipy import stats
import numpy as np


# In[18]:


data = pd.read_csv('s.csv', sep='\t')


# In[19]:


data


# In[31]:


data[data["subtree"]==1]['Distance'].mean()
    


# In[32]:


data[data["subtree"]==2]['Distance'].mean()


# In[33]:


sub1 = data[data['subtree'] == 1]['Distance']
sub2 = data[data['subtree'] == 2]['Distance']
stats.ttest_ind(sub1, sub2)   

