#working on days & months
import random #brings in a library with functions such as randint(low,high)

# Introduction to Oregon Trail Game
print("Welcome to " + "Oreogn Trail")

# Functions
# name: update_days
# purpose: uses a while loop to call add_day function
# input: number_of_days
# returns: none
def update_days (number_of_days):
 while(number_of_days > 0):
  add_day()
  #subtract 1 from number_of_days
  number_of_days = number_of_days - 1

# name: add_day
# purpose: updates food, checks for random days to -2 hp
# input: none
# returns: none
def add_day():
  # update food
  global food
  global day1
  global day2
  global hp
  
  #food goes down by 5 each day
  food = food - 5
  # update day and possibly month
  global curr_month
  global curr_day
  global MONTHS_WITH_31_DAYS
  global new_month
  
  #decrease hp 
  if day1 == curr_day or day2 == curr_day:
    # hp goes down by 1 
    hp = hp - 1
    
 #update day and month ( if needed)
#1
  if curr_day == 31 and curr_month in MONTHS_WITH_31_DAYS:
     curr_day = 1 
     curr_month = curr_month + 1
#2 
  elif curr_day == 30:
       curr_day = 1
       curr_month = curr_month + 1
#3 
  else:
    curr_day = curr_day + 1 
#item in list
# name: travel
# purpose: moves you randomly between 30-60 miles and takes 3-7 days (random)
# input:
# returns: miles traveled
def travel():
    global miles_left 
    miles_left = miles_left - random.randint(30,60)
    update_days(random.randint(3,7))
# name: rest
# purpose: increases health 1 level (up to 5 maximum) and takes 2-5 days 
# input: none
# returns: none
def rest():
    global hp
    if hp < 5:
        hp = hp + 1
    else:
       hp = 5
    update_days(random.randint(2,5))
# name: hunt
# purpose: adds 100 lbs of food and takes 2-5 days (random)
# input: none
# returns: none
def hunt():
  global food
  food = food + 100
  update_days(random.randint(2,5))

# name: status
# purpose: lists food, health, distance traveled, and day
# input: none
# returns: nonetravel
def status():
 print("Health: " , hp)
 print("Food: " , food)
 print("Mile traveled: " ,2000 - miles_left)
 print("Today Date:" + str(curr_month) + "/" + str(curr_day))
# name: help
# purpose: lists all the commands
# input: none
# returns: none
def help():
    print("The commands that you can type are: travel , rest , hunt , statue , and quit")

# name: quit
# purpose: end the game
# input: none
# returns: True for game_over
def quit():
  game_over = True
  print("Game is over")

# Variables
hp = 5 
day1 = 4
day2 = 15
food = 500
miles_left = 2000 
curr_day = 1
curr_month = 3
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
game_over = False
user_name = str(input("What is your name?"))

# While Loop for Game
while(game_over == False):
  
  # ask user for a command
  command = str(input("What would you like to do next?"))
  # travel command
  if command == "travel":
     travel()
  # rest command
  elif command == "rest":
      rest()
  # hunt command
  elif command == "hunt":
      hunt()
  elif command == "status":
      status()
  # help command
  elif command == "help":
      help()
  # quit command
  elif command == "quit":
       quit()
  # error message for unrecognizable command
  
  # Game ends if food runs out, days run out, or health runs out
  if  food == 0 or hp == 0 or curr_month == 13:
      print("You Lost. Game Over")
      game_over = True
  if miles_left == 0:
      print("You Win. Game Over")
      game_over = True
  # User wins if they reach Oregon by 12/31
