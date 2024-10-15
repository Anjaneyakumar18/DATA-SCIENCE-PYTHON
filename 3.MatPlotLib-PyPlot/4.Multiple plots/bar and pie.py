import matplotlib.pyplot as plt

bar_vals=[1,3,6,7]
fig,axs=plt.subplots(1,2)
axs[0].pie(x=bar_vals,labels=["one","two","three","four"])
axs[1].bar(x=["one","two","three","four"],height=bar_vals)

plt.savefig("bar and plot.jpg")