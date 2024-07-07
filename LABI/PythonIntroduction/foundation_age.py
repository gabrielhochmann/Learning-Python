import datetime

def calculate_age ():
    foundation = int(input("Input the foundation year: "))
    current_year = datetime.datetime.now().year
    current_age = current_year - foundation
    print("Actual age of the Enterprise is:", current_age)

def main():
    calculate_age()

if __name__ == "__main__":
    main()