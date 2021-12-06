# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save teh file to a path
file_to_save = os.path.join("analysis", "election analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: Perform the analysis
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print each row in the CSV file
    headers = next(file_reader)
    print(headers)
    