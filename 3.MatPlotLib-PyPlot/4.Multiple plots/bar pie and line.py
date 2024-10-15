import matplotlib.pyplot as plt

fig,axs=plt.subplots(2,2)
fig1_name=["USA","CHINA","RUSSIA","INDIA"]
fig1_values=[916,296,109,83.6]
fig1_colors=["blue","Red","VIOLET","orange"]

axs[0][0].bar(x=fig1_name,height=fig1_values,color=fig1_colors)
axs[0][0].set_title("Top 4 Countries Expendeture on defence")
axs[0][0].set_xlabel("Countries")
axs[0][0].set_ylabel("Billions")
axs[0][0].set_facecolor("#0f9995")

axs[0][1].pie(x=fig1_values+[1430],labels=fig1_name+["Others"],colors=fig1_colors+["GREEN"])
axs[0][1].set_title("Top 4 v/s The rest")

india_names=["ARMY","AIR FORCE","NAVY"]
indian_colours=["DARKGREEN",'ORANGE',"BLUE"]
indian_values=[33.4,11.4,7.3]

axs[1][0].pie(x=indian_values,labels=india_names,colors=indian_colours)
axs[1][0].set_title("Indian expendeture on Defence")

costs=[47.40,50.91,51.30,56.64,64.56,66.26,71.47,72.94,76.35,81.36,83.6]
years=[x for x in range(2013,2024)]

axs[1][1].plot(years,costs,color="RED")
axs[1][1].set_title("Past 10 years india on defence")
axs[1][1].set_xlabel("year")
axs[1][1].set_ylabel("Billions")
axs[1][1].set_facecolor('skyblue')

plt.subplots_adjust(wspace=0.2, hspace=0.5)

plt.savefig("bar pie and line.jpg")