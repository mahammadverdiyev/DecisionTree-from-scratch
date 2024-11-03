from patient import Patient
from DecisionTree import DecisionTree

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

malignentPatientCount = sum(1 for p in data if p.checkUpResult() == True)
benignPatientCount = sum(1 for p in data if p.checkUpResult() == False)


print("malignentPatientCount: ", str(malignentPatientCount))
print("benignPatientCount: ", str(benignPatientCount))


# going to split the data into training and test sets where each
# half of it will contain an equal numbeer of cases: benign and malignent patients


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

# print(len(data))
# print(len(training_data), len(test_data))
tree = DecisionTree()

lows, highs = tree.splitData(data, 2, 4)

malignents_lows = sum(1 for p in lows if p.checkUpResult() == True)
malignents_highs = sum(1 for p in highs if p.checkUpResult() == True)

benign_lows = sum(1 for p in lows if p.checkUpResult() == False)
benign_highs = sum(1 for p in highs if p.checkUpResult() == False)


# for p in highs:
#     print(p.patientData[2])
