# a=[1,2,3]
# b=[4,5,6]
# a.append(b)
# print(a)
# a.extend(b)
# print(a)
#
# a="ACCENTURE"
# b=list(a)
# b.extend(b)
# print(b)
#
# string="ACCENTURE"
# b=list()
# for char in string:
#     b.append(char)
#     b.append(char)
# print(b)

string="ACCENTURE"
b=list()
for char in string:
    b.extend(char*2)
print(b)
#
# string="ACCENTURE"
# b=list()
# for char in string:
#     b.extend(char)
#     b.extend(char)
# print(b)

string="ACCENTURE"
b=list()
for char in string:
    b.append(char*2)
print(b)

# string="ACCENTURE"
# b=list()
# for char in string:
#     if char not in b:
#            b.append(char)
#            b.append(char)
#
# print(b)
#
# string="ACCENTURE"
# b=list()
# for char in string:
#     for char1 in range(0,2):
#         b.append(char)
# print(b)