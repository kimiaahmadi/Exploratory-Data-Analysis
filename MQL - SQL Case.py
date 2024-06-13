#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

raw_data = pd.read_csv('downloads/MQL-SQL Raw data.csv')
raw_data.head()


# ### Question 1: What is the overall MQL to SQL conversion rate by week (assume weeks start on mondays and end on sundays)?

# In[10]:


raw_data['MQL Created Date'] = pd.to_datetime(raw_data['MQL Created Date'])


raw_data['Week'] = raw_data['MQL Created Date'].dt.to_period('W').apply(lambda r: r.start_time)

weekly_data = raw_data.groupby('Week').agg(
    MQLs=('Client Status', 'count'),
    SQLs=('Client Status', lambda x: (x == 'SQL').sum())
)

weekly_data['Conversion Rate'] = (weekly_data['SQLs'] / weekly_data['MQLs']) * 100


weekly_data.reset_index(inplace=True)


print(weekly_data)


# ### Question 2: How has the overall MQL conversion rate changed over time?

# As seen in the table above, the overall MQL conversion rate decreased over time

# ### Question 3: What is the main reason that the overall MQL conversion rate changed so drastically from week 1 to week 4?

# In[11]:


weekly_data_summary = raw_data.groupby('Week').agg(
    MQLs=('Client Status', 'count'),
    SQLs=('Client Status', lambda x: (x == 'SQL').sum()),
    Email=('Source', lambda x: (x == 'Email').sum()),
    Web=('Source', lambda x: (x == 'Web').sum()),
    Other=('Source', lambda x: (x.isin(['Email', 'Web']) == False).sum())
)

weekly_data_summary['Conversion Rate'] = (weekly_data_summary['SQLs'] / weekly_data_summary['MQLs']) * 100
weekly_data_summary.reset_index(inplace=True)


print(weekly_data_summary)


# The table above illustrates the significant increase in MQLs from "Other" sources, particularly in the 3rd and 4th week. These leads could have been more broad/difficult to convert, therefore negatively affecting the conversion rate 

# In[ ]:




