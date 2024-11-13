
"""
import random

for i in range(100):
    random_time = f"{random.randint(0, 23):02d}:{random.randint(0, 0):02d}"
    print(random_time)"""
    
    
import pandas as pd
import random

# Sample day and time data
day_time_data = {
    'Day of week': [
    'Saturday', 'Wednesday', 'Tuesday', 'Saturday', 'Friday', 'Saturday', 'Thursday', 'Wednesday', 'Wednesday', 'Friday',
    'Friday', 'Sunday', 'Friday', 'Thursday', 'Friday', 'Monday', 'Friday', 'Thursday', 'Wednesday', 'Monday', 'Monday',
    'Saturday', 'Friday', 'Wednesday', 'Friday', 'Friday', 'Saturday', 'Monday', 'Thursday', 'Tuesday', 'Monday', 'Saturday',
    'Thursday', 'Saturday', 'Thursday', 'Monday', 'Sunday', 'Monday', 'Wednesday', 'Sunday', 'Monday', 'Sunday', 'Tuesday',
    'Wednesday', 'Wednesday', 'Monday', 'Thursday', 'Saturday', 'Sunday', 'Monday', 'Sunday', 'Sunday', 'Monday', 'Thursday',
    'Sunday', 'Saturday', 'Wednesday', 'Wednesday', 'Monday', 'Tuesday', 'Sunday', 'Wednesday', 'Thursday', 'Sunday', 'Tuesday',
    'Sunday', 'Saturday', 'Monday', 'Tuesday', 'Wednesday', 'Tuesday', 'Monday', 'Monday', 'Thursday', 'Tuesday', 'Monday',
    'Friday', 'Saturday', 'Sunday', 'Tuesday', 'Sunday', 'Friday', 'Monday', 'Saturday', 'Saturday', 'Friday', 'Wednesday',
    'Monday', 'Wednesday', 'Monday', 'Thursday', 'Thursday', 'Friday', 'Saturday', 'Tuesday', 'Friday', 'Sunday', 'Thursday',
    'Sunday', 'Thursday', 'Thursday', 'Thursday', 'Sunday', 'Monday', 'Monday', 'Sunday', 'Monday', 'Tuesday', 'Sunday', 'Wednesday',
    'Thursday', 'Sunday', 'Tuesday', 'Sunday', 'Saturday', 'Monday', 'Thursday', 'Friday', 'Saturday', 'Wednesday', 'Wednesday',
    'Tuesday', 'Saturday', 'Friday', 'Saturday', 'Thursday', 'Wednesday', 'Wednesday', 'Friday', 'Friday', 'Sunday', 'Friday',
    'Thursday', 'Friday', 'Monday', 'Friday', 'Thursday', 'Wednesday', 'Monday', 'Friday', 'Sunday', 'Friday', 'Thursday', 'Friday',
    'Monday', 'Thursday', 'Wednesday', 'Monday', 'Saturday', 'Friday', 'Wednesday', 'Friday', 'Friday', 'Saturday', 'Sunday',
    'Friday', 'Saturday', 'Thursday', 'Thursday', 'Friday', 'Monday', 'Friday', 'Thursday', 'Wednesday', 'Monday', 'Friday',
    'Sunday', 'Friday', 'Thursday', 'Friday', 'Monday', 'Monday', 'Friday', 'Thursday', 'Wednesday', 'Monday', 'Saturday', 'Saturday','Monday', 'Thursday', 'Thursday', 'Friday', 'Saturday', 'Tuesday', 'Friday', 'Sunday', 'Thursday',
    'Sunday', 'Thursday', 'Sunday', 'Monday', 'Monday', 'Sunday', 'Wednesday',
    'Thursday', 'Sunday', 'Tuesday', 'Saturday', 'Monday'
],
    'Time of day': [
    '01:00', '21:00', '05:00', '14:00', '20:00', '20:00', '00:00', '17:00', '14:00', '03:00', '15:00', '04:00', '13:00',
    '19:00', '01:00', '14:00', '08:00', '16:00', '13:00', '21:00', '20:00', '21:00', '17:00', '18:00', '01:00', '09:00',
    '10:00', '20:00', '20:00', '19:00', '07:00', '02:00', '00:00', '06:00', '20:00', '08:00', '01:00', '18:00', '19:00',
    '04:00', '21:00', '00:00', '05:00', '10:00', '08:00', '05:00', '00:00', '18:00', '11:00', '11:00', '13:00', '16:00',
    '07:00', '17:00', '09:00', '20:00', '06:00', '02:00', '06:00', '15:00', '07:00', '17:00', '08:00', '17:00', '17:00',
    '07:00', '10:00', '02:00', '22:00', '07:00', '10:00', '05:00', '09:00', '08:00', '07:00', '22:00', '17:00', '19:00',
    '01:00', '06:00', '02:00', '16:00', '00:00', '18:00', '16:00', '09:00', '01:00', '21:00', '01:00', '13:00', '12:00',
    '21:00', '17:00', '06:00', '11:00', '09:00', '14:00', '19:00', '20:00', '21:00', '15:00', '03:00', '13:00', '04:00',
    '17:00', '16:00', '11:00', '23:00', '21:00', '20:00', '03:00', '15:00', '03:00', '13:00', '04:00', '08:00', '15:00',
    '15:00', '16:00', '04:00', '19:00', '09:00', '12:00', '15:00', '20:00', '03:00', '20:00', '09:00', '11:00', '21:00',
    '18:00', '06:00', '11:00', '23:00', '21:00', '10:00', '04:00', '11:00', '09:00', '14:00', '19:00', '20:00', '21:00',
    '19:00', '14:00', '19:00', '04:00', '01:00', '13:00', '02:00', '19:00', '17:00', '09:00', '12:00', '23:00', '22:00',
    '07:00', '19:00', '03:00', '22:00', '01:00','00:00', '05:00', '10:00', '08:00', '05:00', '00:00', '18:00', '11:00', '11:00', '13:00', '16:00',
    '07:00', '17:00', '20:00', '06:00', '02:00', '06:00', '15:00', '07:00', '17:00', '08:00', '17:00', '17:00',
    '07:00', '10:00', '02:00', '08:00', '07:00', '22:00', '17:00', '19:00',
    '01:00', '06:00', '02:00', '16:00', '00:00', '18:00', '16:00'
]
}

def generate_temperature(day, time):
    # Simulate temperature changes based on the time of day
    if 6 <= int(time.split(':')[0]) < 18:  # Daytime (6:00 to 18:00)
        return round(random.uniform(23, 38))  # Simulate warmer temperatures
    else:  # Nighttime
        return round(random.uniform(12, 23))  # Simulate colder temperatures

# Apply the temperature function to the data
temperature_data = pd.DataFrame(day_time_data)
temperature_data['Temperature'] = temperature_data.apply(lambda row: generate_temperature(row['Day of week'], row['Time of day']), axis=1)

# Save to CSV file
temperature_data.to_csv('temperature_data.csv', index=False)

# Display the result
print(temperature_data)


"""
import pandas as pd
import random

# Your provided data
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

time_of_day_data = [
    '01:00', '21:00', '05:00', '14:00', '20:00', '20:00', '00:00', '17:00', '14:00', '03:00', '15:00', '04:00', '13:00',
    '19:00', '01:00', '14:00', '08:00', '16:00', '13:00', '21:00', '20:00', '21:00', '17:00', '18:00', '01:00', '09:00',
    '10:00', '20:00', '20:00', '19:00', '07:00', '02:00', '00:00', '06:00', '20:00', '08:00', '01:00', '18:00', '19:00',
    '04:00', '21:00', '00:00', '05:00', '10:00', '08:00', '05:00', '00:00', '18:00', '11:00', '11:00', '13:00', '16:00',
    '07:00', '17:00', '09:00', '20:00', '06:00', '02:00', '06:00', '15:00', '07:00', '17:00', '08:00', '17:00', '17:00',
    '07:00', '10:00', '02:00', '22:00', '07:00', '10:00', '05:00', '09:00', '08:00', '07:00', '22:00', '17:00', '19:00',
    '01:00', '06:00', '02:00', '16:00', '00:00', '18:00', '16:00', '09:00', '01:00', '21:00', '01:00', '13:00', '12:00',
    '21:00', '17:00', '06:00', '11:00', '09:00', '14:00', '19:00', '20:00', '21:00', '15:00', '03:00', '13:00', '04:00',
    '17:00', '16:00', '11:00', '23:00', '21:00', '20:00', '03:00', '15:00', '03:00', '13:00', '04:00', '08:00', '15:00',
    '15:00', '16:00', '04:00', '19:00', '09:00', '12:00', '15:00', '20:00', '03:00', '20:00', '09:00', '11:00', '21:00',
    '18:00', '06:00', '11:00', '23:00', '21:00', '10:00', '04:00', '11:00', '09:00', '14:00', '19:00', '20:00', '21:00',
    '19:00', '14:00', '19:00', '04:00', '01:00', '13:00', '02:00', '19:00', '17:00', '09:00', '12:00', '23:00', '22:00',
    '07:00', '19:00', '03:00', '22:00', '01:00','00:00', '05:00', '10:00', '08:00', '05:00', '00:00', '18:00', '11:00', '11:00', '13:00', '16:00',
    '07:00', '17:00', '20:00', '06:00', '02:00', '06:00', '15:00', '07:00', '17:00', '08:00', '17:00', '17:00',
    '07:00', '10:00', '02:00', '08:00', '07:00', '22:00', '17:00', '19:00',
    '01:00', '06:00', '02:00', '16:00', '00:00', '18:00', '16:00'
]

# Generate temperature data based on the provided logic
def generate_humidity(season, time_of_day):
    # Simulate humidity values based on the season and time of day
    if season == "Summer":
        if 6 <= int(time_of_day.split(':')[0]) < 18:  # Daytime (6:00 to 18:00)
            return round(random.uniform(40, 60), 2)  # Simulate higher humidity during the day in summer
        else:  # Nighttime
            return round(random.uniform(30, 50), 2)  # Simulate lower humidity at night in summer
    elif season == "Winter":
        if 6 <= int(time_of_day.split(':')[0]) < 18:  # Daytime (6:00 to 18:00)
            return round(random.uniform(20, 40), 2)  # Simulate higher humidity during the day in winter
        else:  # Nighttime
            return round(random.uniform(10, 30), 2)  # Simulate lower humidity at night in winter
    else:
        return round(random.uniform(30, 50), 2)  # For other seasons, simulate moderate humidity

humidity_data = pd.DataFrame({'Season': season_data, 'Time of day': time_of_day_data})

# Apply the humidity function to the data
humidity_data['Humidity (%)'] = humidity_data.apply(lambda row: generate_humidity(row['Season'], row['Time of day']), axis=1)

# Save the DataFrame to a CSV file
humidity_data.to_csv('humidity_data.csv', index=False)




print(len(season_data))

"""
