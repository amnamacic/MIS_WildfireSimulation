import numpy as np
import matplotlib.pyplot as plt

# Example data (replace with your actual simulation results)
fire_spread_distances_heavy_wind = [3.0, 19.0, 36.1, 33.1, 24.2]
time_to_ignition_heavy_wind = [865, 440, 469, 386, 475]
fire_duration_heavy_wind = [4148, 2249, 1924, 2024, 1195]
num_trees_burned_heavy_wind = [1599, 1410, 1592, 1583, 1424]

fire_spread_distances_slow_wind = [2.0, 6.0, 33.0, 8.5, 17.0]
time_to_ignition_slow_wind = [7271, 2762, 4659, 4228, 2552]
fire_duration_slow_wind = [7271, 2762, 4659, 4228, 2552]
num_trees_burned_slow_wind = [936, 1404, 996, 753, 416]

# Calculate mean and median for each scenario
mean_fire_spread_distance_heavy_wind = np.mean(fire_spread_distances_heavy_wind)
median_time_to_ignition_heavy_wind = np.median(time_to_ignition_heavy_wind)
mean_fire_duration_heavy_wind = np.mean(fire_duration_heavy_wind)
mean_num_trees_burned_heavy_wind = np.mean(num_trees_burned_heavy_wind)

mean_fire_spread_distance_slow_wind = np.mean(fire_spread_distances_slow_wind)
median_time_to_ignition_slow_wind = np.median(time_to_ignition_slow_wind)
mean_fire_duration_slow_wind = np.mean(fire_duration_slow_wind)
mean_num_trees_burned_slow_wind = np.mean(num_trees_burned_slow_wind)

# Print the results table
print(f"| Metric                    | Heavy Wind Scenario | Slow Wind Scenario |")
print(f"|---------------------------|---------------------|--------------------|")
print(f"| Fire Spread Distance      | Mean: {mean_fire_spread_distance_heavy_wind:.2f} | Mean: {mean_fire_spread_distance_slow_wind:.2f} |")
print(f"| Time to Ignition          | Median: {median_time_to_ignition_heavy_wind} | Median: {median_time_to_ignition_slow_wind} |")
print(f"| Fire Duration             | Mean: {mean_fire_duration_heavy_wind:.2f} | Mean: {mean_fire_duration_slow_wind:.2f} |")
print(f"| Number of Trees Burned    | Mean: {mean_num_trees_burned_heavy_wind:.2f} | Mean: {mean_num_trees_burned_slow_wind:.2f} |")

# Plot the results
scenarios = ['Heavy Wind', 'Slow Wind']
metrics = ['Fire Spread Distance', 'Time to Ignition', 'Fire Duration', 'Number of Trees Burned']

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

for i, metric in enumerate(metrics):
    ax = axs[i // 2, i % 2]
    data = [eval(f"mean_{metric.lower()}_heavywind"), eval(f"mean_{metric.lower()}_slowwind")]
    ax.bar(scenarios, data, color=['red', 'blue'])
    ax.set_title(metric)

plt.tight_layout()
plt.show()