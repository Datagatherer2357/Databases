# g00364693 - Gareth Duffy - Applied Databases Project
# pymongo functions for Python menu (Options 4 & 5)

import pymongo
import menu

myclient = None 

def connect():
	global myclient
	print("In connect()")

	myclient = pymongo.MongoClient()
	myclient.admin.command('ismaster')
	
# Q4 - MongoDB - Find car by Engine Size:
					
def find_engine():
	print("Connecting...")
	if (not myclient):
		try:
			connect()
			find_engine()
			
		except Exception as e:
			print("Error", e)
	db = myclient["appdb"]
	col = db["project"]
	
	engine = float(input("Engine Size:"))
	
	query = {"car.engineSize": engine}
	docs = col.find(query)
	for d in docs:
		print(d["_id"],"|",d["car"]["reg"],"|",d["car"]["engineSize"],"|",d["addresses"])
		menu.main()

	
# Q5 - MongoDB - Add New Car:
				
def add_newcar():
	print("Connecting...")
	if (not myclient):
		try:
			connect()
			add_newcar()
						
		except Exception as e:
			print("Error", e)
	db = myclient["appdb"]
	col = db["project"]
	
	id = input("Enter ID:")
	regi = input("Enter Reg:")
	engsize = input("Engine Size:")
		
	newdoc = [{"_id":id, "car":{"reg":regi, "engineSize":engsize}}]
	
	try:
		col.insert_many(newdoc, ordered =	False) # False:all inserts attempted
	
	except pymongo.errors.BulkWriteError as e:
		print("Error inserting document")
	except Exception as e:
		print("Error", e)
				
			
