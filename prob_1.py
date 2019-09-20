def is_Palindrome():
    inp=input("Enter the string: ")
    oup=inp [::-1]
    if inp==oup:
        print("%s is a Palindrome" % inp)
    else:
        print("%s is not a Palindrome" % inp)

is_Palindrome()
