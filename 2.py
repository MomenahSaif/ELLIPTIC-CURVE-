def is_point_on_curve(x, y, a, b, p):
    """
    Verify if the given point (x, y) lies on the elliptic curve y^2 = x^3 + ax + b (mod p).
    
    Parameters:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.
        a (int): The 'a' parameter of the curve equation.
        b (int): The 'b' parameter of the curve equation.
        p (int): The prime modulus.
    
    Returns:
        bool: True if the point lies on the curve, False otherwise.
    """
    # Calculate left-hand side (LHS) and right-hand side (RHS) of the curve equation
    LHS = (y ** 2) % p
    RHS = (x ** 3 + a * x + b) % p

    # Check if LHS equals RHS
    return LHS == RHS


x = int(input("Enter the value of x cordinate of point: "))
y = int(input("Enter the value of x cordinate of point: "))
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
p = int(input("Enter the value of mod: "))

print("\nIs the point on the curve?", is_point_on_curve(x, y, a, b, p))
