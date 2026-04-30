import numpy as np
import matplotlib.pyplot as plt

# 1. Math Functions
def f(x):
    return x**2 + 5

def f_derivative(x):
    return 2 * x

# 2. Gradient Descent Algorithm (with debugging prints)
def gradient_descent_1d(derivative_func, initial_x, learning_rate=0.1, max_epochs=100, tolerance=1e-6):
    print(f"--- Starting Gradient Descent ---")
    x = initial_x
    history = [x]
    
    for epoch in range(max_epochs):
        gradient = derivative_func(x)
        new_x = x - (learning_rate * gradient)
    
        if abs(new_x - x) < tolerance:
            print(f"--- Converged at epoch {epoch}! ---")
            x = new_x
            history.append(x)
            break
        x = new_x

        history.append(x)
        
    return x, history

# 3. Execution & Plotting
starting_point = 10.0  
alpha = 0.05            

# Run the algorithm
min_x, x_history = gradient_descent_1d(f_derivative, starting_point, alpha)

print(f"\nAlgorithm finished. Found minimum at x = {min_x:.6f}")
print("Now drawing the plot...")

# Visualization
x_curve = np.linspace(-12, 12, 100)
y_curve = f(x_curve)
y_history = [f(x) for x in x_history]

plt.figure(figsize=(10, 6))
plt.plot(x_curve, y_curve, 'b-', label='f(x) = x^2 + 5', linewidth=2)
plt.plot(x_history, y_history, 'ro-', label='Gradient Descent Path', markersize=6, alpha=0.8)
plt.plot(x_history[0], y_history[0], 'go', markersize=10, label='Start')
plt.plot(x_history[-1], y_history[-1], 'y*', markersize=15, label='Minimum Reached')

plt.title('1D Gradient Descent Visualization', fontsize=14)
plt.xlabel('x (Parameter)', fontsize=12)
plt.ylabel('f(x) (Loss / Cost)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

print("Plot drawing complete!")