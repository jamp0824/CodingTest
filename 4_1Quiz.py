array = [215,513,712,803]
target = 10
start = 1                           	# 탐색 배열의 시작 인덱스
end = max(array)                        # 탐색 배열의 끝 인덱스

def binary_search(arr, target,start,end):
    
    if(end - start < 0):               
        return end                      # end 반환 값이 start값 보다 작은 경우 end값으로 키 값 반환
    mid = (start + end) //2             # 중앙 값 설정
    lines = 0

    for i in arr:                       # 각 길이 추출 
        lines += i//mid                 # 길이를 키값으로 나눈 line 갯수
      
    if lines >= target:                 # 총 line 갯수가  키 값으로 나눈 갯수보다 적은 경우
        return binary_search(arr,target,mid+1,end)  # start = mid+1로 계산하여 재귀함수 실행
      
    else:
        return binary_search(arr,target,start,mid-1)     # 길이값이 키 값보다 작을 때
                                                    # end = mid-1로 계산하여 재귀함수 실행
   
print(binary_search(array,target,start,end))


