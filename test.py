import os
import csv 

current_dir = os.path.dirname(__file__)

# Name of the CSV file
csv_file_name = 'data.csv'

# Path to the CSV file
csv_file_path = os.path.join(current_dir, csv_file_name)

print (csv_file_path)
# Ask for input from the user
amount = int(input("Deposit Amount: "))
print(amount)


# Open CSV file in write mode
with open(csv_file_path, mode='w',newline='') as file:
  # Create a CSV writer object
  writer = csv.writer(file)

  # Write the data to the CSV file
  writer.writerow([amount])


# Open and create csv file
# Write into csv file and autosaves in file
  

# We want to store multiple numbers. How can we store it to make it easier
  #to retrieve later on. Build a table. 

  # Store column wise, amount, date. 
  #column 1 | column 2
#<amount>|<date>
#so it would look like:
#32.0, 26-02-2024 