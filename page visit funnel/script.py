import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

visit_cart = visits.merge(cart,how='left')

is_nulla = len(visit_cart[visit_cart.cart_time.isnull()])
cart_length = len(visit_cart.cart_time)

empty_carta = (is_nulla/cart_length) * 100

cart_checkout = cart.merge(checkout,how='left')
cart_checkout_length = len(cart_checkout)
is_nullb = len(cart_checkout[cart_checkout.checkout_time.isnull()])
empty_cartb = (is_nullb/cart_checkout_length)*100
#funnel

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

#percentage of users proceeded to checkout, but did not purchase a t-shirt
checkout_notpurchase = len(all_data[(all_data['checkout_time'].notnull()) & (all_data['purchase_time'].isnull())])
length = len(all_data)
checkout_not_purchase = (checkout_notpurchase/length) * 100

checkout = len(all_data[all_data.checkout_time.isnull()])
purchase = len(all_data[all_data.purchase_time.isnull()])
cart = len(all_data[all_data.cart_time.isnull()])

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time


average_timetopurchase = all_data.time_to_purchase.mean()

print(average_timetopurchase)