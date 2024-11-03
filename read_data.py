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
    if p.checkUpResult():
        malignentPatientCount += 1
    else:
        benignPatientCount += 1


print("malignentPatientCount: ", str(malignentPatientCount))
print("benignPatientCount: ", str(benignPatientCount))


# going to split the data into training and test sets where each
# half of will contain an equal numbeer of cases: benign and malignent patients


# but first we have to sort the data based on the their medical examination result

data.sort(key=lambda x: x.checkUpResult())

# sorted the data in a way that benign patients come first
# print(*data, sep='\n')

training_data = []
test_data = []


halfMalignentCount = malignentPatientCount // 2
halfBenignCount = benignPatientCount // 2

print("halfMalignentCount: ", str(halfMalignentCount))
print("halfBenignCount: ", str(halfBenignCount))


benign_patients = data[:benignPatientCount]
malignant_patients = data[benignPatientCount:]

training_data = benign_patients[:halfBenignCount] + \
    malignant_patients[:halfMalignentCount]
test_data = benign_patients[halfBenignCount:] + \
    malignant_patients[halfMalignentCount:]

print(len(data))
print(len(training_data), len(test_data))
