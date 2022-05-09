import statistics

data = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

result = statistics.mean(data)

result_f = round(result, 1)

print(data, result, result_f)
