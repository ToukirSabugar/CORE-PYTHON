'''
Implementation of Stack

This script contain three functions
1. push
2. pop
3. peep

User will be given choice to perform action from above three.

Script will be kept running until user chooses to exit.
'''
class Stack:


    """
        A class to represent a stack data structure.
        A stack is a linear data structure that stores items in a 
        Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. 
        In stack, a new element is added at one end and an element is 
        removed from that end only. 
        The insert and delete operations are often called push and pop.
        top() / peek() – Returns a reference to the topmost element of the stack 
        – Time Complexity: O(1)

    """
    def __init__(self, max_size):


        '''
        initialize the empty stack

        args:
        max_size(int): max_size of the stack 

        '''
        self.stack = []
        self.max_size = max_size


    def push(self, element):
        '''
        This function is used to append element in stack.
        '''
        if length(self) >= (self.max_size):
            print("error stackoverflow, cannot push more element")
        else:
            self.stack = self.stack + [element];
            print(f"{element} pushed to stack")
            print(f"Current stack: {self.stack}")

    def pop (self):
        '''
        This function removes element from the stack.

        '''

        if not self.stack:
            print("stack is empty")
        else:
            self.stack = self.stack[:-1] 
            print(f"Current stack: {self.stack}")

    def peep(self):
        '''
        This function will give you top element from the stack
        '''
        if not self.stack:
            print("Error: Stack is empty!")
        else:
            print(f"Top element is: {self.stack[-1]}")
            print(f"Current stack: {self.stack}")


def get_valid_choice():
    '''
    Ask the user for valid choice
    '''
    
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice in range(1, 5):
                return choice
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_valid_stack_size():
    '''
    Ask the user for valid stack size
    '''

    while True:
        try:
            size= int(input("enter the size of stack: "))
            if size > 0:
                return size
            else:
                print("Invalid input! enter positive integer for size")

        except ValueError:
            print("Invalid input! enter valid integer")

def get_dynamic_element():

    
    user_input = input("Enter an element to push: ")
    return user_input


def main():



    stack_size = get_valid_stack_size()
    stack = Stack(stack_size)

    """
    
    
    The user can choose to:
    1. Push an element onto the stack
    2. Pop an element from the stack
    3. View the top element (peep)
    4. Exit the program
    """

    while True:
        print("\n enter the choice")
        print("1 for push")
        print("2 for pop")
        print("3 for Peep")
        print("4 for exit")

        choice = get_valid_choice()

        if choice == 1:
            element = get_dynamic_element()
            stack.push(element)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peep()
        elif choice == 4:
            print("Exiting program.")
            break

if __name__ == "__main__":


    def length(self):
        
        count=0
        for i in self.stack:
            count += 1
        return count

    main()



