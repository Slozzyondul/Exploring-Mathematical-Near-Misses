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

def main():
    print("Fermat Near-Miss Finder")
    
    try:
        n = int(input("Enter the exponent n (must be greater than 2): "))
        if n <= 2:
            print("n must be greater than 2.")
            return
        
        max_z = int(input("Enter the maximum value for c (positive integer): "))
        if max_z <= 0:
            print("We need a positive max_z.")
            return
        
        threshold = float(input("Enter the relative error threshold (e.g., 0.01 for 1%): "))
        if threshold <= 0:
            print("Threshold must be positive too.")
            return
        
        filename = input("Enter the filename to save results (e.g., results.txt): ")
        
    except ValueError:
        print("Input must be a number.")
        return
    
    results = find_fermat_near_misses(n, max_z, threshold)
    
    if not results:
        print("No near-misses found. Try increasing max_z or threshold.")
    else:
        print(f"Found {len(results)} near-misses! Saving to '{filename}' ✍️...")
        with open(filename, 'w') as f:
            f.write(f"Near-misses for n = {n} (c < {max_z}, relative error < {threshold}):\n")
            for a, b, c, err in results:
                f.write(f"{a}^{n} + {b}^{n} ≈ {c}^{n} (error = {err:.6f})\n")
        
        print("Done!  Go check your file.")

if __name__ == "__main__":
    main()