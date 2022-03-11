arr = [215,513,712,803]
target = 10

def binary_search(arr, target):

    start = 1           	# 탐색 배열의 시작 인덱스
    end = max(arr)          # 탐색 배열의 끝 인덱스
  
    while (end - start >= 0):
        print('while start============')
        mid = (start + end) // 2         # 중앙값 설정
        lines = 0
        print('start',start)
        print('mid = ',mid)
        print('end = ',end)
        for i in arr:                   # key값을 찾았을때     
            print('for==============')
            print('lines(before) = ',lines)
            lines += i//mid
            print('lines(after) = ',lines)
            print('i= ',i)
            print('mid = ',mid)
            print('for==============')

        if lines >= target:
            print('if==================')
            start = mid+1
            print('start = ',start)
            print('mid =',mid)
            print('end=',end)
            print('if==================')

        else:                            # 길이값이 mid의 값보다 작을때
            print('==========else')
            end = mid-1                  # 끝 인덱스를 증가
            print('start=',start)
            print('mid = ',mid)
            print('end = ',end)
            print('===========else')
        print('while finish=========')
    return end

print(binary_search(arr,target))
            
