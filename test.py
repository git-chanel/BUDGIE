import os
import csv 

current_dir = os.path.dirname(__file__)

# Name of the CSV file
csv_file_name = 'data.csv'

# Path to the CSV file
csv_file_path = os.path.join(current_dir, csv_file_name)

print (csv_file_path)

# Open CSV file for writing 
def store_data_csv(csv_file_name, data):
# Open CSV file in write mode
  with open(csv_file_name, mode='w',newline='') as file:
  # Create a CSV writer object
    writer = csv.writer(file)
  # Write the data to the CSV file
    writer.writerow(['Amount','Date'])
    for row in data:
      writer.writerow(row)

# Appends/adds user input data into CSV
def add_data_csv(csv_file_name, amount, date):
  with open(csv_file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([amount, date])

# Ask for input from the user
def get_user_input():
  amount = int(input("Deposit Amount: "))
  date = str(input("Enter date (DD-MM-YYYY): "))

  return amount, date

# Create the csv with its columns
if not os.path.exists(csv_file_name):
  store_data_csv(csv_file_name, [])
# Ask user for input
amount, date = get_user_input()
print(amount, date)
# Add user input to CSV file
add_data_csv(csv_file_name, amount, date)
# Read data from CSV


# Open and create csv file
# Write into csv file and autosaves in file
  

# We want to store multiple numbers. How can we store it to make it easier
  #to retrieve later on. Build a table. 

  # Store column wise, amount, date. 
  #column 1 | column 2
#<amount>|<date>
#so it would look like:
#32.0, 26-02-2024 
  
