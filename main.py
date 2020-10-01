from reynolds import Reynolds
import pandas

# load data set
df = pandas.read_excel('D:\\....xlsx')
print(df.head())

# set column
gender = df.iloc[:, 0]
age = df.iloc[:, 0]
diabetes = df.iloc[:, 0]
smoker = df.iloc[:, 0]
bloodPersore = df.iloc[:, 0]
totalCholesterol = df.iloc[:, 0]
familyHistory = df.iloc[:, 0]
Hdl = df.iloc[:, 0]
HSCRP = df.iloc[:, 0]

# call function
reynolds = Reynolds()
risk = reynolds.ReynoldsRisk(gender, age, diabetes, smoker, bloodPersore, totalCholesterol, familyHistory, Hdl, HSCRP)
print(risk)