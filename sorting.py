arr = [5,9,3,1,2,8,4,7,6]

def bubbleSort(arr):
    for i in range(len(arr)): 
        for j in range(len(arr) - 1):   
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            
    for i in range(len(arr)):
        print(arr[i], end = " ")
        
def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
                
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
        
    for i in range(len(arr)):
        print(arr[i], end = " ")

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    for i in range(len(arr)):
        print(arr[i], end = " ")
        
