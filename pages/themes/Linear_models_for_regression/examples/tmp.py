import numpy as np
import matplotlib.pyplot as plt

# Define the slope (m) and intercept (b)
m = 3/2
b = 1

# Generate x values
X = np.linspace(-10, 10, 100)
# Calculate y values based on the slope-intercept form
Y = m * X + b

# Plot the line
plt.plot(X, Y, label=f'y = {m}x + {b}')

# Plot auxiliary lines
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

plt.axhline(b, color='red', linestyle='--', linewidth=1)
plt.axvline(m, color='green', linestyle='--',linewidth=1)

plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Slope-Intercept Form of a Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# normalize ticks
plt.xticks(np.arange(-5, 6, 1))
plt.yticks(np.arange(-10, 15, 1))
plt.xlim(-5,5)
plt.ylim(-10,10)


plt.show()