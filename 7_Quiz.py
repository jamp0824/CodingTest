def prime(num):
    a = [False,False] + [True]*(num-1)
    primes=[]
    result = 0
    for i in range(2,num+1):
        if a[i]:
            primes.append(i)
            result+=i
            for j in range(2*i, num+1, i):
                a[j] = False
    str = f'연속된 소수{primes}의 합은 {result}입니다.'            
    return str
print(prime(11))