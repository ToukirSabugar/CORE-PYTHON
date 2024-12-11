'''
Implementation Circular Queue

This script contain four functions

1. Front: Get the front item from queue.

2. Rear: Get the last item from queue.

3. enqueue(value)

4. dequeue()

User will be given choice to perform action from above four.

Script will be kept running until user chooses to exit.
'''
class Circular_Queue:
    '''
    Circular Queue:-A circular queue is a special type of queue in data structures 
    where the last position is connected back to the first position, forming a circle. 

    This means when the queue reaches the end, it wraps around to the beginning. 
    This helps use all available space efficiently without leaving any gaps. 
    '''
    def __init__(self, max_size):
        self.circular_queue_list = [None] * max_size  
        self.max_size = max_size
        self.front = 0
        self.rear = 0
        self.size = 0  # To track the current number of elements in the queue

    def enqueue(self, item):
        '''
    Add an element to the rear of the circular queue.

    Steps:
    Check if the queue is full. If (rear + 1) % size == front, the queue is full.

    If the queue is not full, update the rear pointer to (rear + 1) % size.

    Insert the new element at the rear position.

    If the queue was initially empty (i.e., front was -1), set front to 0.
        '''

        if self.size == self.max_size:
            print("Queue is Full")
        else:
            self.circular_queue_list[self.rear] = item
            self.rear = (self.rear + 1) % self.max_size
            self.size += 1
            
            print("\n[", end = "")
            for i in self.circular_queue_list:
                if i != None:
                    print(f"{i}, ", end ="")
            print("]")


    def dequeue(self):

        '''
    Remove an element from the front of the circular queue.

    Steps:

    Check if the queue is empty. If front == -1, the queue is empty.

    If the queue is not empty, remove the element at the front position.

    Update the front pointer to (front + 1) % size.

    If the queue becomes empty after the dequeue operation (i.e., front equals rear),
     reset both front and rear to -1.

        '''
        if self.size == 0:
            print("Queue is Empty")
        else:
            self.circular_queue_list[self.front] = None  
            self.front = (self.front + 1) % self.max_size
            self.size -= 1

            print("\n[", end = "")
            for i in self.circular_queue_list:
                if i != None:
                    print(f"{i}, ", end ="")
            print("]")

    def get_front(self):

        '''
        View the front element without removing it from the circular queue.

        Steps:
        Check if the queue is empty. If front == -1, the queue is empty.

        If the queue is not empty, return the element at the front position.

        '''
        if self.size == 0:
            print("Queue is Empty")
        else:
            print("Front item:", self.circular_queue_list[self.front])

    def get_rear(self):

        '''
        Check if the circular queue is empty.

        Steps:
        The queue is empty if front == -1.

        '''

        if self.size == 0:
            print("Queue is Empty")
        else:
            print("Rear item:", self.circular_queue_list[(self.rear - 1 + self.max_size) % self.max_size])

def main():

    while True:
        try:
            max_size = int(input("enter the valid size of queue: "))
            if max_size < 1:
                raise ValueError("Queue size must be positive.")
            break

        except ValueError:
            print("Invalid input! please try again")


    circular_queue = Circular_Queue(max_size)
    '''
     
    The user can choose to:
    1. Enqueue an element onto the stack.
    2. Dequeue an element from the stack
    3. View the front element (peek)
    4. View the rear element
    5. Exit
    
    '''

    while True:
        print("\nEnter your choice")
        print("1 for enque")
        print("2 for deque")
        print("3 for front")
        print("4 for rear")
        print("5 for exit")

        c = input("enter the choice: ")

        if c == '1':
            item = input("Enter the element: ")
            circular_queue.enqueue(item)

        elif c == '2':
            circular_queue.dequeue()

        elif c == '3':
            circular_queue.get_front()

        elif c == '4':
            circular_queue.get_rear()

        elif c == '5':
            print("Exiting program")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
