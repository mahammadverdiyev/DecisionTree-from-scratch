from TreeNode import TreeNode


class DecisionTree:
    rootNode = None

    usableFeatureIndices = []

    def __init__(self, comingData) -> None:
        self.rootNode = TreeNode(comingData)

        usableFeatureIndices = [True] * 10

        usableFeatureIndices[0] = False

    def process(self):
        pass

    def findBestSplitPoint(self, comingData, featureIndex):
        bestSplitPoint = 1

        splittedCounts = self.simulateSplitCounts(
            comingData, featureIndex, bestSplitPoint)

        bestEntropy = self.calculateEntropy(splittedCounts)

        for i in range(2, 11):
            splittedCounts = self.simulateSplitCounts(
                comingData, featureIndex, bestSplitPoint)
            tempEntropy = self.calculateEntropy(splittedCounts)
            if tempEntropy < bestEntropy:
                bestEntropy = tempEntropy

    def calculateEntropy(self, splittedCounts):
        malignentLowsCount, benignLowsCount, malignentHighsCount, benignHighsCount = splittedCounts

    def splitData(self, comingData, featureIndex, threshold):
        if featureIndex >= len(comingData) or featureIndex < 0:
            return None

        lows = []
        highs = []

        for patient in comingData:
            if patient.patientData[featureIndex] <= threshold:
                lows.append(patient)
            else:
                highs.append(patient)

        return [lows, highs]

    def countData(self, comingData, boolFilter):
        return sum(1 for p in comingData if p.checkUpResult() == boolFilter)

    def simulateSplitCounts(self, comingData, featureIndex, splitPoint):
        if featureIndex >= len(comingData) or featureIndex < 0:
            return None

        malignentLowsCount = 0
        benignLowsCount = 0
        malignentHighsCount = 0
        benignHighsCount = 0

        for patient in comingData:
            if patient.patientData[featureIndex] <= splitPoint:
                if patient.checkUpResult():
                    malignentLowsCount += 1
                else:
                    benignLowsCount += 1
            else:
                if patient.checkUpResult():
                    malignentHighsCount += 1
                else:
                    benignHighsCount += 1

        return malignentLowsCount, benignLowsCount, malignentHighsCount, benignHighsCount
