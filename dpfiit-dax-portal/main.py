# TODO
from fsdb import FileSystemDatabase
sex = ['', 'Male', 'Female']
age = ['','0 – 12','13 – 18','19 – 44','45 – 64','65 – above']
area = ['','AI','DS','GD','HP','ML','MD','SE','WD']

fs = FileSystemDatabase('dpf.user/population.pcsv')
fs.tabulate()

# li = fs.enlist()
# li.pop(0)

# buf = str()
# for row in li:
#     sex_i = row[4]
#     sex_e = sex_i.upper()

#     age_i = int(row[5])
#     age_e = enums.age[age_i][:7]

#     dom_i = int(row[11])
#     dom_e = enums.dom[dom_i]

#     buf += '{},{},{}\n'.format(sex_e, age_e, dom_e)
# print(buf)
