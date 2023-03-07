import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam, SGD


def create_data():
	# Generate random height and weight data for adults and children
	adult_size = 5000
	child_size = 5000
	scale = 1

	adult_heights = np.random.normal(loc=175, scale=scale, size=adult_size)
	adult_weights = np.random.normal(loc=70, scale=scale, size=adult_size)
	child_heights = np.random.normal(loc=120, scale=scale, size=child_size)
	child_weights = np.random.normal(loc=30, scale=scale, size=child_size)

	# Combine the height and weight data and create labels for adults and children
	heights = np.concatenate((adult_heights, child_heights))
	weights = np.concatenate((adult_weights, child_weights))
	adult_labels = np.ones(adult_size, dtype=int)
	child_labels = np.zeros(child_size, dtype=int)
	labels = np.concatenate((adult_labels, child_labels))

	# Shuffle and join the data
	indices = np.arange(len(labels))
	np.random.shuffle(indices)
	data = np.stack((heights[indices], weights[indices]), axis=-1)
	labels = labels[indices]


	print(adult_heights.min())
	print(adult_heights.max())

	print(child_heights.min())
	print(child_heights.max())

	return (data, labels)

def write_data_to_csv(data, labes):
	df = pd.DataFrame(data = data, columns=['height', 'weight'])
	df['age'] = labels
	# print(df.head())
	# write the dataframe to a csv file
	df.to_csv('adulat_child_1.csv', index=False, header=True)

def read_data(filename):
	df = pd.read_csv(filename)
	return df

def split_train_test_data(df):
	pass

def plot_data(df):
	sns.scatterplot(data=df, x=df.columns[0], y=df.columns[1], hue=df.columns[2])
	plt.show()

def create_and_fit_model(df):
	# init model
	model = Sequential()
	model.add(Dense(128, input_dim=2,activation="relu"))
	model.add(Dense(1,activation='sigmoid'))

	# Compile your model
	model.compile(loss='binary_crossentropy',
				#   optimizer='sgd',
					optimizer=SGD(learning_rate=0.01),
					metrics=['accuracy'])
	# Train the model
	model.fit(x=df.iloc[:,:2], y=df.iloc[:,2], epochs=5, batch_size=32)

def test_model():
	# Define 10 test cases
	test_cases = [
		{'input': [170, 60], 'expected_output': 1},
		{'input': [140, 40], 'expected_output': 0},
		{'input': [150, 50], 'expected_output': 1},
		{'input': [130, 60], 'expected_output': 0},
		{'input': [160, 70], 'expected_output': 1},
		{'input': [120, 30], 'expected_output': 0},
		{'input': [180, 80], 'expected_output': 1},
		{'input': [140, 50], 'expected_output': 0},
		{'input': [160, 50], 'expected_output': 0},
		{'input': [150, 70], 'expected_output': 1}
	]
	# Evaluate the model on the test cases
	num_passed = 0
	num_failed = 0
	for i, test_case in enumerate(test_cases):
					input_data = np.array(test_case['input']).reshape(1, 2)
					expected_output = test_case['expected_output']
					predicted_output = model.predict(input_data)[0][0].round()
					if predicted_output == expected_output:
									num_passed += 1
									# print(f'Test case {i+1} PASSED')
					else:
									num_failed += 1
									# print(f'Test case {i+1} FAILED')
									print(f'failed: {test_case}')

	# Print summary
	print(f'{num_passed} test cases PASSED')
	print(f'{num_failed} test cases FAILED')



df = read_data('./adulat_child_1.csv')
create_and_fit_model(df)

