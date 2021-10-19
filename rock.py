import random

def play():
	user = input("What you choice? 'r' for rock, 'p' for paper, 's' for scissors ")
	pc = random.choice(['r', 'p', 's'])

	if user == pc:
		return print('It\'s a tie')


	if is_win(user, pc):
		return print('You won!!!')


	return print('You Lost')


	def is_win(player, opponent):
		if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
			or (player == 'p' and opponent == 'r'):
			return True

play()