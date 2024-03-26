import random

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def C(n, m):
    return factorial(n)/(factorial(m)*factorial(n-m))

def Q(n,k):
    if k==0:
        if n==1:
            return 1 
        elif n==2:
            return 2
        else:
            return Q(n-1,0) + Q(n,1)
    else:
        if n==2*k:
            return 1
        elif n<2*k:
            return 0
        else:
            return Q(n-2,k-1) + 2*Q(n-1,k) + Q(n,k+1)  



def cal_sum(T, a, b):
    sum = a + (1-a-b)*a
    for k in range(2, T+1):
        sum = sum + (1-a-b)**k*a
        for n in range(1, int(k/2)+1):
                sum = sum + C(k, 2*n)*Q(n, 0)*((1-a-b)**(k-2*n))*(b**n)*(a**n)*a
    
    return sum

def simulate(T, m, a, b):
    sum_sim = 0
    for i in range(1, m+1):
        num = 1; t = 1
        while num>0 and t<=T:
            t = t+1
            p = random.random()
            if p<a:
                num = num - 1
            elif p>(1-b):
                num = num + 1
        if num == 0:
            sum_sim = sum_sim + 1
    return sum_sim/m

a = 0.25; b = 0.25
for T in range(5,50,5):
    print(f'T: {T}; calculate: {cal_sum(T, a, b)}; simulate: {simulate(T, 100000, a, b)}')
