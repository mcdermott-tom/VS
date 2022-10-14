import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./rando/plotting/grain.csv", delimiter=',', index_col=0)

d = data

# Sorts by highest demand in Asia
AsiaDemand = d[d['Region'] == 'Asia' & d['Element'] == 'Total grain demand'].sort_values('Millions of metric tons', ascending=False)
# print(AsiaDemand.head())
AsiaDemand.head().plot()
plt.xlabel("YEEEEEEEEEEEEET")

plt.show()