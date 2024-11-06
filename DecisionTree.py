from TreeNode import TreeNode


class DecisionTree:
    rootNode: TreeNode

    def __init__(self, comingData) -> None:
        usableFeatureIndices = [True] * 10

        usableFeatureIndices[0] = False

        self.rootNode = TreeNode(comingData, usableFeatureIndices)

    def fit(self):
        self.fit_start(self.rootNode)
        self.determine_leaf_classes(self.rootNode)

    def fit_start(currentNode: TreeNode):
        pass

    def determine_leaf_classes(currentNode: TreeNode):
        pass

    def find_best_split_point(self, comingData, featureIndex):
        bestSplitPoint = 1

        splittedCounts = self.simulateSplitCounts(
            comingData, featureIndex, bestSplitPoint)

        bestEntropy = self.calculate_entropy(splittedCounts)

        for i in range(2, 11):
            splittedCounts = self.simulateSplitCounts(
                comingData, featureIndex, bestSplitPoint)
            tempEntropy = self.calculate_entropy(splittedCounts)
            if tempEntropy < bestEntropy:
                bestEntropy = tempEntropy

    def calculate_entropy(self, splittedCounts):
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
