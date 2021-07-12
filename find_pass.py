<<<<<<< HEAD
from random import *
guess =''
password = input('Write password: ')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',\
't', 'u', 'v', 'w', 'x', 'y', 'z'
]
while (guess != password):
	guess = ''
	for letters in password:
		guessletter = letters[randint(0, 25)]
		guess = str(guessletter) + str(guess)
	print(guess)
=======
from random import *
guess =''
password = input('Write password: ')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',\
't', 'u', 'v', 'w', 'x', 'y', 'z'
]
while (guess != password):
	guess = ''
	for letters in password:
		guessletter = letters[randint(0, 25)]
		guess = str(guessletter) + str(guess)
	print(guess)
>>>>>>> ac668391880eb4d49375ad016d6572ab5044b9a9
print('Password!')