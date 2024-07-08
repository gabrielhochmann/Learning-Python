def add_complex(real1, imag1, real2, imag2):
    """
    Adds two complex numbers given their real and imaginary parts separately.
    
    Args:
    real1 (float): Real part of the first complex number.
    imag1 (float): Imaginary part of the first complex number.
    real2 (float): Real part of the second complex number.
    imag2 (float): Imaginary part of the second complex number.
    
    Returns:
    tuple: A tuple containing the real and imaginary parts of the sum of the two complex numbers.
    """
    real_sum = real1 + real2
    imag_sum = imag1 + imag2
    return (real_sum, imag_sum)
    
def subtract_complex(real1, imag1, real2, imag2):
    """
    Subtracts two complex numbers given their real and imaginary parts separately.
    
    Args:
    real1 (float): Real part of the first complex number.
    imag1 (float): Imaginary part of the first complex number.
    real2 (float): Real part of the second complex number.
    imag2 (float): Imaginary part of the second complex number.
    
    Returns:
    tuple: A tuple containing the real and imaginary parts of the difference of the two complex numbers.
    """
    real_diff = real1 - real2
    imag_diff = imag1 - imag2
    return (real_diff, imag_diff)

def main():
    # Read parts of z1
    print("Enter the parts of z1:")
    z1_real = float(input("Real part of z1: "))
    z1_imag = float(input("Imaginary part of z1: "))
    
    # Read parts of z2
    print("Enter the parts of z2:")
    z2_real = float(input("Real part of z2: "))
    z2_imag = float(input("Imaginary part of z2: "))
    
    # Calculate the sum of complex numbers z1 and z2
    z3_real, z3_imag = add_complex(z1_real, z1_imag, z2_real, z2_imag)
    
    # Calculate the subtraction of complex numbers z1 and z2
    z4_real, z4_imag = subtract_complex(z1_real, z1_imag, z2_real, z2_imag)

    # Display results
    print("\nResults:")
    print(f"The sum of complex numbers z1 = {z1_real} + {z1_imag:+.2f}i and z2 = {z2_real} + {z2_imag:+.2f}i is z3 = {z3_real} + {z3_imag:+.2f}i")
    print(f"The substraction of complex numbers z1 = {z1_real} + {z1_imag:+.2f}i and z2 = {z2_real} + {z2_imag:+.2f}i is z4 = {z4_real} + {z4_imag:+.2f}i")

if __name__ == "__main__":
    main()