#Advanced BMI calculator
hei=int(input("Enter your height in m: "))
wei=int(input("Enter your weight in Kg: "))
bmi= wei / (hei ** 2)
if bmi < 18.5:
    print("Your BMI is ",bmi,"and you are underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Your BMI is ",bmi,"and you are normal")
elif bmi >= 25 and bmi < 30:
    print("Your BMI is ",bmi,"and you are overweight")
