#Implementing a stack using Lists
stack = [] #empty stack

stack.append(10) #add 10 to the top of the stack
stack.append(20) #Add 20 to the top of the stack
stack.append(30) #Add 30 to the top of the stack

print("Stack after pushes:", stack)  #[10,20,30]

#peek at top element (last element in the list)
top_element = stack[-1] #Access last element without removing it
print("Top element is:", top_element)  #30

#check if stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")

#Implementing a stack with all key operations in a custom class
class SimpleStack:
    def __init__(self):
#Initialize an empty list to hold stack elements
        self.items=[]
    def is_empty(self):
        #Return true if the stack has no elements,otherwise return false
        return len(self.items)==0
    #add item to the top of the stack
    def push(self,item):
        self.items.append(item)
    #remove an item from the top and return it
    def pop(self):
        #if stack is empty return an error to avoid an invalid operation
        if self.is_empty():
            raise Exception("Cannot pop an empty stack")
        return self.items.pop()
    #Peek: return the top item without removing it
    def  peek(self):
        #raise an error if stack is empty
        if self.is_empty():
            raise Exception("Stack is empty")
        #The top most element is the last to be pushed
        #since actual size of the list is greater than the position by one,
        #minus one return last elements(-1 refers to the last element on the list in python)
        return self.items[-1]
    #Size: return the number of all items in the stack
    def size(self):
        return len(self.items)
    def print_stack(self):
        #print all items in the stack from bottom to top
        print("Stack from bottom to top:", self.items)
        return
#Main meal
if __name__=='__main__':
    #instantiate the class stack by creating an object for it
    stack1 = SimpleStack()
    #Then push some elements
    stack1.push(1000)
    stack1.push(2000)
    stack1.push(3000)
    #print the elements
    stack1.print_stack()
    #peek top element
    print("Top element:", stack1.peek())  #3000
    #Pop elements
    print("Popped:", stack1.pop())  #3000
    stack1.print_stack() #[1000,2000]
    #check if empty
    print("Is stack empty?", stack1.is_empty())
    #pop all to empty
    stack1.pop()
    stack1.pop()
    print("Is stack empty after popping all?", stack1.is_empty())





