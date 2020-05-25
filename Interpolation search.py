#complexity in average case log(log n)
#complexity in worst case O(n)

def interpolation(arr,n):
    arr.sort()
    print('sorted arr',arr)
    left=0
    right=len(arr)-1
    while left<=right:
        mid=left+((right-left)//(arr[right]-arr[left]))*(n-arr[left])
        if arr[mid]==n:
            return mid
        elif arr[mid]>n:
            right=mid-1
        elif arr[mid]<n:
            left=mid+1
        else:
            return -1

arr=list(map(int,input().split()))
n=int(input('Enter Element '))
pos=interpolation(arr,n)
if pos!=-1:
    print('Element found at',pos)
else:
    print('Element not found')