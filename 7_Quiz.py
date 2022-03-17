def answer(num):
    a = [False,False] + [True]*(num-1)
    primes=[]
    result=[]
    for i in range(2,num+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, num+1, i):
                a[j] = False
    sum = 0        
    for k in primes:
        result.append(k)
        sum += k
        if sum == num:
            print(f'연속된 소수{result}의 합은 {num}입니다.')
            break
        elif sum> num: 
            print(f'연속된 소수의 합으로 {num}을 만들 수 없습니다.')
            break
    return str
answer(41)
answer(20)

