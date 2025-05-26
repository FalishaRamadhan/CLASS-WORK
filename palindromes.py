#This imports deque from Python's collections module, which is a double-ended queue ideal for implementing a queue (FIFO behavior).
from collections import deque

class PalindromeChecker:
    def __init__(self):
        # Use list as a stack (LIFO)
        self.stack = [] #initialize an empty stack
        # Use deque as a queue (FIFO)
        self.queue = deque() #initialize a deque

    def push_word(self, word):
        # Push character onto stack
        self.stack.append(word)

    def enqueue_word(self, word):
        # Enqueue character into queue
        self.queue.append(word)

    def pop_word(self):
        # Pop character from stack
        return self.stack.pop()

    def dequeue_word(self):
        # Dequeue character from queue
        return self.queue.popleft() #removes and returns the first element from the queue


# Read input
s = input("Enter a word: ").lower()

# Create object
checker = PalindromeChecker()

# Load all characters into both stack and queue
for word in s: #loops through each character in the string,pushes it to the stack and enqueues it to the queue
    checker.push_word(word)
    checker.enqueue_word(word)

# Check for palindrome by comparing characters from stack and queue
is_palindrome = True
for i in range(len(s) // 2): #check half the characters because we compare both ends
    if checker.pop_word() != checker.dequeue_word():
        is_palindrome = False
        break
#Pops from the stack and dequeues from the queue.

#If they don’t match, the string is not a palindrome, so we set the flag to False and exit the loop.

# Output result
if is_palindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")
