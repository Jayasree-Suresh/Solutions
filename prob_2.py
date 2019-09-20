def rotate_word(a,b):
    st=""
    for i in a:
        c=ord(i)
        c=c+int(b)
        if c in range(97,122):
            w=chr(c)
            st=st+w
        else:
            z=96-c
            y=122-z
            w=chr(y)
            st=st+w

    print(st)

rotate_word("cheer",7)
rotate_word("melon",-10)
