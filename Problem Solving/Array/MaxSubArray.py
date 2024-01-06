# # Resource ->  https://www.youtube.com/watch?v=HCL4_bOd3-4

def maxSumArray(a):
    maxSum=0
    currSum=0
    for i in range(len(a)):
        currSum += a[i]
        if(currSum > maxSum):
            maxSum=currSum
        if(currSum <0):
            currSum =0
    return maxSum

print(maxSumArray([-2,1,-3,4,-1,2,1,-5,4]))

########### My practice  -> Return array as well

def maxSumArray(a):
    maxSum = 0
    currSum = 0
    maxList = []
    tempList = []
    for i in range(len(a)):
        currSum += a[i]
        tempList.append(a[i])
        if currSum > maxSum:
            maxSum = currSum
            maxList = tempList[:]  # copy the list
        if currSum < 0:
            currSum = 0
            tempList = []
    return maxList, maxSum

print(maxSumArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

 