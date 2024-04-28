def get_user_data():
	"""Retrieves user data from the command line

		Arguments: none
		Returns:
			dictionary of the form:
				{
					"name" : "user_name",
					"height": "user heigth in meters",
					"weight": "user weight in kilograms"
				}
	"""
	# YOUR CODE HERE

def calc_BMI(w,h):
	"""Calculates the BMI, using formula bmi== w / (h*h)

		Arguments:
			w [float]: weight in kilograms
			h [float]: heigth in meters

		Returns:
			[float]: calculated BMI
	"""
	# YOUR CODE HERE

def calc_BMI_category(bmi):
	"""Calculates the BMI category

		Arguments:
			bmi [float]: the bmi number index

		Returns:
			[string]: bmi category
	"""
	# YOUR CODE HERE

def print_results(bmi_category):
	"""Prints the BMI category

		Arguments:
			bmi_category [string]: bmi category
	"""
	# YOUR CODE HERE


### TEST:
# user_data = get_user_data()
# bmi = calc_BMI(user_data["weight"],user_data["height"] )
# bmi_category = calc_BMI_category(bmi)
# print_results(
# 	name=user_data['name'],
# 	bmi=bmi,
# 	bmi_category=bmi_category
# )

### EXPECTED OUTPUT
# Enter your name, please: Ada
# I need to know your height in meters: 1.67
# And your weight in kilograms: 56
#
# **************************************************
# Ada, your BMI is 20.08.  Category:  Normal range
# **************************************************

