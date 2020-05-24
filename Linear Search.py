def linear(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return i
    return -1
    
    
arr=list(map(int,input().split()))
n=int(input('Enter element'))
pos=linear(arr,n)
if pos!=-1:
    print('Value Found at',pos)
else:
    print('Not Found.!')
