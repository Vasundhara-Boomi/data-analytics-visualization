import csv

def categorize_season(energy_intensity):
    if energy_intensity == "Not Available":
        return "Not Available"
    
    energy_intensity = float(energy_intensity)
    #low-autumn
    if 0.0 <= energy_intensity < 1.0:
        return "Autumn"
    #medium-spring
    elif 1.0 <= energy_intensity < 2.0:
        return "Spring"
    #High-Summer
    elif 2.0 <= energy_intensity < 3.0:
        return "Summer"
    #Very-High
    else:
        return "Winter"

def categorize_occupancy_type(square_feet):
    if square_feet == "Not Available":
        return "Not Available"
    
    square_feet = float(square_feet)
    
    if square_feet > 40000:
        return "Industrial"
    elif square_feet > 30000:
        return "Commercial"
    else:
        return "Residential"

def categorize_occupants(square_feet):
    if square_feet == "Not Available":
        return "Not Available"
    
    square_feet = float(square_feet)
    if square_feet <= 2000:
        return "1"
    elif square_feet <= 5000:
        return "2"
    elif 5000 < square_feet <= 10000:
        return "4"
    elif 10000 < square_feet <= 20000:
        return "6"
    else:
        return ">6"


square_feet_data = [
    14951, 9774, 1665, 3160, 10866, 14675, 13143, 6696, 304710, 34603,
    14341, 2040, 44277, 6943, 2304, 5500, 4456, 6287, 7275, 17262, 6160,
    10168, 4058, 5645, 4163, 4500, 9880, 9179, 7033, 11834, 9081, 11448,
    6345, 6239, 7815, 12524, 8657, 7586, 5664, 10780, 8391, 5392, 26228,
    5565, 6353, 8622, 2011, 8471, 3720, 1073, 58500, 37800, 29280, 1296,
    7072, 1144, 2460, 2030, 2652, 10132, 2774, 2312, 16804, 2100, 2688,
    1900, 6342, 16689, 1540, 7500, 1069, 5000, 3145, 2684, 15780, 3422,
    7113, 8099, 11408, 3000, 10263, 2250, 10016, 7380, 1989, 50000, 34065,
    10382, 5105, 16925, 10000, 27664, 1798, 4544, 16634, 80000, 44066,
    14400, 5696, 5413, 28146, 11254, 20874, 15868, 22348, 18000, 18476,
    8045, 9232, 5220, 3750, 14172, 18597, 12880, 1298, 7610, 3520, 7910,
    3067, 1843, 2097, 1537, 1631, 11764, 3109, 4004, 24260, 3273, 2856,
    28227, 3542, 21659, 2480, 1848, 4133, 11187, 14951, 9774, 1665, 3160,
    10866, 14675, 13143, 6696, 304710, 34603, 14341, 2040, 44277, 2304,
    5500, 4456, 7275, 17262, 6160, 10168, 4058, 5645, 4500, 9880, 9179,
    11834, 9081, 11448, 6345, 6239, 7815, 12524, 8657, 10780, 8391, 5392,
    26228, 6353, 8622, 58500, 37800, 3750, 7072, 2460, 2312, 2688, 1900,
    16689, 7500, 1069, 3145, 2684, 15780, 7113, 8099, 11408, 3000, 3000,
    7380, 1989, 34065, 16925, 27664
]


energy_data = [
    2.04, 0.97, 3.14, 2.83, 1.12, "Not Available", 1.34, 1.11, 1.37, 0.45,
    0.27, 3.2, 0.39, "Not Available", 0.15, 1.99, 2.54, 1.57, 1.3, 0.46,
    2.18, 1.28, "Not Available", 1.68, 0.47, 2.59, 1.01, 0.69, 1.47, 1.34,
    0.86, 0.83, 2.34, 1.59, 0.85, 0.96, 1.04, 1.3, 0.33, 1.11, 1.65, 1.08,
    0.64, 1.63, 2.34, 1.52, 2.06, "Not Available", 1.22, "Not Available", 2.77,
    1.33, "Not Available", 0.13, 1.78, 3.49, 2.39, 0.05, 0.33, "Not Available",
    0.19, 1.91, "Not Available", 1.75, 1.72, "Not Available", 0.72,
    "Not Available", 3.74, 1.45, 5.02, 0.44, 1.6, 4.47, 0.53, 1.6, 1.12,
    0.49, 0.79, 1.18, 1.82, 7.16, 0.15, 1.46, 3.93, "Not Available", 0.81,
    3.68, "Not Available", 0.89, 0.82, 0.94, 2.31, 3.55, 1.99, 1.85, 0.12,
    0.76, "Not Available", 2.46, 0.92, "Not Available", 1.83, 1.24, 0.96, 0.7,
    1.38, 0.08, 2.48, 1.3, 1.02, 2.75, 0.89, 1.88, 18.84, 1.36, 3.27, 0.25,
    1.5, 0.24, 1.41, 0.44, 3.39, "Not Available", "Not Available", 1.19,
    "Not Available", 0.26, 1.61, 0.72, 2.16, 1.57, 0.15, 2.26, 1.19, 2.41,
    1.73, 2.27, 2.29, 2.14, 1.16, 0.79, 1.35, 1.08, 1.58, 0.54, 0.17, 3.41,
    0.4, 0.43, 1.9, 2.55, 1.27, 0.63, 2.13, 1.53, 1.84, 1.92, 2.68, 0.82,
    0.78, 1.15, 0.91, 0.79, 2.87, 1.93, 1.32, 1.27, 1.22, 1.36, 1.93, 1.34,
    0.87, 2.9, 1.71, 4.07, 1.55, 1.01, 2.33, 2.36, 3.77, 1.52, 2.47, 1.21,
    1.03, 3.7, 1.85, 5.92, 0.78, 1.07, 0.63, 0.93, 0.98, 1.74, 2.03, 5.25,
    1.5, 1.62, 1.22
]

# Create a new list with categorized seasons
seasons = [categorize_season(energy_intensity) for energy_intensity in energy_data]

# # Combine original data, seasons, and headers into a list of lists
# data_to_write = [["Energy Intensity", "Season"]]
# for energy_intensity, season in zip(energy_data, seasons):
#     data_to_write.append([str(energy_intensity), season])

# # Write to a CSV file
# csv_file_path = "building data.csv"
# with open(csv_file_path, mode="w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data_to_write)

# print(f"Results have been written to {csv_file_path}.")

# Create a new list with categorized occupancy type and number of occupants
occupancy_data = [["Square Feet", "Occupancy Type", "No. of Occupants"]]
for square_feet in square_feet_data:
    occupancy_type = categorize_occupancy_type(square_feet)
    occupants = categorize_occupants(square_feet)
    occupancy_data.append([str(square_feet), occupancy_type, occupants])

# Write to a CSV file
csv_file_path = "occupancy_data.csv"
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(occupancy_data)

print(f"Results have been written to {csv_file_path}.")
