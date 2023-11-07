#Pizza python ordering
print("Welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want? S, M, L\n")
add_pep=input("Do you want pepperoni? Y or N\n")
ex_cheese=input("Do you want extra cheese? Y or N\n")
if size=='s':
  cost=15
elif size=='m':
  cost=20
elif size=='l':
  cost=25
if add_pep=='y':
  cost=cost+3
if ex_cheese=='y':
  cost=cost+2
print("Your final bill is: $"+str(cost))
