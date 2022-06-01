def main():
	import time
	import random
	secretNumber=random.randint(1,40)
	print('welcome to the number guessing game!')
	print('the number will be from 1-40')
	time.sleep(2)
	print('please enter your name to continue below')
	userTypeun=input('Please type your name here: ')
	print('Hello,',userTypeun)
	time.sleep(2)
	print('please type "play"to continue')
	userPLay=input('please type play: ')
	if userPLay=='play':
		time.sleep(3)
	print('Your game will begin!')
	def lain():
		secretNumber=random.randint(1,25)
		print('the game has started!')
		userNumber=float(input('Please guess the number'))
		print(userNumber)
		if userNumber==secretNumber:
				print('WELL DONE YOU DID IT, YOU GUESSED THE SECRET NUMBER!!!')
				lain()
		if userNumber!=secretNumber:
			print('Sorry, you did not guess the secret number:(')
			print('the secret number was: ',secretNumber)
			print('you were off by: ',secretNumber-userNumber)
			lain()
	lain()
main()




if userPLay!='play':
	print('please restart the program, this is not the correct word, it was play')
