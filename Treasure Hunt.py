print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
sel1=input("You're on a road with 2 ways you can go, select to go 'left' or 'right'?\n")
sel1.lower()
if sel1=='right':
  print("You fell into a hole and died.\n'")
elif sel1=='left':
  sel2=input("You've come to a lake, select to 'swim' or 'wait'?\n")
  sel2.lower()
  if sel2=='swim':
    print("You drowned and died.")
  elif sel2=='wait':
    sel3=input("You've come to a cave, select to 'enter' or 'leave'?\n")
    sel3.lower()
    if sel3=='enter':
      print("You died because the cave was full of snakes.")
    if sel3=='leave':
      sel4=input("you reach a building with 3 doors, select 'red', 'yellow' or 'blue'\n")
      if sel4=='red':
        print("room was full of fire and you died")
      elif sel4=='yellow':
        print("you found the Treasure!")
      elif sel4=='blue':
        print("you died because the door was locked")
      else:
        print("you died because you didn't select a door")
else:
  print("you died because you didn't select a valid direction\n")
