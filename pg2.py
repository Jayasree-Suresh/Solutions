
for i in range(1,10):  #printing 1 to 9
    print(i)

for i in range(1,10,2):
        print(i)

for i in range(1,10,-1):
    print(i)

a=int(input())
b=int(input())
for i in range(a,b):
    print(i)

even_sum=0  #sum of even and odd numbers
odd_sum=0
for i in range(1,10):
    if i%2==0:
        even_sum=even_sum+i

    elif i%2!=0:
        odd_sum=odd_sum+i
print(even_sum)
print(odd_sum)



string="Welcome"   #printing string in vertical
for i in string:
    print(i)

a=list(string)   #reversing list
b=a[:: -1]
print(b)

#reversing string
l=string[:: -1]
print(l)


count=0   #counting characters in string
for i in string:
    count=count+1
print(count)

count=0          #counting e in string
for i in string:
    if i=='e':
        count=count+1
print(count)

q=string[:3]
print(q)

q=string[1:3]
print(q)

q=string[2:6]
print(q)

j=string.split("l")
print(j)

even_list=[]
odd_list=[]
for i in range(1,10):
    if i%2==0:
        even_list.append(i)
    elif i%2!=0:
        odd_list.append(i)
print(even_list)
print(odd_list)

r=[0,'a',1,'b']
for i in r:
    if type(i)==int:
        print(i)
        print(  )
    else:
        print(i)

num=[]
char=[]
r=[0,'a',1,'b']
for i in r:
    if type(i)==int:
        num.append(i)
    else:
        char.append(i)
print(num)
print(char)

num=[]
alpha=[]
num_count=0
alpha_count=0
j=['0','a','1','b']
for i in j:
    if ord(i)>=97 and ord(i)<=122:
        alpha.append(i)
        num_count=num_count+1
    else:
        num.append(i)
        alpha_count=alpha_count+1
print(alpha)
print(num)
print(num_count)
print(alpha_count)

count_num=0
count_alpha=0
j=['0','a','1','b']
for i in j:
    if i.isdigit():
        count_num=count_num+1
    if i.isalpha():
        count_alpha=count_alpha+1

print(count_num)
print(count_alpha)




