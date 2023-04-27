
# coding: utf-8

# # 一、使用sndHsPr

# In[44]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import os
#get_ipython().magic('matplotlib inline')


# In[47]:
os.chdir(r'D:\demo')
snd = pd.read_csv("sndHsPr.csv")




# In[22]:

#pd.crosstab(snd.district,snd.school).plot(kind = 'bar'

# In[38]:
#标准化的堆叠柱形图
sub_sch = pd.crosstab(snd.dist,snd.school)
sub_sch = sub_sch.div(sub_sch.sum(1),axis = 0)
sub_sch[[0,1]].plot(kind = 'bar',stacked= True)

# In[29]:

# In[30]:


#%%
#考虑样本占比的标准化的堆叠柱形图
from stack2dim import *

stack2dim(snd, i="dist", j="school")
#%%
