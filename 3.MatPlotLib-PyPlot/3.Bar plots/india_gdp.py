import pandas as pd
import matplotlib.pyplot as plt

file=pd.read_excel("D:/data science/3.Matplotlib/Pandas-matplotlin/India_gdp.xlsx")
colors = ["#FFA07A"] * 4 + ["#90EE90"] * 10 + ["#32CD32"] * 6 + ["#006400"] * 5
plt.bar(x=file["Year"],height=file["GDP"],color=colors)
plt.xlabel("YEARS")
plt.ylabel("GDP IN TRILLIONS")
plt.title("INDIA'S GDP PAST 25 YEARS")
plt.show()