'''str1=str(input())
li=[]
dict1={}
for i in str1:
    li.append(i)
for j in li:
    #print(j)
    if j in dict1:
        dict1[j] = dict1[j] + 1
    else:
        dict1[j]=1
print(dict1)
temp=""
for key in dict1:
    l=dict1.get(key)
    temp = temp + (key + str(l))

print(temp)
'''

list1=['five',5,'six',6,'seven',7,'seven',7,'nine',9]






