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