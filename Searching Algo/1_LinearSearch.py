def LinearSearch(arr,target):
    size = len(arr)
    for i in range(size):
       if arr[i]==target :
            return i
    return -1 

arr= [78,56,74,848,17,2,54,8]
    
LinearSearch(arr,2)
print(LinearSearch(arr,8))