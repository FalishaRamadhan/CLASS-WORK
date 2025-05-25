#all comments refer to the line below in my codes
class LinkedListNode:
    #__init__ method is a constructor,it initializes our attributes
    #When you put the next node to none,it is an optional parameter,None is an optional
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode
#a node will be an object
#Here,they are not yet linked,for all of them,the pointer is set to none
#Every data item exists independently,we have memory for every data item
node1=LinkedListNode("1")
node2=LinkedListNode("2")
node3=LinkedListNode("3")
node4=LinkedListNode("4")
node5=LinkedListNode("5")
node6=LinkedListNode("6")
node7=LinkedListNode("7")
node8=LinkedListNode("8")
node9=LinkedListNode("9")
node10=LinkedListNode("10")
#very manual way of creating linked lists
node1.nextNode=node2
node2.nextNode=node3
node3.nextNode=node4
node4.nextNode=node5
node5.nextNode=node6
node6.nextNode=node7
node7.nextNode=node8
node8.nextNode=node9
node9.nextNode=node10
#We now need to define the head
currentNode=node1
#traversing the list
#Difference btn for loop and while loop
while True:
    print(currentNode.value," >>> " , end='')
    #The condition only holds if:
    #we have traversed to the end of the list
    #Or we have only one element in the list
    if currentNode.nextNode is None:
        print("None")
        break #break when the next node is none
    #implement the value of the current node to point to the next node
    currentNode=currentNode.nextNode

















