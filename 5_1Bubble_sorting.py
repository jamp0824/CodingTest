arr = [5,2,9,1,6]
length =len(arr)

print(f"정렬 전:{arr}")
print("전체 길이 len = ",length)
# 배열의 크기만큼 반복
for i in range(length):
    print('첫번째 for문의 i = ',i)
    # 배열의 총 크기에서, i값과 1을 뺀 만큼 반복한다.
    for j in range(0, length-i-1):
        print('두번째 for문의 j = ',j)
        print('두번째 for문의 length-i-1 = ',length-i-1)
        # 현재 j 인덱스 위치의 값이 j+1 인덱스 위치의 값이 더 크다면
        if arr[j]>arr[j+1]:
            # 두 값의 위치를 변경한다.
            arr[j],arr[j+1]= arr[j+1],arr[j]

print(f"정렬 후: {arr}")