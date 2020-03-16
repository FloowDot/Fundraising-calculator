
#Not blank function goes here
def noAlpha(question):
  while True:
    response = input(question)
    for letter in response:
      if letter.isalpha():
        continue
      else:
        if response == "":
          continue
        else:
          return response

hasErrors = False

#Get user profit goal
profitGoal = noAlpha("Please enter the profit goal for your compaign: ")
#Make sure profit goal is a number


