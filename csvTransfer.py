import csv

# Define input and output CSV filenames
input_csv_filename = './ProccessedData_2.csv'
output_csv_filename = './ProccessedData.csv'

# Define fieldnames for input and output CSV files
input_fieldnames = [
    "Type of crime",
    "Date of Offend",
    "Off.Name",
    "Off.age",
    "Off.gender",
    "crime description",
    "crime Location",
    "Name of victim",
    "Victim Gender",
    "Victim Age",
    "Conclusion",
    "Link/source",
    "lat",
    "long",
    "Time_of_Day",
    "Location_Type",
    "Weather_Conditions"
]

output_fieldnames = input_fieldnames

# Read data from input CSV file and append to output CSV file
with open(input_csv_filename, 'r', newline='') as input_csv_file, \
     open(output_csv_filename, 'a', newline='') as output_csv_file:
    
    reader = csv.DictReader(input_csv_file, fieldnames=input_fieldnames)
    writer = csv.DictWriter(output_csv_file, fieldnames=output_fieldnames)
    
    # Skip header in input CSV file
    next(reader)
    
    # Check if output file is empty
    output_empty = output_csv_file.tell() == 0
    
    # Write header in output CSV file if it's empty
    if output_empty:
        writer.writeheader()
    
    # Write each row from input CSV file to output CSV file
    for row in reader:
        writer.writerow(row)