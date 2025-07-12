import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NYC', 'LA', 'Chicago', 'Houston'],
    'Salary': [70000, 80000, 90000, 100000]
}

df = pd.DataFrame(data)

#print(df['Name'])
#print(df[['Name', 'Salary']])
#print(df.loc[2]) # Row for Charlie

print(df[df['Age'] > 30])
