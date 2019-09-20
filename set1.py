width = 17
height = 12.0
delimiter = '.'
a=width/2
print("width/2 is: ",a)
print(type(a))
b=width/2.0
print("width/2.0 is: ",b)
print(type(b))
c=height/3
print("height/3 is: ",c)
print(type(c))
d=1 + 2 * 5
print("1 + 2 * 5 is: ",d)
print(type(d))
e=delimiter * 5
print("delimiter * 5 is: ",e)
print(type(e))

x = -25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
numGuesses += 1
if ans**2 < x:
    low = ans
else:
    high = ans
ans = (high + low)/2.0
print ('numGuesses =', numGuesses)
print (ans, 'is close to square root of', x)

ratios=[]
def getRatios(vect1, vect2):
    if len(vect1)==len(vect2):
        for i in range(len(vect1)):
            try:
                ratios.append(vect1[i]/vect2[i])
            except:
                print("DivideByZeroException")
    print(ratios)

# getRatios([4,8,9],[2,6,9])
getRatios([4,8,9],[0,6,9])

def isln(str1,str2):
    if str1 in str2:
        print("True")
    elif str2 in str1:
        print("True")
    else:
        print("False")

isln("cat","catalogue")

s="1.23,2.4,3.123"
t=s.split(",")
sum=0
for i in t:
    sum=sum+float(i)
print(sum)

i=int(input("Enter a number: "))
pwr = 0
root = 0

while root <= i:
    root += 1
    while pwr < 6:
        pwr += 1
        if root**pwr == i:
            print(root, pwr)
    pwr = 0

current_hours = 6
current_minutes = 52
easy_pace_minutes = 8
easy_pace_seconds = 15
tempo_pace_minutes = 7
tempo_pace_seconds = 12
easy_miles = 2
tempo_miles = 3

easy_time = (easy_pace_minutes * 60 + easy_pace_seconds) * easy_miles
print(easy_time)
tempo_time = (tempo_pace_minutes * 60 + tempo_pace_seconds) * tempo_miles
print(tempo_time)
run_time = easy_time + tempo_time
print(run_time)
current_time = current_hours * 3600 + current_minutes * 60
print(current_time)
end_time = current_time + run_time
print(end_time)
end_hours = end_time // 3600
print(end_hours)
end_minutes = (end_time % 3600) // 60
print(end_minutes)
end_seconds=(end_time % 3600) % 60
print(end_seconds)
print("I will go home for breakfast at ",end_hours,":",end_minutes,":",end_seconds," am")

cover_price=24.95
dis_rate=0.4
shipping_first=3
shipping_further=0.75
dis_amount=cover_price*dis_rate
sale_price=cover_price-dis_amount
total_copies=60
wholesale_cost= (total_copies*sale_price) + shipping_first + (shipping_further * (total_copies-1))
print("The wholesale cost is ",wholesale_cost)

r=int(input("Enter radius: "))
vol= (4 * 3.14 * r**3)/3
print("The volume of the sphere is ",vol)

r=int(input("Enter radius: "))
vol= (4/3) * 3.14 * r**3
print("The volume of the sphere is ",vol)

num=[int(input("Enter a num:")) for i in range(10)]
num.sort()
num.reverse()
odd=0
for i in num:
    if i % 2 == 1:
        print(i," is the largest odd number")
        odd=1
        break
if odd==0:
    print("No odd numbers")

num=[int(input("Enter a num:")) for i in range(10)]
odd=[i for i in num if i % 2 == 1]
odd.sort()
if odd:
    print("largest odd number is ",odd[len(odd)-1])
else:
    print("No odd")

largest=0
for i in range(0,10):
    num=int(input("Enter a number:"))
    if num % 2 != 0 and num >= largest:
        largest = num
if largest == 0:
    print("No odd")
else:
    print(largest)

def right_justify(s):
    length=len(s)
    print(" "*(70-length),s)

right_justify("Cigna")


largest=0
for i in range(0,3):
    num=int(input("Enter a number:"))
    if num % 2 != 0 and num >= largest:
        largest = num
if largest == 0:
    print("No odd")
else:
    print(largest)