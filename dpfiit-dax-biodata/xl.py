# Import the required modules
import openpyxl

# Connect to the ms excel file
excel = openpyxl.load_workbook('bio.xlsx', data_only=True)

# Extract single cell
cell = excel['Sheet1']['A1']
data = cell.value
print(data)

# Extract multiple cells (vertical)
cells = excel['Sheet1']['D3:D7']
data = list()
for cell in cells:
    data.append(cell[0].value)
print(data)

# Extract multiple cells (horizontal)
cells = excel['Sheet1']['A3:D3']
data = list()
for cell in cells[0]:
    data.append(cell.value)
print(data)
