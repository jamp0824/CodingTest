import time
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_prime_by_range(n):
    cnt = 0
    for i in range(2,n+1):
        if is_prime(i):
            print(i,end=' ')
            cnt+=1
    print()        
    print('소수의 개수:',cnt)

start = time.time()
print_prime_by_range(50000)
end = time.time()
print("실행시간(초):",end-start)