import csv

file_path = "C:/Users/HP/Desktop/csv port/insurance.csv"

# Saving to column names as variables
ages = []
sexes = []
bmis = []
num_children = []
smoker_status = []
regions = []
insurance_charge = []

#Converting the csv file to be used in our python code
with open(file_path) as insurance_csv:
    insurance_file = csv.DictReader(insurance_csv)
    
    #We want to see the first 10 rows in our dataset
    count = 0
    for i in insurance_file:
        #print(i)
        count += 1
        if count == 10:
            break
    
    #filling up our column names
    
    ages = [int(item['age']) for item in insurance_file]
    sexes = [ str(item['sex']) for item in insurance_file]
    bmis = [int(item['bmi']) for item in insurance_file]
    num_children = [int(item['children']) for item in insurance_file]
    smoker_status = [str(item['smoker']) for item in insurance_file]
    regions = [str(item['region']) for item in insurance_file]
    insurance_charge = [int(item['charges']) for item in insurance_file]
 
#Let's create a function to find the average of the fields with numerical values
def average_calculator(name, value):
    average =  sum(value) / len(value)
    print("The average {} is {}".format(name, average))
    return average

#Calling our function to find the avarage age 
average_calculator( "age",  ages)
