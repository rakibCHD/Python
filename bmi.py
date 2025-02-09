def bmi_calculation(h_feet, h_inches, weight):
    height = (h_feet * 0.3048) + (h_inches * 0.0254)
    bmi = weight / (height * height)
    return bmi
 
def display():
    print("-------------BMI-----------")
    print("------Body Mass Index------\n")
    print("Underweight   = <18.5")
    print("Normal weight = 18.5-24.9")
    print("Overweight    = 25-29.9")
    print("  Obesity     = 30++ ")
    print("---------------------------\n")

def input_output():
    weight_kg = float(input("Enter Your Weight(kg): "))
    height_feet = float(input("Enter Your Height(feet): "))
    height_inches = float(input("Enter Your Height(inches): ")) 
    
    print("Calculating........\n")
    final_result = bmi_calculation(height_feet, height_inches, weight_kg)

    if final_result < 18.5:
        print(f"Your BMI is: {final_result:.4f}")
        print("You are Underweighted.")
    elif 18.5 <= final_result <= 24.9:
        print(f"Your BMI is: {final_result:.4f}")
        print("You are Normal weighted.")
    elif 25 <= final_result <= 29.9:
        print(f"Your BMI is: {final_result:.4f}")
        print("You are Overweighted.")
    elif final_result >= 30:
        print(f"Your BMI is: {final_result:.4f}")
        print("You are in Obesity & it is a risk to health.") 

if __name__ == "__main__":
    display()
    input_output() 
 
