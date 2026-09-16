import random
import sys

# Increase recursion depth just in case, though we rely on iteration
sys.setrecursionlimit(2000)

def is_prime_miller_rabin(n, k=10):
    """
    Probabilistic primality test. 
    Extremely fast for huge numbers.
    k: number of tests (higher = more certain)
    """
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def sqrt_mod_prime(n, p):
    """
    Tonelli-Shanks algorithm to find x such that x^2 = n (mod p).
    We specifically need this for p = 1 mod 4 to find sqrt(-1).
    """
    if pow(n, (p - 1) // 2, p) != 1:
        return None  # No square root exists
    
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)
    
    # Standard Tonelli-Shanks
    s = p - 1
    r = 0
    while s % 2 == 0:
        s //= 2
        r += 1
        
    z = 2
    while pow(z, (p - 1) // 2, p) == 1:
        z += 1
        
    c = pow(z, s, p)
    x = pow(n, (s + 1) // 2, p)
    t = pow(n, s, p)
    m = r
    
    while t % p != 1:
        tt = t
        i = 0
        while tt != 1:
            tt = pow(tt, 2, p)
            i += 1
            if i == m: 
                return None # Should not happen if p is prime and n is QR
        
        b = c
        for _ in range(m - i - 1):
            b = pow(b, 2, p)
            
        m = i
        c = pow(b, 2, p)
        t = (t * c) % p
        x = (x * b) % p
        
    return x

def cornacchia_two_squares(p):
    """
    Finds x, y such that x^2 + y^2 = p.
    Requires prime p = 1 mod 4.
    """
    # 1. Find z such that z^2 = -1 mod p
    # -1 is equivalent to p-1
    z = sqrt_mod_prime(p - 1, p)
    
    # 2. Euclidean Descent (Gaussian GCD)
    r0, r1 = p, z
    limit = int(p**0.5)
    
    while r1 > limit:
        r0, r1 = r1, r0 % r1
        
    x = r1
    y = int((p - x*x)**0.5)
    return x, y

def decompose_four_squares(n):
    """
    Decomposes integer n into sum of 4 squares: n = a^2 + b^2 + c^2 + d^2.
    """
    if n == 0: return [0, 0, 0, 0]
    
    # Handle factor of 4: n = 4^k * m
    # decompose m, then multiply results by 2^k
    multiplier = 1
    while n % 4 == 0:
        n //= 4
        multiplier *= 2
        
    # If n % 8 == 7, Lagrange theorem says it can be 4 squares.
    # But usually, we can find a solution where one or two are zero, 
    # effectively doing a 3-square or 2-square decomposition.
    
    # STRATEGY: 
    # Pick random a, b such that p = n - a^2 - b^2 is a prime where p = 1 mod 4.
    # Then decompose p into two squares.
    
    while True:
        # Heuristic: Pick a near sqrt(n/2) to keep remainders large enough for primality testing
        limit = int(n**0.5)
        a = random.randint(0, limit)
        rem1 = n - a*a
        
        if rem1 < 0: continue
        
        # We can try to be lucky and set b=0 (trying for 3-square decomposition)
        # or pick b randomly. Random is safer for large inputs distribution.
        b = random.randint(0, int(rem1**0.5))
        p = rem1 - b*b
        
        # We need p > 0, Prime, and p % 4 == 1
        if p > 0 and p % 4 == 1:
            if is_prime_miller_rabin(p):
                c, d = cornacchia_two_squares(p)
                result = [a, b, c, d]
                # Apply the multiplier from the divide-by-4 step
                return sorted([x * multiplier for x in result])

# --- TEST HARNESS ---
if __name__ == "__main__":
    print("--- Teacher's Stress Test ---")
    
    # 1. Test a "Small" Huge Number (2^128)
    exp = 128
    print(f"\nTesting random number near 2^{exp}...")
    num = random.getrandbits(exp)
    print(f"Number: {num}")
    squares = decompose_four_squares(num)
    print(f"Squares: {squares}")
    check = sum(x*x for x in squares)
    print(f"Check: {check == num} (Sum: {check})")

    exp = 1024
    print(f"\nTesting random number near 2^{exp}...")
    num = random.getrandbits(exp)
    num |= 1 
    
    print(f"Number (truncated): {str(num)[:30]}... ({len(str(num))} digits)")
    
    import time
    start = time.time()
    squares = decompose_four_squares(num)
    end = time.time()
    
    print(f"Squares found in {end - start:.4f} seconds.")
    print(f"Squares (top 2): {squares[-2:]}") 
    check = sum(x*x for x in squares)
    print(f"Valid Decomposition: {check == num}")