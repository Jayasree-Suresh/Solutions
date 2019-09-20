# import sys
#
# list1=[sys.argv[1],sys.argv[2],sys.argv[3]]
# if len(list1)==3:
#     res=max(list1)
#     print(res)
# elif len(list1)<3:
#     print("Insufficient arguments")
# else:
#     print("Arguments length should be only 3")

import sys
a=sys.argv[1]
b=sys.argv[2]
c=sys.argv[3]
list1=[a,b,c]
if len(list1)==3:
    if a>b and a>c:
        print(a)
    elif b>c and b>a:
        print(b)
    else:
        print(c)
elif len(list1)<3:
    print("Insufficient arguments")
else:
    print("Arguments length should be only 3")
