'''
Bubble sort

Use a static list 

Use bubble sort to sort this list
'''

def bubble_sort(arr):
    '''
    Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, 
    compares adjacent elements, and swaps them if they are in the wrong order. 
    It is named "Bubble Sort" because smaller elements "bubble" to the top of the list.
    '''
    n = len(arr)
    
    '''
    Let's break down the steps of the Bubble Sort algorithm:

    1. Iterate through the list: Start from the beginning of the list and compare each pair of adjacent 
       elements.
    2. Compare and swap: If the elements are in the wrong order, swap them. This ensures that the larger 
       element "bubbles up" and the smaller one moves down.
    3. Continue iterating: Repeat the process for each pair of adjacent elements until the end of the 
       list is reached.
    4. Repeat until sorted: Keep iterating through the list until no more swaps are needed. 
       At this point, the list is sorted.
    '''
    for i in range(n):
        swapped = False

        
        for j in range(0, n-i-1):

          # Swap if the element found is greater than the next element    
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]  # Sample list to be sorted 
    print("original array: \n", arr)

    bubble_sort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
