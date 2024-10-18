import numpy as np

import matplotlib.pyplot as plt

years=np.arange(2014,2024)

japan=np.array([41.6,42.1,43.6,44.3,45.7,50.8,51.4,50.9,56.1,58.1])

india=np.array([45.2,48,50.7,53.5,59.7,62.8,66,69.3,72.6,78.9])

plt.bar(x=[year-0.2 for year in years],height=japan,width=0.4,color="Red",label="Japan Milatary expenditure")
plt.bar(x=[i+0.2 for i in years],height=india,width=0.4,color="blue",label="India Milatary expenditure")


plt.legend()
plt.xlabel("year")
plt.ylabel("Expenditure in Billions")

plt.title("India v/s Japan yearly milatary Expenditure")
plt.savefig("india vs japan.png")