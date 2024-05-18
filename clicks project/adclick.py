import numpy as np
import pandas as pd
df= pd.read_csv('addclick.csv')

#How many views (i.e., rows of the table) came from each utm_source?
views_per_utmsource = df.groupby('utm_source').user_id.count().reset_index()

#If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.
df['is_click'] = df['ad_click_timestamp'].isnull()

#We want to know the percent of people who clicked on ads from each utm_source.
clicks_by_source = df.groupby(['utm_source','is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(
    columns='is_click',
    index='utm_source',
    values='user_id').reset_index()

#clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source
clicks_pivot['percent_clicked'] = (clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]))

#Were approximately the same number of people shown both ads? group by add
add_num = df.groupby('experimental_group').user_id.count().reset_index() #the same amount of peole saw both adds
#this pivot table gives how many people click add a and add b
clicks_peradd = df.groupby(['is_click','experimental_group']).user_id.count().reset_index()
add_pivot = clicks_peradd.pivot(
    columns='experimental_group',
    index='is_click',
    values='user_id').reset_index()


#create a data frame for clicks of A add and b add
a_clicks = df[df.experimental_group == 'A']
b_clicks = df[df.experimental_group == 'B']
#calculates the amount of click per day
aclicks_perday = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()
bclicks_perday = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()


aclicks_pivot = aclicks_perday.pivot(
    columns='is_click',
    index='day',
    values='user_id').reset_index()

aclicks_pivot['percent_clicked_of_A'] = (aclicks_pivot[True] / (aclicks_pivot[True] + aclicks_pivot[False]))

bclicks_pivot = bclicks_perday.pivot(
    columns='is_click',
    index='day',
    values='user_id').reset_index()
bclicks_pivot['percent_clicked_of_B'] = (bclicks_pivot[True] / (bclicks_pivot[True] + bclicks_pivot[False]))






