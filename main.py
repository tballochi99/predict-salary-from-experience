import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_Data.csv")

x = df['YearsExperience']
y = df['Salary']

plt.title('Salary x YearsExperience')
plt.xlabel("YearsExperience")
plt.ylabel("Salary")

plt.scatter(x, y, alpha=0.5)
plt.show()





