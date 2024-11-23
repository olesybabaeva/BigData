import sys

for line in sys.stdin:
    data = line.strip().split(',')
    if len(data) == 16:
        price = data[9]
        print("{0}t{1}".format("price", price))
