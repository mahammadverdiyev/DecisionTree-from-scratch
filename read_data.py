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


for p in data:
    print(p)
