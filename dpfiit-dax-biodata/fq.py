# Import the required modules
import numpy
import matplotlib.pyplot as matplotlib

# Extract the dataset
data = ['M', 'F', 'M', 'F', 'M', 'F', 'M']

# Sort intervals in the dataset (bins)
distinct = set(data)
bins = list(distinct)
bins.sort()
x_axis = numpy.array(bins)

# Count intervals in the dataset (frequency)
freq = list()
for e in bins:
    n = data.count(e)
    freq.append(n)
y_axis = numpy.array(freq)

# Plot the chart
matplotlib.bar(x_axis, y_axis)
matplotlib.title('FREQUENCY DISTRIBUTION CHART')
matplotlib.xlabel('INTERVALS')
matplotlib.ylabel('FREQUENCY (f)')
matplotlib.grid(axis='y', linestyle='dotted', color='grey')
matplotlib.show()
