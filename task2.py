#!/usr/bin/env python3

import csv

products_list = [0,1,2,3,4,5]
prod0_list = []
prod1_list = []
prod2_list = []
prod3_list = []
prod4_list = []
prod5_list = []
customers_dict = {}

def update_prod_dict(i, x):
  if i == 0:
    prod0_list.append(x)
  elif i == 1:
    prod1_list.append(x)
  elif i == 2:
    prod2_list.append(x)
  elif i == 3:
    prod3_list.append(x)
  elif i == 4:
    prod4_list.append(x)
  elif i == 5:
    prod5_list.append(x)

def update_customers_dict(product):
  if product == 0:
    customers_dict.update({product:' '.join(prod0_list)})
  elif product == 1:
    customers_dict.update({product:' '.join(prod1_list)})
  elif product == 2:
    customers_dict.update({product:' '.join(prod2_list)})
  elif product == 3:
    customers_dict.update({product:' '.join(prod3_list)})
  elif product == 4:
    customers_dict.update({product:' '.join(prod4_list)})
  elif product == 5:
    customers_dict.update({product:' '.join(prod5_list)})

for product in products_list:
  with open('orders.csv') as orders:
    reader = csv.reader(orders, delimiter=',')
    next(orders)
    for row in reader:
      my_list = list(dict.fromkeys(row[2].split()))
      if str(product) in my_list:
          update_prod_dict(product, row[1])
  update_customers_dict(product)

with open('product_customers.csv', 'w') as product_customers:
  writer = csv.writer(product_customers)
  writer.writerow(['id','customers_ids'])
  writer.writerows(customers_dict.items())
