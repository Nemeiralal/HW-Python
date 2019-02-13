import os
import csv

csvpath=os.path.join('..','Resources','budget_data.csv')
print(csvpath)
with open(csvpath,newline='') as csvfile:
    csvrdr=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    Month = []
    Profit_Loss = []
    Diff_of_succ_profit_loss = []
    Greatest_Increase_During_Month = ""
    Greatest_Decrease_During_Month = ""
    outputContents = []
    
    for row in csvrdr:
        Month.append(row[0])   
        Profit_Loss.append(int(row[1]))
      
        
    for i in range(1, len(Profit_Loss)):
        
        Diff_of_succ_profit_loss.append(Profit_Loss[i] - Profit_Loss[i-1])
        Average_Change = sum(Diff_of_succ_profit_loss) / len(Diff_of_succ_profit_loss)
        Greatest_Increase = max(Diff_of_succ_profit_loss)
        Greatest_Increase_During_Month = str(Month[Diff_of_succ_profit_loss.index(max(Diff_of_succ_profit_loss))+1])
        Greatest_Decrease = min(Diff_of_succ_profit_loss)
        Greatest_Decrease_During_Month = str(Month[Diff_of_succ_profit_loss.index(min(Diff_of_succ_profit_loss))+1])
    
    
    output_file_path = os.path.join('..','Resources','budget_data.csv'.split(".")[0] + "_Result.txt")
    
    result_buffer = open(output_file_path, "w")
    
    outputContents.append("Financial Analysis")
    outputContents.append("----------------------------------------")
    outputContents.append("Total Months: "+str(len(Month)))
    outputContents.append("Net Total: $"+str(sum(Profit_Loss)))
    outputContents.append("Average Change: $"+str(round(Average_Change,2)))
    outputContents.append("Greatest Increase in Profits: "+str(Greatest_Increase_During_Month) + "($" + str(Greatest_Increase) + ")")
    outputContents.append("Greatest Decrease in Profits: "+str(Greatest_Decrease_During_Month) + "($" +  str(Greatest_Decrease) + ")")
    outputContents.append("The Result is also stored as/at "+'budget_data.csv'.split(".")[0] + "_Result.txt")

    for outputContent in outputContents:
        print(outputContent)
        if outputContent != outputContents[-1]:
          print(outputContent,file=result_buffer)
        
    print()
    
    result_buffer.close()



