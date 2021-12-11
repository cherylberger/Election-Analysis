# Election-Analysis
Module 3 - Python or PyPoll
# PyPoll - Analysis of the Election Results using Python
## Project Overview
### Overview of Election Audit: Explain the purpose of this election audit analysis.
The purpose of the analysis was to audit the election results and perform additional analysis.  The data will be analyzed to provide additional information on the voter turnout.  The analysis will provide a summary of the total vote count in each county and determine the county with the highest turnout.  In addition, the percentage of votes from each county as a percent of the total will be displayed.     
## Results

### Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

#### How many votes were cast in this congressional election?
To determine the total number of votes cast: 
  '# Initialize a total vote counter.
    total_votes = 0
   Write a for statement to loop through the data to add votes as applicable
  '# For each row in the CSV file.
      for row in reader:
  '# Add to the total vote count
      total_votes = total_votes + 1
      
#### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

    First create a new list for the county and a dictionary to define the total votes in each county.
     '# Create a county list and county votes dictionary.
        county_list = []
        county_votes_dict = {} 
    Then from the county list, look for rows with matching county names.
    '# Extract the county name from each row. 
       county_name = row [0]
    Define the output fields for the country with the highest total votes (largest_county) and the county with the highest voter turnout. 
    '# 2: Track the largest county and county voter turnout.
        largest_county = ""
        county_turnout = 0
#### Which county had the largest number of votes?
    '# 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:
    '# 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
    '# 4c: Begin tracking the county's vote count.
            county_votes_dict[county_name] = 0
     '# 5: Add a vote to that county's vote count.
            county_votes_dict[county_name] += 1
      
#### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
 '# 6a: Write a for loop to get the county from the county dictionary.
    for row in reader:
  '# 6b: Retrieve the county vote count.
     county_votes = county_votes[county_name]
  '# 6c: Calculate the percentage of votes for the county. 
      county_vote_percentage = float(county_votes) / float(total_votes) * 100
  '# 7: Print the county with the largest turnout to the terminal.
       largest_county = (
         f"{county_name}: {county_vote_percentage:.1f}% ({total_votes:,})\n")        
         print (largest_county)
   '# 8: Save the county with the largest turnout to a text file.
         txt_file.write(largest_county)


#### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
 '# Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

  '# Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

   '# Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
   '#  Save the candidate results to our text file.
        txt_file.write(candidate_results)

   '# Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    '# Print the winning candidate (to terminal)
        winning_candidate_summary = (
          f"-------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"-------------------------\n")
            print(winning_candidate_summary)

    '# Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)

## Resources



## Summary
### Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
Summarize what code is easily translated to other elections.  
  1) Use of lists and dictionaires, 
  2) use of conditional statements to append the lists of candidate and county names allows for modifications to the file beyond the current structure of the data frame (more counties and more candidates).
  3) Formulas for total vote count and percentage varaibles are defined by indexing through the rows of data to calculate rather than defining a specific range.  All vote counters are programmed to start at zero.
The script could be modifed to analyze a different data file by changing the directory and file name indicated in the with open statements
The script could be modified to 
