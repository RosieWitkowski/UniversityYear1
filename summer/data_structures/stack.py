class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Stack:
    def __init__(self):
        self.top = None 
        self.size = 0

    # O(1) constant time
    def __len__(self):
        return self.size 

    # O(n) linear time 
    def __repr__(self):
        items = []
        current = self.top 
        while current:
            items.append(f"| {current.value} |")
            current = current.next 
        return '\n'.join(items)

    # O(1) constant time
    def is_empty(self):
        return self.top is None 

    # O(1) constant time 
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1 

    # O(1) constant time
    def pop(self):
        if not self.top:
            return None # Could be made a raise ValErr depending on context
        
        return_val = self.top.value
        # Removal works even if only one element in stack, as will point to next
        self.top = self.top.next
        self.size -= 1 

        return return_val 

    # O(1) constant time 
    def peak(self):
        if self.top:
            return self.top.value 
        else:
            return None 

if __name__ == "__main__":
    stackExample = Stack()
    print("Stack is empty? ", stackExample.is_empty()) # True 

    for i in range(5, 26):
        stackExample.push(i)

    print(stackExample) # calls repr dunder 
    print("Size: ", stackExample.size)
    print("Top item: ",stackExample.peak())
    """While can print size attribute, use peak to avoid attempting to print top.value where
    top is None (thus .value would error) """

    for i in range(5):
        stackExample.pop()
        # Note, can only pop top item - compare to LinkedList pop by index and delete by value

    print(stackExample)
    print("Size: ", len(stackExample)) # Note, can use built-in len as well due to dunder implementation
    print("Top item: ",stackExample.peak()) # Note, top item changed as pop removed from top LIFO

    print("Stack empty?", stackExample.is_empty()) # False 


    