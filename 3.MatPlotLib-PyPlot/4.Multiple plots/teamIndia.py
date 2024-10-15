import matplotlib.pyplot as plt
import pandas as pd

fig,axs=plt.subplots(2,4)
data=pd.read_excel("D:/data science/3.Matplotlib/multiple figures/teamIndia..xlsx")

test_data=data[data["format"]=="test"]
odi_data=data[data["format"]=="odi"]
t20_data=data[data["format"]=="t20"]
plt.suptitle("Team India performance against Australia")
axs[0][0].pie(x=[((test_data["result"] == "W") & (test_data["first"]=="bat")).sum(),
           ((test_data["result"]== "L") & (test_data["first"]=="bat")).sum(),
           ((test_data["result"] == "D") & (test_data["first"]=="bat")).sum()],
        labels=["win","lose","draw"],colors=["green","red","orange"],autopct='%1.1f%%')
axs[0][0].set_title("India in test bat first")

axs[1][0].pie(x=[((test_data["result"] == "W") & (test_data["first"]=="bowl")).sum(),
           ((test_data["result"]== "L") & (test_data["first"]=="bowl")).sum(),
           ((test_data["result"] == "D") & (test_data["first"]=="bowl")).sum()],
        labels=["win","lose","draw"],colors=["green","red","orange"],autopct='%1.1f%%')
axs[1][0].set_title("India in test bowl first")


axs[0][1].pie(x=[((odi_data["result"] == "W") & (odi_data["first"]=="bat")).sum(),
           ((odi_data["result"]== "L") & (odi_data["first"]=="bat")).sum(),
           ((odi_data["result"] == "D") & (odi_data["first"]=="bat")).sum()],
        labels=["win","lose","Tie"],colors=["green","red","orange"],autopct='%1.1f%%')
axs[0][1].set_title("India in ODI bat first")

axs[1][1].pie(x=[((odi_data["result"] == "W") & (odi_data["first"]=="bowl")).sum(),
           ((odi_data["result"]== "L") & (odi_data["first"]=="bowl")).sum(),
           ((odi_data["result"] == "D") & (odi_data["first"]=="bowl")).sum()],
        labels=["win","lose","Tie"],colors=["green","red","orange"],autopct='%1.1f%%')
axs[1][1].set_title("India in Odi bowl first")


axs[0][2].pie(x=[((t20_data["result"] == "W") & (t20_data["first"]=="bat")).sum(),
           ((t20_data["result"]== "L") & (t20_data["first"]=="bat")).sum(),
           ((t20_data["result"] == "T") & (t20_data["first"]=="bat")).sum(),
           ((t20_data["result"] == "NR") & (t20_data["first"]=="bat")).sum()],
        labels=["win","lose","Tie","n/r"],colors=["green","red","orange"],autopct='%1.1f%%')
axs[0][2].set_title("India in t20s bat first")

axs[1][2].pie(x=[((test_data["result"] == "W") & (test_data["first"]=="bowl")).sum(),
           ((test_data["result"]== "L") & (test_data["first"]=="bowl")).sum(),
           ((test_data["result"] == "D") & (test_data["first"]=="bowl")).sum(),
           ((t20_data["result"] == "NR") & (t20_data["first"]=="bat")).sum()],
        labels=["win","lose","Tie","n/r"],colors=["green","red","orange"],autopct='%1.1f%%')
axs[1][2].set_title("India in t20s bowl first")

axs[0][3].pie(x=[((data["result"] == "W") & (data["first"]=="bat")).sum(),
           ((data["result"]== "L") & (data["first"]=="bat")).sum(),
           ((data["result"] == "T") & (data["first"]=="bat")).sum(),
           ((data["result"] == "D") & (data["first"]=="bat")).sum(),

           ((data["result"] == "NR") & (data["first"]=="bat")).sum()],
        labels=["win","lose","Tie","Draw","n/r"],colors=["green","red","orange","blue","violet"],autopct='%1.1f%%')
axs[0][3].set_title("India in all formats bat first")

axs[1][3].pie(x=[((data["result"] == "W") & (data["first"]=="bowl")).sum(),
           ((data["result"]== "L") & (data["first"]=="bowl")).sum(),
           ((data["result"] == "T") & (data["first"]=="bowl")).sum(),
           ((data["result"]=="D") & (data["first"]=="bowl")).sum(),
           ((data["result"] == "NR") & (data["first"]=="bowl")).sum()],
        labels=["win","lose","Tie","Draw","n/r"],colors=["green","red","orange","blue","violet"],autopct='%1.1f%%')
axs[1][3].set_title("India in all formats t20s bowl first")

plt.savefig("team india performance.jpg")

