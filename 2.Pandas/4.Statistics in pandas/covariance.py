import pandas as pd

data={"col":[ x for x in range(100)]}

df=pd.DataFrame(data)

print(f" covariance is {df.cov()}")

