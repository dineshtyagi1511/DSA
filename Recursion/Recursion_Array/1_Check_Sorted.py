def CheckSorted1(arr):
    if len(arr)==0 or len(arr)==1:
        return True 
    ans = CheckSorted1(arr[1:])

    if arr[0]<arr[1]:
        return True
    else:
        return False
    
arr= [4,5,6,78,178,179,200]
 


def CheckSorted2(arr):
    if len(arr)==0 or len(arr)==1:
        return True
    if arr[0]>=arr[1]:
        return False
    return CheckSorted2(arr[1:])

arr= [488,5,6,78,178,179,200]
print(CheckSorted2(arr))
