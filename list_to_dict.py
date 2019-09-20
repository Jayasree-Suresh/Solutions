list1=['five',5,'six',6,'seven',7,'seven',7,'nine',9]
keys=[]
values=[]
mydict={}
for i in list1:
     if type(i)==str:
        keys.append(i)
     else:
         values.append(i)
print(keys)
print(values)
mydict=(dict.fromkeys(keys))
print(mydict)
li=[]
li1=[]
for i in values:
    if values.count(i)>1:
        li.append(i)
        mydict['seven']=li
    else:
        if i==5:
            mydict['five']=i
        elif i==6:
            mydict['six']=i
        elif i==9:
            mydict['nine']=i

print(mydict)

for k in range(0,len(keys)):
    if keys[k] in mydict:
        val=mydict.get(keys[k])
        mydict[keys[k]]=[val,values[k]]
    else:
        mydict[keys[k]] = values[k]

print(mydict)

