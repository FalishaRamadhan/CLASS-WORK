#Implementing a stack using linked lists
#Node for linked list
class StackNode:
    def __init__(self,value):
        self.value = value #Store the nodes data
        self.next = None #Pointer to the next node(below in stack)
    #Stack implemented using LL
class LinkedListStack:
        def __init__(self):
            self.top= None #points to the top node in the stack
        def is_empty(self):
            #Stack is empty if top pointer in None
            return self.top is None
        def push(self,value):
            #create a new node with the value
            new_node = StackNode(value)
            #New node's next pointer should point to the current top node
            new_node.next = self.top
            #Update top pointer to new node(new top of stack)
            self.top= new_node
        def pop(self):
            #If stack is empty raise error
            if self.is_empty():
                raise Exception("Cannot pop from empty stack")
            #Retrieve value from top node
            popped_value = self.top.value
            #move top pointer to next node down the stack
            self.top = self.top.next
            #Return popped value
            return popped_value
        def peek(self):
            #Return the top element without removing it
            if self.is_empty():
                raise Exception("Cannot peek from empty stack!")
            return self.top.value
        def display(self):
            #print stack from top to bottom
            current = self.top #start at the top of the stack
            values = []
            while current: #Loop through each node as long as it's not none
                values.append(str(current.value)) #change the values to string and add it to the list
                current=current.next #move to the next node
            print("Stack from top to bottom:," ,  " -> ".join(values)) #Join all values with -> and print them in top-to-bottom order.
#Example usage
if __name__=="__main__":
    stack_ll = LinkedListStack()
    stack_ll.push(5)
    stack_ll.push(10)
    stack_ll.push(15)
    stack_ll.display()  #stack from top to bottom
    print("Peek top:" ,stack_ll.peek())
    print("Pop:" , stack_ll.pop())
    stack_ll.display()


