import numpy

data = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

q1 = numpy.percentile(data, 25)

q3 = numpy.percentile(data, 75)

iqr = q3 - q1

print(data, q1, q3, iqr)
