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


# print("malignentPatientCount: ", str(malignentPatientCount))
# print("benignPatientCount: ", str(benignPatientCount))


# I'm going to split the data into training and test sets where each
# half of it will contain an equal numbeer of cases: benign and malignent patients


# but first we have to sort the data based on the their medical examination result

data.sort(key=lambda x: x.checkUpResult())

# sorted the data in a way that benign patients come first
# print(*data, sep='\n')

training_data = []
test_data = []


halfMalignentCount = malignentPatientCount // 2
halfBenignCount = benignPatientCount // 2

# print("halfMalignentCount: ", str(halfMalignentCount))
# print("halfBenignCount: ", str(halfBenignCount))


benign_patients = data[:benignPatientCount]
malignant_patients = data[benignPatientCount:]

training_data = benign_patients[:halfBenignCount] + \
    malignant_patients[:halfMalignentCount]
test_data = benign_patients[halfBenignCount:] + \
    malignant_patients[halfMalignentCount:]

# print(len(data))
# print(len(training_data), len(test_data))
# tree = DecisionTree()

# lows, highs = tree.splitData(data, 2, 4)

# malignent_lows = tree.countData(lows, True)
# malignents_highs = tree.countData(highs, True)

# benign_lows = tree.countData(lows, False)
# benign_highs = tree.countData(highs, False)

# for p in highs:
#     print(p.patientData[2])


tree = DecisionTree(training_data)
tree.fit()

correct_guess = 0
wrong_guess = 0

for p in training_data:
    p_guess = tree.test_patient(p)
    if p_guess == p.isMalignent:
        correct_guess += 1
    else:
        wrong_guess += 1

print("Number of correct guesses on training data: " + str(correct_guess) +
      " and number of wrong guesses on training data: " + str(wrong_guess))
print("Training data accuracy: " +
      str(correct_guess / (correct_guess + wrong_guess)))

correct_guess = 0
wrong_guess = 0

for p in test_data:
    p_guess = tree.test_patient(p)
    if p_guess == p.isMalignent:
        correct_guess += 1
    else:
        wrong_guess += 1

print("Number of correct guesses on test data: " + str(correct_guess) +
      " and number of wrong guesses on test data: " + str(wrong_guess))
print("Test data accuracy: " +
      str(correct_guess / (correct_guess + wrong_guess)))
