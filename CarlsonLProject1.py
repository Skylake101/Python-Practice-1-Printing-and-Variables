#This is a basic Python program designed to ask the user question, accept inputs and perform simple calculations.

ADULT_TICKETS = 7.25 #Initial value for tickets
CHILD_TICKETS = 3.75
SENIOR_TICKETS = 4.50
FEES = 0.074
print ("--------------------------------------------------")#4 lines of introduction text
print ("||         Python Ticketing Services	         ||")
print ("--------------------------------------------------")
print ("***ORDER INFORMATION***")

userName = input("Enter your name >> ")
userEmail = input("Enter your Email address: ")
movieChoice = input("What movie would you like to see >> ")
numAdults = int(input("How many adults are in your group? >> "))
numChildren = int(input ("How many children are in your group? >> "))
numSeniors = int(input("How many seniors are in your group? >> "))

print ("\n***ORDER CONFIRMATION***") #Sends back to the user an array of information, including some the user previously provided
print ("Contact Name: " , userName)
print ("Contact email: " , userEmail)
numAll = numAdults + numChildren + numSeniors
print ("You have ordered", numAll, "tickets for", movieChoice)

'''
You probably noticed at this point I start doing something unusual; I switch from using int's in the previous
question to using floats in the next. I do this because floats are necessary to print a price, however I
don't want users to be able to print that they have fractions of a person. i.e. 9.5 adults, 7.2839 children, etc.

Now, rather then allowing them to do this, it will spit out an error message.
'''

One = float (ADULT_TICKETS * numAdults)
Two = float (CHILD_TICKETS * numChildren)
Three = float (SENIOR_TICKETS * numSeniors)

#totalCost = float ((One + Two + Three) / FEES) #This adds the cost, and takes fees off of it
#The total cost is not calculated properly. totalcost = totalcost + totalcost*FEES

totalCost = float ((One + Two + Three) + (One + Two + Three) * FEES)

print ("Your total cost is: $", round(totalCost, 2)) #This displays the final cost, and also rounds it to 2 decimal places

print ("--------------------------------------------------") #Programs finishing message
print ("||              Thanks for using                ||")
print ("||          Python Ticketing Services           ||")
print ("--------------------------------------------------")
