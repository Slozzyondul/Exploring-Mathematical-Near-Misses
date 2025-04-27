import math

def find_fermat_near_misses(n, max_z=1000, threshold=0.01):
    """
    Find near-misses for a^n + b^n ≈ c^n where |(a^n + b^n - c^n)/c^n| < threshold.
    
    Args:
        n (int): Exponent (n > 2).
        max_z (int): Maximum value for c.
        threshold (float): Allowed relative error.
    
    Returns:
        List of tuples (a, b, c, relative_error).
    """
    near_misses = []
    
    for c in range(1, max_z + 1):
        c_pow = c ** n
        
        for a in range(1, c):
            a_pow = a ** n
            
            for b in range(a, c):
                b_pow = b ** n
                sum_pow = a_pow + b_pow
                
                # Check if c^n is close to a^n + b^n
                diff = abs(sum_pow - c_pow)
                relative_error = diff / c_pow
                
                if relative_error < threshold:
                    near_misses.append((a, b, c, relative_error))
    
    return near_misses

# Example usage:
n = 3  # Exponent (try n=3,4,5,...)
max_z = 1000  # Upper limit for c
threshold = 0.001  # Allowed relative error (1e-3 = 0.1%)

results = find_fermat_near_misses(n, max_z, threshold)

# Print results
print(f"Near-misses for n = {n} (c < {max_z}, relative error < {threshold}):")
for a, b, c, err in results:
    print(f"{a}^{n} + {b}^{n} ≈ {c}^{n} (error = {err:.6f})")