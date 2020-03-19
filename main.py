import csv
#Not blank function goes here
#make sure the variables that need to be numbers dont have letters
def noLetters (question):
  valid = False
  while not valid:
    response = input(question)
    onlyNumbers = response.isdecimal()
    if onlyNumbers == False:
      continue
    else: 
      return response

def noNumbers (question):
  valid = False
  response = input(question)
  for letter in response:
    if letter.isdigit() == True:
      hasLetter == True

#Get name of campaign

#Get user profit goal
profitGoal = noLetters("Please enter the profit goal for your campaign: ")
#Make sure profit goal is a number

print(profitGoal)

#Create a list of the products
productList = []
valid = False
while not valid:
  product = input("Enter product name, enter  xx to finish list:")
  productList.append(product)
  if product == "xx":
    productList.pop()
    print("Heres your list: \n", productList)
    break