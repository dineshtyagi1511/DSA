def BinarySearch(arr,target):
    size =len(arr)
    start= 0
    end = size-1
    while start<= end:
        mid= (start+end)//2
        if arr[mid]==target:
            return mid
        if arr[mid] >target :
            end = mid-1
        if arr[mid]<target:
            start = mid+1 

arr =[7,8,47,54,69,78,45]
target = 69
BinarySearch(arr,target)
print(BinarySearch(arr,target))