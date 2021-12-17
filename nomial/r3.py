import random

histogram = [ 0] * 20

for i in range(1000):

  i = int(random.normalvariate( 5, 1) * 2)

histogram[i] = histogram[i] + 1

m = max(histogram)

for v in histogram:
  print( "#" * int(v * 50/m))