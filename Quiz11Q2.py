def check_banana(x):
    a=open(x,"r")
    n=0
    for i in a:
        r=i.lower()
        sub=r.find("banana")
        while sub !=(-1):
            n=n+1
            sub=r.find("banana",(sub+1))
    return(n)

b=check_banana("banana.txt")
print("Número de bananas: ",b)
