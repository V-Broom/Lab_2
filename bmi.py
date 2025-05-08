def calculate_bmi(height, weight):
    print("Height = ", height)
    print("Weight = ", weight)

    bmi = weight/(height**2)
    print("BMI = ", round(bmi,2))

    if bmi < 18.5:
        print("Underweight")
    elif bmi >25.0:
        print("Overweight")
    else:
        print("Normal weight")

calculate_bmi(1.73, 57)
