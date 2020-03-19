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



#Get user profit goal
profitGoal = noLetters("Please enter the profit goal for your campaign: ")
#Make sure profit goal is a number

print(profitGoal)

productList = []
valid = False
while not valid:
  product = input("Enter product name, enter  xx to finish list:")
  productList.append(product)
  if product == "xx":
    print("Heres your list: ", productList)
    break