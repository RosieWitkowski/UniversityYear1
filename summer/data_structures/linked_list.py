class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    # O(n) linear time
    def __repr__(self) -> str:
        last = self.head
        if not last:
            return "[]"
        repr_str = f"[{last.value}"
        while last.next:
            last = last.next
            repr_str += f", {last.value}"
        return repr_str + "]"

    # O(n) linear - potential for O(1) constant time 
    """ 
    Note: Can become O(1) constant if hold size attribute in constructor, then 
    update in each method that alters it
    Useful if size likely to be accessed freqently, else can be unneccesary
    code bulk - up to context
    """
    def __len__(self) -> int:
        last, count = self.head, 0 
        while last:
            count += 1 
            last = last.next 
        return count 


    # O(n) linear time
    def __contains__(self, value: int) -> bool:
        last = self.head 
        while last:
            if last.value == value:
                return True 
            last = last.next 
        return False 

    # O(n) linear time
    def get(self, index):
        if not self.head: 
            return f"List empty, index not found." 
            """Note to self: could be argued wether to raise an exception or return error - 
            dependant on context of linked list's use"""
        
        last = self.head
        for _ in range(index):
            if not last.next:
                return f"Index not found."
            last = last.next 
        return last.value


    # O(n) linear time
    def append(self, value: int):
        last = self.head
        if not last:
            # Empty list, new node is the head
            self.head = Node(value)
        else:
            while last.next:
                last = last.next 
            # Point last node of the list to the new node
            last.next = Node(value) 

    # O(1) constant time
    def prepend(self, value: int):
        new_node = Node(value)
        # Even if list is empty, will point to None - functioning correctly
        new_node.next = self.head
        self.head = new_node 

    # O(n) linear time
    def insert(self, index: int, value: int) -> str:
        if index == 0:
            self.prepend(value) 
        else:
            last = self.head 
            if not last:
                return f"Insertion of {value} at index {index} failed, due to index out of range."
            
            for _ in range(index-1):
                last = last.next 
                if not last:
                    return f"Insertion of {value} at index {index} failed, due to index out of range."

            # Ensure change new_node pointer first - to maintain last's original pointer (else next node lost)
            new_node = Node(value)
            new_node.next = last.next
            last.next = new_node
            return f"Inserted {value} at index {index}."

    # O(n) linear time 
    def delete(self, value) -> str:
        # Note, in some lower level languages like C - would need to free memory (and malloc when creating)
        last = self.head 
        if not last:
            return f"Value {value} not found"
        elif last.value == value:
            self.head = last.next # Remove head
            return f"Value {value} deleted"
        
        while last.next:
            if last.next.value == value:
                last.next = last.next.next # Delete middle 
                return f"Value {value} deleted" 
            last = last.next 
        return f"Value {value} not found"

    # O(n) linear time
    def pop(self, index) -> str:
        last = self.head
        if not last:
            return f"Nothing to remove"
        elif index == 0:
            self.head = last.next 
            return f"Removed item at index {index}"
        
        for _ in range(index-1):
            if not last.next:
                return f"Index {index} not found."
            last = last.next 
        last.next = last.next.next 
        return f"Deleted item at index {index}"


if __name__ == "__main__":
    class_scores = LinkedList()

    class_scores.append(50)
    class_scores.append(80)
    class_scores.append(32)

    print(class_scores)

    print("+== Testing get ==+")
    score = class_scores.get(2)
    print(score) # 32
    print(f"Score at index 100: ", class_scores.get(100)) # Index not found

    print("+== Testing insert ==+")
    print(class_scores.insert(20, 10)) # Insertion failed
    print(class_scores.insert(2, 10)) # Insertion pass

    print("+== Testing delete ==+")
    print("50 present: ", 50 in class_scores) # True
    print(class_scores.delete(50)) # Value 50 deleted
    print("50 present: ", 50 in class_scores) # False

    print("+== Testing pop ==+")
    print("Updated class scores: ", class_scores)
    
    print("Index 1: ", class_scores.get(1)) # 10
    print(class_scores.pop(1)) # Deleted item at index 1 
    print("Index 1: ", class_scores.get(1)) # 32

    print(class_scores.pop(100)) # Index 100 not found

    print("+== Testing dunder len and contains, using for in ==+")
    tests_entered = len(class_scores)
    print(f"Number of tests entered for analysis: {tests_entered}")

    print("Checking for specific results...")
    print('apple' in class_scores) # False
    print(50 in class_scores) # True
    print("Checks complete!")

        