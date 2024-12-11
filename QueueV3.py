'''
Implementation Queue

This  script contain three functions

1. enqueue
2. dequeue
3. peek 

User will be given choice to perform action from above three.

Script will be kept running until user chooses to exit.
'''
class Queue:

    '''
    Like a stack, the queue is a linear data structure that stores items in a 
    First In First Out (FIFO) manner. With a queue, the least recently added 
    item is removed first. A good example of a queue is any queue of 
    consumers for a resource where the consumer that came first is served first.
    Time Complexity : O(1)
    '''

    def __init__(self, max_size):

        self.queue = []
        self.max_size = max_size #max_size (int): The maximum number of elements the queue can hold.
        self.count = 0

    def enqueue(self, element):
        '''
        This function will append/add new element in queue.
        '''

        if (self.count) == (self.max_size):
            print("Queue is full! Cannot add more elements")

        
        elif length(self) >= self.max_size:
            print("Queue is full! Cannot add more elements") 

        else:
            self.queue = self.queue + [element] #The element to be added to the queue.
            self.count +=1  # if count is equal max_size it will not enque new element
            print(f"{element} is added in queue")
            print(f"current queue: {self.queue}")



    def dequeue(self):
        '''
        This function will remove element from the queue.
        '''
        if not self.queue:
            print("Queue is empty!! Cannot dequeue")
        else:
            self.queue = self.queue[1:]
            print(self.queue)

    def peek(self):
      
        if not self.queue:
            print("Queue is empty! No elements to peek.")
        elif length(self) == 0:
            print("queue is empty")
        else:
            print(f"The front element is: {self.queue[0]}") 



def main():
    '''
    
    Main function to interact with the Queue class.
    Allows the user to perform enqueue, dequeue, and peek operations until they choose to exit.
    
    If the max_size is not int or non-negative or string number it will
     not except that value.
    '''



    while True:
        try:
            max_size = int(input("Enter the maximum size of the queue: "))
            if max_size <= 0:
                raise ValueError("Queue size must be a positive integer.")
            break

        except ValueError:
            print(f"Invalid input!! Please try again.")

    queue = Queue(max_size)

    """
    The user can choose to:
    1. Enqueue an element onto the stack.
    2. Dequeue an element from the stack
    3. View the front element (peek)
    4. Exit the program
    """

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            element = input("Enter the element to enqueue: ")
            queue.enqueue(element)

        elif choice == '2':
            queue.dequeue()

        elif choice == '3':
            queue.peek()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":

    def length(self):
        
        count=0
        for i in self.queue:
            count += 1
        return count


    main()

