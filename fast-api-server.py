from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymysql

# Connect to the database

import os
import uvicorn
from pydantic import BaseModel
import time
import datetime

def current_milli_time():
    return round(time.time() * 1000)

def getDateYYYYMMDD():
    return datetime.today().strftime('%Y-%m-%d')

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    user_id: str
    username: str
    password: str
    created: str
    role_id: int
    status:int


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/demo")
async def demo():
    results = await query("SELECT * FROM turnkey-charter-352313.appjedi_store.quizes")

    return results

@app.get("/sp-demo/{orderBy}")
async def demo(orderBy):
    qry=f"call appjedi_store.ups_python_demo ({orderBy})" 
    results = await query(qry)

    return results

@app.get("/api/users")
async def getUsers ():
    results = await query("SELECT * FROM users")
    rows=[]
    for result in results:
        row={
            'userId': result[0],
            'username': result[1],
            'password': result[2],
            'roleId': result[3],
            'status': result[4],
            'created':result[5],
        }

        rows.append(row)
    return rows


async def query (sql, values=None):
    conn=getConn()
    cursor=conn.cursor()

    if values!=None:
        cursor.execute(sql, values)
    else:
        cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return results

def getConn():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password="Jedi2023",
        db='dev',
    )
    return connection

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7001)