def validate_brace_pair(str):
  # 문자열의 처음부터 끝까지 여는 중괄호의 개수가 같거나 많아야 한다.
  # 문자열이 종료되었을 때, 여는 중괄호의 개수와 닫는 중괄호의 개수가 같아야한다.

  # { { } }는 여는 중괄호가 먼저 2개 나오고, 닫는 중괄호가 2개 
  print('유효한 중괄호 쌍입니다.')
  #  } { 는 여는 중괄호와 닫는 중괄호 모두 1개이므로 갯수는 올바르지만,
  #  닫는 중괄호가 먼저 나오기 때문에
  print('유효하지 않은 중괄호 쌍입니다.')
  
validate_brace_pair("{{}}{}")
validate_brace_pair("{{}")
validate_brace_pair("{{{}}}")
validate_brace_pair("}{{{}}}{")

#def validate_brace_pair(self): self 단위 팝 push 
MAX_STACK_SIZE=100

class Stack:
    def __init__(self):
        self.arr=[None]*MAX_STACK_SIZE
        self.top=-1
    
    def is_full(self):
        if self.top>=MAX_STACK_SIZE-1:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            print("스택이 가득 찼습니다.")
        else:
            self.top +=1
            self.arr[self.top] = value
    
    def is_empty(self):
        if self.top<0:
            return True
        else:
            return False

    def pop(self):
        if(self.is_empty()):
            print("스택이 비어있습니다.")
        else:
            value = self.arr[self.top]
            self.top-=1
            return value
    
    
