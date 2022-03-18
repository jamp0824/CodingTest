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

queue = Queue()

for i in range(7):
    n,time = map(int, input().split())
    queue.enqueue([n,time])

total =0
mid_time = 0
n_arr = []

while not queue.is_empty():
    n,time = queue.dequeue()
    total += time
    print('total = ',total)
    print('0time = ',time)
    if (mid_time + time) > 50:
        print('1mid_time = ',mid_time)
        print('2time = ',time)
        print(n_arr)
        n_arr = [n]
        print('3[n]',[n])
        print('4n_arr = ',n_arr)
        mid_time += (time-50)
        print('5mid_time = ',mid_time)
    
    else:
        print('6mid_time = ',mid_time)
        mid_time += time
        n_arr.append(n)
        

print(n_arr)
t = (total/50)*10
print(t)
total += (total/50)*10
print("총 소요시간", total, "분")
    
