from math import sqrt

def calculate_distance (x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    x1 = float(input("Input the x1 here: "))
    y1 = float(input("Input the y1 here: "))
    x2 = float(input("Input the x2 here: "))
    y2 = float(input("Input the y2 here: "))

    print(f"The distance beetwen ({x1}, {y1}) and ({x2}, {y2}) is: {calculate_distance(x1, y1, x2, y2)})")

if __name__ == "__main__":
    main()