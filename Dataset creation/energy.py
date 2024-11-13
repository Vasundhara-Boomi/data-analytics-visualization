import pandas as pd
import random
import csv

ghg_emissions = [
    206, 64.3, 32.2, 57.3, 81.8, None, 123.8, 27.9, 2218.3, 124.6, 10.9, 22.1, 117.6, None, 1.3, 73.8, 74.6, 65.8, 66.2, 53.4, 87.3, 86.9, None, 64.4, 13.8,
    77.5, 66.9, 39.3, 69.7, 101.7, 52, 63.4, 97.3, 68, 43.4, 81, 57, 64.3, 13.3, 76.7, 93.6, 35.1, 119, 60.3, 102.6, 89.8, 26.5, None, 30.8, None, 1205.4,
    408, None, 0.4, 77.3, 27.7, 25.1, 0, 4.6, None, 2.4, 23.5, None, 25.2, 26, None, 12.8, None, 26.5, 70.2, 33.1, 15.1, 31.7, 81.7, 60.4, 35.8, 48.4, 24.2,
    57.2, 19.2, 115.3, 113.8, 8.4, 68.5, 32.3, None, 221.5, 244.6, None, 91.8, 54.9, 176.8, 31, 103.7, 219.1, 1313, 43.1, 69.3, None, 100.7, 161.1, None,
    240.9, 136.1, 182.9, 90, 160.5, 3.2, 139.4, 43.1, 16, 245.1, 131.8, 150.9, 202.9, 67, 92, 12.3, 34.4, 2, 13.8, 3.4, 39.2, None, None, 32.5, None, 4.4,
    35.2, 130.4, 49.4, 216, 1.7, 27.7, 30.2, 213, 150.1, 144.7, 21, 47.3, 76.6, 60.7, 114.8, 27.8, 2355.6, 143.5, 7.8, 26, 106.6, 3.6, 70.8, 71.3, 61.2,
    67.8, 82.7, 89.6, 46.9, 59.3, 81.4, 58.5, 44.4, 84.9, 56.7, 64.7, 105.2, 72.5, 54.9, 88.7, 53.1, 73.8, 88, 37.5, 113.4, 102.7, 78.3, 1122.5, 363.8,
    23.3, 68.6, 23.1, 44.7, 23.6, 15.8, 90.9, 53.9, 21.1, 25.4, 76.2, 57.4, 44.3, 25.3, 61.2, 15.1, 17.8, 81.4, 32.2, 346.6, 112.1, 160.2
]

print(len(ghg_emissions))


temperature_data = [
    20, 15, 13, 32, 18, 14, 18, 38, 33, 23, 35, 18, 30, 23, 13, 31, 26, 30, 24, 17, 20, 17, 27, 21, 21, 26, 32, 13, 20, 17, 36, 18, 22, 30, 18, 28, 18, 21, 21,
    19, 12, 15, 18, 38, 34, 16, 15, 15, 27, 37, 38, 32, 34, 24, 27, 17, 33, 13, 30, 31, 32, 31, 27, 32, 27, 37, 35, 20, 17, 37, 28, 22, 34, 36, 24, 18, 31, 23,
    14, 29, 13, 36, 19, 22, 37, 36, 19, 19, 22, 28, 33, 21, 29, 37, 24, 35, 36, 20, 17, 22, 26, 17, 30, 19, 28, 36, 23, 20, 14, 17, 21, 33, 19, 35, 15, 28, 30,
    24, 32, 20, 16, 29, 37, 27, 13, 22, 20, 27, 25, 21, 12, 28, 29, 19, 22, 37, 19, 31, 35, 27, 19, 20, 17, 16, 24, 13, 20, 22, 23, 22, 16, 24, 35, 28, 13, 19,
    26, 15, 14, 19, 19, 16, 17, 25, 28, 22, 15, 18, 31, 33, 33, 24, 29, 33, 21, 29, 22, 34, 38, 34, 35, 35, 25, 26, 31, 37, 13, 28, 24, 15, 35, 20, 22, 29, 22,
    32, 18, 12, 38
]

humidity_data = [
    40.37, 33.46, 25.43, 42.1, 39.3, 30.96, 49.9, 31.61, 33.68, 42.49, 38.04, 26.77, 42.48, 43.47, 32.52, 46.75, 56.4, 31.41, 30.46, 47.14, 32.1, 49.09, 35.67,
    43.43, 45.65, 45.13, 34.43, 41.99, 44.19, 48.41, 41.66, 42.57, 47.2, 34.01, 44.28, 44.24, 43.51, 42.25, 45.11, 34.82, 40.7, 43.75, 36.88, 32.06, 55.02, 46.48,
    37.02, 38.73, 46.56, 47.63, 42.74, 48.73, 30.44, 44.99, 38.61, 15.68, 58.09, 42.28, 30.04, 49.92, 39.67, 43.96, 42.01, 42.52, 38.66, 49.93, 43.21, 48.65,
    27.96, 32.54, 29.44, 41.83, 31.64, 28.32, 45.59, 42.63, 41.48, 34.08, 44.37, 40.57, 46.17, 22.84, 35.14, 47.04, 39.04, 46.31, 37.12, 11.31, 33.41, 46.55,
    44.93, 41.21, 52.68, 31.76, 44.17, 34.69, 40.31, 32.89, 43.53, 41.06, 33.54, 38.42, 37.95, 39.5, 31.78, 47.97, 30.77, 45.89, 43.1, 35.64, 39.21, 43.2, 48.82,
    32.99, 23.01, 34.84, 29.16, 46.13, 34.16, 42.68, 35.76, 49.79, 38.07, 42.24, 38.5, 40.94, 38.97, 40.74, 40.45, 31.67, 40.3, 31.17, 46.35, 39.36, 38.35,
    58.33, 43.54, 53.37, 58.75, 40.61, 43.66, 42.33, 44.64, 41.75, 38.05, 30.14, 36.79, 14.12, 49.67, 34.03, 43.55, 46.93, 32.52, 30.07, 33.03, 43.33, 42.11,
    47.67, 49.73, 41.91, 45.19, 30.46, 32.59, 32.81, 50.96, 35.48, 33.02, 46.1, 42.79, 43.72, 40.64, 41.59, 31.07, 42.48, 39.01, 32.22, 48.23, 31.04, 47.38,
    47.51, 39.38, 32.4, 51.47, 47.78, 31.9, 35.06, 38.91, 22.09, 36.72, 49.45, 45.2, 46.53, 38.8, 35.07, 47.78, 24.72, 47.22, 32.96, 32
]

season_data = [
    "Summer", "Autumn", "Winter", "Summer", "Spring", "Not Available", "Spring", "Spring", "Spring", "Autumn",
    "Autumn", "Winter", "Autumn", "Not Available", "Autumn", "Spring", "Summer", "Spring", "Spring", "Autumn",
    "Summer", "Spring", "Not Available", "Spring", "Autumn", "Summer", "Spring", "Autumn", "Spring", "Spring",
    "Autumn", "Autumn", "Summer", "Spring", "Autumn", "Autumn", "Spring", "Spring", "Autumn", "Spring", "Spring",
    "Spring", "Autumn", "Spring", "Summer", "Spring", "Summer", "Not Available", "Spring", "Not Available", "Summer",
    "Spring", "Not Available", "Autumn", "Spring", "Winter", "Summer", "Autumn", "Autumn", "Not Available", "Autumn",
    "Spring", "Not Available", "Spring", "Spring", "Not Available", "Autumn", "Not Available", "Winter", "Spring",
    "Winter", "Autumn", "Spring", "Winter", "Autumn", "Spring", "Spring", "Autumn", "Autumn", "Spring", "Spring",
    "Winter", "Autumn", "Spring", "Winter", "Not Available", "Autumn", "Winter", "Not Available", "Autumn", "Autumn",
    "Autumn", "Summer", "Winter", "Spring", "Spring", "Autumn", "Autumn", "Not Available", "Summer", "Autumn",
    "Not Available", "Spring", "Spring", "Autumn", "Autumn", "Spring", "Autumn", "Summer", "Spring", "Spring",
    "Summer", "Autumn", "Spring", "Winter", "Spring", "Winter", "Autumn", "Spring", "Autumn", "Spring", "Autumn",
    "Winter", "Not Available", "Not Available", "Spring", "Not Available", "Autumn", "Spring", "Autumn", "Summer",
    "Spring", "Autumn", "Summer", "Spring", "Summer", "Spring", "Summer", "Summer", "Summer", "Spring", "Autumn",
    "Spring", "Spring", "Spring", "Autumn", "Autumn", "Winter", "Autumn", "Autumn", "Spring", "Summer", "Spring",
    "Autumn", "Summer", "Spring", "Spring", "Spring", "Summer", "Autumn", "Autumn", "Spring", "Autumn", "Autumn",
    "Summer", "Spring", "Spring", "Spring", "Spring", "Spring", "Spring", "Spring", "Autumn", "Summer", "Spring",
    "Winter", "Spring", "Spring", "Summer", "Summer", "Winter", "Spring", "Summer", "Spring", "Spring", "Winter",
    "Spring", "Winter", "Autumn", "Spring", "Autumn", "Autumn", "Autumn", "Spring", "Summer", "Winter", "Spring",
    "Spring", "Spring"
]
# Define a function to determine energy source based on season, humidity, and GHG emissions
def determine_energy_source(season, humidity, ghg_emission):
    if season in ["Spring", "Summer"]:
        if humidity > 40 and ghg_emission < 100:
            return "Solar"
        else:
            return "Electricity"
    elif season in ["Autumn", "Winter"]:
        if humidity > 30 and ghg_emission < 150:
            return "Wind"
        else:
            return "Electricity"
    else:
        return "Electricity"

# Create a list to store energy source data
energy_source_data = []

# Populate the energy source list based on season, humidity, and GHG emissions
for season, humidity, ghg_emission in zip(season_data, humidity_data, ghg_emissions):
    energy_source_data.append(determine_energy_source(season, humidity, ghg_emission))

# Combine all data into a list of lists
all_data = list(zip(ghg_emissions, temperature_data, humidity_data, season_data, energy_source_data))

# Write data to a CSV file
with open('energy_source_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(['GHG Emissions', 'Temperature', 'Humidity', 'Season', 'Energy Source'])
    
    # Write data rows
    writer.writerows(all_data)

print("CSV file generated successfully.")



