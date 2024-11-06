from typing import List


class TreeNode:
    patientDataIndex = None
    splitPoint = None

    dataList = []

    lows_node = None
    highs_node = None

    usableFeatureIndices = []
    isMalignent = None

    def __init__(self, data, incomingUsableFeatureIndices: List[bool]) -> None:
        self.dataList = data
        incomingUsableFeatureIndices
        self.usableFeatureIndices = incomingUsableFeatureIndices.copy()
        self.splitPoint = -1
        self.patientDataIndex = -1

        self.isMalignent = False
