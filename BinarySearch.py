def binary_search(arr,target):
    low= 0
    high= len(arr)-1
    
    while low <= high:
        mid= (low + high ) //2
        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            low= mid +1
        else:
             high= mid-1
             
    return-1
            
#orderd list
arr=[1,3,5,7,9,11,13,15,17,19]
target = 13
result= binary_search(arr,target)
if result !=-1:
    print(f"the element is found at index:{result}")
else:
    print("the element is not present in the list")
        