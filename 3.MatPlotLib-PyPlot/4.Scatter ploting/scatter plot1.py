import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,4,3]
y=[3,5,3,2,5,6,7,8,9]

plt.scatter(x,y)
plt.scatter([10,11,12],[4,5,3])
plt.scatter([10,11,12],[10,10,10])
plt.scatter([1,2,1],[0.5,0.9,0.7])
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Scatter Plotting")
plt.savefig("scatter plot1.png")