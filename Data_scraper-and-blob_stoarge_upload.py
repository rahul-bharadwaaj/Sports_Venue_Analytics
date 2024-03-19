#!/usr/bin/env python
# coding: utf-8

# In[45]:


pip install azure-storage-blob


# In[49]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from io import StringIO
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


# In[43]:


url = 'https://en.wikipedia.org/wiki/List_of_sports_venues_by_capacity'


# In[44]:


response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


table = soup.find('table', {'class': 'wikitable'})

# Extract the table header and rows
headers = [header.text.strip() for header in table.find_all('th')]
rows = []
for row in table.find_all('tr'):
    cells = row.find_all(['td', 'th'])
    if len(cells) > 1:  
        rows.append([cell.text.strip() for cell in cells])


df = pd.DataFrame(rows, columns=headers)


# In[46]:


# turn df into csv
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)


# In[47]:


connect_str = 'DefaultEndpointsProtocol=https;AccountName=sportvenuedata;AccountKey=RyAtI+PsfgZx4rfKb7x3hpbmUnrKFGoxUAeyRiAu73CRkHy+d7ELAACXqj3J5GwY7Lke48x+psSe+AStA5DY8Q==;EndpointSuffix=core.windows.net' 
container_name = 'raw-data'
blob_name = 'sports_venues_capacity.csv'


# In[54]:


blob_service_client = BlobServiceClient.from_connection_string(connect_str)
blob_client = blob_service_client.get_blob_client(container = container_name,blob = blob_name)


# In[55]:


csv_buffer.seek(0)
blob_client.upload_blob(csv_buffer.getvalue(), overwrite=True)
print("Data uploaded to Azure Blob Storage")


# In[ ]:




