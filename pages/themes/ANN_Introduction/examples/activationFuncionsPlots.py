import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------- Sigmoid --------------------------------- #
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

x = np.array([1, 2, 3, 4, 1, 2, 3])
y = softmax(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('softmax(x)')
plt.title('Softmax Activation Function')

# Save the figure as a PNG file
plt.savefig('../images/softmax-plot.png')
plt.show()

