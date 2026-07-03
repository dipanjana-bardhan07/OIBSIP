def calculate_bmi():
    print("=== Welcome to the Oasis Infobyte BMI Calculator ===")
    


    try:
        # User se input lena
        weight = float(input("Enter your weight in kilograms (e.g., 70): "))
        height = float(input("Enter your height in meters (e.g., 1.75): "))
        
        # Input validation (Negative values check karna)
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers!")
            return



        # BMI Formula
        bmi = weight / (height ** 2)
        
        # Result ko 2 decimal places tak round karna
        print(f"\nYour calculated BMI is: {round(bmi, 2)}")
        

        
        # Categories check karna
        if bmi < 18.5:
            print("Health Status: Underweight")
        elif 18.5 <= bmi < 25:
            print("Health Status: Normal weight (Healthy)")
        elif 25 <= bmi < 30:
            print("Health Status: Overweight")
        else:
            print("Health Status: Obese")
            
    except ValueError:
        print("Error: Please enter valid numbers only!")

if __name__ == "__main__":
    calculate_bmi()