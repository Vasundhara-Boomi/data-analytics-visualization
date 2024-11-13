from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# URL of the website with the data
url = 'https://github.com'

# Replace 'path/to/chromedriver' with the path to your ChromeDriver executable
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('path/to/chromedriver')

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the URL
driver.get(url)

# Extract data by finding HTML elements
# Replace these class names with the actual class names or other locators on the website
building_ids = driver.find_elements_by_css_selector('.building-id-class')  # Replace '.building-id-class' with the actual CSS selector
energy_sources = driver.find_elements_by_css_selector('.energy-source-class')  # Replace '.energy-source-class' with the actual CSS selector
consumptions = driver.find_elements_by_css_selector('.consumption-class')  # Replace '.consumption-class' with the actual CSS selector
temperatures = driver.find_elements_by_css_selector('.temperature-class')  # Replace '.temperature-class' with the actual CSS selector
hvac_systems = driver.find_elements_by_css_selector('.hvac-system-class')  # Replace '.hvac-system-class' with the actual CSS selector
lightning_types = driver.find_elements_by_css_selector('.lightning-type-class')  # Replace '.lightning-type-class' with the actual CSS selector
footage_areas = driver.find_elements_by_css_selector('.footage-area-class')  # Replace '.footage-area-class' with the actual CSS selector
facility_equipments = driver.find_elements_by_css_selector('.facility-equipment-class')  # Replace '.facility-equipment-class' with the actual CSS selector
costs = driver.find_elements_by_css_selector('.cost-class')  # Replace '.cost-class' with the actual CSS selector
# Repeat for other fields...

# Store the data in a CSV file
csv_filename = 'energy_data.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['Building_Id', 'Energy Source', 'Consumption', 'Temperature', 'HVAC System', 'Lightning Type',
                  'Footage area', 'Facility equipment', 'Cost', 'Occupancy status', 'Occupancy_type',
                  'Day of week', 'Time of day', 'Season', 'Building location', 'Building Construction Year',
                  'No.of Floors', 'Energy source effieciency rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write data rows
    for i in range(len(building_ids)):
        row_data = {
            'Building_Id': building_ids[i].text,
        'Energy Source': energy_sources[i].text,
        'Consumption': consumptions[i].text if i < len(consumptions) else None,
        'Temperature': temperatures[i].text if i < len(temperatures) else None,
        'HVAC System': hvac_systems[i].text if i < len(hvac_systems) else None,
        'Lightning Type': lightning_types[i].text if i < len(lightning_types) else None,
        'Footage Area': footage_areas[i].text if i < len(footage_areas) else None,
        'Facility Equipment': facility_equipments[i].text if i < len(facility_equipments) else None,
        'Cost': costs[i].text if i < len(costs) else None,
        
        }
        writer.writerow(row_data)

# Close the browser window
driver.quit()
