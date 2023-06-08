import csv

file_path = "C:/Users/HP/Desktop/csv port/insurance.csv"

# Saving to column names as variables
ages = []
sexes = []
bmis = []
num_children = []
smoker_status = []
regions = []


#Converting the csv file to be used in our python code
with open(file_path) as insurance_csv:
    insurance_data = csv.DictReader(insurance_csv)
    
    #We want to see the first 10 rows in our dataset
    count = 0
    for i in insurance_data:
        #print(i)
        count += 1
        if count == 10:
            break
    
    #filling up our column names
    insurance_file = list(insurance_data)
    ages = [int(item['age']) for item in insurance_file]
    sexes = [item['sex'] for item in insurance_file]
    bmis = [float(item['bmi']) for item in insurance_file]
    num_children = [int(item['children']) for item in insurance_file]
    smoker_status = [str(item['smoker']) for item in insurance_file]
    regions = [str(item['region']) for item in insurance_file]
    insurance_charge = [float(item["charges"]) for item in insurance_file]
 
#creating a function to find the average of the fields with numerical values
def average_calculator(name, value):
    average =  sum(value) / len(value)
    print("The average {} is {}".format(name, average))
    return average

#Calling our function to find the avarage age 
average_calculator( "age",  ages)
# The Average age is 39.24

#Calling our function to find the avarage bmi
average_calculator( "bmi",  bmis)
# The average BMI is 30.67

# Calling our function to find the avarage Charge
average_calculator( "charges",  insurance_charge)
# The average charges is 13292.39

#finding the number of Males and Females in this dataset
males = []
females = []
for i in sexes:
    if i == 'male':
        males.append(i)
    else:
        females.append(i)
        # Printing the number of males and females
print("There are " + str(len(males)) + " males in this dataset")
print("There are " + str(len(females)) + " females in this dataset")
# There are 671 males and 657 females in this dataset

#finding the maximum and minimum BMIs in the dataset
max_bmi = max(bmis)
print("The maximum BMI in this dataset is " + str(max_bmi))
min_bmi = min(bmis)
print("The minimum BMI in this dataset is " + str(min_bmi))
#The maximum is 53.13 and minimum 15.96

# calculating the total number of people representing each region
distinct_regions = set(regions)
print(distinct_regions)
#the code above shows that there are 4 distinct regions in the dataset
southwest = []
southeast = []
northwest = []
northeast = []
for i in regions:
    if i == "southwest":
        southwest.append(i)
    elif i == "southeast":
        southeast.append(i)
    elif i == "northwest":
        northwest.append(i)
    else :
        northeast.append(i)
        
print( "There are", len(southwest), "people from southwest in this dataset") #324 people
print( "There are", len(southeast), "people from southeast in this dataset") #360 people
print("There are", len(northwest), "people from northwest in this dataset") #321 people
print("There are", len(northeast), "people from northeast in this dataset") #323 people

# finding the oldest and youngest individuals in the dataset
oldest = max(ages)
print("The oldest person in this dataset is " + str(oldest), "years old") #64
youngest = min(ages)
print("The oldest person in this dataset is " + str(youngest), "years old") #18



