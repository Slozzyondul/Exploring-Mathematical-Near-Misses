import math
import sympy
import scipy.integrate
import scipy.special
import matplotlib.pyplot as plt
import numpy as np

# 1. Count actual primes up to x
def prime_count(x):
    return sympy.primepi(x)

# 2. Approximate pi(x) ~ x / log(x)
def prime_approx(x):
    return x / math.log(x)

# 3. Approximate pi(x) ~ Li(x) (Logarithmic integral)
def li_approx(x):
    if x < 2:
        return 0
    result, _ = scipy.integrate.quad(lambda t: 1 / math.log(t), 2, x)
    return result

# 4. Prime power counting function J(x)
def prime_power_count(x):
    total = 0
    n = 1
    while True:
        power = x ** (1 / n)
        count = sympy.primepi(power)
        if count == 0:
            break
        total += (1 / n) * count
        n += 1
    return total

# 5. Zeta function for Re(s) > 1
def zeta_naive(s, terms=100000):
    return sum(1 / (n ** s) for n in range(1, terms + 1))

# 6. Error between true pi(x) and approximations
def compute_errors(x_values):
    errors_log = []
    errors_li = []
    for x in x_values:
        real_pi = prime_count(x)
        approx_log = prime_approx(x)
        approx_li = li_approx(x)

        error_log = abs(real_pi - approx_log)
        error_li = abs(real_pi - approx_li)

        errors_log.append(error_log)
        errors_li.append(error_li)

    return errors_log, errors_li

# 7. Main demonstration
def main():
    x_values = np.linspace(10, 1000, 50)

    # Compute errors
    errors_log, errors_li = compute_errors(x_values)

    # Plot errors
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, errors_log, label="Error: pi(x) vs x/log(x)", linestyle="--")
    plt.plot(x_values, errors_li, label="Error: pi(x) vs Li(x)", linestyle="-")
    plt.xlabel("x")
    plt.ylabel("Error")
    plt.title("Error between Real Prime Count and Approximations")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Example Zeta computation
    print(f"Naive approximation of zeta(2): {zeta_naive(2)} (should be close to π²/6 ≈ {math.pi**2/6})")
    print(f"Naive approximation of zeta(3): {zeta_naive(3)}")
    print(f"Prime power counting function J(100): {prime_power_count(100)}")
    print(f"Prime count pi(100): {prime_count(100)}")

if __name__ == "__main__":
    main()
