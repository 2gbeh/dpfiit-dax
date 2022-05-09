import statistics
import numpy

data = [20, 25, 64, 10, 72, 41, 7, 34, 18, 29, 2, 69, 65]

data = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

print(len(data))

print(sum(data))

print(statistics.mean(data))

print(statistics.median(data))

print(statistics.mode(data))

print(min(data))

print(max(data))

print(max(data) - min(data))

print(statistics.stdev(data))

print(statistics.variance(data))

print(numpy.percentile(data, 25))

print(numpy.percentile(data, 75))

print(numpy.percentile(data, 75) - numpy.percentile(data, 25))

input()
