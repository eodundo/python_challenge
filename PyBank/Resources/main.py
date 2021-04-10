#importing packages
import os
import csv

#loading in csv file
budget_data = os.path.join("budget_data.csv")

#creating lists
profits = []
net_change = []
months =[]

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

# Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    for row in csvreader:
    
#Count the number of months 
        months.append(row[0])
        each_month = len(set(months))
        #months = months + 1

#Calculate total profits
        profits.append(int(row[1]))
        total_profits = sum(profits)

#for loop appending the net change list for each month 

    for i in range(0,len(profits) -1): 

        net_change.append(int(profits[i+1]) - int(profits[i]))
#calculate the averae
    average_profits = sum(net_change)/len(net_change)
#append max n min 
        #max_min_dates.append(row[0])

#find the increase and decrease
    greatest_increase = max(profits)
    greatest_decrease = min(profits)
    
#dates of max and min
    max_profit_date = months[profits.index(greatest_increase)]
    min_profit_date = months[profits.index(greatest_decrease)]

#print statements
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Number of Months: {str(each_month)}")
    print(f"Total: ${str(int(total_profits))}")
    print(f"Average Change: $ {str(int(average_profits))}" )
    print("Greatest Increase in Profits: " + str(max_profit_date) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(min_profit_date) + " ($" + str(greatest_decrease)+ ")")
    
#will output the program to a text file
with open("output.txt", "w") as x: 
   print("Financial Analysis \n", file = x)
   print("-----------------------------------\n", file=x)
   print(f"Total Number of Months: {str(months)}\n", file = x)  
   print(f"Total: ${str(int(total_profits))}\n", file = x)
   print(f"Average Change: $ {str(int(average_profits))}\n", file = x )
   print("Greatest Increase in Profits: " + str(max_profit_date) + " ($" + str(greatest_increase) + ")\n", file = x)
   print("Greatest Decrease in Profits: " + str(min_profit_date) + " ($" + str(greatest_decrease)+ ")\n", file = x)



