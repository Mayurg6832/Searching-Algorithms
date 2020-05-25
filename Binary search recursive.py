def binary_recur(arr,n,left,right):
    arr.sort()
    if right>=left:
        mid=(left+right)//2
        if arr[mid]==n:
            return mid
        elif arr[mid]<n:
            return binary_recur(arr,n,mid+1,right)
        elif arr[mid]>n:
            return binary_recur(arr,n,left,mid-1)
    else:
        return -1

arr=list(map(int,input().split()))
n=int(input('Enter element'))
pos=binary_recur(arr,n,0,len(arr)-1)
if pos!=-1:
    print('Element found at',pos)
else:
    print('Not Found')