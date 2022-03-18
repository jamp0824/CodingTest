MAX_QUEUE_SIZE = 5

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
queue.enqueue("data 1")
queue.enqueue("data 2")
queue.enqueue("data 3")

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

queue.enqueue("data 4")
queue.enqueue("data 5")
queue.enqueue("data 6")


print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())



    
