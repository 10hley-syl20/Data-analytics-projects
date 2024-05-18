age =  28
sex= 0
bmi= 26.2
num_of_children= 3
smocker = 0

insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 2400 * smocker - 12500
print("This person's insurance cost is " +  str(insurance_cost) + " dollars.");
#variation in age
age += 4
new_insurance_cost_considering_age = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 2400 * smocker - 12500
print("This person's insurance cost is " +  str(new_insurance_cost_considering_age) + " dollars.");
change_in_insurance_cost_considering_age = new_insurance_cost_considering_age- insurance_cost;

print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost_considering_age) + " dollars")

#variation in the weight
age = 28
bmi += 3.1
new_insurance_cost_considering_bmi = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 2400 * smocker - 12500
change_in_insurance_cost_considering_bmi = new_insurance_cost_considering_bmi - insurance_cost;

print("The change in estimated insurance cost after increasing BMI by 3.2 is  " + str(change_in_insurance_cost_considering_bmi) + " dollars")

#variation in gender in medical insurance
bmi = 26.2
sex = 1
new_insurance_cost_considering_gender = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 2400 * smocker - 12500
change_in_insurance_cost_considering_gender = new_insurance_cost_considering_gender - insurance_cost;

print("The change in estimated cost for being male instead of female is  " + str(change_in_insurance_cost_considering_gender) + " dollars")


#business intelligence data analyst refactor using function
def calculate_insurance_cost( name, age, sex, bmi,  num_of_children, smocker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smocker - 12500;
    return 'The estimated insurance cost for ' + name + ' is ' + str(estimated_cost) + 'dollars.'


maria_insurance_cost = calculate_insurance_cost(name = 'Maria', age = 28, sex = 0, bmi = 26.2, num_of_children= 3, smocker= 0)
omar_insurance_cost = calculate_insurance_cost( name = 'Omar', age = 35, sex = 1, bmi = 22.2, num_of_children= 0, smocker= 1)
print(maria_insurance_cost)
print(omar_insurance_cost)

#the outprint of maria and omar cost contain strings, i have to redefine them or remvoe the strigns easy way is to redefine them
def calculate_insurance_cost_integer( name, age, sex, bmi,  num_of_children, smocker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smocker - 12500;
    return estimated_cost
maria_insurance_cost = calculate_insurance_cost_integer(name = 'Maria', age = 28, sex = 0, bmi = 26.2, num_of_children= 3, smocker= 0)
omar_insurance_cost = calculate_insurance_cost_integer( name = 'Omar', age = 35, sex = 1, bmi = 22.2, num_of_children= 0, smocker= 1)

def difference_in_cost_between_individual (cost1,cost2):
    result =  cost2 - cost1
    return 'The difference in insurance cost is ' + str(result) + 'dollars'

check_difference_in_cost = difference_in_cost_between_individual(maria_insurance_cost, omar_insurance_cost)
print(check_difference_in_cost)

def difference_in_cost_beteween_individual (cost1, cost2):
    return cost1- cost2


#calculation using function
def analyze_smoker(smocker_status):
    if smocker_status == 1:
        print('To lower your cost, you should consider quitting smoking.')
    else:
        print('Smoking is not an issue for you.')


def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker);
  return estimated_cost

 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)



names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost = 0
for cost in actual_insurance_costs:
   total_cost += cost
   print(total_cost)


def sum_list(list):
  result = 0
  for num in list:
     result += num
  return result
  
#print(total_cost)
average_cost  = sum_list(actual_insurance_costs)/len(actual_insurance_costs)
#using range in loops
for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print(f'The insurance cost for {name} is {insurance_cost} dollars.')
  
  if(insurance_cost) > average_cost:
    print(f'The insurance cost for {name} is above average')
  elif(insurance_cost) < average_cost:
      print(f'The insurance cost for {name} is below average.')
  else:
        print(f'The insurance cost for {name} is equal to the average')

  updated_estimated_costs = [ n * 11/10 for n in estimated_insurance_costs ]

print(updated_estimated_costs)



# Function to estimate insurance cost using list concepts
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
names = [ 'Maria', 'Rohan', 'Valentina']
insurance_cost = [ 4150.0, 5320.0, 35210.0]

insurance_data = list(zip(names,insurance_cost))
print('Here is the actual insurance cost data ' + str(insurance_data))
estimated_insurance_data = []
estimated_insurance_data.append(('Maria', maria_insurance_cost))
estimated_insurance_data.append(('Rohan', rohan_insurance_cost))
estimated_insurance_data.append(('valentina', valentina_insurance_cost))
print('Here is the estimated insurance cost data:'+ str(estimated_insurance_data))








































































































