import time
import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        print('n = ',n)
        print('i = ',i)
        print('math.sqrt(n)+1',int(math.sqrt(n))+1)
        print('n /%/i =', n%i)
        if n % i ==0:
            return False
    return True

def print_prime_by_range(n):
    cnt = 0
    for i in range(2,n+1):
        if is_prime(i):
            cnt+=1
    print()        
    print('소수의 개수:',cnt)

start = time.time()
print_prime_by_range(50)
end = time.time()
print("실행시간(초):",end-start)