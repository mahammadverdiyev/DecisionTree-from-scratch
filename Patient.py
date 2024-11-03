class Patient:
    patientData = []
    dataSize = 10

    isMalignent = None

    def __init__(self, comingData) -> None:
        self.patientData = comingData.copy()

        if self.patientData[self.dataSize] == 4:
            self.isMalignent = True
        else:
            self.isMalignent = False

    def result(self):
        return self.isMalignent

    def __str__(self):
        return f"Patient Data: {' '.join(map(str,self.patientData))}, Malignant: {self.isMalignent}"
