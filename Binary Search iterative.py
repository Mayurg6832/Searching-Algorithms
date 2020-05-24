def binary(arr,n):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==n:
            return mid
        elif arr[mid]>n:
            right=mid-1
        elif arr[mid]<n:
            left=mid+1
    return -1
  
arr=list(map(int,input().split()))
n=int(input('Enter Element'))
pos=binary(arr,n)
if pos!=-1:
    print('Element found at',pos)
else:
    print('Not found')

        
