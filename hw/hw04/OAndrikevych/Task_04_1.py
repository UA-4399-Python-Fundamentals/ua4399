# Version 1
print("Version 1: Celsius to Fahrenheit Temperature Converter")

def temperature_converter():
    try:
        t = float(input("\nEnter the temperature in Celsius: "))
        # Check if the user enters a temperature below absolute zero
        if t < -273.15:
            print("Temperature below absolute zero (-273.15°C)")
        else:
            # Convert the temperature using the formula: F = (C * 9/5) + 32
            far = (t * 9 / 5) + 32
            print(f"{t}°C is equivalent to {far:.2f}°F")
    except ValueError:
        # You can assume that the user will enter a valid input
        print("Invalid input. Please enter a numeric value")
temperature_converter()

# Version 2
print("\nVersion 2: Temperature measurements and Statistics in Fahrenheit")
import random
import numpy as np
import matplotlib.pyplot as plt

# Generate 10 random float numbers between -60°C and 60°C
t = [round(random.uniform(-60, 60), 2) for _ in range(10)]
print(f"\nOriginal range in °C: {t}")

# Convert temperatures to Fahrenheit
far = [round((temp * 9 / 5 + 32), 2) for temp in t]
print(f"Range in Fahrenheit: {far}")

# Sort temperatures in ascending
far.sort()

# Calculate statistics
min_t = min(far)  # Minimum
max_t = max(far)  # Maximum
median_t = np.median(far)  # Median
avg_t = np.mean(far)  # Average
quartiles = np.percentile(far, [25, 75])
first_quartile = quartiles[0]  # 1st quartile
third_quartile = quartiles[1]  # 3rd quartile
std_dev = np.std(far)  # Standard deviation
variance = np.var(far)  # Variance

# Print statistics
print(f"\nStatistics with Numpy:")
print(f"Min: \t\t\t{min_t:.2f}°F")
print(f"Max: \t\t\t{max_t:.2f}°F")
print(f"Median: \t\t{median_t:.2f}°F")
print(f"Average: \t\t{avg_t:.2f}°F")
print(f"1st Quartile: \t{first_quartile:.2f}°F")
print(f"3rd Quartile: \t{third_quartile:.2f}°F")
print(f"Standard Dev: \t{std_dev:.2f}°F (N-normalized)")
print(f"Variance: \t\t{variance:.2f} (N-normalized)")

# With Pandas
import pandas as pd
# Convert list to pandas Series for statistical calculations
s = pd.Series(far)

# Calculate statistics
min_t = s.min()  # Minimum
max_t = s.max()  # Maximum
median_t = s.median()  # Median
avg_t = s.mean()  # Average
first_quartile = s.quantile(0.25)  # 1st quartile
third_quartile = s.quantile(0.75)  # 3rd quartile
std_dev = s.std()  # Standard deviation
variance = s.var()  # Variance

# Print statistics
print(f"\nStatistics with Pandas:")
print(f"Min: \t\t\t{min_t:.2f}°F")
print(f"Max: \t\t\t{max_t:.2f}°F")
print(f"Median: \t\t{median_t:.2f}°F")
print(f"Average: \t\t{avg_t:.2f}°F")
print(f"1st Quartile: \t{first_quartile:.2f}°F")
print(f"3rd Quartile: \t{third_quartile:.2f}°F")
print(f"Standard Dev: \t{std_dev:.2f}°F (N-1 normalized)")
print(f"Variance: \t\t{variance:.2f} (N-1 normalized)")

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(far, marker='o', label='Temperatures in Fahrenheit')
plt.axhline(y=min_t, color='blue', linestyle='--', label=f'Min: {min_t:.2f}°F')
plt.axhline(y=max_t, color='green', linestyle='--', label=f'Max: {max_t:.2f}°F')
plt.axhline(y=median_t, color='orange', linestyle='--', label=f'Median: {median_t:.2f}°F')
plt.axhline(y=avg_t, color='red', linestyle='--', label=f'Average: {avg_t:.2f}°F')
plt.axhline(y=first_quartile, color='purple', linestyle='--', label=f'1st Quartile: {first_quartile:.2f}°F')
plt.axhline(y=third_quartile, color='brown', linestyle='--', label=f'3rd Quartile: {third_quartile:.2f}°F')
plt.title("Temperature measurements and Statistics in Fahrenheit")
plt.xlabel("Measurements")
plt.ylabel("Temperature, °F")
plt.legend()
plt.grid()
plt.show()