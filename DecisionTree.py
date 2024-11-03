class DecisionTree:

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
