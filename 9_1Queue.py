MAX_QUEUE_SIZE = 5

class Queue:
    def __init__(self) -> None:
        self.arr = [None]*MAX_QUEUE_SIZE
        #HEAD: 가장 오래된 데이터의 위치
        #tail: 가장 최근 추가된 데이터의 위치
        self.head = -1
        self.tail = -1

    def is_empty(self):
        if self.head == self.tail:
            return True
        return False

    def is_full(self):
        if self.tail >= MAX_QUEUE_SIZE-1:
            return True
        return False
    
    def enqueue(self,item):
        if self.is_full():
            print("큐에 더이상 데이터를 넣을 수 없습니다.")
        else:
            self.tail+=1
            self.arr[self.tail] = item

    def dequeue(self):
        if self.is_empty():
            print("큐가 비어있습니다.")
            return None
        else:
            self.head += 1
            return self.arr[self.head]

queue = Queue()
# queue.enqueue("data1")
# queue.enqueue("data2")
# queue.enqueue("data3")

# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)