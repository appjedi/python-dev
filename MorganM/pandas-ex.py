import pandas as pd

df = pd.read_csv('testfile.csv')
#print(df.head())


for index, row in df.iterrows():
	# Access data using row['column_name'] or row[column_index]
	print(f"Index: {index}")
	print(f"Column A: {row[0]}, Column B: {row[1]}")
