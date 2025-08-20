# employee_viz.py
# Contact: 24f2009046@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import io, base64

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

# Save plot to buffer and encode as base64 (for embedding in HTML)
buf = io.BytesIO()
plt.savefig(buf, format="png", dpi=150, bbox_inches="tight")
plt.close()
buf.seek(0)
img_b64 = base64.b64encode(buf.read()).decode("utf-8")

# Build HTML content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Employee Performance Visualization</title>
</head>
<body>
  <h1>Employee Performance Visualization</h1>
  <p><b>Email (verification):</b> 24f2009046@ds.study.iitm.ac.in</p>
  <p><b>Finance Department Count:</b> {finance_count}</p>
  <h2>Department Distribution</h2>
  <img src="data:image/png;base64,{img_b64}" alt="Department Distribution">
</body>
</html>
"""

# Save as HTML file
with open("employee_viz.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ HTML file 'employee_viz.html' generated successfully.")


