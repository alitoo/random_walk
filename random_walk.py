import numpy as np
import matplotlib.pyplot as plt

def generate_random_points_on_sphere(N, r):
    points = []
    for _ in range(N):
        z = np.random.uniform(-r, r)
        phi = np.random.uniform(0, 2 * np.pi)
        x = np.sqrt(r**2 - z**2) * np.cos(phi)
        y = np.sqrt(r**2 - z**2) * np.sin(phi)
        points.append((x, y, z))
    return np.array(points)

def random_walk_on_sphere(start_point, num_steps, step_size, r):
    points = [start_point]
    current_position = np.array(start_point)
    for _ in range(num_steps):
        theta = np.random.uniform(0, np.pi)
        phi = np.random.uniform(0, 2 * np.pi)
        step = step_size * np.array([
            np.sin(theta) * np.cos(phi),
            np.sin(theta) * np.sin(phi),
            np.cos(theta)
        ])
        current_position += step
        current_position = r * current_position / np.linalg.norm(current_position)
        points.append(current_position)
    return np.array(points)

def calculate_squared_end_to_end_distance(points):
    start_point = points[0]
    end_point = points[-1]
    return np.linalg.norm(end_point - start_point) ** 2

# Parameters
r = 1.0  # Radius of the sphere
step_size = 0.1  # Step size
num_simulations = 10000  # Number of random walks to average

#  length  for random walks
num_steps_list = [100, 250, 500, 750, 10000]

# Calculate average squared end-to-end distance for various N
average_squared_end_to_end_distances = []

for num_steps in num_steps_list:
    squared_distances = []
    for _ in range(num_simulations):
        start_point = generate_random_points_on_sphere(1, r)[0]
        walk_points = random_walk_on_sphere(start_point, num_steps, step_size, r)
        squared_distance = calculate_squared_end_to_end_distance(walk_points)
        squared_distances.append(squared_distance)
    
    # Average squared end-to-end distance
    average_squared_distance = np.mean(squared_distances)
    average_squared_end_to_end_distances.append(average_squared_distance)

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(num_steps_list, average_squared_end_to_end_distances, marker='o', label='Squared Distance')

# plot
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Number of Lengeth (N)")
plt.ylabel("Average Squared End-to-End Distance")
plt.title("Number of lengeth vs the Average Squared End-to-End Distance")
plt.grid(True)

# Inset plot to show 
plt.show()
