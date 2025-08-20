# employee_viz.py
# Contact: 24f2009046@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

# Load employee data (100 rows)
df = pd.read_csv("employee_data_100.csv")

# Calculate frequency count for Finance department
finance_count = (df["department"] == "Finance").sum()
print(f'Frequency count for "Finance" department: {finance_count}')

# Plot histogram (department distribution)
dept_counts = df["department"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
dept_counts.plot(kind="bar")
plt.title("Department Distribution (100 Employees)")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()

# Save the plot as PNG
plt.savefig("department_distribution.png", dpi=150)

# Optionally show the plot
plt.show()

