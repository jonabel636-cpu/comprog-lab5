import numpy as np
import pandas as pd

# ===============================
# GLOBAL STUDENT INFO (FIXED)
# ===============================
STUDENT_NAME = "Jonabel Jocson"
STUDENT_ID = 1268

print("\n==============================")
print("Student:", STUDENT_NAME)
print("ID:", STUDENT_ID)
print("==============================\n")

# ===============================
# NUMPY BASICS
# ===============================

years_exp = np.array([1, 3, 5, 7, 10])
print("Years of Experience:", years_exp)

salaries = np.array([[50, 60, 70], [80, 90, 100]])
print("Salary Matrix:\n", salaries)

zeros_array = np.zeros((2, 2))
ones_array = np.ones((2, 3))

print("Zeros Array:\n", zeros_array)
print("Ones Array:\n", ones_array)

# ===============================
# ARRAY OPERATIONS
# ===============================

exp_plus_5 = years_exp + 5
exp_times_2 = years_exp * 2

print("\nYears + 5:", exp_plus_5)
print("Years * 2:", exp_times_2)

sample1 = np.array([1, 2, 3])
sample2 = np.array([4, 5, 6])
print("Dot Product:", np.dot(sample1, sample2))

# ===============================
# MATHEMATICAL FUNCTIONS
# ===============================

print("\nYears - 2:", years_exp - 2)
print("Years in Decades:", years_exp / 10)

print("\nExponential:", np.exp(sample1))
print("Log:", np.log(years_exp))

# ===============================
# INDEXING & SLICING
# ===============================

print("\nFirst year:", years_exp[0])
print("First two salaries:", salaries[0, :2])
print("Second column:", salaries[:, 1])
print("Last year:", years_exp[-1])

# ===============================
# REVERSING & SLICING
# ===============================

print("\nReversed Years:", years_exp[::-1])
print("Reversed Salaries:\n", salaries[::-1])

print("Subgroup:\n", salaries[1:3] if salaries.shape[0] > 2 else salaries)
print("First rows:\n", salaries[:2])

# ===============================
# RESHAPE & TRANSPOSE
# ===============================

reshaped = np.arange(1, 7).reshape(2, 3)
print("\nReshaped:\n", reshaped)

print("Flattened:", reshaped.flatten())
print("Transpose:\n", reshaped.T)

data = np.arange(1, 13)

print("\n3x4 Matrix:\n", data.reshape(3, 4))
print("6x2 Matrix:\n", data.reshape(6, -1))
print("3D Tensor:\n", data.reshape(2, 3, 2))
print("Transposed 4x3:\n", data.reshape(3, 4).T)

# ===============================
# BROADCASTING
# ===============================

bonus = np.array([5, 10, 15])
print("\nSalaries with bonus:\n", salaries + bonus)

scaled = salaries * 1.1
dept_growth = np.array([1.05, 1.10, 1.20])

print("\nScaled salaries:\n", scaled)
print("Dept scaling:\n", salaries * dept_growth)

# ===============================
# STATISTICS
# ===============================

print("\nMean:", np.mean(years_exp))
print("Std:", np.std(years_exp))
print("Max:", np.max(salaries))
print("Min:", np.min(salaries))
print("Sum:", np.sum(salaries))

print("\nMedian:", np.median(years_exp))
print("25th percentile:", np.percentile(years_exp, 25))
print("75th percentile:", np.percentile(years_exp, 75))

# ===============================
# TRIGONOMETRY
# ===============================

angles = np.array([0, np.pi/4, np.pi/2])
print("\nSine:", np.sin(angles))
print("Cosine:", np.cos(angles))

print("Row sums:", np.apply_along_axis(np.sum, 1, salaries))

# ===============================
# DATA TRANSFORMATIONS
# ===============================

print("\nSqrt:", np.sqrt(years_exp))
print("Log salaries:\n", np.log(salaries))

def bonus_logic(row):
    return row * 1.10 if np.mean(row) > 100 else row * 1.05

print("Adjusted:\n", np.apply_along_axis(bonus_logic, 1, salaries))

# ===============================
# PANDAS SECTION
# ===============================

df = pd.DataFrame(np.random.randint(1, 50, (5, 3)), columns=['X', 'Y', 'Z'])

df['Log_X'] = np.log(df['X'])
df['Sqrt_Y'] = np.sqrt(df['Y'])

print("\nDataFrame:\n", df)
print("\nCorrelation:\n", df.corr())

df['Square_Z'] = np.square(df['Z'])
df['Exp_X'] = np.exp(df['X'])

print("\nUpdated DF:\n", df)

# ===============================
# SAVE & LOAD CSV
# ===============================

df.to_csv("sample_data.csv", index=False)
df2 = pd.read_csv("sample_data.csv")

df2['Sum_XY'] = df2['X'] + df2['Y']
df2['Z_per_X'] = df2['Z'] / df2['X']

print("\nCSV Loaded:\n", df2.head())
print("\nDescribe:\n", df2.describe())

df2.to_csv("modified_sample_data.csv", index=False)

# ===============================
# CLEANED STACK OVERFLOW ANALYSIS
# ===============================

df_kaggle = pd.DataFrame({
    'Country': ['PH', 'USA', 'UK', 'Canada', 'Germany'],
    'EdLevel': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master'],
    'YearsCodePro': [2, 12, 8, 15, 10],
    'ConvertedComp': np.random.randint(40000, 150000, 5)
})

df_kaggle.dropna(inplace=True)

df_kaggle['ExperienceLevel'] = np.where(
    df_kaggle['YearsCodePro'] >= 10,
    'Senior',
    'Junior'
)

grouped = df_kaggle.groupby(
    ['Country', 'ExperienceLevel']
)['ConvertedComp'].mean().reset_index()

print("\nGrouped Data:\n", grouped)

# ===============================
# FINAL TEST ARRAY (STUDENT)
# ===============================

np.random.seed(STUDENT_ID)
arr = np.random.randint(1, 100, 10)

print("\nFinal Array:", arr)
print("Mean:", np.mean(arr))
print("Std:", np.std(arr))