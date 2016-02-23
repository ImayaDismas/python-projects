import pymongo
from bson.objectid import objectid

conncetion = pymongo.Connection()
db = conncetion["tutorial"]
employees = db["employees"]

employees.inser({"name": "Dismas Imaya", 'gender':'m', 'phone':'0700415505', 'age': 22})

cursor = db.employees.find()
for employee in db.employees.find():
	print(employee)