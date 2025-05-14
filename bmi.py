def calculate_bmi(height, weight):
    print("Height = ", height)
    print("Weight = ", weight)

    bmi = weight/(height**2)
    print("BMI = ", round(bmi,2))

    if bmi < 18.5:
        print("Underweight")
        return -1
    elif bmi >25.0:
        print("Overweight")
        return 1
    else:
        print("Normal weight")
        return 0

calculate_bmi(1.73, 57)
