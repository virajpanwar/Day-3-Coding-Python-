#Love Calculator
print("Welcome to love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
names= name1+name2
names.lower()
#Counting Letters
t=names.count('t')
r=names.count('r')
u=names.count('u')
e=names.count('e')
tr=t+r+u+e
lov=names.count('l')
o=names.count('o')
v=names.count('v')
e=names.count('e')
lo=lov+o+v+e
love = str(tr)+str(lo)
if int(love) < 10 or int(love) > 90:
  print(f"Your score is {love}, you go together like coke and mentos.")
elif int(love) > 40 and int(love) < 50:
  print(f"Your score is {love}, you are alright together.")
else:
  print(f"Your score is {love}.")
