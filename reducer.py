import sys
import numpy as np

total_count = 0
total_price = 0
total_price_squared = 0

for line in sys.stdin:
    key, value = line.strip().split('t')
    if key == "price":
        price = float(value)
        total_count += 1
        total_price += price
        total_price_squared += price ** 2
mean_price = total_price / total_count
variance_price = (total_price_squared / total_count) - (mean_price ** 2)

print("Mean price: {:.2f}".format(mean_price))
print("Variance of price: {:.2f}".format(variance_price))
