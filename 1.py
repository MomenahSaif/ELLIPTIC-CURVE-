def is_valid_elliptic_curve(a, b, p):
    """
    Verify if the given elliptic curve y^2 = x^3 + ax + b (mod p) is valid.
    
    Parameters:
        a (int): The 'a' parameter of the curve equation.
        b (int): The 'b' parameter of the curve equation.
        p (int): The prime modulus.
    
    Returns:
        bool: True if the curve is valid, False otherwise.
    """
    # Check if 4a^3 + 27b^2 (mod p) is not equal to 0
    delta = (4 * pow(a, 3, p) + 27 * pow(b, 2, p)) % p
    if delta == 0:
        return False

    return True

# Example usage:
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
p = int(input("Enter the value of mod: "))

print("\nIs the elliptic curve valid?", is_valid_elliptic_curve(a, b, p))
