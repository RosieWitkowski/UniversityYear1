class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None 
        self.size = 0  

    # O(1) constant time 
    def __len__(self):
        return self.size 

    # O(n) linear time 
    def __repr__(self):
        q = "FRONT "
        current = self.front 
        while current: 
            q += f" | {current.value}"
            current = current.next 
        return q + " REAR"

    # O(1) constant time 
    def enqueue(self, value):
        new_node = Node(value)
        if not self.rear:
            # Empty queue
            self.front = self.rear = new_node
        else: 
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1 

    # O(1) constant time 
    def dequeue(self):
        if not self.front: 
            return None 
        removed_val = self.front.value 
        self.front = self.front.next 
        if self.front is None:
            # Last element (rear) removed 
            self.rear = None  
        self.size -= 1 
        return removed_val 

    # O(1) constant time 
    def peak(self):
        if not self.front:
            return None 
        return self.front.value 

    # O(1) constant time 
    def is_empty(self):
        return self.front is None 

if __name__ == "__main__":
    qExample = Queue()
    print(qExample) # FRONT REAR
    print("Peak: ", qExample.peak()) # None 
    print("Length: ", len(qExample)) # 0
    print("Is empty? ", qExample.is_empty()) # True 

    for i in range(4, 15):
        qExample.enqueue(i)

    print(qExample) 
    print("Peak: ", qExample.peak()) # 4
    print("Length: ", len(qExample)) # 11
    print("Is empty? ", qExample.is_empty()) # False

    for _ in range (3):
        qExample.dequeue()

    print(qExample)
    print("Peak: ", qExample.peak()) # 7
    print("Length: ", len(qExample)) # 8
    print("Is empty? ", qExample.is_empty()) # False 

    print("Removing remaining elements... ")
    for _ in range(7):
        qExample.dequeue()
    print("Last element removed: ", qExample.dequeue()) # 14
    print(qExample.is_empty()) # True 

    
    print("Element removed from empty queue: ", qExample.dequeue()) # None 
    

    
