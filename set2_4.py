# Write a program that computes the decimal equivalent of the binary number 10011?

num=10011
string=str(num)
mylist=list(string)
print(mylist)
val=0
for i in range(len(mylist)):
    j=mylist.pop()
    if j=='1':
        val=val+pow(2,i)
print(val)