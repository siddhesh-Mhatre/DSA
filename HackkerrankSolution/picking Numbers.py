a=[1,1,2,2,4,4,5,5,5]
unque_value= set(a)
temp=[]
for i in unque_value:
    temp.append((i,a.count(i)))
 
sum =temp[0][1] + temp[0+1][1]
for j in range(len(temp)-1):
    Diff_var=temp[j][0] - temp[j+1][0]
    sum_count=temp[j][1] + temp[j+1][1]
    if  Diff_var<=1 and sum>sum_count:
        sum = sum_count

print(sum)



## Steps
'''first group number with count '''
'''then chek the number differce negative and count is less'''