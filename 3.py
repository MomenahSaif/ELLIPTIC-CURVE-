class Point:
    def __init__(self, x, y, infinity=False):
        self.x = x
        self.y = y
        self.infinity = infinity

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.infinity == other.infinity

    def __repr__(self):
        if self.infinity:
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
        if P.infinity:
            return Q
        if Q.infinity:
            return P
        if P.x == Q.x and (P.y != Q.y or P.y == 0):
            return Point(float('inf'), float('inf'), True)

        if P == Q:
            s = ((3 * P.x ** 2 + self.a) * pow(2 * P.y, -1, self.p)) % self.p
        else:
            s = ((Q.y - P.y) * pow(Q.x - P.x, -1, self.p)) % self.p

        x = (s ** 2 - P.x - Q.x) % self.p
        y = (s * (P.x - x) - P.y) % self.p
        return Point(x, y)

    def scalar_multiply(self, k, P):
        R = Point(0, 0, True)
        while k > 0:
            if k & 1:
                R = self.add_points(R, P)
            k >>= 1
            P = self.add_points(P, P)
        return R

    def generate_keypair(self, n=None):
        pr=int(input("Enter 1 for Random private key and 2 for input of private key: "))
        if(pr==1):
           private_key = n if n is not None else random.randint(1, self.n - 1)
        elif(pr==2):
            private_key = int(input("Enter the value of random number: "))  
        public_key = self.scalar_multiply(private_key, self.G)
        print("Private key:", private_key)
        print("Public key:", public_key)
        return private_key, public_key

    def generate_shared_secret(self, private_key, public_key):
        shared_secret = self.scalar_multiply(private_key, public_key)
        return shared_secret


# Example usage:
import random

# Define the parameters of the elliptic curve y^2 = x^3 + ax + b (mod p)
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
p = int(input("Enter the value of mod: "))

# Generator point G coordinates
Gx = int(input("Enter the value of G's x-coordinate: "))
Gy = int(input("Enter the value of G's y-coordinate: "))

# Order of the generator point G
n = int(input("Enter the value of n: "))

# Initialize ECC with parameters
ecc = ECC(a, b, p, Gx, Gy, n)

# Alice generates her keypair
print("\nAlice:")
alice_private_key, alice_public_key = ecc.generate_keypair()
# Bob generates his keypair
print("\nBob:")
bob_private_key, bob_public_key = ecc.generate_keypair()
# Alice computes the shared secret using her private key and Bob's public key
alice_shared_secret = ecc.generate_shared_secret(alice_private_key, bob_public_key)

# Bob computes the shared secret using his private key and Alice's public key
bob_shared_secret = ecc.generate_shared_secret(bob_private_key, alice_public_key)

print("\nShared Secrets:")
print("Alice's shared secret:", alice_shared_secret)
print("Bob's shared secret:", bob_shared_secret)
