#names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages: this function removes the M and the Bs from the list floating this value to billions and millions
def floating(list):
    updated_list = []
    for item in list:
        if 'M' in item:
            updated_list.append(int(float(item.replace('M', '')) * 1e6))
        elif 'B' in item:
            updated_list.append(int(float(item.replace('B', '')) * 1e9))
        else:
            updated_list.append(item)
    return updated_list

# 2 
def dictionary_maker_based_on_names(names, months, years, max_sustained_winds, areas_affected,damages, deaths):
    
    hurricane_dictionaries=[{'Name':names, 'Month':months, 'Year': years, 'Max Sustained wind': max_sustained_winds, 'Areas Affected': areas_affected, 'Damages': damages, 'Deaths':deaths} for names, months, years, max_sustained_winds, areas_affected,damages,deaths in zip(names, months, years, max_sustained_winds, areas_affected,damages,deaths)]
    hurricanes = { hurricane['Name']: {'Month': hurricane['Month'], '': hurricane['Year'], 'Max Sustained wind': hurricane['Max Sustained wind'], 'Areas affected': hurricane['Areas Affected'], 'Damages': hurricane['Damages'], 'Deaths': hurricane['Deaths']} for hurricane in hurricane_dictionaries}
    return hurricanes
   
# Create and new the hurricanes dictionary
hurricane_names = dictionary_maker_based_on_names(names, months, years, max_sustained_winds, areas_affected, damages,deaths)

# 3
# Organizing by Year
def dictionary_maker_based_on_year(names, months, years, max_sustained_winds, areas_affected,damages, deaths):
    floating(damages)
    hurricane_dictionaries=[{'Name':names, 'Month':months, 'Year': years, 'Max Sustained wind': max_sustained_winds, 'Areas Affected': areas_affected, 'Damages': damages, 'Deaths':deaths} for names, months, years, max_sustained_winds, areas_affected,damages,deaths in zip(names, months, years, max_sustained_winds, areas_affected,damages,deaths)]
    hurricanes = { hurricane['Year']: { 'Name': hurricane['Name'],'Month': hurricane['Month'], 'Year': hurricane['Year'], 'Max Sustained wind': hurricane['Max Sustained wind'], 'Areas affected': hurricane['Areas Affected'], 'Damages': hurricane['Damages'], 'Deaths': hurricane['Deaths']} for hurricane in hurricane_dictionaries}
    return hurricanes
# create a new dictionary of hurricanes with year and key


# 4
# function that counts how often each area is listed as an affected area of a hurricane

def count_affected_areas(hurricanes):
  area_counts = {}
  for hurricane in hurricanes.values():
    for area in hurricane['Areas affected']:
      if area not in area_counts:
        area_counts[area] = 1
      else:
        area_counts[area] += 1
  return area_counts

print(count_affected_areas(hurricane_names))

#this function return an obj where the names of the hurricanes are the key
def dictionary_maker(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  final_dict = {}
  for i in range(len(names)):
    final_dict[names[i]] = {
      'Name': names[i],
      'Month': months[i],
      'Year': years[i],
      'Max Sustained Wind': max_sustained_winds[i],
      'Area Affected': areas_affected[i],
      'Damage': damages[i],
      'Death': deaths[i],
    }
  return final_dict

hurricane_dictionary = dictionary_maker(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(hurricane_dictionary)

#function that count how often each of the areas of the atlantic are affected using the area affected list
def count_area_affected(areas_affected):
  area_counts = {}
  for affected_area in areas_affected:
    for area in affected_area:
      if area not in area_counts:
        area_counts[area] = 1
      else:
          area_counts[area] += 1
  return area_counts  


  #function that counts how often each of the areas of the atlantic are affected using the hurricane dic
def count_affected_areas(hurricanes):
  area_counts = {}
  for hurricane in hurricanes.values():
    for area in hurricane['Area Affected']:
      if area not in area_counts:
        area_counts[area] = 1
      else:
         area_counts[area] += 1
  return area_counts
count_area_affected = count_affected_areas(hurricane_dictionary)


#area affected by the most hurricanes how often it was hit  
def most_affected_area(affected_areas_count):
    max_area = None
    max_area_count = 0
    for area, count in affected_areas_count.items():
        if count > max_area_count:
            max_area = area
            max_area_count = count

    return f'the most affected area was {max_area} and it was hit, {max_area_count} times'

#function that finds the hurricane that caused the highest number of deaths and how many deaths it caused
def count_death_by_hurricane(hurricanes):
    death_counts = {}
    for name, hurricane in hurricanes.items():
        num = hurricane['Death']  
        death_counts[name] = num
    return death_counts

death_num  = count_death_by_hurricane(hurricane_dictionary)
def deadliest_hurricane(death_num):
    max_hurricane = None
    max_death_count = 0
    for hurricane, death_count in death_num.items():
        if death_count > max_death_count:
          max_hurricane = hurricane
          max_death_count = death_count
    return f'The deadliest hurricane is {max_hurricane} and it caused {max_death_count} deaths'

    
#a better way to do the same directly on the hurricane object
def max_death (hurricane_dictionary):
  max_hurricane = None
  max_death_count = 0
  for name, hurricane_info in hurricane_dictionary.items():
    death_count = hurricane_info['Death']
    if death_count > max_death_count:
      max_hurricane =  name
      max_death_count = death_count
    return f'The deadliest hurricane is {max_hurricane} and it caused {max_death_count} deaths'
print(max_death(hurricane_dictionary))

#function that rates hurricanes based on windspeed
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def mortality_rating(hurricanes):
    mortality_scale = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for name, hurricane in hurricanes.items():
        deaths = hurricane['Death']
        if deaths > 10000:
            mortality_scale[5].append(hurricane)
        elif deaths > 1000:
            mortality_scale[4].append(hurricane)
        elif deaths > 500:
            mortality_scale[3].append(hurricane)
        elif deaths > 100:
            mortality_scale[2].append(hurricane)
        elif deaths > 0:
            mortality_scale[1].append(hurricane)
        else:
            mortality_scale[0].append(hurricane)
    return mortality_scale































