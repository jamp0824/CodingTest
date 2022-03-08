#Linear Search(선형 탐색)
arr1={1,2,3,4,5,6,7,8,9,10}

for item in arr1:
    if item == 6:
        print("배열이 6이 존재합니다.")

#Binary Search(이진 탐색)

def binary_search(arr, length, target):
    start = 0   				# 탐색 배열의 시작 인덱스
    end = length - 1 			# 탐색 배열의 끝 인덱스

    while (end - start >= 0):
        mid = (start + end) // 2     # 중앙값 설정
        print(mid)

        if (arr[mid] == target):	# key값을 찾았을때     
            return 1				# 1을 리턴

        elif (arr[mid] > target):   # key값이 mid의 값보다 작을때
            end = mid - 1 			# 끝 인덱스를 감소

        else:                   	# key값이 mid의 값보다 클때
            start = mid + 1 		# 시작 인덱스를 증가
	
    return 0

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = 10
target = 11
 
result = binary_search(arr, length, target)

if result:
    print(f"배열에 {target}가 존재합니다.")
else:
    print(f"배열에 {target}가 존재하지 않습니다.")
