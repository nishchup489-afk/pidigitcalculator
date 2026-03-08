# Attempt 1
# ------------
# Pi = SUM k=0 to infinity 16-k [ 4/(8k+1) – 2/(8k+4) – 1/(8k+5) – 1/(8k+6) ].
# Problem : max 50 , worst idea for a small project 


#Uncomment ⬇️



# isRunning = True

# while isRunning:
#     try:
#         num = int(input("Enter your number:(ctrl + c to exit)  "))
#     except ValueError:
#         print("Enter only digits !")

#     numbers = []
#     for n in range(num):


#         fp1 = 4/((8*n) + 1)
#         fp2 = 2/((8*n) + 4)
#         fp3 = 1/((8*n) + 5)
#         fp4 = 1/((8*n) + 6)
#         fps = fp1 - fp2 - fp3 - fp4
#         fp5 = 16**(-n)
#         fp6 = (fp5 * fps)
#         numbers.append(fp6)
        

#     nth_pi = sum(numbers)
#     print(f"{nth_pi:.{num}f}")







# -----------------------------------------------










#Attempt 2
# ------------
# same thing with python module "math"



#Uncomment ⬇️

# import math

# def findPi(n):
#     if n > 15:
#         print("Warning: Standard float precision limits accuracy beyond 15 digits.")
#     return f"{math.pi:.{n}f}"

# try:
#         n = int(input("Enter the number of decimal places (max 50): "))
#         if n < 0:
#             print("Please enter a positive number.")
#         else:
#             print(f"PI to {n} decimal places: {findPi(n)}")
# except ValueError:
#         print("Invalid input. Please enter an integer.")











# -----------------------------------------------------------------------





# Attempt 3: Chudnovsky algortithm

# $$\frac{1}{\pi} = \frac{12}{(640320)^{3/2}} \sum_{k=0}^{\infty} \frac{(-1)^k (6k)! (13591409 + 545140134k)}{(3k)! (k!)^3 (640320)^{3k}}$$



## imports
from math import factorial
from decimal import Decimal, getcontext  #| float/double cant handle too much numbers

# set precision : max digits of that number
getcontext().prec = 5000


# take imports



def chudnovsky(n):

    # IMPORTANT : chudnovsky gives 14.18 digits per iteration , but we need 1 digit per iteration
    iteration = ( n // 14) + 1

    sum_total = Decimal(0) # a bucket where currently no numbers

    for k in range(iteration):
        # Numerator: (-1)^k * (6k)! * (13591409 + 545140134k)
        num = ((-1)**k) * factorial(6*k) * (13591409 + 545140134*k)
        
        # Denominator: (3k)! * (k!)^3 * 640320^(3k)
        den = factorial(3*k) * (factorial(k)**3) * (640320**(3*k))

        sum_total += ( Decimal(num) / Decimal(den))

    constant = Decimal(426880) * Decimal(10005).sqrt()

    pi = constant / sum_total
    return pi

while True:
    try:
            n = input("Enter the number of decimal places (max 50) (q to exit): ")
            n = int(n)
            if n < 0:
                print("Please enter a positive number.")
            result = chudnovsky(n)

    except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"PI to {n} decimal places: {result:.{n}f}")