#Oscar Lopez
import statistics
def sumar(L):
    s = sum(L)
    return s
def average(L):
    avg = sumar(L) / 10.0
    return avg
def std(L):
    st = statistics.stdev(L)
    return st
 
a = float(input("Give me the first number: "))
b = float(input("Give me the second number: "))
c = float(input("Give me the third number: "))
d = float(input("Give me the fourth number: "))
e = float(input("Give me the fifth number: "))
f = float(input("Give me the sixth number: "))
g = float(input("Give me the seventh number: "))
h = float(input("Give me the eighth number: "))
i = float(input("Give me the ninth number: "))
j = float(input("Give me the tenth number: "))
L = []
L.append(a)
L.append(b)
L.append(c)
L.append(d)
L.append(e)
L.append(f)
L.append(g)
L.append(h)
L.append(i)
L.append(j)
x = sumar(L)
y = average(L)
z = std(L)
print("The total of the numbers is: ", x)
print("The average of the numbers is: ", y)
print("The standard deviation of the numbers is: ", z)
