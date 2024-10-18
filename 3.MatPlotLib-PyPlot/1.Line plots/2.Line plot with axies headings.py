import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[3,4,5,6,7]

plt.plot(x,y)

plt.xlabel("X axis label")
plt.ylabel("Y axis label")
plt.title("Simple Graph")
plt.savefig("simple line plot.png")