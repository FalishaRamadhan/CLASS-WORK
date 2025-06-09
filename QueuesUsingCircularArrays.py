class CIRCULARARRAYQUEUE:
    #Define the max no of elements that our queue will hold
    DEFAULT_CAPACITY= 10
    def __init__(self):
        #create an empty queue by _data: list filled with None values,the Array
        #_size:How many elements are at a given timestamp.Initialize to zero
        #_front:The index of first element.Initialize to zero
        #Create a list with default capacity slots,all filled with none.
        self._data = [None]
        #Keep track of how many elements are in the list
        self._size = 0
        #Keep track of the first element
        self._front = 0

    def __len__(self):
        #returns the size of an attribute created in the primary constructor
        return self._size

    def is_empty(self):
        #returns a boolean, denoted by ==.
        #returns true if array is empty or when it;s filled none,and false if it has at least one element
        return self._size == 0

    def first(self):
        #Behaves like peek method,returns the element at the front of the queue without removing it
        #Raises an exception if queue is empty
        if self.is_empty():
            raise Empty('Queue is empty')
        #The front element is at position self._front in our array
        return self._data[self._front]

    def dequeue(self):
        #removes and returns the first element in the queue
        if self.is_empty():
            raise Empty('Queue is empty')
        #Get the element at the front of the queue and save it in an attribute
        item_to_dequeue = self._data[self._front]
        #Clear the old front position
        self._data[self._front] = None
        #Move  the front pointer to the next position
        #The MODULO operator makes it wrap around,if we are at the last position then add 1.which will go back to 0
        self._front = (self._front + 1 ) % len(self._data)
        #Decrease the queue size by one
        self._size -= 1
        #the method should return the dequeued element
        return item_to_dequeue

    def enqueue(self,element):
        #Adding an element to the back of our queue
        #We calculate where  the back of the queue is using modulo arithmetic(front+size)%capacity
        #This automatically wraps around the array when needed
        #We will start with an is_full check,and if true,we increase the size of our queue
        if self._size == len(self._data):
            self._resize(2*len(self._data)) #double the capacity
        #Calculate where to put the new element at the back
        #if front=3,which means head is at 3, and size=4,which is the default capacity,then back position=(3+4)%10=7
        back_of_the_queue = (self._front  + self._size) % len(self._data)
        #Place the new element at the back position of our queue,where enqueueing takes place
        self._data[back_of_the_queue] = element
        #increase the size
        self._size +=1
#What if the queue is full , but we still need to enqueue?
    def _resize(self,new_capacity):
        #doubles the size of the queue only when there are no empty slots
        #The current size of the queue is multiplied by a factor specified by the user,in this case,new capacity
        #when we resize,we need to unwrap the circular array
        #and create a new linear arrangement starting from index 0 so that we can double the capacity quite easily
        #create a new,bigger array
        old_data = self._data #hold the existing data here
        self._data  = [None] * new_capacity
        #Copy all elements from the old array to the new one,from the front
        current_index=self._front
        for item in range(self._size):
            #Copy each element to the new array in order
            self._data[item]=old_data[current_index]
            #Move to the next element,remember to wrap around if necessary
            current_index= (current_index + 1) % len(old_data)
        #finally,we reset the front position to 0 since we've reorganized everything
        self._front=0
#This is the class with a custom exception message for empty queue operations
class Empty(Exception):
    #Raise exception when trying to access elements from an empty queue
    def __init__(self,message="Queue is empty"):
        self.message=message
        super().__init__(self.message)

if __name__=='__main__':
    #Create a new queue
    queue = CIRCULARARRAYQUEUE()
    print("Queues using circular arrays")
    print(f"The initial queue size is: {len(queue)}")
    print(f"Is queue empty? {queue.is_empty()}")
    #enqueue our queue
    print("\n Enqueueing our queue")
    elements_to_enqueue = ['Alice','Bob','William','Dorothy','Jessica']

    for person in elements_to_enqueue:
        queue.enqueue(person)
        print(f"Added{person}. Queue size is now: {len(queue)}")
        #Show the front element without removing it
        print(f"\n Person at the front of the line: {queue.first()}")
        #Remove some elements dequeue operations,then return it.
        print("\n Serving people from the front queue:")
    for i in range(3):
        served_person = queue.dequeue()
        print(f"Served: {served_person}. Queue size is now: {len(queue)}")
        #To demo the circular nature,we can introduce an overflow to see if it behaves correctly
        print("\n Adding more people to introduce a wrap around in the array")
        more_people = ['Frank','Linda','Ford']

    for person in more_people:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")
    #Show what's left in the queue
    print(f"\n Person currently at the front: {queue.first()}")
    print(f"Total people still in queue: {len(queue)}")
    #Demonstrate the wrap around by showing internAal state
    print(f"\n Internal details:")
    print(f"Front index: {queue._front}")
    print(f"Array contents: {queue._data}")
    #None values are empty slots in a circular array
