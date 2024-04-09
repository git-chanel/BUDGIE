import os
import csv 
from datetime import datetime

# Open CSV file for writing 
def store_data_csv(csv_file_name, data):
  # Check if file exists
  if not os.path.exists(csv_file_name):
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
  with open(csv_file_name, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([amount, date])
   
# Ask for input from the user
def get_user_input():
  while True:
    amount = str(input("Deposit Amount: "))
    if validate_amount(amount):
      break
  while True:
    date = str(input("Enter date (DD-MM-YYYY): "))
    if validate_date(date):
      break

  return amount, date

def validate_amount(amount):
  try: 
      print(float(amount))
      return True
  except ValueError as e:
      print("Incorrect input")
      print(e)
      return False

def validate_date(date):
  try:
    date = datetime.strptime(date, "%d-%m-%Y")  
    print(date)
    return True
  except ValueError as e:
    print("Incorrect input")
    return False
  
# Read data from CSV
def read_data_csv(csv_file_name):
  deposit = {}
  with open(csv_file_name, mode='r', newline='') as file:
    # Reads CSV as a dictionary where keys are dates amd values are amount
    reader = csv.DictReader(file)
    for row in reader:
      # Add userAmounts of the same dates
      
      
      # Pass not the variables, but the name of the columns prewritten in data.csv
      key = (row['Date'])
      value = row['Amount']
      if key in deposit:
        deposit[key] = float(value) + float(deposit[key])
      else:
        deposit[key] = float(value)
      print(row)
  return deposit

# Get the file name and path
def getDataFilePath():
  # Hardcoded name of the CSV file
  csv_file_name = 'data.csv'

  # Path to the CSV file
  return os.path.join(current_dir, csv_file_name)

if __name__ == '__main__': 
  current_dir = os.path.dirname(__file__)

  csv_file_path = getDataFilePath()

  # Create the csv with its columns
  store_data_csv(csv_file_path, [])
  # Ask user for input
  amount, date = get_user_input()
  #print(amount, date)
  # Add user input to CSV file
  add_data_csv(csv_file_path, amount, date)
  print (csv_file_path)
  deposit = read_data_csv(csv_file_path)
  print(deposit)

# Open and create csv file
# Write into csv file and autosaves in file
  
# We want to store multiple numbers. How can we store it to make it easier
  #to retrieve later on. Build a table. 

  # Store column wise, amount, date. 
  #column 1 | column 2
#<amount>|<date>
#so it would look like:
#32.0, 26-02-2024 
  
# Make a function to read the data.csv and make it return a dictionary, str date as a key
# and amount as value

# make the functions work properly with its parameters
# and adjust all function calls and variables in main
# so it can print and input just the way how it did before.
  
  # we are refactoring
