'''
Selection sort

Use a static list 

Use selection sort to sort this list
'''



def selection_sort(arr):
    '''
    The selection sort algorithm sorts an array by repeatedly finding the minimum element 
    (considering ascending order) from unsorted part and putting it at the beginning.
    '''
    n = len(arr)
    for i in range(n - 1):
      
        
        min_idx = i
        
        
        for j in range(i + 1, n):
              # select the minimum element in every iteration
            if arr[j] < arr[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
                 # swapping the elements to sort the array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def is_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    is_array(arr)
    
    selection_sort(arr)
    
    print("Sorted array: ", end="")
    is_array(arr)
