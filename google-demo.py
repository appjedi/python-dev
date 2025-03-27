# connect to BigQuery https://www.youtube.com/watch?v=lLPdRRy7dfE
# create service account https://www.youtube.com/watch?v=gb0bytUGDnQ
# insert row https://www.youtube.com/watch?v=fmGhBvA5tSo&t=208s
import os
from matplotlib import pyplot as plt
import pymysql
def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='appjedi.net',
        user='appjedin_dba',
        password="$Data2022",
        db='appjedin_student_temp',
    )

    return  conn

def query (sql):
    conn = mysqlconnect()
    cur=conn.cursor()
    cur.execute(sql)
    result=cur.fetchall()
    return result
# CREATE TABLE quizes (quiz_id INT64, time_studied FLOAT64, average_score FLOAT64)


def main():
    orderBy = input("order by")
   # qry=f"call appjedi_store.ups_python_demo ({orderBy})" 
    qry = "SELECT * FROM quizes"
    #qry="SELECT * FROM `turnkey-charter-352313.appjedi_store.quizes` ORDER BY quiz_id"
    result=query(qry)
    
    time_studied = []
    average_scores = []
    quizes = []
    idx=0
    for row in result:
        quizes.append(row[0])
        time_studied.append(row[1])
        average_scores.append(row[2])
        print("Quiz: %2d\tTime Studied: %4.2f\tAverage Score: %4.2f" % (row[0], row[1], row[2]))
        idx=idx+1

    xs = [ i for i, _ in enumerate(quizes)]

    plt.plot( xs, time_studied, 'y--', label='time studied')
    plt.plot( xs, average_scores, 'g:', label='average scores')
    #plt.plot( xs, water, 'b-', label='water')
    plt.legend(loc=6)
    plt.xlabel('Time Studied')
    plt.ylabel('Quiz Scores')
    plt.title('Time Studying vs. Quiz Scores')
    plt.xticks( xs, quizes)  # xs is used for plotting, but this line substitutes months for xs
    plt.show()
    return

def insert_user ():

    table_id = 'appjedi_store.users'

    rows_to_insert = [
        {'username':'python2', 'password':'Test2024', 'role_id':1, 'status':1},
    ]
    client = bigquery.Client()
    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        print('New rows have been added.')
    else:
        print(f'Encountered errors while inserting rows: {errors}')

main()