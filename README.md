# **PyPoll - Analysis of the Election Results using Python**
##  Module 3 - Python or PyPoll
### Overview of Election Analysis
The purpose of the analysis was to audit the congressional election results and perform additional analysis for the Colorado election comission.  The data for analysis can be found in https://github.com/cherylberger/Election-Analysis/blob/main/Resources/election_results.csv.  The data will be analyzed to provide additional information on the voter turnout by county.  The analysis will provide a summary of the total vote count in each county and determine the county with the highest turnout.  In addition, the percentage of votes from each county as a percent of the total will be displayed.     
### Results

#### How many votes were cast in this congressional election?
  
  **There were 369,711 votes cast in the congressional election.**
  
  *First, set the code to create a vote counter variable and set the counter to zero (0) as displayed below:* 
  
      # Initialize a total vote counter.
      total_votes = 0
      
  *Next, open the datafile (.csv) and covert it into a list of dictionaries called "election_data" and read the header row.*
  
      # Read the csv and convert it into a list of dictionaries
      with open(file_to_load) as election_data:
        reader = csv.reader(election_data)
           # Read the header
        header = next(reader)
        
  *Then, index through the rows in the file and add 1 to the vote counter for each row in the file to calculate the total votes.*
  
        # For each row in the CSV file.
        for row in reader:
            # Add to the total vote count
        total_votes = total_votes + 1

#### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    
    **Jefferson 10.5% 38,885**
    **Denver 82.8% 306,055**
    ***Arapahoe 6.7% 24,801**

         

*To determine the number of votes in each county and the percentatge of the total, we must calculate the number of votes cast in each country and the percentage of the total votes. First, identify the arrays needed to perform the calculations* 
      # 2: Track the largest county and county voter turnout.
        Winning_county = ""
        Winning_county_turnout = 0
        Winning_county_percentage = 0    

*Then, loop through the data to retrieve the vote count for each county and calculate the percent of votes in each county by dividing by the total.  Set the values to display with the correct data formats and print the results.*

     # 6a: Write a for loop to get the county from the county dictionary.
        for county_name in county_votes:
          # 6b: Retrieve the county vote count.
          cvotes= county_votes.get(county_name)
          # 6c: Calculate the percentage of votes for the county.
          county_vote_percentage = float(cvotes) / float(total_votes) * 100
          county_results = (
              f"{county_name}: {county_vote_percentage:.1f}% ({cvotes:,})\n")
          # 6d: Print the county results to the terminal.
          print(county_results)

#### Which county had the largest number of votes?

**Denver had the largest number of votes, 306,055** 

*To count the votes in each county, define the index for the name of the country (column B) in the datafile*

        # 3: Extract the county name from each row. 
          county_name = row[1]
          
 *Use conditionals to count votes for each county named in the data file, add votes by an increment of "1".*
 
        # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_options:
            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
            # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1 
            
#### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

  **Charles Casper Stockham: 23.0% (85,213)**
  **Diana DeGette: 73.8% (272,892)**
  **Raymon Anthony Doane: 3.1% (11,606)** 

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    
#### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

    **Winner: Diana DeGette**
    **Winning Vote Count: 272,892**
    **Winning Percentage: 73.8%**
  
 *The candidate results can be analyzed using similar code except that the variable is candidate rather than county for this analysis:* 
 
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:
    # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
    #  Save the candidate results to our text file
        txt_file.write(candidate_results)
    # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
     # Print the winning candidate (to terminal)
        winning_candidate_summary = (
          f"-------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"-------------------------\n")
            print(winning_candidate_summary)
            
## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.63.0

## Summary
The election commission may find the following advantages to the use of this script when analyzing election outcomes:  
  1) Use of lists and dictionaires rather than pseuocode makes the PyPoll_Challenge_CB.py script more easily modified to other datafiles.  
  2) Use of conditional statements to append the lists of candidate and county names allows for modifications to the election_results.csv. beyond the current structure of the    data frame such as adding additional counties and/or other candidates.
  3) Formulas for total vote count and percentage varaibles are defined by indexing through the rows of data to calculate rather than defining a specific range.  All vote counters are programmed to start at zero.
  4) Although some cleaning of the data file will be needed, and the analyst must be aware of available information; The script could be modifed to analyze a different data file by changing the directory and file name indicated in the with open statements.  In addition, the script could be modified to analyze the number of votes for each candidate by county to determine if the outcome in the largest country predicted the overall election outcome.
