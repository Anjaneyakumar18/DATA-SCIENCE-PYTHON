import matplotlib.pyplot as plt
import numpy as np
years=np.arange(2013,2024)

india_wins=np.array([4,5,5,9,7,8,7,3,8,4,6])

pak_wins=np.array([4,2,4,5,4,4,3,2,7,4,5])

plt.plot(years,india_wins,color="blue",label="India test wins")
plt.plot(years,pak_wins,color="Red",label="Pak Test wins")
plt.xlabel("year")
plt.ylabel("Wins")
plt.title("Ind v/s Pak test match wins from 2013-2023")
plt.legend()
plt.savefig("ind vs pak.png")