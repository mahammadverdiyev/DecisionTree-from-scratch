from patient import Patient


data = []

with open('breast-cancer-wisconsin.data.txt', 'r') as file:
    l = []
    for line in file:
        line = line.strip()
        line = line.split(',')
        if '?' in line:
            continue
        curr_data = list(map(int, line))
        data.append(Patient(curr_data))


# for p in data:
#     print(p)

malignentPatientCount = 0
benignPatientCount = 0

for p in data:
    if p.isMalignent():
        malignentPatientCount += 1
    else:
        benignPatientCount += 1
