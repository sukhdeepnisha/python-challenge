import os
import csv

# path for csv file
csv_path = os.path.join('..', 'PyBank\Resources','budget_data.csv')
# path for output txt file
output_file_path=os.path.join('..', 'PyBank\Analysis','output.txt')

total_months=0
total_amount=0
total_change_profit_loss=0
greatest_decrease_profit=0
greatest_increase_profit =0
month_of_greatest_increase_profit=""
month_of_greatest_decrease_profit=""


# reading using CSV 
with open(csv_path) as csv_file:

    # CSV reader specifies delimeter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row first (skip if there is no header)
    csv_header = next(csv_reader)

    # to save the value of profit in previos month
    previous_profit = 0

    for row in csv_reader:
        # extract the date and Profit/loss values
        date = row[0]
        current_profit = int(row[1])
        
        # counting total months
        total_months = total_months + 1
        
        # counting total amount
        total_amount= total_amount + current_profit
        
        # counting profit by subtracting this month profit with the previous one
        profit_loss = current_profit - previous_profit
        
        if(profit_loss > greatest_increase_profit):
            greatest_increase_profit = profit_loss
            month_of_greatest_increase_profit=date
        
        if(profit_loss < greatest_decrease_profit):
            greatest_decrease_profit = profit_loss
            month_of_greatest_decrease_profit=date

        # counting total change in value of profit for the entire period
        total_change_profit_loss = total_change_profit_loss + profit_loss
        
        previous_profit = current_profit

with open(output_file_path,"w") as file:

    # finding average by dividing total change in profit with number of months
    average_change=total_change_profit_loss/total_months

    file.write("Financial Analysis\n")
    print("Financial Analysis")

    file.write("----------------------------\n")
    print("----------------------------")

    file.write("Total Months: " + str(total_months)+"\n")
    print("Total Months: " + str(total_months))

    file.write("Total: $"+ str(total_amount)+"\n")
    print("Total: $"+ str(total_amount))


    file.write("Average Change: $"+str(average_change)+"\n")
    print("Average Change: $"+str(average_change))

    file.write("Greatest Increase in Profits: "+month_of_greatest_increase_profit+" ($"+str(greatest_increase_profit)+")\n")
    print("Greatest Increase in Profits: "+month_of_greatest_increase_profit+" ($"+str(greatest_increase_profit)+")")
    
    file.write("Greatest Decrease in Profits: "+month_of_greatest_decrease_profit+" ($"+str(greatest_decrease_profit)+")")
    print("Greatest Decrease in Profits: "+month_of_greatest_decrease_profit+" ($"+str(greatest_decrease_profit)+")")
   