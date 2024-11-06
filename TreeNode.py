from typing import List


class TreeNode:
    patientDataIndex = None
    splitPoint = None

    dataList = []

    lows = []
    highs = []

    usableFeatureIndices = []
    isMalignent = None

    def __init__(self, data, incomingUsableFeatureIndices: List[bool]) -> None:
        self.dataList = data
        incomingUsableFeatureIndices
        self.usableFeatureIndices = incomingUsableFeatureIndices.copy()
        self.splitPoint = -1
        self.patientDataIndex = -1

        self.isMalignent = False
