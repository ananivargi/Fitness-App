# Calculate BMI
height = float(input("Enter height: "))
weight = float(input("Enter weight: "))

with open('userinfo.txt', 'w') as f:
    f.write(f"{height}\n{weight}\n")

action = input("Where would you like to go? ").upper()

if action == "BMI":
    with open('userinfo.txt', 'r') as f:
        height, weight = map(float, f.read().split())
        bmi = weight / (height ** 2)
        print(f"Your BMI is {bmi}")