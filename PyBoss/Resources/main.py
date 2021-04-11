import os
import csv

# Declare variables:
employeeCSV = os.path.join('employee_data.csv')
outputfilename = 'reformatted_employee_data.csv'
id = []
name = []
dob = []
ssn = []
state = []
first_name = []
last_name = []
dob_reformatted = []
dob_reformatted = []
ssn_reformatted = []
state_reformatted = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Open file stream for reading:
with open(employeeCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for line in csvreader: # format as each line is read and save in memory
        id.append(line[0])
        name = line[1].split(" ")
        first_name.append(name[0])
        last_name.append(name[1])
        dob = line[2]
        dob_reformatted.append(dob.replace("-","/"))
        ssn = line[3]
        ssn_reformatted.append(f"***-**-{ssn[7:11]}")
        state = line[4]
        state_reformatted.append(us_state_abbrev[state])

zipped = zip(id, first_name, last_name, dob_reformatted, ssn_reformatted, state_reformatted)

# Open file stream for writing reformatted file:
with open(outputfilename, 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerows(list(zipped))

