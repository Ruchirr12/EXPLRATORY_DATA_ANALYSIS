#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[77]:


k=pd.read_csv("wine.csv")


# In[78]:


k


# In[79]:


k.describe().T


# In[81]:


k.shape


# In[84]:


k.isnull().sum()


# In[93]:


k=df.drop(columns="Id")


# In[94]:


k


# In[92]:


df["quality"]=df["quality"].astype("int")


# In[76]:


fig, ax = plt.subplots(ncols=6, nrows=2, figsize=(20,10))
index=0
ax = ax.flatten()
for col, value in k.items():
    sns.distplot(value, ax = ax[index])
    index +=1
plt.tight_layout(pad=0.5, w_pad=0.7, h_pad=5.0)
    


# In[44]:


df.shape


# In[75]:


fig, ax = plt.subplots(ncols=6, nrows=2, figsize=(20,10))
index=0
ax = ax.flatten()
for col, value in k.items():
    sns.barplot(value, ax = ax[index])
    index +=1
plt.tight_layout(pad=0.5, w_pad=0.7, h_pad=5.0)
    


# In[73]:


fig, ax = plt.subplots(ncols=6, nrows=2, figsize=(20,10))
index=0
ax = ax.flatten()
for col, value in k.items():
    sns.lineplot(value, ax = ax[index])
    index +=1
plt.tight_layout(pad=0.5, w_pad=0.7, h_pad=5.0)
    


# In[74]:


fig, ax = plt.subplots(ncols=6, nrows=2, figsize=(20,10))
index=0
ax = ax.flatten()
for col, value in k.items():
    sns.histplot(value, ax = ax[index])
    index +=1
plt.tight_layout(pad=0.5, w_pad=0.7, h_pad=5.0)
    


# In[54]:


fig, ax = plt.subplots(ncols=6, nrows=2, figsize=(20,10))
index=0
ax = ax.flatten()
for col, value in df.items():
    sns.boxplot(value, ax = ax[index])
    index +=1
plt.tight_layout(pad=0.5, w_pad=0.7, h_pad=5.0)
    


# In[56]:


fig, ax = plt.subplots(ncols=6, nrows=2 + 1, figsize=(20,10))
index=0
ax = ax.flatten()
for col, value in df.items():
    sns.barplot(y = df[col], x = df['quality'], data = df, ax = ax[index])
    index +=1
plt.tight_layout(pad=0.5, w_pad=0.7, h_pad=5.0)

    


# In[70]:


fig, ax=plt.subplots(ncols=6, nrows=2, figsize=(20,10))
index=0
ax=ax.flatten()
for col, value in k.items():
    sns.countplot(value, ax=ax[index])
    index+=1
plt.tight_layout(pad=0.5, w_pad=0.7, h_pad=5.0)
    


# In[68]:


k=df.drop(columns='Id')


# In[69]:


k


# In[63]:


df.head()


# In[64]:


df.describe()


# In[ ]:




