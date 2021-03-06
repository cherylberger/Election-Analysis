counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county":"Arapahoe", "registered voters": 422829}, {"county":"Denver", "registered_voters":463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?")
message_to_candidate = ("
    f"You received {candidate_votes} number of votes. " 
    f"The total number of votes in the election was {total_votes}. " 
    f"You received {candidate_votes/total_votes *100}% of the total votes. "")
    print(message_to_candidate)