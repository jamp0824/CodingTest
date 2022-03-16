import time

def print_prime_by_range(n):

    # 인덱스는 0번부터 시작하기 때문에, n+1 세팅
    prime_range = n + 1
    print('prime_range',prime_range)
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    prime_list = [True] * prime_range
    print('prime_list',prime_list)

    sqrt = int(n ** 0.5)
    print('sqrt',sqrt)
    for i in range(2, sqrt + 1):
        print('i = ',i)
        print('sqrt+1 = ',sqrt+1)
        if prime_list[i]:  # i가 소수인 경우
            print('prime_list[i] = ',prime_list[i])
            for j in range(i + i, prime_range, i):  # i이후 i의 배수들을 False 판정
                print('j = ',j)
                print('i+1 = ',i+1)
                print('prime_range = ',prime_range)
                print('i =',i)
                print('prime_list[j] = ',prime_list[j])
                prime_list[j] = False
    # 소수 개수 리턴
    print('prime_list.count(True)-2',prime_list.count(True)-2)
    print('prime_list',prime_list)
    return prime_list.count(True) - 2

start = time.time()

prime_count = print_prime_by_range(10)
print("소수 개수: ", prime_count)

end = time.time()
print("실행시간(초) : ", end - start)