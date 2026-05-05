def jabili(a):
    if a == 1:
        return
    i=2
    while(a%i !=0):
        i=i+1
    print(i,end=" ")
    jabili(a/i)
a=int(input("Enter any num:"))
jabili(a)
    
    
        
