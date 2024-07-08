def calculate_new_salary():
    try:
        current_salary = float(input("Input employee current salary ($): "))
        percentual_increasy = float(input("Input the percentage increasy: "))
    except ValueError:
        print("Error: Please enter valid numeric inputs.")
        return
    
    if percentual_increasy < 0:
        print("Error: Percentage increase cannot be negative.")
        return
    
    new_salary = current_salary * (1 + percentual_increasy / 100)
     
    print(f"The New salary is: ${new_salary:.2f}")  
        
calculate_new_salary()

