import csv 
data_set = []
with open('insurance.csv') as insurance_data:
  contents = csv.DictReader(insurance_data)
  for row in contents:
    data_set.append(row)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('insurance.csv')


#exploring the data


#Median Insurance Cost: Encounter the middle point of the charges.

#Average Insurance Cost: Calculate the overall average cost of insurance across all individuals in the dataset.
#Average Insurance Cost by Gender: Break down the average cost of insurance by gender to identify any disparities between males and females.
#Average Insurance Cost by Age Group: Segment the insured population into age groups to examine how age affects insurance costs.
#Average Insurance Cost by Region: Analyze the insurance costs across different geographic regions to identify regional cost variations and potential factors contributing to these differences.
#Smokers vs. Non-Smokers Average Cost: Compare the average insurance costs for smokers and non-smokers, highlighting the financial impact of smoking on medical insurance.
#BMI Analysis: Create a histogram of BMI (Body Mass Index) groups to explore the distribution of BMI among the insured population and analyze the average insurance cost by BMI group.

'''
1) Find out the average age of the patients in the dataset.
2) Analyze where a majority of the individuals are from.
3) Averege costs between smokers vs. non-smokers.
4) Male female isurace costs on averege
5) Figure out what the average age is for someone who has at least one child in this dataset.
6) How number of children correlates with smoking for males and females
7) Split the data for male/ female and see price difference for each changing atribute (BMI - below and above averege, smoker/non-smokers, children/no children)
'''


#function to get average
#this function calculates the means of the numerical data in the dataset
def get_mean(data, key):
  list = []
  for record in data:
    list.append(float(record[key]))
    mean = statistics.mean(list)
  return f'the average age for {key} is {mean}'
# this function calculates the median for the numerical data in the dataset


def get_median(data,key):
  list = []
  for record in data:
    list.append(float(record[key]))
  median = statistics.median(list)
  return f'the median for  {key} is {median}'

#this function calculates the deviation for each  numerical data in the dataset
def get_dev(data,key):
  list = []
  for record in data:
    list.append(float(record[key]))
  deviation = statistics.stdev(list)
  return f'the deviation for {key} is {deviation}'
#this function calculates the mode of each numerical data in teh dataset


def get_mode(data,key):
  list = []
  for record in data:
    list.append(float(record[key]))
  mode = statistics.mode(list)
  return f'the mode for {key} is {mode}'

#descriptive statistics(distribution)
#age statistics
mean_of_age = get_mean(data_set,'age')
median_of_age = get_median(data_set,'age')
deviation_of_age = get_dev(data_set,'age')
mode_of_age = get_mode(data_set,'age')
#bmi statistics
mean_of_bmi = get_mean(data_set,'bmi')
deviation_of_bmi = get_dev(data_set,'bmi')
median_of_bmi = get_median(data_set,'bmi')
mode_of_bmi = get_mode(data_set,'bmi')
#dhildren statistics
mean_of_children = get_mean(data_set,'children')
median_of_children = get_median(data_set,'children')
deviation_of_children = get_dev(data_set,'children')
mode_of_children = get_mode(data_set,'children')
#charges statistics
mode_of_charges = get_mode(data_set,'charges')
deviation_of_charges = get_dev(data_set,'charges')
median_of_charges = get_median(data_set,'charges')
mean_of_charges = get_mean(data_set,'charges')

#demographics
#smocker 
smoker_cost = sum(float(record['charges']) for record in data_set if record['smoker'] == 'yes') #amount paid by smoker
avg_smoker_cost =  sum(float(record['charges']) for record in data_set if record['smoker'] == 'yes') / sum(1 for record in data_set if record['smoker'] == 'yes') if data_set else 0
smoker_bmi = sum(float(record['bmi']) for record in data_set if record['smoker'] == 'yes')
#nonsmoker
non_smoker_cost = sum(float(record['charges']) for record in data_set if record['smoker'] == 'no') #amount paid by non smoker
avg_non_smoker_cost= average_smoker_cost = sum(float(record['charges']) for record in data_set if record['smoker'] == 'no') / sum(1 for record in data_set if record['smoker'] == 'no') if data_set else 0
non_smoker_bmi = sum(float(record['bmi']) for record in data_set if record['smoker'] == 'no')
# men statistics
total_charge_male = sum(float(record['charges']) for record in data_set if record['sex'] == 'male') #total amount paid for males
avg_charge_male = sum(float(record['charges']) for record in data_set if record['sex'] == 'male') / sum(1 for record in data_set if record['sex'] == 'male') if data_set else 0
smoker_cost_male= sum(float(record['charges'])for record in data_set if record['smoker'] == 'yes' and record['sex'] == 'male') #amount paid by male smoker
avg_cost_male_smoker = sum(float(record['charges'])for record in data_set if record['smoker'] == 'yes' and record['sex'] == 'male') / sum(1 for record in data_set if record['smoker'] == 'yes'and record['sex'] == 'male') if data_set else 0
non_smoker_male_cost = sum(float(record['charges'])for record in data_set if record['smoker'] == 'no' and record['sex'] == 'male') # amount paid by male non smoker
avg_cost_male_non_smoker = sum(float(record['charges'])for record in data_set if record['smoker'] == 'no' and record['sex'] == 'male') / sum(1 for record in data_set if record['smoker'] == 'no'and record['sex'] == 'male') if data_set else 0
 #bmi men
male_bmi = sum(float(record['bmi']) for record in data_set if record['sex'] == 'male')
avg_male_bmi = sum(float(record['bmi']) for record in data_set if record['sex'] == 'male')/sum( 1 for record in data_set if record['sex'] == 'male') if data_set else 0
male_smoker_bmi = sum(float(record['bmi']) for record in data_set if record['smoker'] == 'yes' and record['sex'] == 'male')
male_non_smoker_bmi = sum(float(record['bmi']) for record in data_set if record['smoker'] == 'no' and record['sex'] == 'male')
avg_male_smoker_bmi = sum(float(record['bmi']) for record in data_set if record['smoker'] == 'yes' and record['sex'] == 'male') / sum(1 for record in data_set if record['smoker'] == 'yes'and record['sex'] == 'male') if data_set else 0
avg_male_non_smoker_bmi = sum(float(record['bmi']) for record in data_set if record['smoker'] == 'no' and record['sex'] == 'male')/ sum(1 for record in data_set if record['smoker'] == 'no' and record['sex'] == 'female') if data_set else 0
#women statistics
total_charge_female= sum(float(record['charges'])for record in data_set if record['sex'] == 'female') #total amount paid for females
avg_charge_female = sum(float(record['charges'])for record in data_set if record['sex'] == 'female')/ sum(1 for record in data_set if record['sex'] == 'female') if data_set else 0
smoker_cost_female = sum(float(record['charges']) for record in data_set if record['smoker'] == 'yes' and record['sex'] == 'female') #amount paid by female smoker
avg_cost_female_smoker = sum(float(record['charges']) for record in data_set if record['smoker'] == 'yes' and record['sex'] == 'female')/ sum(1 for record in data_set if record['smoker'] == 'yes'and record['sex'] == 'female') if data_set else 0
non_smoker_female_cost =sum(float(record['charges'])for record in data_set if record['smoker'] == 'no' and record['sex'] == 'female') #amount paid by female non smoker
avg_cost_female_non_smoker = sum(float(record['charges'])for record in data_set if record['smoker'] == 'no' and record['sex'] == 'male') /sum( 1 for record in data_set if record['smoker'] == 'no'and record['sex'] == 'male') if data_set else 0
#bmi women
female_bmi = sum(float(record['bmi']) for record in data_set if record['sex'] == 'female')
avg_female_bmi = sum(float(record['bmi'])for record in data_set if record['sex'] == 'female')/ sum(1 for record in data_set if record['sex'] == 'female') if data_set else 0
female_smoker_bmi = sum(float(record['bmi']) for record in data_set if record['smoker'] == 'yes' and record['sex'] == 'female')
female_non_smoker_bmi = sum(float(record['bmi']) for record in data_set if record['smoker'] == 'no' and record['sex'] == 'female')
avg_female_smoker_bmi = sum(float(record['bmi']) for record in data_set if record['smoker'] == 'yes' and record['sex'] == 'female')/ sum(1 for record in data_set if record['smoker'] == 'yes' and record['sex']== 'female') if data_set else 0
avg_female_non_smoker_bmi = sum(float(record['bmi']) for record in data_set if record['smoker'] == 'no' and record['sex'] == 'female') / sum(1 for record in data_set if record['smoker'] == 'no' and record['sex']=='female') if data_set else 0
#cost comparison taking into account the bmi



# Create a figure and a set of subplots
fig, axs = plt.subplots(2, figsize=(8, 8))

# Plot BMI comparison
bmi_categories = ['Avg Male BMI', 'Avg Female BMI', 'Avg Male Smoker BMI', 'Avg Female Smoker BMI', 'Avg Male Non-Smoker BMI', 'Avg Female Non-Smoker BMI']
bmi_values = [avg_male_bmi, avg_female_bmi, avg_male_smoker_bmi, avg_female_smoker_bmi, avg_male_non_smoker_bmi, avg_female_non_smoker_bmi]
axs[0].bar(bmi_categories, bmi_values, color='turquoise')
axs[0].set_title('BMI Comparison')
axs[0].set_ylabel('Average BMI')
axs[0].set_yscale('log')  # Set a logarithmic scale
axs[0].set_xticklabels(bmi_categories, rotation=45, ha='right')

# Plot Cost comparison
cost_categories = ['Avg Smoker Cost', 'Avg Non-Smoker Cost', 'Avg Male cost', 'Avg Female cost', 'Avg Cost Male Smoker', 'Avg Cost Female']
cost_values = [avg_smoker_cost, avg_non_smoker_cost, avg_charge_male, avg_charge_female, avg_cost_male_smoker, avg_cost_female_smoker]
axs[1].bar(cost_categories, cost_values, color='green')
axs[1].set_title('Insurance Cost Comparison')
axs[1].set_ylabel('Average Insurance Cost')
axs[1].set_xticklabels(cost_categories, rotation=45, ha='right')

# Adjust layout to prevent overlap
plt.tight_layout()


# here we plot the distribution of age,sex, and region 
# Create a histogram for Age
plt.figure(figsize=(10, 4))
plt.hist(df['age'], bins=10, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
#plt.show()

# Create a bar chart for Sex
plt.figure(figsize=(10, 4))
df['sex'].value_counts().plot(kind='bar')
plt.title('Sex Distribution')
plt.xlabel('Sex')
plt.ylabel('Count')
#plt.show()

# Create a bar chart for Region
plt.figure(figsize=(10, 4))
df['region'].value_counts().plot(kind='bar')
plt.title('Region Distribution')
plt.xlabel('Region')
plt.ylabel('Count')
#plt.show()





#insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 2400 * smocker - 12500
#The function estimate_insurance_cost() estimates the medical insurance cost for an individual, based on four variables:
#age: age of the individual in years
#sex: 0 for female, 1 if male
#num_of_children: number of children the individual has
#smoker: 0 for a non-smoker, 1 for a smoker
#insurance cost for each record in the data set

#this function calculates the expected cost for each record in my dataset
def get_insurance_cost(data):
    costs = []
    for record in data:
        if record['sex'] == 'male':
            record['sex'] = 1
        else:
            record['sex'] = 0
        if record['smoker'] == 'yes':
            record['smoker'] = 1
        else:
            record['smoker'] = 0
        insurance_cost = 250 * float(record['age']) - 128 * float(record['sex']) + 370 * float(record['bmi']) + 425 * float(record['children']) + 2400 * float(record['smoker']) - 12500
        costs.append(insurance_cost)
    return costs

records_insurance_cost = get_insurance_cost(data_set)


#compare calculated male cost vs female cost
def get_insurance_cost_for_males(data): #expected insurance cost 
    costs = []
    for record in data:
        if record['sex'] == 'male': 
            record['sex'] = 1
        else:
            record['sex'] = 0

        if record['smoker'] == 'yes':  
            record['smoker'] = 1
        else:
            record['smoker'] = 0
            
        insurance_cost = 250 * float(record['age']) - 128 * float(record['sex']) + 370 * float(record['bmi']) + 425 * float(record['children']) + 2400 * float(record['smoker']) - 12500
        costs.append(insurance_cost)
    return costs

def get_insurance_cost_for_females(data): #expected insurance cost females
    costs = []
    for record in data:
        if record['sex'] == 'female':  
            record['sex'] = 0
        else:
            record['sex'] = 1

        if record['smoker'] == 'yes':  
            record['smoker'] = 1
        else:
            record['smoker'] = 0
            
        insurance_cost = 250 * float(record['age']) - 128 * float(record['sex']) + 370 * float(record['bmi']) + 425 * float(record['children']) + 2400 * float(record['smoker']) - 12500
        costs.append(insurance_cost)
    return costs

males_cost = get_insurance_cost_for_males(data_set) #expected insurance cost for males
females_cost = get_insurance_cost_for_females(data_set) # expected insurance cost for females


# Add the calculated costs to the DataFrame
df['Calculated_Costs'] = records_insurance_cost
#these are the calculated the cost 
mean_costs = df['Calculated_Costs'].mean()
std_costs = df['Calculated_Costs'].std()



# Calculate the mean and standard deviation of the actual charges and calculated costs
mean_charges = df['charges'].mean()
std_charges = df['charges'].std()




# Create a histogram of the actual cost they paid(charges)
#this where we plot the comparison between charges vs calculated cost 
plt.figure(figsize=(10, 6))
plt.hist(df['charges'], bins=10, alpha=0.5, label='Actual Charges')

# Create a histogram of the calculated costs
plt.hist(df['Calculated_Costs'], bins=10, alpha=0.5, label='Calculated Costs')

# Add lines for the mean and standard deviation
plt.axvline(mean_charges, color='blue', linestyle='dashed', linewidth=1, label='Mean of Actual Charges')
plt.axvline(mean_charges - std_charges, color='blue', linestyle='dotted', linewidth=1, label='Std Dev of Actual Charges')
plt.axvline(mean_charges + std_charges, color='blue', linestyle='dotted', linewidth=1)
plt.axvline(mean_costs, color='orange', linestyle='dashed', linewidth=1, label='Mean of Calculated Costs')
plt.axvline(mean_costs - std_costs, color='orange', linestyle='dotted', linewidth=1, label='Std Dev of Calculated Costs')
plt.axvline(mean_costs + std_costs, color='orange', linestyle='dotted', linewidth=1)

# Add labels and title
plt.xlabel('Cost')
plt.ylabel('Frequency')
plt.title('Actual Charges vs Calculated Costs')
# Add a legend
plt.legend()
#Show the plot
plt.show()








#compare actual charges betwen  sexes(male,female)
total_cost_male = sum(males_cost) # calculated at the beginning of the program(dataset)
total_cost_female = sum(females_cost)
# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(5, 5))

# Plot total charges for males vs females
axs[0, 0].bar(['Males', 'Females'], [total_charge_male, total_charge_female], color=['blue', 'purple'])
axs[0, 0].set_title('Actual amount paid : Males vs Females')
axs[0, 0].set_ylabel('Actual amount paid')

# Plot males cost vs females cost
axs[0, 1].bar(['Males', 'Females'], [total_cost_male, total_cost_female], color=['blue', 'purple'])
axs[0, 1].set_title('Expected Insurance Cost: Males vs Females in $')
axs[0, 1].set_ylabel('Expected Insurance Cost')

# Plot total charges males vs insurance cost males
axs[1, 0].bar(['Amount paid', 'Insurance Cost'], [total_charge_male, total_cost_male], color=['blue', 'green'])
axs[1, 0].set_title('Males: Actual amount paid vs Expected Insurance Cost in $')
axs[1, 0].set_ylabel('Amount')

# Plot total charge females vs insurance cost females
axs[1, 1].bar(['Amount paid', 'Insurance Cost'], [total_charge_females, total_cost_females], color=['purple', 'green'])
axs[1, 1].set_title('Females: Actual Amount Paid vs Expected Insurance Cost in $')
axs[1, 1].set_ylabel('Amount')

# Adjust layout
plt.tight_layout()
plt.show()



#smoker vs non smoker
# Create a bar chart
labels = ['Smoker', 'Non-Smoker', 'Smoker Male', 'Smoker Female', 'Non-Smoker Male', 'Non-Smoker Female']
costs = [smoker_cost, non_smoker_cost, smoker_cost_male, smoker_cost_female, non_smoker_male_cost, non_smoker_female_cost]
plt.bar(labels, costs, color=['red', 'green', 'blue', 'purple', 'blue', 'purple'])
plt.title('Insurance Cost Comparison')
plt.ylabel('Insurance Cost')
plt.xticks(rotation=45)

plt.show()

#comparing cost (smoker vs non smoker) (male,female) (bmi)
labels = ['Smoker', 'Non-Smoker', 'Female Smoker', 'Male Smoker', 'Female Non-Smoker', 'Male Non-Smoker']
bmis = [smoker_bmi, non_smoker_bmi, female_smoker_bmi, male_smoker_bmi, female_non_smoker_bmi, male_non_smoker_bmi]

plt.bar(labels, bmis, color=['red', 'green', 'purple', 'blue', 'purple', 'blue'])
plt.title('BMI Comparison')
plt.ylabel('BMI')
plt.xticks(rotation=45)

plt.show()

#comparing cost and bmi 
labels = ['Smoker', 'Non-Smoker', 'Smoker Male', 'Non-Smoker Male', 'Smoker Female', 'Non-Smoker Female']
costs = [smoker_cost, non_smoker_cost, smoker_cost_male, non_smoker_male_cost, smoker_cost_female, non_smoker_female_cost]
bmis = [smoker_bmi, non_smoker_bmi, male_smoker_bmi, male_non_smoker_bmi, female_smoker_bmi, female_non_smoker_bmi]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, axs = plt.subplots(2, 1, figsize=(6, 6))

# Plot costs
axs[0].bar(labels, costs, color=['red', 'green', 'blue', 'purple', 'blue', 'purple'])
axs[0].set_title('Insurance Cost Comparison')
axs[0].set_ylabel('Insurance Cost')

# Plot BMIs
axs[1].bar(labels, bmis, color=['red', 'green', 'blue', 'purple', 'blue', 'purple'])
axs[1].set_title('BMI Comparison')
axs[1].set_ylabel('BMI')

plt.tight_layout()
plt.show()




















