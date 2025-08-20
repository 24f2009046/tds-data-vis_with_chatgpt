# employee_viz.py
# Contact: 24f2009046@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import io, base64, textwrap
from datetime import datetime

# Load the dataset
csv_path = "employee_data_100.csv"
df = pd.read_csv(csv_path)

# Frequency count for Finance department
finance_count = (df["department"] == "Finance").sum()
print(f'Frequency count for "Finance" department: {finance_count}')

# Create histogram (bar chart of departments)
dept_counts = df["department"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
dept_counts.plot(kind="bar")
plt.title("Department Distribution (100 Employees)")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()

# Save plot to memory buffer for embedding in HTML
buf = io.BytesIO()
plt.savefig(buf, format="png", bbox_inches="tight", dpi=150)
plt.close()
buf.seek(0)
img_b64 = base64.b64encode(buf.read()).decode("utf-8")

# Python code snippet for embedding in HTML
runnable_code = textwrap.dedent("""\
    import pandas as pd
    import matplotlib.pyplot as plt

    # Path to your CSV (place your 100-row dataset here)
    csv_path = "employee_data_100.csv"

    # Load data
    df = pd.read_csv(csv_path)

    # Frequency count for "Finance"
    finance_count = (df["department"] == "Finance").sum()
    print(f'Frequency count for "Finance" department: {finance_count}')

    # Department distribution (bar chart)
    dept_counts = df["department"].value_counts().sort_index()

    plt.figure(figsize=(8, 5))
    dept_counts.plot(kind="bar")
    plt.title("Department Distribution (100 Employees)")
    plt.xlabel("Department")
    plt.ylabel("Count")
    plt.tight_layout()

    # Save the figure if you want a separate image file
    plt.savefig("department_distribution.png", dpi=150, bbox_inches="tight")
    plt.close()
""")

# Timestamp
generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Build HTML
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Employee Department Visualization</title>
<style>
  body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 2rem; }}
  h1, h2 {{ margin: 0 0 0.5rem 0; }}
  .meta {{ color: #444; margin-bottom: 1.25rem; }}
  .card {{ border: 1px solid #ddd; border-radius: 12px; padding: 1rem 1.25rem; margin-bottom: 1rem; }}
  pre {{ background: #f7f7f7; border-radius: 10px; padding: 1rem; overflow-x: auto; }}
  code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
  img {{ max-width: 100%; height: auto; display: block; }}
</style>
</head>
<body>
  <h1>Employee Department Visualization</h1>
  <div class="meta">Generated on: {generated_time}</div>

  <div class="card">
    <h2>Contact</h2>
    <p>Email (for verification): <strong>24f2009046@ds.study.iitm.ac.in</strong></p>
  </div>

  <div class="card">
    <h2>Finance Department Frequency</h2>
    <p>Frequency count for "Finance" department (from the loaded CSV): <strong>{finance_count}</strong></p>
  </div>

  <div class="card">
    <h2>Department Distribution</h2>
    <img alt="Department Distribution" src="data:image/png;base64,{img_b64}" />
  </div>

  <div class="card">
    <h2>Python Code Used</h2>
    <p>Save your full dataset as <code>employee_data_100.csv</code> in the same folder, then run:</p>
    <pre><code>{runnable_code}</code></pre>
  </div>

  <div class="card">
    <h2>Notes</h2>
    <ul>
      <li>This HTML is self-contained and embeds the chart as base64 so it works via the raw GitHub URL.</li>
      <li>Replace the CSV with your 100-row dataset and rerun the Python to refresh the numbers and figure.</li>
    </ul>
  </div>
</body>
</html>"""

# Save HTML file
with open("employee_viz.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ HTML file 'employee_viz.html' generated successfully (includes code + output).")