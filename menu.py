# g00364693 - Gareth Duffy - Applied Databases Project
# Python menu for interacting with MySQL and MongoDB

import menuDB
import mongomenuDB

def main():
	display_menu()
	
	while True:
			choice = input("Enter choice:")
			
			# Choice 1:
			if (choice == "1"): 
				print("Choice: 1")
				menuDB.show_cities()
				display_menu()
				
			# Choice 2:
			elif (choice == "2"):
				print("Choice: 2")
				print("Cities By Population")
				print("--------------------")
				oper = input("Enter < > or =:")
				pop = int(input("Enter population:"))
				try:
					menuDB.showpop_cities(oper, pop)
				except Exception as e:
					print(e)
				display_menu()
			
			# Choice 3:
			elif (choice == "3"):
				print("Choice: 3")
				print("Add New City")
				print("------------")
				name = input("Enter city name:")
				code = input("Country Code:")
				dist = input("District:")
				popul = int(input("Population:"))
				try:
					menuDB.add_city(name, code, dist, popul)
				except Exception as e:
					print("*** ERROR ***: CountryCode", code, "does not exist")
				display_menu()
			
			# Choice 4:
			elif (choice == "4"):
				print("Choice: 4")
				print("Show Cars by Engine Size")
				print("------------------------")
				
				try:
					mongomenuDB.find_engine()
					main()
				except Exception as e:
					print(e)
				
			
			# Choice 5:
			elif (choice == "5"):
				print("Choice: 5")
				print("Add New Car")
				print("-----------")
				
				try:
					mongomenuDB.add_newcar()
					main()
				except Exception as e:
					print(e)
			
			
			# Choice 6:
			elif (choice == "6"):
				print("Choice: 6")
				print("Countries by Name")
				print("-----------------")
				
				countryname = input("Enter Country Name:")
				try:
					menuDB.Country_name(countryname)
				except Exception as e:
					print(e)
				display_menu()
				
			# Choice 7:
			elif (choice == "7"):
				print("Choice: 7")
				print("Countries by Pop")
				print("----------------")
				opera = input("Enter < > or =:")
				popul = int(input("Enter population:"))
				try:
					menuDB.showpop_countries(opera, popul)
					display_menu()	
				
				except Exception as e:
					print(e)
				
			
			# Choice x:
			elif (choice == "x"): # Exit Application
				print("Choice: Exiting the menu...")
				return 
			
			# Hidden choice (INNOVATION):
			elif (choice == "h"):
				try: 
					secret()
				except Exception as e:
					print(e)
			# Anything else:
			else: 
				display_menu()
				

# Main menu display:
def display_menu():
	print("")
	print("World DB")
	print("--------")
	print("")
	print("MENU")
	print("----")
	print("1 - View 15 Cities")
	print("2 - View Cities by population")
	print("3 - Add New City")
	print("4 - Find Car by Engine Size")
	print("5 - Add New Car")
	print("6 - View Countries by name")
	print("7 - View Countries by population")
	print("x - Exit application")
	print("Choice:")
	
	
# Hidden menu display: (To access menu you must press the 'h' key)
def hidden_menu():
	print("")
	print("HIDDEN MENU")
	print("-----------")
	print("a - Country with biggest population per continent")
	print("b - Minimum city population of youngest person(s)")
	print("c - Country Independence")
	print("d - Return to the main menu")
	print("e - Pick a number for fun...")
	print("f - Cities with over a million people")
	print("x - Exit application")
	
	
def secret():
	hidden_menu()
	
	while True:
			option = input("Enter option:")	
			
			# Option A:
			if (option == "a"): 
				print("Option: a")
				menuDB.pop_per_cont()
				hidden_menu()
			
			# Option B:
			elif (option == "b"): 
				print("Option: b")
				menuDB.minpop_youngestper()
				hidden_menu()
			
			# Option C:
			elif (option == "c"): 
				print("Option: c")
				menuDB.count_indep()
				hidden_menu()
			
			# Option D:				
			elif (option == "d"): 
				print("Option: d")
				main()
			
			# Option E:				
			elif (option == "e"): 
				print("Option: e")
				menuDB.collatz()
				hidden_menu()
				
			# Option F:
			elif (option == "f"): 
				print("Option: f")
				menuDB.onemillion()
				hidden_menu()
						
			# Option x:
			elif (option == "x"): # Exit Application
				print("Choice: Exiting the menu...")
				return 
				
			# Anything else:
			else: 
				hidden_menu()
				
# Execute only if run as a script:
if __name__ == "__main__":
	 main()
	 
