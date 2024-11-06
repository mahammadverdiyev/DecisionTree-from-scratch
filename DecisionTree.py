from TreeNode import TreeNode
import math

from patient import Patient


class DecisionTree:
    rootNode: TreeNode

    def __init__(self, comingData) -> None:
        usableFeatureIndices = [True] * 10

        usableFeatureIndices[0] = False

        self.rootNode = TreeNode(comingData, usableFeatureIndices)

    def fit(self):
        self.fit_recursive(self.rootNode)
        self.determine_leaf_classes(self.rootNode)

    def fit_recursive(self, currentNode: TreeNode):
        best_feature_index = -1
        best_entropy = 2
        best_split_point = -1

        for i in range(10):

            if currentNode.usableFeatureIndices[i]:
                split_p, entropy = self.find_best_split_point(
                    currentNode.dataList, i)
                if entropy <= best_entropy:
                    best_feature_index = i
                    best_entropy = entropy
                    best_split_point = split_p

        if best_feature_index != -1:

            currentNode.usableFeatureIndices[best_feature_index] = False
            currentNode.splitPoint = best_split_point
            currentNode.patientDataIndex = best_feature_index

            currentNode.lows_node = TreeNode(
                [], currentNode.usableFeatureIndices)
            currentNode.highs_node = TreeNode(
                [], currentNode.usableFeatureIndices)

            lows, highs = self.splitData(
                currentNode.dataList, best_feature_index, best_split_point)

            currentNode.lows_node.dataList = lows
            currentNode.highs_node.dataList = highs

            self.fit_recursive(currentNode.lows_node)
            self.fit_recursive(currentNode.highs_node)

    def determine_leaf_classes(self, node: TreeNode):
        if node.lows_node is None and node.highs_node is None:

            malignents = 0
            benigns = 0

            for p in node.dataList:
                if p.checkUpResult():
                    malignents += 1
                else:
                    benigns += 1

            if malignents >= benigns:
                node.isMalignent = True
            else:
                node.isMalignent = False
        else:
            self.determine_leaf_classes(node.lows_node)
            self.determine_leaf_classes(node.highs_node)

    def test_patient(self, p: Patient):
        return self.patient_test_process(p, self.rootNode)

    def patient_test_process(self, p: Patient, node: TreeNode):
        if node.lows_node == None and node.highs_node == None:
            return node.isMalignent
        else:
            if p.patientData[node.patientDataIndex] <= node.splitPoint:
                return self.patient_test_process(p, node.lows_node)
            else:
                return self.patient_test_process(p, node.highs_node)

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

        return bestSplitPoint, bestEntropy

    def log2(self, x):
        if x == 0:
            return 0
        else:
            return math.log2(x)

    def calculate_entropy(self, splittedCounts):
        if splittedCounts is None:
            return float('inf')

        malignentLowsCount, benignLowsCount, malignentHighsCount, benignHighsCount = splittedCounts

        lows_sum = malignentLowsCount + benignLowsCount
        highs_sum = malignentHighsCount + benignHighsCount

        if lows_sum == 0 or highs_sum == 0:
            # Return a large value to indicate an invalid split
            return float('inf')

        lows_malignent_ratio = malignentLowsCount / lows_sum
        lows_benign_ratio = 1 - lows_malignent_ratio

        highs_malignent_ratio = malignentHighsCount / highs_sum
        highs_benign_ratio = 1 - highs_malignent_ratio

        lows_malignent_res = lows_benign_ratio >= highs_benign_ratio

        if lows_malignent_res:
            pa = lows_benign_ratio
            pb = highs_malignent_ratio
            entropy = -pa * self.log2(pa) - pb * self.log2(pb)
        else:
            pa = lows_malignent_ratio
            pb = highs_benign_ratio
            entropy = -pa * self.log2(pa) - pb * self.log2(pb)

        return entropy

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

        return lows, highs

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
