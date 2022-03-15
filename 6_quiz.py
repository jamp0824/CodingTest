def validate_brace_pair(str):
    stack = []
    #문자열 -> stack 배열에 넣음
    for i in str:
       stack.append(i)
    print(stack)
    print('>',end='')
    #stack 배열의 길이 
    length = len(stack)
    result = 0
    # 문자열이 종료되었을 때, 여는 중괄호의 개수와 닫는 중괄호의 개수가 같아야한다.
    if (length%2 ==0):
        for i in range(length):
            #{ = -1 , #} = +1
            if stack.pop() == '{':
                result -= 1
                # 문자열의 처음부터 끝까지 여는 중괄호의 개수가 같거나 많아야 한다.
                if result<0:
                    print('유효하지 않은 중괄호 쌍입니다.')
                    return 
                else:
                    continue
            else:
                result += 1
                continue
        print('유효한 중괄호 쌍입니다.')        
            
    else: 
        print('유효하지 않은 중괄호 쌍입니다.')    
    
validate_brace_pair("{{}}{}")
validate_brace_pair("{}}{{}")
validate_brace_pair("{{}")
validate_brace_pair("{{{}}}")
validate_brace_pair("}{{{}}}{")
