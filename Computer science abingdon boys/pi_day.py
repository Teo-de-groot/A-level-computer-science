import random 
import time
from decimal import Decimal, getcontext
import math

def square_pi(r):
    start = time.time()
    total_c =0
    for _ in range(r):
        pointx = random.random()
        pointy= random.random()
        if pointx**2 +pointy**2<1:
            total_c+=1
    end = time.time()
    times = (end-start)
    return f"pi == {(total_c/r)*4}",(f"done in {times}s")
            

print(f"Monte carlo : {square_pi(200000)}")





def calculate_pi(precision):
    start = time.time()
    getcontext().prec = precision + 2
    
    num_iterations = (precision // 14) + 1
    sum_total = Decimal(0)
    
    for k in range(num_iterations):
        top = ((-1)**k) * (math.factorial(6*k)) * (13591409 + 545140134*k)
        
        exponent = Decimal(3) * k + Decimal('1.5')
        bottom = (math.factorial(3*k)) * (math.factorial(k)**3) * (Decimal(640320)**exponent)
        
        sum_total += Decimal(top) / Decimal(bottom)
    
    pi = 1 / (sum_total * 12)
    end = time.time()
    times = end-start
    return f"pi == {pi}",(f"done in {times}s")


print(f"Chudnovsky Method : {calculate_pi(200)}")

def sequence():
    total =0
    heads = 0
    while heads <= total// 2:
        head = random.randint(0,1)
        if head == 1:
            total+=1
            heads+=1  
        else:
            total+=1
    return heads /total

def coin_flip(attempts):
    total = 0
    for _ in range(attempts):
        total += sequence()
    return (total/attempts *4)
print(f"Coin Flip Method: {coin_flip(200)}")