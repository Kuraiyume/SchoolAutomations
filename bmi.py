def bmi_calculator():
    def validate_input(prompt, input_type=float):
        while True:
            try:
                value = input_type(input(prompt))
                if value <= 0:
                    raise ValueError("Value must be greater than zero")
                return value
            except ValueError as ve:
                print(f"Invalid input: {ve}. Please try again.")

    def calculate_bmi(weight, height, unit_system):
        if unit_system == 'metric':
            bmi = weight / (height ** 2)
        else:
            bmi = 703 * weight / (height ** 2)
        return round(bmi, 2)

    def classify_bmi(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25.0 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    while True:
        while True:
            print("Select unit system:\n1. Metric (kg, meters)\n2. Imperial (lbs, inches)")
            unit_choice = input("Enter the number: ")
            if unit_choice == '':
                continue
            elif unit_choice == '1':
                unit_system = 'metric'
                break
            elif unit_choice == '2':
                unit_system = 'imperial'
                break
            else:
                print("Invalid choice")

        if unit_system == 'metric':
            weight = validate_input("Enter your weight in kilograms: ")
            height = validate_input("Enter your height in meters: ")
        else:
            weight = validate_input("Enter your weight in pounds: ")
            height = validate_input("Enter your height in inches: ")
    
        bmi = calculate_bmi(weight, height, unit_system)
        category = classify_bmi(bmi)
   
        print("-" * 20)
        print(f"BMI: {bmi}")
        print(f"Category: {category}")
        print("-" * 20)

bmi_calculator()

