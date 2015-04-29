import statistics
def numeros(x):
    a=open(x,"r")
    y=0
    b=0
    list=[]
    for i in x:
        y=y+int(i)
        b=b+1
        list.append(int(i))
    r=statistics.stdev(list)
    print("El total de los valores son:",y)
    print("El numero de valores son:",b)
    print("La medida aritmetica de los valores es:",(y/b))
    print("La division es:", r)

numeros("numeros.txt")
