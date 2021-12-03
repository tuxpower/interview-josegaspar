#!/usr/bin/env python3

import csv

products_list = []
prices_dict = {}

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

with open('orders.csv') as orders:
  reader = csv.reader(orders, delimiter=',')
  next(orders)
  for row in reader:
    prices_dict.update({int(row[0]):calculate_prices(row[2].split())})

with open('order_prices.csv', 'w') as order_prices:
  writer = csv.writer(order_prices)
  writer.writerow(['id','euros'])
  writer.writerows(prices_dict.items())
