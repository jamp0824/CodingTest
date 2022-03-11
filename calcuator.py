arr = [215,513,712,803]
target = 10
start = 1
end = max(arr)
def binary_search(arr, target,start,end):
    
    if(end - start < 0):
        return None
    mid = (start + end) //2
    lines = 0

    for i in arr:                   # key값을 찾았을때     
        lines += i//mid
      
    if lines >= target:
        return binary_search(arr,target,mid+1,end)
      
    else:
        return binary_search(arr,target,start,mid-1)                            # 길이값이 mid의 값보다 작을때
                       # 끝 인덱스를 증가
    return end 




