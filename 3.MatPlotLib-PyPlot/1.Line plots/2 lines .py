import matplotlib.pyplot as plt

# Virat Kohli's cumulative runs across all formats (ODI, T20, Test) from 2010 to 2020
virat_runs = [1564, 2078, 2580, 2568, 2818, 2491, 2595, 2818, 2735, 2455, 842]  # Total runs per year

# Rohit Sharma's cumulative runs across all formats (ODI, T20, Test) from 2010 to 2020
rohit_runs = [1142, 1285, 1138, 1572, 1356, 1926, 2286, 2640, 2291, 2442, 1310]  # Total runs per year

# Years corresponding to the runs
years = list(range(2010, 2021))

# Calculate cumulative sum of runs for each year
virat_cumulative = [sum(virat_runs[:i+1]) for i in range(len(virat_runs))]
rohit_cumulative = [sum(rohit_runs[:i+1]) for i in range(len(rohit_runs))]

# Plotting the cumulative data
plt.plot(years, virat_cumulative, label="Virat Kohli (Cumulative Runs)")
plt.plot(years, rohit_cumulative, label="Rohit Sharma (Cumulative Runs)")

# Adding labels and title
plt.xlabel("Year")
plt.ylabel("Cumulative Runs")
plt.title("Virat Kohli vs Rohit Sharma Cumulative Runs (2010-2020)")

# Displaying the legend
plt.legend()

# Show the plot
plt.savefig("Virat vs Rohit.png")
