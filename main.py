<<<<<<< HEAD
from pathlib import Path
import shutil
import json
import csv
import time

# =========================
# BASIC SETUP
# =========================
student_id = "TUPM-25-1268"
student_name = "Jonabel Jocson"

documents_path = Path.home() / "Documents" / "Activity_5_Files"
documents_path.mkdir(parents=True, exist_ok=True)

# =========================
# CREATE AND WRITE FILE
# =========================
file_path = documents_path / f"intro_{student_id}.txt"
file_path.write_text(
    f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!"
)

print(f"File created and text written at: {file_path}")

# READ FILE
content = file_path.read_text()
print(content)

# APPEND TO FILE
with file_path.open("a") as f:
    f.write("\nThis is a new line.")

print("Line appended!")

# =========================
# WRITE MULTIPLE LINES
# =========================
lines = ["Line 1", "Line 2", "Line 3"]

lines_file = documents_path / f"lines_{student_id}.txt"
with lines_file.open("w") as f:
    f.write("\n".join(lines))

# READ LINES
with lines_file.open("r") as f:
    for line in f:
        print(line.strip())

# WORD COUNT
text = lines_file.read_text()
word_count = len(text.split())
print("Word count:", word_count)

# =========================
# COPY FILE
# =========================
src = documents_path / f"intro_{student_id}.txt"
dst = documents_path / f"intro_copy_{student_id}.txt"

shutil.copy(src, dst)
print(f"File copied successfully from {src.name} to {dst.name}.")

# =========================
# RENAME FILE
# =========================
old_file = documents_path / f"intro_copy_{student_id}.txt"
new_file = documents_path / f"intro_renamed_{student_id}.txt"

old_file.rename(new_file)
print(f"File renamed successfully from {old_file.name} to {new_file.name}.")

# =========================
# DELETE FILE
# =========================
if new_file.exists():
    new_file.unlink()
    print(f"File deleted successfully from: {new_file}")
else:
    print("File not found.")

# =========================
# CREATE DIRECTORY
# =========================
new_dir = documents_path / f"data_{student_id}"
new_dir.mkdir(parents=True, exist_ok=True)

print(f"Subdirectory created at: {new_dir}")

# =========================
# JSON FILE
# =========================
json_data = {
    "name": student_name,
    "age": 19,
    "course": "Python Programming"
}

json_file = new_dir / f"student_{student_id}.json"

with json_file.open("w") as f:
    json.dump(json_data, f, indent=4)

print(f"JSON file written at: {json_file}")

# READ JSON
with json_file.open("r") as f:
    data = json.load(f)

print(data)

# =========================
# CSV FILE
# =========================
csv_file = documents_path / f"students_{student_id}.csv"

rows = [
    ["Name", "Student ID", "Score"],
    ["Anna", "2025-1001", 90],
    ["Ben", "2025-1002", 85],
    [student_name, student_id, 95]
]

with csv_file.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"CSV file created at: {csv_file}")

# READ CSV
with csv_file.open("r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# =========================
# FILE NOT FOUND HANDLING
# =========================
missing_file = documents_path / f"missing_file_{student_id}.txt"

try:
    print(missing_file.read_text())
except FileNotFoundError:
    print(f"File not found for Student ID: {student_id}")

# =========================
# LIST FILES
# =========================
txt_files = list(documents_path.glob("*.txt"))

print(f"Student ID: {student_id}")
print(f"Found {len(txt_files)} .txt files")

for file in txt_files:
    print(file.name)

# =========================
# FILE INFO
# =========================
if file_path.exists():
    stat = file_path.stat()
    print(f"File: {file_path.name}")
    print(f"Size: {stat.st_size} bytes")
    print(f"Last Modified: {time.ctime(stat.st_mtime)}")

# =========================
# FORMAT LINES
# =========================
if not lines_file.exists():
    lines_file.write_text("Line 1\nLine 2\nLine 3")

lines = lines_file.read_text().splitlines()

with lines_file.open("w") as f:
    for i, line in enumerate(lines, 1):
        f.write(f"{i}: {line.upper()}\n")

print("Lines formatted.")

# =========================
# REVERSE LINES
# =========================
lines = lines_file.read_text().splitlines()
lines.reverse()

with lines_file.open("w") as f:
    f.write("\n".join(lines))

print("Lines reversed.")

# =========================
# MERGE FILES
# =========================
file1 = documents_path / f"intro_{student_id}.txt"
file2 = documents_path / f"lines_{student_id}.txt"
merged_file = documents_path / f"merged_{student_id}.txt"

if not file1.exists():
    file1.write_text("Sample intro file")

if not file2.exists():
    file2.write_text("Line 1\nLine 2\nLine 3")

with merged_file.open("w") as mf:
    mf.write(file1.read_text())
    mf.write("\n")
    mf.write(file2.read_text())

print("Files merged successfully.")
=======
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
>>>>>>> f46040103e68b10b32d9639ef5a23ca67aa6a659
