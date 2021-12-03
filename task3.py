#!/usr/bin/env python3

import csv
import pandas as pd

products_list = []
total_euros_list = []
customers_list = []
orders_list = []
firstname_list = []
lastname_list = []

def get_firstname(id):
  return customers_firstname.get(id)

def get_lastname(id):
  return customers_lastname.get(id)

def calculate_prices(products):
  my_list = []
  for p in products:
    my_list.append(float(products_dict.get(int(p))))
  return sum(tuple(my_list))

with open('products.csv') as products:
  reader = csv.reader(products, delimiter=',')
  next(products)
  for row in reader:
    products_list.append(row[2])

products_dict = {i: x for i,x in enumerate(products_list)}

with open('customers.csv') as customers:
  reader = csv.reader(customers, delimiter=',')
  next(customers)
  for row in reader:
    firstname_list.append(row[1])
    lastname_list.append(row[2])

customers_firstname = {i: x for i,x in enumerate(firstname_list)}
customers_lastname = {i: x for i,x in enumerate(lastname_list)}

with open('orders.csv') as orders:
  my_dict = {}
  fname_list = []
  lname_list = []
  reader = csv.reader(orders, delimiter=',')
  next(orders)
  for row in reader:
    customers_list.append(row[1])
    fname_list.append(get_firstname(int(row[1])))
    lname_list.append(get_lastname(int(row[1])))
    total_euros_list.append(calculate_prices(row[2].split()))
    my_dict.update({'id':customers_list,'firstname':fname_list,'lastname':lname_list,'total_euros':total_euros_list})
  df = pd.DataFrame(my_dict)
  df_customers = df.groupby(['id','firstname','lastname']).sum()

with open('customer_ranking.csv', 'w') as customer_ranking:
  customer_ranking.write(df_customers.sort_values(by='total_euros',ascending=False).to_csv())
