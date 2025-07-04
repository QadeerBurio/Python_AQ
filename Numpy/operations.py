# Statical operations
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

print(np.mean(arr))  # Mean
print(np.median(arr))  # Median
print(np.std(arr))  # Standard deviation
print(np.var(arr))  # Variance
print(np.min(arr))  # Minimum
print(np.max(arr))  # Maximum

# Reshaping and transpose

arr = np.arange(1, 13).reshape(3, 4)  # Reshape into 3x4
print(arr)

transposed = arr.T  # Transpose (flip rows & columns)
print(transposed)


# random number generations
np.random.seed(42)  # Reproducibility

rand_arr = np.random.rand(3, 3)  # Random values between 0 and 1
print(rand_arr)

rand_ints = np.random.randint(10, 50, size=(3, 3))  # Random integers
print(rand_ints)

normal_dist = np.random.randn(5)  # Standard normal distribution
print(normal_dist)


# handling missing data
arr = np.array([1, 2, np.nan, 4, 5])

# Remove NaN values
cleaned = arr[~np.isnan(arr)]
print(cleaned)

# Replace NaN with mean
mean_val = np.nanmean(arr)
arr[np.isnan(arr)] = mean_val
print(arr)
