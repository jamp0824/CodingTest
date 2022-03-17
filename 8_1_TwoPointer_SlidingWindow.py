"""
연속된 수 N개로 구성된 수열이 입력으로 주어진다.

이 수열의 i번째 수부터 j번째 수까지 합이 M이 되는 경우의 수를 구하세요.



첫째 줄엔 N, 둘째 줄엔 공백으로 구분된 N개의 수가 입력됩니다.

셋째 줄엔 목표 값 M이 주어집니다.
"""

num = int(input())
n2 = [int(x) for x in input().split()]
#print(n2)
arr = []
length = 0
M = int(input())
for i in n2:
    arr.append(i)
print(arr)
length = len(arr)
count = 0
result = 0
for i in range(length) :
    for j in range(i,length):
        if arr[i]+arr[j] == M:
            print('i =',arr[i])
            print('j = ',arr[j])
            print('i+j = ',arr[i]+arr[j])
            count+=1
print('count = ',count)




    

    
    
