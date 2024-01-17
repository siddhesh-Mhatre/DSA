# set smallest number and place in 
arr = [7,8,3,1,2]

for i in range(len(arr)-1):
    smallest=i
    for j in range(i+1,len(arr)): # bcz its staring
        if(arr[smallest] > arr[j]):
            smallest=j
    arr[smallest] , arr[i] = arr[i] , arr[smallest]

print(arr) 


# time complexcity
#O(n^2)