largest=0
for i in range(0,3):
    num=int(input("Enter a number:"))
    if num % 2 != 0 and num >= largest:
        largest = num
if largest == 0:
    print("No odd")
else:
    print(largest)