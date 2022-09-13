print( "__file__:", __file__)
print( "__name__:", __name__)

def get_user_name():
	return input('Enter your name:')

def greet(user_name):
	print(f'Hello, {user_name}!')