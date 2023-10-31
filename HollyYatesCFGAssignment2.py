#Scenario:
#Creating a program that interacts with the HarryPotter api that contains a list of all students
#at Hogwarts in the Harry Potter Book series, with their information (such as school house, age, their wand, etc).
#From this api I am taking the names and corresponding school house of each student out of this list of information
#and storing this into a file, in a readable format.
#The program also asks the user to choose a house and then counts how many students are in that house
#and runs a message at the end to display this output clearly.
#The program also asks the user to enter a Character's name to see if they attended Hogwarts in the books.
#If the character did attend, it prints a message to inform the user of this. If the character name the user entered
#did not attend Hogwarts, a message is printed to inform them of this too.
#This API does not require any keys to be set up.

#-------Importing Module and using API--------#
import requests      #Importing the necessary module to make requests to an API.
from pprint import pprint #Importing pprint module to pretty-print data into a more readable format.
apiurl= 'https://hp-api.onrender.com/api/characters/students' #Creating a variable to store the Harry Potter API in.
theresponse = requests.get(apiurl) #Making a call to the above API and storing it in the variable 'theresponse'
students = theresponse.json() #Getting the data from the API to convert it into JSON strings
##pprint(students)

#---------- Creating a file & using a for loop --------------#
with open("Hogwarts_students.txt", "w") as thefile:   #Creating a file to store the API data in
    thefile.write("🧙Students attending Hogwarts in the Harry Potter Series and Their Houses🧙‍:" + "\n") #Using .write() to Create a title for the txt file.
    for item in students: #Using a for loop to loop through the API data and pull out and save the relevant data to the txt file in a clear readable format.
        thefile.write("The character" + " " + item['name'] + " " + "is in the hogwarts house" + " " + item['house'] +'\n')
#Using "\n" to create a new line to display the data more clearly in the text file.


#------- Creating functions -----------#
#I am creating a function to count how many students are in a user- chosen hogwarts house.
house = input("Enter a Hogwarts House, your choices are: Gryffindor, Hufflepuff, Ravenclaw or Slytherin ").title()
#Asking for user input for a house and storing it in the variable "house".
#I am using the .title() in-built python method to ensure that regardless of user input, the capitalisation matches that in the txt file to be counted.

#Creating the function to count how many students in each house by creating a word counter (however many times a house appears in the file is how many students are in it).
def houseselection():
    data = file.read()
    words = data.split()
    words_count = words.count(house) #Using the variable "house" to state which word (or in this case which hogwarts house) to count.
    return "There are {} students in {}".format(words_count, house)

#Calling the function to use for the txt file:
with open('Hogwarts_students.txt', 'r') as file:
    housetotal = houseselection()
    print(housetotal)

#--------------- Using if....else statements ------------ #
#I am creating a function to enable the user to enter a character's name to see if they attended hogwarts.
#I am using an if...else statement to branch logic in the program to print different answers depending on if the name entered is a Hogwarts student or not.
#I am using .title() again to ensure user input matches the text in the file from the API.
Name_search = input("Enter a character's first name to see if they are student at Hogwarts in the series:").title()
def charactername():
    info = file.read()
    names = info.split()
    names_count = names.count(Name_search)
    if names_count >=1: #If the name appears less than once in the count then the character name is not a student at Hogwarts, as the file is a list of students at hogwarts from the API.
        print("{} attends Hogwarts in the Harry Potter Book series!".format(Name_search))
    else:
        print("{} is not a student at Hogwarts in the Harry Potter series".format(Name_search) + "\n" " - Which means your character was a teacher,"
              "relative, member of staff or attended another wizarding school in the Harry Potter series!".format(
            Name_search) + "\n" + "Alternatively the name you entered isn't a character in the books 😉!")

#Calling the function to use it for the file:
with open("Hogwarts_students.txt", 'r') as file:
    charactername()

#------------- Using a list to store data (the professors in the HP book series) and returning a boolean value based on whether or not 'profs' value appears
#in the list proffessors --------------------#
profs = input("Enter the surname of a professor in the Harry Potter Books: ").title()
professors = ["Hagrid", "Dumbledoor", "Snape", "Lupin", "Mcgonagall", "Spore","Everand", "Fortescue", "Derwent", "Nigellus-Black", "Dippet", "Vector", "Sinistra", "Kettleburn", "Grubblyplank", "Flitwick", "Carrow", "Merrythought", "Quirrell", "Lockheart", "Crouch", "Umbridge", "Trelawney", "Firenze", "Hooch", "Sprout", "Binns",
              'Burbage', "Slughorn", "Babbling"]
check = profs in professors
print("{} is a professor at Hogwarts:".format(profs), check)
#This will run the 'profs' variable against the stored list elements, and will produce a boolean value depending on if the name is in the 'professors' list data structure or not.
#If the 'profs' variable is in the 'professors' list, the return will be 'True'. If it is not, the return will be False.


#---------------Using 2 in-built functions for assignment requirements-------------#:
#Here I am using the two in built functions len() and print().
#len() is returning the number of characters in the apiurl string we set up earlier.
#print() is displaying the output of len() which I have stored in the variable "inbuiltfunctionexample".
inbuiltfunctionexample = len(apiurl)
print(inbuiltfunctionexample)

#----------importing additional module for assignment requirements---------#
import datetime #Importing datetime module.
currenttime = datetime.datetime.now() #Storing this in a variable
print(currenttime.strftime("Today is %A, and the current time is: %H:%M"))
#Using datetime character codes to print the current date and time when accessed.


#------------------Using string slicing for assignment requirements--------------------#
with open("Hogwarts_students.txt")as doc:
    string = doc.readlines() #Using readlines() to pull out data from the API stored in the file.
    print(string[1:4]) #Using string slicing to display the first three lines of the text file (by using indexes 1:4 it will not print the title or the fourth line).