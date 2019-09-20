# def has_no_e(s):
#
#     if 'e' not in s:
#         return True
#     else:
#         return False
#

# sample=[1,2,3,3,3,3,4,5]
# unique=[]
# for i in sample:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# string="green-red-yellow-black-white"
#
# mylist=string.split("-")
# mylist.sort()
# res="-".join(mylist)
# print(res)

# def upper_lower_count(s):
#     upper=0
#     lower=0
#     for i in s:
#         asc=ord(i)
#         if asc in range(65,91):
#             upper=upper+1
#         else:
#             lower=lower+1
#
#     print("No. of Upper case characters :",upper)
#     print("No. of Lower case characters :",lower)
# upper_lower_count('The quick Brow Fox')

def pangram(string):
    string1="abcdefghijklmnopqrstuvwxyz"
    for i in string1:
        if i not in string.lower():
            return False
        else:
            return True

print(pangram('The quic brown fox jumps'))