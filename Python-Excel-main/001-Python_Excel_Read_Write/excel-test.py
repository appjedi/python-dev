import pandas as pd
# **Video Tutorial: ** https: // youtu.be/bI68wnoINwc

# **Difficulty:** Beginner

# **Tags/Keywords:** Python, Excel, Pandas

# Code Examples

# ex1.0.1 DataFrame Creation

excel_file = 'excel-test.xlsx'
df = pd.read_excel(excel_file)

for index, row in df.iterrows():
    print(row['Name'], row['Email'])

# print(df['Name'].loc[df.index[0]])

# print(df["A1"])
