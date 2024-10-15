import numpy as np

def mean_var_std(data: list[int]) -> None:
    ans = {
        "mean": [],
        "variance": [],
        'standard deviation': [],
        "max": [],
        "min": [],
        "sum": []
    }

    arr = np.array([data[0:3], data[3:6], data[6:9]])

    ans["mean"].append(arr.mean(axis=0).tolist())  # Mean across rows (column-wise)
    ans["mean"].append(arr.mean(axis=1).tolist())  # Mean across columns (row-wise)
    ans["mean"].append(arr.flatten().mean())       # Mean of entire array

    ans["variance"].append(arr.var(axis=0).tolist())  # Variance across rows
    ans["variance"].append(arr.var(axis=1).tolist())  # Variance across columns
    ans["variance"].append(arr.flatten().var())       # Variance of entire array

    ans["standard deviation"].append(arr.std(axis=0).tolist())  # Std dev across rows
    ans["standard deviation"].append(arr.std(axis=1).tolist())  # Std dev across columns
    ans["standard deviation"].append(arr.flatten().std())       # Std dev of entire array

    ans["max"].append(arr.max(axis=0).tolist())  # Max across rows
    ans["max"].append(arr.max(axis=1).tolist())  # Max across columns
    ans["max"].append(arr.flatten().max())       # Max of entire array

    ans["min"].append(arr.min(axis=0).tolist())  # Min across rows
    ans["min"].append(arr.min(axis=1).tolist())  # Min across columns
    ans["min"].append(arr.flatten().min())       # Min of entire array

    ans["sum"].append(arr.sum(axis=0).tolist())  # Sum across rows
    ans["sum"].append(arr.sum(axis=1).tolist())  # Sum across columns
    ans["sum"].append(arr.flatten().sum())       # Sum of entire array

    print(ans)

mean_var_std([0,1,2,3,4,5,6,7,8,9])