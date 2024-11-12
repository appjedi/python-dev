MONGO_URL="mongodb+srv://appuser:AppData2022@cluster0.aga82.mongodb.net/test"

from pymongo import MongoClient
client = MongoClient(MONGO_URL)

mydatabase = client['test']

users=mydatabase['users']


newUser ={
    'username':'python3',
    'password':'Bite1234',
    'fullname':'Monty Python',
    'email':'python3@example.com',
    'birthday':'2000-01-01',
    'role':2,
    'favorites':[1,2,3]
}
id="67333dc8927931223c606614"
filter = { 'username': 'python3' }
 
# Values to be updated.
newvalues = { "$set": { 'favorites': [1,2,3] } }
#users.update_one(filter, newvalues)
#users.insert_one(newUser)

for user in users.find():
    print(user)
