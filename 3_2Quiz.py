arr = [215,513,712,803]
target = 10

def binary_search(arr, target):

    start = 1           	# 탐색 배열의 시작 인덱스
    end = max(arr)          # 탐색 배열의 끝 인덱스
  
    while (end - start >= 0):
        mid = (start + end) // 2         # 중앙값 설정
        lines = 0
      
        for i in arr:                   # key값을 찾았을때     
            lines += i//mid
      
        if lines >= target:
            start = mid+1
      
        else:                            # 길이값이 mid의 값보다 작을때
            end = mid-1                  # 끝 인덱스를 증가
    
    return end

print(binary_search(arr,target))
            
