"""
50분을 일하면 10분을 쉬어야 한다
>Work = 50 Rest = 10
이로 인해 문의 사항을 받기 이전 고객의 아이디와 처리 예상 시간을 먼저 받고
>고객의 아이디 = custId , 처리 예상 시간 = exeTime
신청한 순서대로 처리
>FIFO

아래의 순서대로 고객들의 문의 요청이 들어오게 되었다고 가정할 때,

한 번의 근무 시간( 50분 )동안 처리한 고객의 아이디를 한 줄씩 출력하고,
>print(id in 50min)
모든 요청을 처리했을 때 소요되는 총 시간을 출력하세요.
>print(total time 2 execute including break hour) 
❗ 쉬는시간도 총 시간에 포함됩니다.
"""
MAX_QUEUE_SIZE = 50
totalT=0
idList = []
timeList = []
for num in range(0,int(input("transaction 단위를 입력하세요"))):
    a, b = input("고객의 아이디와 처리시간을 띄어쓰기로 구분해서 입력하시오").split(" ")
    idList.append(int(a))
    timeList.append(int(b))
    #print(mydict[a])
print('idList = ',idList)
print('timeList = ',timeList)

class Queue:
    def __init__(self) -> None:
        self.arr = [None]*MAX_QUEUE_SIZE
        self.head = 0
        self.tail = 0
    
    def is_empty(self):
        if self.head == self.tail:
            return True
        return False
    
    def is_full(self):
        if(self.tail+1)%MAX_QUEUE_SIZE ==self.head:
            return True
        return False

    def enqueue(self,item):
        if self.is_full:
            pass

    
