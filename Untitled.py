#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd


# In[76]:


dataset = pd.read_csv("data-analyst-test-data.csv")



# In[77]:


dataset.head()


# In[78]:


dataset['date'] = pd.to_datetime(dataset['date'], format='%Y/%m/%d', errors='coerce')


# In[86]:


positive_keywords = ['impressed', 'excellent', 'nice', 'friendly', 'clean', 'professional', 'spacious', 'comfortable', 'amazing', 'fantastic', 'good']
negative_keywords = ['poor', 'sink', 'tiny', 'small', 'ridiculous', 'dirty', 'rude', 'limited', 'smoking', 'very bad', 'horrible', 'not clean', 'smell', 'needs work', 'no free', 'useless', 'issues', 'bad', 'dirty', 'uncomfortable', 'complaint']


# In[87]:


positive_comments = dataset[dataset['Review'].str.contains('|'.join(positive_keywords), case=False, na=False)]


# In[88]:


negative_comments = dataset[dataset['Review'].str.contains('|'.join(negative_keywords), case=False, na=False)]


# In[89]:


top_positive_comments = positive_comments.sort_values(by='date', ascending=False).head(5)
top_negative_comments = negative_comments.sort_values(by='date', ascending=False).head(5)


# In[90]:


# Print the top positive comments
print("\nTop Positive Comments:")
for index, row in top_positive_comments.iterrows():
    # Extract the date and comment text
    date_str = row['date'].strftime('%Y/%m/%d')
    comment_text = row['Review'].split(',', 1)[-1]
    # Print the formatted comment if both date and comment are valid
    if date_str and comment_text.strip():
        print(f"Date: {date_str}, Comment: {comment_text.strip()}")


# In[92]:


# Print the top negative comments
print("\nTop Negative Comments:")
for index, row in top_negative_comments.iterrows():
    # Extract the date and comment text
    date_str = row['date'].strftime('%Y/%m/%d')
    comment_text = row['Review'].split(',', 1)[-1]
    # Print the formatted comment if both date and comment are valid
    if date_str and comment_text.strip():
        print(f"Date: {date_str}, Comment: {comment_text.strip()}")


# In[ ]:





# In[ ]:





# In[ ]:




