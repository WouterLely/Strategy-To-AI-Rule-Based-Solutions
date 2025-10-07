import matplotlib.pyplot as plt
import pandas as pd

def staffing_margin(inkoop, verkoop):
    margin = ((verkoop - inkoop) / inkoop) * 100
    if margin < 5:
        margin = 5
    if margin >= 10:
        status = "✅ OK (profitable)"
    else:
        status = "⚠️ Warning (margin too low)"
    return margin, status

scenarios = [
    {"inkoop": 50, "verkoop": 55},
    {"inkoop": 60, "verkoop": 63},
    {"inkoop": 70, "verkoop": 65},
    {"inkoop": 80, "verkoop": 90},
    {"inkoop": 100, "verkoop": 105},
]

results = []
for s in scenarios:
    margin, status = staffing_margin(s["inkoop"], s["verkoop"])
    results.append({"inkoop": s["inkoop"], "verkoop": s["verkoop"], "margin": margin, "status": status})

df = pd.DataFrame(results)

print("{:<8} {:<8} {:<8} {:<25}".format("inkoop", "verkoop", "margin", "status"))
for index, row in df.iterrows():
    print("{:<8} {:<8} {:<8.1f} {:<25}".format(row['inkoop'], row['verkoop'], row['margin'], row['status']))

plt.figure(figsize=(8,6))
plt.scatter(df["inkoop"], df["margin"], color="red", label="Inkoop vs Margin", marker="o")
plt.scatter(df["verkoop"], df["margin"], color="blue", label="Verkoop vs Margin", marker="x")

plt.axhline(10, color="green", linestyle="--", label="Target 10% Margin")
plt.axhline(5, color="orange", linestyle="--", label="Minimum 5% Margin")

plt.fill_between(
    x=[df["inkoop"].min()-5, df["verkoop"].max()+5], 
    y1=5, 
    y2=10, 
    color="yellow", 
    alpha=0.2, 
    label="⚠️ Warning Zone (5%-10%)"
)

plt.title("What-if Analysis: Staffing Margins")
plt.xlabel("Tarief (€)")
plt.ylabel("Margin %")
plt.legend()
plt.grid(True)
plt.show()
