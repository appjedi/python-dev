import pandas as pd

excel_file = 'excel-test.xlsx'
csv_file = 'books.csv'

df = pd.read_excel(excel_file)
dff = pd.read_csv(csv_file)
