# employee_viz.py
# Contact: 24f2009046@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import io, base64, textwrap

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

# The Python code itself (to embed in HTML for verification)
script_code = textwrap.dedent("""\
    import pandas as pd
    import matplotlib.pyplot as plt
    import io, base64

    df = pd.read_csv("employee_data_100.csv")

    finance_count = (df["department"] == "Finance").sum()
    print(f'Frequency count for "Finance" department: {finance_count}')

    dept_counts = df["department"].value_counts().sort_index()

    plt.figure(figsize=(8, 5))
    dept_counts.plot(kind="bar")
    plt.title("Department Distribution (100 Employees)")
    plt.xlabel("Department")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("department_distribution.png", dpi=150)
    plt.show()
""")

# Build HTML content with code + results + visualization
html_content = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Employee Performance Visualization</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 2em; }}
    pre {{ background: #f4f4f4; padding: 1em; border-radius: 8px; }}
    img {{ max-width: 100%; height: auto; }}
  </style>
</head>
<body>
  <h1>Employee Performance Visualization</h1>
  <p><b>Email (verification):</b> 24f2009046@ds.study.iitm.ac.in</p>

  <h2>Python Code</h2>
  <pre>{script_code}</pre>

  <h2>Finance Department Count</h2>
  <p>{finance_count}</p>

  <h2>Department Distribution</h2>
  <img src="data:image/png;base64,{img_b64}" alt="Department Distribution">
</body>
</html>
"""

# Save as HTML file
with open("employee_viz.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ HTML file 'employee_viz.html' generated successfully (includes code + output).")


