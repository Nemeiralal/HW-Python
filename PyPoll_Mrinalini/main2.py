import os
import csv

csvpath=os.path.join('..','Resources','election_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    Candidates = {}
    Count = 0
    Votes_Cast = 0
    percent_of_votes = 0
    Most_Votes = 0
    Most_Voted = ""
    outputContents = []
    
    
    for row in csvreader:
        
        # Total votes casted
        candidate = row[2]
        Count += 1
        if candidate in Candidates.keys():
            Candidates[candidate] += 1
        else:
            Candidates[candidate] = 1
        #print(Candidates)
    
    
    # Print Statements
    outputContents.append("Election Results")
    outputContents.append("----------------------------------------")
    outputContents.append("Total Votes: "+ str(Count))
    outputContents.append("----------------------------------------")
    
            
    #total number of votes for each candidate
    for candidate in Candidates:
        Votes_Cast = Candidates[candidate]
    
        # percent of votes for each candidate
        percent_of_votes = (Candidates[candidate])/(Count) * 100
        outputContents.append(candidate+": "+ str(round(percent_of_votes,3))+"% "+ "("+str(Votes_Cast)+")")
        
        if Candidates[candidate] > Most_Votes:
            Most_Voted = candidate
            Most_Votes = Candidates[candidate]
        
        output_file_path = os.path.join('..','Resources','election_data.csv'.split(".")[0] + "_Result.txt")
        result_buffer = open(output_file_path, "w")
        
    
    #Print the winner's name
    outputContents.append("----------------------------------------")
    outputContents.append("Winner: "+ str(Most_Voted))
    outputContents.append("----------------------------------------")
    outputContents.append("The Result is also stored as/at _Result.txt")

    

    for outputContent in outputContents:
        print(outputContent)
        if outputContent != outputContents[-1]:
          print(outputContent,file=result_buffer)
        
    print()
    
    result_buffer.close()

    

        