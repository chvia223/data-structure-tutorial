"""
Queues - Problem 1

Scenario: 
Taking inspiration from the Apple scenario described, we are a tech startup that's releasing an all new phone.
We decided we want to do a preorder system instead of a physical line so people can go about their lives. This
program will take in orders and then once preorders close, we will fulfill each order moving from first to last.
"""

class Queue:
    """
    A basic implementation of a Queue
    """

    def __init__(self):
        """
        Start with an empty queue.
        """
        self.queue = []

    def enqueue(self, value):
        """
        Add an item to the queue
        """
        self.queue.insert(0, value)

    def dequeue(self):
        """
        Remove the next item from the queue. 
        """
        value = self.queue[0]
        del self.queue[0]
        return value

    def is_empty(self):
        """
        Check to see if the queue is empty.
        """
        return len(self.queue) == 0
    
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """
        Provide a string representation for this object.
        """
        result = "["
        for item in self.queue:
            result += str(item)
            result += ", "
        result += "]"
        return result



# Test Cases

# Test 1
# Scenario: Preorders have opened and we need to be able to take orders! Make sure the queue is working as expected.

# Exepcted Result: Dave -> 1, Sally -> 2, Deborah -> 1, Shane -> 3
print("Test 1")
print("=====================")
preorder_queue = Queue()
preorder_queue.enqueue(("Dave", 1))
preorder_queue.enqueue(("Sally", 2))
preorder_queue.enqueue(("Deborah", 1))
preorder_queue.enqueue(("Shane", 3))

while len(preorder_queue) > 0:
    order = preorder_queue.dequeue()
    print(f"Name: {order[0]:10} -> Quantity: {order[1]}")

print("=====================")
print()

# Test 2
# Scenario: We want to know how many orders we need to fulfill. How long is our queue?

# Exepcted Result: 4
print("Test 2")
print("=====================")
preorder_queue = Queue()
preorder_queue.enqueue(("Dave", 1))
preorder_queue.enqueue(("Sally", 2))
preorder_queue.enqueue(("Deborah", 1))
preorder_queue.enqueue(("Shane", 3))

# Add code here.

print("=====================")
print()

# Test 3
# Scenario: We want our program to tell us when the queue is empty using the is_empty function.
#           If the queue is empty the program should print "The queue is finished."

# Exepcted Result: "The queue is finished."
print("Test 2")
print("=====================")
preorder_queue = Queue()
preorder_queue.enqueue(("Dave", 1))
preorder_queue.enqueue(("Sally", 2))
preorder_queue.enqueue(("Deborah", 1))
preorder_queue.enqueue(("Shane", 3))

# Add code here

print("=====================")
print()