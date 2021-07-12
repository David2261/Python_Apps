goods = {"appel" : 4.5,
	"orange" : 6.2,
	"mango" : 10.0,
	"banana" : 3.8}
for good, price in goods.items():
	print(good, " - ", price)
cost = 0
while True:
	good = input("What? (n - nothing) ")
	if good == 'n':
		break
	qty = int(input("How many? "))
	cost += goods[good] * qty

print("Price: ", cost)