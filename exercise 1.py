import numpy as np
# Example data for testing purposes
data = np.array([0.1, 0.2, 9.8, 0.15, 0.22, 9.78, 0.12, 0.21, 9.81, 0.11, 0.23, 9.79])
# Reshape the data into a 2D array with 3 columns (x, y, z)
reshaped_data = data.reshape(-1, 3)