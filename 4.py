import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        if self.x == float('inf'):
            return "Infinity"
        else:
            return f"({self.x}, {self.y})"

class ECC:
    def __init__(self, a, b, p, Gx, Gy, n):
        self.a = a
        self.b = b
        self.p = p
        self.G = Point(Gx, Gy)
        self.n = n  # Order of the generator point G

    def add_points(self, P, Q):
        if P.x == float('inf'):
            return Q
        if Q.x == float('inf'):
            return P
        if P.x == Q.x and (P.y != Q.y or P.y == 0):
            return Point(float('inf'), float('inf'))

        if P.x == Q.x and P.y == Q.y:
            s = ((3 * P.x ** 2 + self.a) * pow(2 * P.y, -1, self.p)) % self.p
        else:
            s = ((Q.y - P.y) * pow(Q.x - P.x, -1, self.p)) % self.p

        x = (s ** 2 - P.x - Q.x) % self.p
        y = (s * (P.x - x) - P.y) % self.p
        return Point(x, y)

    def scalar_multiply(self, k, P):
        R = Point(float('inf'), float('inf'))
        for _ in range(k):
            R = self.add_points(R, P)
        return R

    def generate_keypair(self):
        pr=int(input("Enter 1 for Random private key and 2 for input of private key: "))
        if(pr==1):
           private_key = random.randint(1, self.n - 1)
        elif(pr==2):
            private_key = int(input("Enter the value of private key: "))  
        public_key = self.scalar_multiply(private_key, self.G)
        return private_key, public_key

    def encrypt(self, message, recipient_public_key):
        pr=int(input("Enter 1 for Random k value and 2 for input of k value: "))
        if(pr==1):
           k = random.randint(1, self.n - 1)
        elif(pr==2):
            k = int(input("Enter the value of k: "))  
        
        C1 = self.scalar_multiply(k, self.G)
        C2 = self.add_points(message, self.scalar_multiply(k, recipient_public_key))
        return C1, C2

    def decrypt(self, C1, C2, private_key):
        S = self.scalar_multiply(private_key, C1)
        print("nB*C1: ",S)
        plaintext = self.add_points(C2, Point(S.x, -S.y))
        return plaintext

# Define the parameters of the elliptic curve y^2 = x^3 + ax + b (mod p)
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
p = int(input("Enter the value of mod: "))

# Generator point G coordinates
Gx = int(input("Enter the value of G's x-coordinate: "))
Gy = int(input("Enter the value of G's y-coordinate: "))

# Order of the generator point G
n = int(input("Enter the value of n: "))

ecc = ECC(a, b, p, Gx, Gy, n)
print("\nBob:")
# Bob generates his key pair
bob_private_key, bob_public_key = ecc.generate_keypair()

print("Private key: ",bob_private_key)
print("Public key: ",bob_public_key)
print("\nAlice:")
x = int(input("Enter the value of Message x-cordinate: "))
y = int(input("Enter the value of Message y-cordinate: "))

# Message in (x, y) point form
message = Point(x, y)

# Alice encrypts the message using Bob's public key
C1, C2 = ecc.encrypt(message, bob_public_key)
print("\nC1: ",C1)
print("C2: ",C2)

# Bob decrypts the message using his private key
decrypted_message = ecc.decrypt(C1, C2, bob_private_key)

print("\nOriginal Message:", message)
print("Decrypted Message:", decrypted_message)
