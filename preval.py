import pandas as pd
import numpy as np
import chardet
import json

# reads original data and prints columns names with more than 50 percent full data
df = pd.read_csv("utdallas_contest_data-1.csv",low_memory=False,index_col="dataright_seq")
counts_raw = df.count().as_matrix()
counts = np.true_divide(counts_raw,df.shape[0])
one_hot = counts
one_hot[one_hot<0.5] = 0

for i in range(len(one_hot)):
	if one_hot[i] !=0:
		print df.columns[i]

df = pd.ExcelFile('dictionary.xlsx',encoding='utf-8')
df = pd.read_excel(df,'demos',index_col='Allant ID')
valid_columns = pd.read_csv('more_than_fifty.txt')
'Homeowner_Renter_90303' in  valid_columns.header.values


category = {}
for index, row in df.iterrows():
	if row['Allant Field Name'] in valid_columns.header.values:
		if row.Category in category:
			category[row.Category].append(row['Allant Field Name'])
		else:
			category[row.Category] = []
			category[row.Category].append(row['Allant Field Name'])

