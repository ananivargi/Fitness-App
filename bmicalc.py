
while True:
    try:
        height = float(input("Please enter your height in centimeters (between 50 and 250): "))
        if 50 <= height <= 250:
            break
        else:
            print("Height must be between 50 and 250.")
    except ValueError:
        print("Height must be a decimal number.")
    
while True:
    try:
        weight = float(input("Please enter your weight in kilograms (between 20 and 300): "))
        if 20 <= weight <= 300:
            break
        else:
            print("Weight must be between 20 and 300.")
    except ValueError:
        print("Weight must be a decimal number.")

# Calculate BMI, rounding to 1 d.p
bmi = round(float(weight)/ ((float(height)/100)** 2), 2)
print (f"Your BMI is {bmi}")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi <= 24.9:
    # Pointer at healthy 
    print("You are healthy.")
elif 25 <= bmi <= 29.9:
    # Pointer at overweight  
    print("You are overweight.")
elif 30 <= bmi <= 39.9:
    print("You are obese. ")
else:
    print("You are extremely obese. ")
# Display calculated BMI 

