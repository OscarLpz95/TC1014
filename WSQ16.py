#Oscar Lopez
def banana(file):
	c=0
	sumprice= 0
	sumcity= 0
	sumhigh= 0
	for line in file:
		c=c+1
		if(c%2==1):
			price = line[42:46]
			prices = float(price)
			sumprice= sumprice+prices
			city = line[52:54]
			cities = float(city)
			sumcity= sumcity+cities
			high = line[55:57]
			highs = float(high)
			sumhigh= sumhigh+highs
	cars=c/2
	average_price= sumprice/cars
	average_city= sumcity/cars
	average_high= sumhigh/cars
	return(average_price, average_city, average_high)
	
txt = open("93cars.dat.txt")
(a,b,c) = banana(txt)
a= str(a)
b= str(b)
c= str(c)
print("The average midrange price(in $1000) is: ", a[0:5])
print("The average city MPG is: ", b[0:5])
print("The average highway MPG is: ", c[0:5])
