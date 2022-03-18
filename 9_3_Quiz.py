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
1 30
2 20
5 23
3 40
9 1
8 50
7 13
"""
MAX_QUEUE_SIZE = 8

class Queue:
    def __init__(self) -> None:
        self.arr = [None]*MAX_QUEUE_SIZE
        #head: 가장 오래된 데이터의 위치
        #tail: 가장 최근 추가된 데이터의 위치
        self.head = 0
        self.tail = 0
    
    def is_empty(self):
        if self.head == self.tail:
            return True
        return False

    def is_full(self):
        if(self.tail+1)%MAX_QUEUE_SIZE == self.head:
            return True
        return False
    
    def enqueue(self,item):
        if self.is_full():
            print("큐에 더이상 데이터를 넣을 수 없습니다.")
        else:
            self.tail = (self.tail +1) % MAX_QUEUE_SIZE
            self.arr[self.tail] = item

    def dequeue(self):
        if self.is_empty():
            print("큐가 비어있습니다.")
        
        else:
            self.head = (self.head +1 ) % MAX_QUEUE_SIZE
            return self.arr[self.head]
totalT=0
midterm = 0
arrT = []

queue = Queue()

for num in range(7):
    id, time = map(int,input("고객의 아이디와 처리시간을 띄어쓰기로 구분해서 입력하시오").split())
    queue.enqueue([id,time])


while not queue.is_empty():
    id,time = queue.dequeue()
    totalT += time

    if(midterm + time) > 50:
        arrT = [id]
        midterm += (time -50)
    
    else: 
        midterm += time
        arrT.append(id)

print(arrT)
totalT += (totalT/50)*10
print(totalT,"분")