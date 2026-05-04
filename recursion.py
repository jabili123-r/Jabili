def naresh(a):
    if a==1:
        return 1
    else:
        return a * naresh(a-1)
a=6
x=naresh(a)
print(x)
