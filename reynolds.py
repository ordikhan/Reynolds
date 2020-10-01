import numpy as np


class Reynolds:
    def __init__(self, gender, age, diabetes, smoker, bloodPersore, totalCholesterol, familyHistory, Hdl, HSCRP):
        self.gender = gender
        self.age = age
        self.diabetes = diabetes
        self.smoker = smoker
        self.bloodPersore = bloodPersore
        self.totalCholesterol = totalCholesterol
        self.Hdl = Hdl
        self.familyHistory = familyHistory
        # HighSensitivitycreactiveprotein
        self.HSCRP = HSCRP

    def ReynoldsRisk(self):
        RiskScore = [self.age * 0.0799, (np.log(self.bloodPersore)) * 3.137, (np.log(self.HSCRP)) * 0.180,
                     (np.log(self.totalCholesterol)) * 1.382, (np.log(self.Hdl)) * (-1.172)]
        if self.diabetes == 1:
            RiskScore.append(10 * 0.134)
        if self.smoker == 1:
            RiskScore.append(0.818)
        if self.familyHistory == 1:
            RiskScore.append(0.438)

        Score = (1 - 0.98634 * np.exp(float(RiskScore[0]) - 22.325)) * 100
        return Score
