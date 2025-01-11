# importing csv module
import csv
import pymysql

# csv file name
def importFile (filenames):
# initializing the titles and rows list
	fields = []
	rows = []

    # name of the csv file
	# reading csv file
	with open(filename, 'r',encoding='unicode_escape') as csvfile:
		# creating a csv reader object
		csvreader = csv.reader(csvfile)
		
		# extracting field names through first row
		fields = next(csvreader)

		# extracting each data row one by one
		for row in csvreader:
			rows.append(row)

		# get total number of rows
		print("Total no. of rows: %d"%(csvreader.line_num))

	# printing the field names
	print('Field names are:' + ', '.join(field for field in fields))
	insert = "INSERT INTO zipcodes(`AREA_NAME`,`AREA_CODE`,`DISTRICT_NAME`,`DISTRICT_NO`,`DELIVERY_ZIPCODE`,`LOCALE_NAME`,`PHYSICAL_DELV_ADDR`,`PHYSICAL_CITY`,`PHYSICAL_STATE`,`PHYSICAL_ZIP`,`PHYSICAL_ZIP_4`)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

	# printing first 5 rows
	print('\nFirst 5 rows are:\n')
	ct=0
	for row in rows:
		# parsing each column of a row
		values=[]
		for col in row:
			values.append(col)

		print(values,'\n')
		if len(values)>0:
			query(insert, values)
			ct+=1

	print ("ct: %d"%(ct))

def getConn():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password="Jedi2023",
        db='appjedin_student_temp',
    )
    return connection
def query (sql, values=None):
    conn=getConn()
    cursor=conn.cursor()

    if values!=None:
        cursor.execute(sql, values)
    else:
        cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.commit()
    print(results)
    return results
filename = "/Users/roberttimlin/Documents/zipcodes.csv"
importFile(filename)