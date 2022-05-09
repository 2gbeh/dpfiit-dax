import numpy

data = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

result = numpy.percentile(data, 75)

print(data, result)
