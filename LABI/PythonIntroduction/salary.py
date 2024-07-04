
def calculate_new_salary ():
    current_salary = float(input("Input employee current salary ($): "))
    percentual_increasy = float(input("Input the percentual increasy: "))
    
    new_salary = current_salary * (1 + percentual_increasy / 100) 

    print(f"The New salary is: ${new_salary:.2f}")

calculate_new_salary()

