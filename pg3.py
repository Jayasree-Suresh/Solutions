string=str(input())
mydict={}
for i in string:
    if i not in mydict:
        mydict[i]=1
    else:
        mydict[i]+=1
print(mydict)

# Accenture
# {'A': 1, 'c': 2, 'e': 2, 'n': 1, 't': 1, 'u': 1, 'r': 1}

s=""
for i,j in mydict.items():
    s=s+i+str(j)
print(s)
#A1c2e2n1t1u1r1

'''a = "Helulo, World!"
first=a.find('l')
print(first)
second=a.find('l',first+1)
print(second)
b=slice(second,len(a))
print(a[b])
j=a[b].replace("l", "z", 1)
print(j)
i=slice(first+1)
print(a[i])
con=a[i]+j
print(con)'''

# 2
# 3
# lo, World!
# zo, World!
# Hel
# Helzo, World!

'''a = "Helulo, World!"
first=a.find('l')
print(first)
second=a.find('l',first+1)
print(second)
b=slice(second,len(a))
print(a[b])
j=a[b].replace("l", "z", 1)
print(j)
i=slice(first+1)
print(a[i])
con=a[i]+j
print(con)'''

# 2
# 4
# lo, World!
# zo, World!
# Helu
# Heluzo, World!

# def avg(a,b,c):
#     def total(a,b,c):
#         return a+b+c
#     return (a+b+c)/3
# print(avg(1,2,3))

#2.0

# def avg(a,b,c):
#     return (a+b+c)/3
# print(avg(1,2,3))

# 2.0

string="Accenture"
mylist=list(string)
mylist.reverse()
print(mylist)
s=""
for i in mylist:
     s=s+i
print(s)

print(string)

original=str(input())
reverse=original[::-1]
print(reverse)
if reverse==original:
    print(reverse)
else:
    print("It is not a palindrome")

string="Acccenture"
mydict={}
for i in string:
    if i not in mydict:
        mydict[i]=1
    else:
        mydict[i]+=1
print(mydict)
list1=[]
for i in mydict:
     list1.append(mydict[i])
list1.sort()
x=list1[len(list1)-1]
for i,j in mydict.items():
    if j==x:
     print(i,j)



original=str(input())
mylist=list(string)
mylist.reverse()
print(mylist)
s=""
for i in mylist:
     s=s+i
print(s)
if s==original:
    print(s)
else:
    print("It is not a palindrome")


word = "Hello World"

a='7'.join(reversed(word))
print(a)

b=word.replace('e','')
print(b)



