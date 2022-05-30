MAX_STACK_SIZE=3

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

stack = Stack()

stack.pop()

stack.push("data 1")
stack.push("data 2")
stack.push("data 3")

print("pop:",stack.pop())
print("pop:",stack.pop())
print("pop:",stack.pop())
print("pop:",stack.pop())
/*test*/
