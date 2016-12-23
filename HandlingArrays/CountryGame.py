#!/bin/python3

import random

#This is a country quizz game w/ Database options. Get 100 points before getting 5 incorrect answers to beat the game.

#Establish conditions for special cases
conditions = ["\n","","a","b","c","d","skip","SKIP","Skip","y","Y","Yes","yes","YES","n","N","No","no","NO"]
#Load Questions
questions = [[1,"What is the total population of "],[2,"How extense (km) is the surface of "],[3,"What is the capital of "],[4,"Name one official currency of "],
[5,"Name one official language of "],[6,"What is the location of "]]

#Load incorrect answer bank for 'choose the best answer'
incorrectPop = [7899999, 76899999, 367888, 3453675, 4838487, 5393489]
incorrectSize = [5676787, 667687, 56786, 6676566, 665656, 6646666]

#Define oftenly used functions
		
def f_answer() : # Full Write-in answers
			
	global answer, wrong, points
	while answer in conditions[:2] :
		print("Please answer the question.")
		answer = input("Your answer: ")

	if answer in conditions[6:9] :
		wrong += 1
		print("\nSkipped Question.\nWrongs:",wrong)

	elif answer.lower() in [element.lower() for element in fVar] :
		points += 10
		print("Correct!\nYou have gained 10 points, for a total of",points,"points.")

	else :
		wrong += 1
		if len(fVar) > 1 :
			print("Wrong.\nValid answer(s): ",end="")
			for element in fVar :
				print(element,end=" ")
			print("\nWrongs:",wrong)
		else :
			print("Wrong. The correct answer is:", fVar[0],"\nWrongs:",wrong)

def m_choice() : #Multiple Choice

	global fVar
	n = 97 #In ASCII, 97 is 'a' - we will call n later. Resets n on every function call
	fVar = random.sample(fVar, 3) #Choose three answers at random from incorrect bank
	fVar.append(correct[0])
	random.shuffle(fVar)

	for choices in fVar :
		print(chr(n),") ",choices,sep="")
		n += 1 #Increases n to go from 'a' to 'b' to 'c' and so on...

def final() : # End of game question (return to main menu or quit app?)

	global answer, end, choice
	answer = input("Do you wish to return to the main menu? y/n : ")
	while answer not in conditions[9:] :
		print("Please answer in a 'yes' or 'no' fashion.")
		answer = input("Do you wish to return to the main menu? y/n : ")
	if answer in conditions[9:14] : #This could be eliminated, as well as 'end' variables. It was just easier to cite to each other. 
		end = True
	elif answer in conditions[14:] : 
		end = True
		choice = "Q"

def countryInf() : # Country Information
	print("ID:", country[0][0])
	print("Country:", country[1][0])
	print("Capital:", country[2][0])
	print("Population:", country[3][0])
	print("Extension:", country[4][0])
	print("Continent:", country[5][0])
	print("Languages:", end=" ")
	for languages in country[6] :
		print(languages, end=" ")
	print("\nCurrencies:", end=" ")
	for currencies in country[7] :
		print(currencies, end=" ")
	print("\n------------------")

def editAtribute(lineNum, change) : #Edits Atribute chosen 
    	lines = open('CountryList.txt', 'r').readlines()
    	lines[lineNum] = str(change)+"\n"
    	out = open('CountryList.txt', 'w')
    	out.writelines(lines)
    	out.close()

def lineSearch(ID) : #searches for ID of chosen country
	global lineNum
	with open('CountryList.txt') as myFile :
		for num, line in enumerate(myFile) :
			if ID in line :
				lineNum = num
def addCountry(change) :
	with open("CountryList.txt", "a") as myFile :
		myFile.write(change)
		myFile.write("\n")


choice = "null" #Beacause of downstream logistics, we have defined choice as null (we are pre-defining 'choice' for the upcoming 'while' statement)
while choice.upper() != "Q" : 

	#Reads list from file, needs to be within loop to reload if modified
	with open('CountryList.txt') as f :
		#Skips first line in list file (used as guidence for users)
		next(f)
		#Creates list from text in lines, split enables sublists per line when multiple strings are given
		lst = [line.strip().split(', ') for line in f]
		#Group countries in sub-lists (creates brackets around groups of 8 lines)
		subLst = [lst[n:n+8] for n in range(0, len(lst), 8)]
	
	#Option Menu
	print('''====Menu====
	\rA. Play Game
	\rB. Database
	\rQ. Quit''')
	choice = input("Choose an option: ")

	if choice.upper() == "A" :
		end = False
		points = 0
		wrong = 0
		
		#Game Start Message
		print("\nYour wits will be tested in the subject of Geography.\nGoal: Reach 100 points before accumulating 5 incorrect answers.")

                #Game condition
		while end == False :
			#Question Counter
			counter = 1
			while points < 100 and wrong < 5 :

				#Randomize Questions (Questions organized in sublists of [ID, Question])
				askedQ = random.choice(questions)
				#Randomize Country (Sublist) to be evaluated
				askedC = random.choice(subLst)
                   		#State number of question (increases)             
				print("\nQuestion", counter)
				#Decides question type (written answer vs choose the best answer)
				if askedQ[0] not in range(1,3) :
					#Print Complete Question and Read Input
					answer = input(str(askedQ[1])+str(askedC[1][0])+"?\nYour Answer: ")

					if askedQ[0] == 3 : 
						fVar = askedC[2]
						f_answer()

					elif askedQ[0] == 4 : #Multiple possible answers
						fVar = askedC[7]
						f_answer()

					elif askedQ[0] == 5 : #Multiple possible answers
						fVar = askedC[6]
						f_answer()

					elif askedQ[0] == 6 :
						fVar = askedC[5]
						f_answer()

				else :
					
					#Asks question
					print(askedQ[1],askedC[1][0],"?")
	
					if askedQ[0] == 1 :   #If question was population related
						correct = askedC[3] #Correct answer
						fVar = incorrectPop #Rather than reseting incorrectPop
						m_choice()
		
					elif askedQ[0] == 2 : #If question was extension related
						correct = askedC[4] #Correct answer
						fVar = incorrectSize #Rather than reseting incorrectPop
						m_choice()

	                                #Ask for user answer
					answer = input("Your Answer: ")
					while answer in conditions[:6] :
						if answer in conditions[:2] :
							print("Please answer the question.")
							
						elif answer.lower() in conditions[2:6] :
							print("Please write in the complete answer (e.g. \'Alexandria\')")
						#Ask for answer again
						answer = input("Your Answer: ")

					if answer in conditions[6:9] :
						wrong += 1
						print("\nSkipped Question.\nWrongs:",wrong)

					elif answer.lower() == correct[0].lower() :
						points += 5
						print("Correct!\nYou have gained 5 points, for a total of",points,"points.")

					else :	
						wrong += 1	
						print("Wrong. The correct answer is:", correct[0],"\nWrongs:",wrong)

				#Increase question count
				counter += 1
			if points >= 100 :
				print("\nCongratulations!\nYou have won the game.\n")
				final()
 
			else :
				print("\nGAME OVER\nYou need to study more!\n")
				final()
					
				
	#Database Menu
	elif choice.upper() == "B" :
		while choice.upper() != "Q" :
			print('''***Database***
			\rA. Search Database
			\rB. Edit Database
			\rC. Back
			\rQ. Quit''')
			choice = input("Choose an option: ")
			#Search Menu
			if choice.upper() == "A" :

				while choice.upper() != "Q" :
					print('''***Search Database***
					\rA. All Countries  D. Currencies
					\rB. Continents     E. Back 
					\rC. Languages      Q. Quit''')
					choice = input("Choose an option: ")

					if choice.upper() == "A" : #All countries
						nCountries = 0 #Country counter
						for country in subLst :
							countryInf()
							nCountries += 1
						print("Total of countries in Database:",nCountries,"\n")

					elif choice.upper() == "B" : #Continent Search

						while True :
							print('''***Search by Continent***
							\rYou may see all the countries in the database within a specified 
							\rcontinent. Type in 'back' to go to Database Menu, and 'quit' to\nclose the application''')
							print("Continents in Database:")
							noRep = []
							for country in subLst : #Fills noRep 
								if country[5][0] not in noRep :
									noRep.append(country[5][0])
							for continent in noRep :
								print(continent)

							choice = input("Continent of choice: ")
							
							if choice.lower() == "back" :
								break

							elif choice.lower() == "quit" :
								choice = "Q"
								break 
							else :
								population = 0
								nCountries = 0
								print("\nCountries within",choice,":")
								for country in subLst :
									if choice.lower() in country[5][0].lower() :
										population += int(country[3][0])
										nCountries += 1
										countryInf()

								if nCountries >= 1 :
									print("\n!!!!!!!!!!!!Factoids!!!!!!!!!!!!")
									print("Total number of countries in",choice,"within the database:",nCountries)
									print("Population total in",choice,"estimated from database:",population)
									print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
								else :
									print("There are no countries in the database associated to this continent")				


					elif choice.upper() == "C" : #Language Search
						while True :
							print('''***Search by Language***
							\rYou may see all the countries in the database within that speak 
							\ra particular language. Type in 'back' to go to Database Menu, and\n'quit' to close the application''')
							print("Languages in Database:")
							noRep = []
							for country in subLst :
								for language in country[6] :
									if language not in noRep :
										noRep.append(language)
							for language in noRep :
								print(language)

							choice = input("Language of choice: ")
							
							if choice.lower() == "back" :
								break

							elif choice.lower() == "quit" :
								choice = "Q"
								break 
							else :
								population = 0
								nCountries = 0
								print("\nCountries that speak",choice,":")
								for country in subLst :
									if choice.lower() in [language.lower() for language in country[6]] :
										population += int(country[3][0])
										nCountries += 1
										countryInf()

								if nCountries >= 1 :
									print("\n!!!!!!!!!!!!Factoids!!!!!!!!!!!!")
									print("Total number of countries that speak",choice,"within the database:",nCountries)
									print("Population total that speaks",choice,"estimated from database:",population)
									print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
								else :
									print("There are no countries in the database associated to this language")

					elif choice.upper() == "D" : #Currency Search
						while True :
							print('''***Search by Currency***
							\rYou may see all the countries in the database within that use 
							\ra particular currency. Type in 'back' to go to Database Menu, and\n'quit' to close the application''')
							print("Currencies in Database:")
							noRep = []
							for country in subLst :
								for currency in country[7] :
									if currency not in noRep :
										noRep.append(currency)
							for currency in noRep :
								print(currency)

							choice = input("Currency of choice: ")
							
							if choice.lower() == "back" :
								break

							elif choice.lower() == "quit" :
								choice = "Q"
								break 
							else :
								population = 0
								nCountries = 0
								print("\nCountries that use the",choice,":")
								for country in subLst :

									if choice.lower() in [currency.lower() for currency in country[7]] :
										population += int(country[3][0])
										nCountries += 1
										countryInf()

								if nCountries >= 1 :
									print("\n!!!!!!!!!!!!Factoids!!!!!!!!!!!!")
									print("Total number of countries that use the",choice,"within the database:",nCountries)
									print("Population total that use",choice,"estimated from database:",population)
									print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
								else :
									print("There are no countries in the database associated to this currency")

					elif choice.upper() == "E" : #Back
						break

					elif choice.upper() == "Q" : #Quit
						break

					else :
						print("Please choose one of the options listed")
			
			#Edit Database Menu		
			elif choice.upper() == "B" :

				while choice.upper() != "Q" :

					print('''***Edit Database***
					\rA. Modify Country Atributes
					\rB. Add Country
					\rC. Remove Country
					\rD. Back
					\rQ. Quit''')
					choice = input("Choose an option: ")

					if choice.upper() == "A" : #Modify

						print("\nEDIT MODE\nCountries available in Database (ID | Country):")
						for country in subLst :
							print(country[0][0], end = " | ")
							print(country[1][0])

						while choice.upper() != "Q" :
							print("Type in 'back' to return to previous menu or 'quit' to quit") 
							ID = input("Choose a country (use ID): ")
							if ID.lower() == "back" :
								break

							elif ID.lower() == "quit" :
								choice = "Q"
								break 
							
							else :
								lineSearch(ID)
								inside = [ID in element for element in lst[0::8]] #Stores boolean True or False
								if ID.isdigit() and True in inside :

									while choice.upper() != "Q" :

										print('''\nWhat attribute do you wish to edit?
										\rA. ID          F. Continent 
										\rB. Country     G. Languages
										\rC. Capital     H. Currencies
										\rD. Population  I. Back
										\rE. Extension   Q. Quit''')
										choice = input("Choose an attribute: ")

										if choice.upper() == "A" :
											while True :
												
												change = input("New ID: ")
												if change.isnumeric() :
													print("\nAttribute has been succesfully changed.")
													editAtribute(lineNum,change)	
													break
												else :
													print("Please choose an interger for ID")
										
										elif choice.upper() == "B" :
											while True :
												for country in subLst :
													if ID in country[0] :
														pattern = country[1][0]
												lineSearch(pattern)
												change = input("New Country: ")
												print("\nAttribute has been succesfully changed.")
												editAtribute(lineNum,change)	
												break
												
										elif choice.upper() == "C" :
											while True :
												for country in subLst :
													if ID in country[0] :
														pattern = country[2][0]
												lineSearch(pattern)
												change = input("New Capital: ")
												print("\nAttribute has been succesfully changed.")
												editAtribute(lineNum,change)	
												break

										elif choice.upper() == "D" :
											while True :
												for country in subLst :
													if ID in country[0] :
														pattern = country[3][0]
												lineSearch(pattern)
												change = input("New Population: ")
												print("\nAttribute has been succesfully changed.")
												editAtribute(lineNum,change)	
												break

										elif choice.upper() == "E" :
											while True :
												for country in subLst :
													if ID in country[0] :
														pattern = country[4][0]
												lineSearch(pattern)
												change = input("New Extension: ")
												print("\nAttribute has been succesfully changed.")
												editAtribute(lineNum,change)	
												break

										elif choice.upper() == "F" :
											while True :
												for country in subLst :
													if ID in country[0] :
														pattern = country[5][0]
												lineSearch(pattern)
												change = input("New Continent: ")
												print("\nAttribute has been succesfully changed.")
												editAtribute(lineNum,change)	
												break

										elif choice.upper() == "G" :
											while True :
												for country in subLst :
													if ID in country[0] :
														pattern = country[6][0]
												lineSearch(pattern)
												change = input("New Languages: ")
												print("\nAttribute has been succesfully changed.")
												editAtribute(lineNum,change)	
												break

										elif choice.upper() == "H" :
											while True :
												for country in subLst :
													if ID in country[0] :
														pattern = country[7][0]
												lineSearch(pattern)
												change = input("New Currencies: ")
												print("\nAttribute has been succesfully changed.")
												editAtribute(lineNum,change)	
												break

										elif choice.upper() == "I" :
											break
										
										elif choice.upper() == "Q" :
											break


								elif ID.isnumeric() and False in inside :
									print("ID is missing from file")
								else :
									print("Please use ID")	
					
					#Add Country					
					elif choice.upper() == "B" :
						while True :
							print("\nADDING NEW COUNTRY")
							ID = input("ID: ")
							lineSearch(ID)
							inside = [ID in element for element in lst[0::8]] #Inside ID sublists
							if ID.isdigit() and False in inside :
								addCountry(ID)
								added = input("Country: ")
								inside = [added in element for element in lst[1::8]] #Inside country name sublists

								if True in inside :

									#Delete added ID and break
									print("Country already exists in file") 
									with open("CountryList.txt", "r") as myFile :
										lines = myFile.readlines()
										lines = lines[:-1]

									with open("CountryList.txt", "w") as myFile :
										myFile.writelines(lines)

									break
									
								else :

									addCountry(added)
									added = input("Capital: ")
									addCountry(added)
									added = input("Population: ")
									addCountry(added)
									added = input("Extension: ")
									addCountry(added)
									added = input("Continent: ")
									addCountry(added)
									added = input("Languages: ")
									addCountry(added)
									added = input("Currencies: ")
									addCountry(added)
									print("\nNew country added succesfully")
									break
								
							elif ID.isdigit() and True in inside :
								print("ID already exists in file")
								break
							else :
								print("Please use an interger for ID")	
								
					#Remove country
					elif choice.upper() == "C" :
						print("\nREMOVING COUNTRY")
						print("List of countries in Database: ")
						for country in subLst :
							print(country[0][0], end = " | ")
							print(country[1][0])
						while True :
							ID = input("Choose country to remove (use ID): ")
							lineSearch(ID)
							inside = [ID in element for element in lst[0::8]]

							if ID.isdigit() and True in inside :
								lineSearch(ID) #Will give us line number where ID is located at
								with open("CountryList.txt", "r") as myFile :
									lines = myFile.readlines()
									del lines[lineNum:lineNum+8] #delete this range

									with open("CountryList.txt", "w") as myFile :
										myFile.writelines(lines)
								break
					
							elif ID.isdigit() and False in inside :
								print("ID not present in database")

							else :
								print("Please use an interger for ID")

					#Back
					elif choice.upper() == "D" :
						break
					#Quit
					elif choice.upper() == "Q" :
						break
									
							
							
			#Back to main menu
			elif choice.upper() == "C" : 
				break
			#Quit
			elif choice.upper() == "Q" : 
				break
			else :
				print("Please choose one of the options listed")
	#Quit					
	elif choice.upper() == "Q" :
		break
	else :
		print("Please choose one of the options listed")
