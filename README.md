# Exploring-Mathematical-Near-Misses
(Fermat's Last Theorem Approximations &amp; Riemann-Zeta Zeroes)


# Overview 

[Link Document](https://people.math.harvard.edu/~elkies/ferm.html)

# 1. Fermat near-misses.

Fermat "near-misses" approximates the solution of x^n + y^n ~= z^n for all integers, with 0<x<=y<z<2^n in a given interval of n integers.

Extended from z<10^6 to z<2^23 = 8388608 with a threshold of the absolute value r = nz^(n-3)/(z^n - y^n - x^n) at 1 relative error threshold.

Heuristic suggests that for all n and r0, the number of solutions of |r|<r0 with z<N, should be asymptotically propotional to CnLog(N)/r0 where Cn is the area of Ln "circle" |x|^n + |y|^n < 1 and r<<z^0(1) holds for all n>3.

This is random though in some cases systematic families of solutions exceed random expectations.

One known family (2nt^n+1)^n -(2nt^n-1)^n with r = (3/(n-2)(n-1)) + O(t^-n) grows faster than expected but was below the threshold of |r|< 1.

# New polynomial families
a). Another family of (32t^9 + 6t)^8 + (32t^8 + 7)^8 with r = t^5/21 + O(t^−3) when n = 8. 

b). Whenever 3n(n−2) is a square,that is n=(2, 3,) 8, 27, 98, 363,... with the computation from 10^6 to 2^23 for (192t^8 + 24t^4 − 1)^4 − (192t^8 − 24t^4 − 1)^4 − (192t^7)^4, this yield r = −4t^4 + O(1) = (z/12)^(1/2) + O(1). 

This two gives rational curves on twisted Fermat hypersurfaces of degree n>4 in projective (n−2)-space.

# Key points 
- Finding "near-misses" is not random — special patterns exist.

- Certain values of n (like 8, 27, 98, 363...) have hidden families of near-misses based on deep number theory structure.

- The work shows how ancient math (Fermat's Last Theorem) can lead to new and surprising discoveries.

- Even though integer solutions (for n > 2) don't exist, near-misses tell a deeper story about how numbers behave.

# Python program 
Python program that outputs near-misses of Fermat's Last Theorem based on the input n, c and a threshold level

Approach:
Brute-force search within a given range for a,b,c and n.

Check near-miss condition: Compute ∣a^n+b^n−c^n∣ and see if it's "small" relative to c^n.

Parameter tuning: Adjust thresholds for what counts as a "near-miss."

# How to run 
git clone https://github.com/Slozzyondul/Fermat-Near-Misses.git

cd Fermat-Near-Misses

python3 fermat_near_misses.py

# Terminal variables explanation
You will be prompted to input the variables based on your desired range 

n = to what power degree are you targeting must be greater than 2

c = maximum value (z^n)

relative error threshold = allowed relative error

Key in the name you want the results to be stored in at the parent folder of the project.



# 2. Riemann-Zeta Zeroes

To properly understand the Riemann-Zeta zeroes, we need to understand first the prime number theorem.

The prime number theorem approximates how many primes exists less than any given integer x. Since its an approximation, there exists an error because its not actual values.

Riemann hypothesis explores how big that error is.

Error term is related to Riemann-Zeta function when is equal to zero.

So, Riemann hypothesis concludes that the zeros of the Riemann-zeta function all lie on the line (1/2 + it) where it is the complex/imaginary part while 1/2 is the real part.

a.) Prime number theory by Gauss: pi(x) = represents the number of primes less than x.

Therefore, pi(x)/(x/log(x)) -> 1 as x -> infinity or pi(x) ~ x/log(x)

For instance, when x=100, pi(100) = 25 but 100/log(100) ~ 22 and when x=1000000000, pi(1000000000) = 50847534 but 1000000000/log(1000000000) ~ 48254942

This implies the error reduces proportionality when x is a large number.

b.) Dirichlet and Gauss approximation for pi(x) 

pi(x) ~ Li(x) =  ∫1/(log(x)) dt  at an interval of [2, x] where Li(x) is the logarthmic integral of x.

For instance, pi(1000000000) = 50847534 but Li(1000000000) = 50849234 wgich is more accurate approximation for pi(x).


