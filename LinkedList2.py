#Defining a node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#this class is creating the linked list for us
class LinkedList:
    def __init__(self):
        self.head=None
#define a method that will do the work for us
    #it's inserting data at the beginning of the list
    def insertAtTheBeginning(self,new_data):
        #create a variable,call the class Node,parameter new data
        new_node = Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data, end=' ')
            #implement
            temp=temp.next
        print()
    def insertAtTheEnd(self,new_data):
        new_node = Node(new_data)
        #means that we have only one element in the list
        if self.head is None:
            self.head=new_node
            return None
            #if it is none,point to the new data that we are inserting
        temp=self.head


        while temp.next:
            temp=temp.next
        temp.next=new_node



if __name__=='__main__':
    llist = LinkedList()
    #call the method for inserting new elements
    #pass some data
    #The first shall be the last,fox is last
    llist.insertAtTheBeginning("Fox")
    llist.insertAtTheBeginning("Brown")
    llist.insertAtTheBeginning("Quick")
    llist.insertAtTheBeginning("The")
    #call the method to print
    llist.printLinkedList()
    llist.insertAtTheEnd("Jumps")
    llist.printLinkedList()