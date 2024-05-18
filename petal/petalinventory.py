
import pandas as pd
import numpy as np

inventory = pd.read_csv('petalpowerinventory.csv')
staten_island = inventory[:10] 
product_request = staten_island[staten_island['location'] == 'Staten Island']
seed_request = inventory[(inventory.location == 'Staten Island')& (inventory.product_type =='seeds')]

inventory['in_stock'] = inventory.quantity.apply(lambda n: True if n > 0 else 0)

inventory['total_value'] = inventory.price * inventory.quantity

combine_lambda = lambda row:f'{row.product_type} - {row.product_description}'

inventory['full_description'] = inventory.apply(combine_lambda,axis = 1)

