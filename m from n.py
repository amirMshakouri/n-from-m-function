def m_n(num1,num2):        #p(n,m)= n! // (n-m)!
    n = 0
    factorial = 1
    for i in range(1,num1+1):
         factorial *= i
    n = factorial

    m = num1- num2  
    factorial2 = 1
    for i in range(1,m+1):
         factorial2 *= i
    m = factorial2
    p = n // m
    return p
         

print(m_n(5,3))
