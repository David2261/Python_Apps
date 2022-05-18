
def adder(*nums):
    sum = 0

    for n in nums:
        sum += n

    print("Sum: ", sum)





def intro(**data):
    print("\nData type of argument: ",type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))



def main():
	adder(3, 5)
	adder(4, 5, 6, 7)
	adder(1, 2, 3, 5, 6)
	intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
	intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


if __name__ == '__main__':
	main()