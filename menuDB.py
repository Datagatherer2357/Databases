# g00364693 - Gareth Duffy - Applied Databases Project
# pymysql functions for Python menu (Options 1,2,3,6,7)

import pymysql
import pandas as pd
from pandas import DataFrame
import menu
from pandas import ExcelWriter

#Q1 - Show the first 15 cities:

def show_cities():
	db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "world", cursorclass = pymysql.cursors.DictCursor)
	
	sql = 	"""select * 
			from city
			limit 15;
			"""
	with db:
		cursor = db.cursor()
		cursor.execute(sql)
		cities = cursor.fetchall()
		for c in cities:
			print(c["ID"],"|", c["Name"], "|", c["CountryCode"], "|", c["District"], "|", c["Population"])
		
		
# Q2 - Show city populations:

def showpop_cities(o, p):
	db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "world", cursorclass = pymysql.cursors.DictCursor)
	
	query = "SELECT * FROM city WHERE Population " + o + " %s";
	

	with db:
		cursor = db.cursor()
		cursor.execute(query, (p))
		cities = cursor.fetchall()
		#print(cities)
		for c in cities:
			print(c["ID"],"|", c["Name"], "|", c["CountryCode"], "|", c["District"], "|", c["Population"])
			

# Q3 - Add a new city:

def add_city(n, cc, d, p):
	db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "world", cursorclass = pymysql.cursors.DictCursor)
	
	sql = "INSERT INTO city (Name, CountryCode, District, Population) Values (%s, %s, %s, %s);"
	
	with db:
		cursor = db.cursor()
		x = cursor.execute(sql, (n, cc, d, p))
		print(x)
		


# Q6 - View Countries by Name:

local_data_loaded = False
		
def Country_name(cn):
	db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "world", cursorclass = pymysql.cursors.DictCursor)
	global local_data_loaded
	global df
	
	sql = """select * from country where Name like %s""".format(cn)
	
	if(local_data_loaded == True):
		
		df = df[['Name', 'Continent', 'Population', 'HeadOfState']] # Filtering column selection
		column_list = [df.columns.values.tolist()] + df.values.tolist() # Convert the DataFrame into a list/array
		f = '{:<45}|{:<15}|{:<15}|{:<8}' # Formatting the layout

		for i in column_list: # Loop to format a tabular structure instead of array structure
			print(f.format(*i))
		
		print("")
		print("Queries are now applied only to the locally stored dataframe above...")
		print("")
		print("The result of you local query result is outputted below...")
		print("")
		print(df[df['Name'].str.contains(cn)==True]) # Command that queries the locally stored data
		print("")
		print("Why not try another query?!")
		print("")
		while True:
			choice = input("Or would you like to save your data to Excel?...Please type y or n:")
			if (choice == "y"): 
				print("")
				print("Saving to Excel!...")
				writer = ExcelWriter('Choice_6_output.xlsx')
				df.to_excel(writer,'Choice_6_output')
				writer.save()
				menu.main()
				
			elif(choice == "n"):
				print("")
				print("Returning to main menu...")
				menu.main()
			False
	
	else:
		with db:
			cursor = db.cursor()
			cursor.execute(sql, ('%' + cn + '%',))
			countries = cursor.fetchall()

			for c in countries:
				print(c["Name"],"|", c["Continent"], "|", c["Population"], "|", c["HeadOfState"])

				if(local_data_loaded == False):
						df=pd.DataFrame(countries)
						local_data_loaded=True
						print("")
						print("Saving output query data locally...")
						print("")

	
# Q7 - View Countries by population:

local_data_load = False

def showpop_countries(op,pop):
	db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "world", cursorclass = pymysql.cursors.DictCursor)
	global local_data_load
	global df
	
	query = "SELECT * FROM country WHERE Population " + op + " %s"; 
	
	if(local_data_load == True):
		
		df = df[['Code', 'Name', 'Continent', 'Population']] # Filtering column selection
		column_list = [df.columns.values.tolist()] + df.values.tolist() # Convert the DataFrame into a list/array
		f = '{:<8}|{:<45}|{:<15}|{:<8}' # Formatting the layout

		for i in column_list: # Loop to format a tabular structure instead of array structure
			print(f.format(*i))
		
		print("")
		print("Queries will now be applied to the locally stored data above...")
		print("")
		print("The result of you local query result is outputted below...")
		print("")
			
		# Control flow for filtering local queries, fully formatted:
		if(op =="<"): # For less than queries 
			print(df[df['Population'] <= pop], f.format)

		elif(op ==">"): # For greater than queries
			print(df[df['Population'] >= pop], f.format)
			
		else:
			print(df[df['Population'] == pop], f.format) # For equal to queries
		print("")
		print("Why not try another query?!")
		print("")
		while True:
			choice = input("Or would you like to save your data to Excel?...Please type y or n:")
			if (choice == "y"): 
				print("")
				print("Saving to Excel!...")
				writer = ExcelWriter('Choice_7_output.xlsx')
				df.to_excel(writer,'Choice_7_output')
				writer.save()
				menu.main()
				
			elif(choice == "n"):
				print("")
				print("Returning to main menu...")
				menu.main()
			False
		
	else:
		with db:
			cursor = db.cursor()
			cursor.execute(query, (pop))
			countries = cursor.fetchall()
			for c in countries:
				print(c["Code"],"|", c["Name"], "|", c["Continent"], "|", c["Population"]) 
					
				if(local_data_load == False):
					df=pd.DataFrame(countries)
					local_data_load=True
					print("")
					print("Saving output query data locally...")
					print("")
					
	  
# INNOVATION (Hidden menu):

# Option A:

def pop_per_cont():
	db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "world", cursorclass = pymysql.cursors.DictCursor)
	
	sql = 	"""SELECT continent, name, population as "Population of most populated country"
		FROM country
		WHERE population 
		IN (SELECT MAX(population) FROM country group BY continent)
		ORDER BY population 
		DESC
		LIMIT 7; """
	
	with db:
		cursor = db.cursor()
		cursor.execute(sql)
		country = cursor.fetchall()
		for c in country:
			print(c)

#Option B:	
		
def minpop_youngestper():
	db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "world", cursorclass = pymysql.cursors.DictCursor)
	
	sql = """ 	select p.personname, p.age, ci.name, min(ci.population)
				from person p 
				inner join hasvisitedcity hvc
				on p.personID = hvc.personID
				inner join city ci
				on hvc.cityID = ci.ID
				where p.age = (select min(p.age) from person p); """
	
	with db:
		cursor = db.cursor()
		cursor.execute(sql)
		person = cursor.fetchall()
		for p in person:
			print(p)

# Option C:

def count_indep():
	db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "world", cursorclass = pymysql.cursors.DictCursor)
	
	sql =   """ Select Name, IndepYear, 
				IF(IndepYear is NULL, 'n/a', 
				IF(IndepYear between 2010 and 2019, CONCAT("New ",GovernmentForm), 
				IF(IndepYear between 1970 and 2009, CONCAT("Modern ",GovernmentForm), 
				IF(IndepYear between 1919 and 1969, CONCAT("Early ",GovernmentForm),
				IF(IndepYear <= 1918, CONCAT("Old ",GovernmentForm),GovernmentForm)))))
				as `Desc`
				from country
				Union
				Select Name, IndepYear, 
				IF(Population >= 100000000, CONCAT("Large ",GovernmentForm),GovernmentForm)
				as `Desc`
				from country; """

	with db:
		cursor = db.cursor()
		cursor.execute(sql)
		indep = cursor.fetchall()
		for i in indep:
			print(i["Name"],"|", i["IndepYear"],"|",i["Desc"])
			
# Option E:

# A little program that demonstrates the Collatz Cnjecture sequence

def collatz():
	x = int(input("Please enter a number to demonstrate the Collatz sequence:"))

	while x >= 1:  #  Specified starting value of 1 or higher.
		if x % 2 == 0:  # if loop that divides by 2 if number is even, and returns result.
			x = x / 2
			print (int(x))
		else:  # # else loop that multiplies by 3 if number is odd, and returns result.
			x = (x * 3) + 1
			print (int(x))
		if x == 1:  # if statement that terminates loop once the integer 1 is reached. 
			break
			
		
# Option F:

def onemillion():
	db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "world", cursorclass = pymysql.cursors.DictCursor)
	
	sql =   """ Select Name, Population 
				From city
				Where Population >= 1000000; """

	with db:
		cursor = db.cursor()
		cursor.execute(sql)
		mill = cursor.fetchall()
		for m in mill:
			print(m["Name"],"|", m["Population"])
	

					