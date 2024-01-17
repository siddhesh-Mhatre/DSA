arr=[7,8,3,1,2]

for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1] , arr[j]
print(arr)


# time complexity 
# worst case -> n-1 
# O(n^2)
# pair wice sawp