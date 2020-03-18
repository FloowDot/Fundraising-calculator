
import csv
#Not blank function goes here

def noLetters (question):
  valid = False
  while not valid:
    response = input(question)
    onlyNumbers = response.isdecimal()
    if onlyNumbers == False:
      continue
    else: 
      return response



#Get user profit goal
profitGoal = noLetters("Please enter the profit goal for your compaign: ")
#Make sure profit goal is a number

print(profitGoal)
