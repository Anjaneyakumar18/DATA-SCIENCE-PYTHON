import pandas as pd

data={
    "Team":["REDS","GREENS","BLUES","REDS","GREENS","BLUES","REDS","GREENS","BLUES"],
    "POINTS":[9,5,7,9,5,7,8,7,8]
}
lab=[chr(x) for x in range(65,74)]
df=pd.DataFrame(data,index=lab)
grouped=df.groupby("Team").mean("POINTS")
print(grouped)

# we have caluculated the average points of each team

# heighest avg points team

print(grouped["POINTS"].idxmax())

# heighest average team

print(grouped["POINTS"].max())

# min

print(grouped["POINTS"].idxmin(),grouped["POINTS"].min())