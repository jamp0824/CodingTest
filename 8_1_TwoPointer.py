N = int(input())
arr = list(map(int,input().split()))
M = int(input())

start, end = 0,0
partial_sum = 0
answer = 0

while(start<N):
    #배열합이 목표값보다 크거나
    #end가 배열의 끝에 도달한 경우
    if partial_sum>M or end >=N:
        partial_sum -= arr[start]
        start += 1
    #배열합이 목표값보다 작거나 같으면
    elif partial_sum<= M:
        partial_sum += arr[end]
        end += 1
    #배열합이 목표값과 같으면
    if partial_sum == M:
        print(arr[start:end],start,end)
        answer += 1

print(answer)