import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Load the data from Excel
data = pd.read_excel("D:/data science/3.Matplotlib/scatter plot/bumrah bowling stacts.xlsx")

# Create subplots
fig, axs = plt.subplots(1, 2)

# Scatter plot for different results
axs[0].scatter(x=data[data["result"] == "B"]["speed"],
               y=data[data["result"] == "B"]["swing"],
               color="green", label="Boundary")

axs[0].scatter(x=data[data["result"] == "R"]["speed"],
               y=data[data["result"] == "R"]["swing"],
               color="orange", label="Runs")

axs[0].scatter(x=data[data["result"] == "D"]["speed"],
               y=data[data["result"] == "D"]["swing"],
               color="gray", label="Dot")

axs[0].scatter(x=data[data["result"] == "W"]["speed"],
               y=data[data["result"] == "W"]["swing"],
               color="red", label="Wicket")

# Calculating wickets for pie chart
speed_less_equal_135_wickets = len(data[(data["speed"] <= 135) & (data["result"] == "W")])
speed_greater_135_wickets = len(data[(data["speed"] > 135) & (data["result"] == "W")])

# Plot the pie chart
axs[1].pie(x=[speed_less_equal_135_wickets, speed_greater_135_wickets],
           labels=["Speed <= 135 & Wicket", "Speed > 135 & Wicket"],
           autopct='%1.3f%%', startangle=90)

# Set labels and title for the scatter plot
axs[0].set_xlabel("Speed in KMPH")
axs[0].set_ylabel("Swing in degrees")
axs[0].set_title("Bumrah Bowling analysis")
axs[0].legend()

# Set title for the pie chart
axs[1].set_title("Bumrah wickets speed v/s wickets")

# Adjust spacing between subplots
plt.subplots_adjust(hspace=0.3, wspace=0.3)

# Set a strong border for both subplots
for ax in axs:
    ax.spines['top'].set_edgecolor('black')
    ax.spines['bottom'].set_edgecolor('black')
    ax.spines['left'].set_edgecolor('black')
    ax.spines['right'].set_edgecolor('black')
    ax.spines['top'].set_linewidth(2.5)
    ax.spines['bottom'].set_linewidth(2.5)
    ax.spines['left'].set_linewidth(2.5)
    ax.spines['right'].set_linewidth(2.5)

# Set a strong border around the pie chart axes
rect = Rectangle((0, 0), 1, 1, transform=axs[1].transAxes,  # Coordinates relative to axes
                 fill=False, color='black', linewidth=2.5)
axs[1].add_patch(rect)

# Show the plot
plt.show()
