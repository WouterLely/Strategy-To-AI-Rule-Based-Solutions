import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# Function to predict budget exhaustion
def predict_budget_exhaustion(total_budget, actuals, current_date):
    spent_so_far = sum(actuals)
    last_month_spend = actuals[-1]
    remaining_budget = total_budget - spent_so_far
    
    if last_month_spend <= 0:
        return None
    
    months_left = int(remaining_budget // last_month_spend)
    days_into_next_month = int(((remaining_budget % last_month_spend) / last_month_spend) * 30)
    
    exhaustion_date = current_date + timedelta(days=(months_left * 30 + days_into_next_month))
    return exhaustion_date.date()

# Dataset
providers = [
    {"health_care_provider": "Achmea", "total_budget": 12_000_000, "actuals": [950_000, 1_050_000, 980_000, 1_000_000]},
    {"health_care_provider": "Zilveren Kruis", "total_budget": 8_000_000, "actuals": [600_000, 620_000, 610_000, 630_000]},
    {"health_care_provider": "VGZ", "total_budget": 15_000_000, "actuals": [1_200_000, 1_150_000, 1_250_000, 1_300_000]},
    {"health_care_provider": "CZ", "total_budget": 10_000_000, "actuals": [800_000, 790_000, 820_000, 810_000]},
]

current_date = datetime(2025, 4, 30)

# Prepare DataFrame
rows = []
for provider in providers:
    exhaustion_date = predict_budget_exhaustion(provider["total_budget"], provider["actuals"], current_date)
    rows.append({
        "health_care_provider": provider["health_care_provider"],
        "actuals_month_1": provider["actuals"][0],
        "actuals_month_2": provider["actuals"][1],
        "actuals_month_3": provider["actuals"][2],
        "actuals_month_4": provider["actuals"][3],
        "budget_expiration_date": exhaustion_date
    })

df = pd.DataFrame(rows)

# Plot the table
fig, ax = plt.subplots(figsize=(10, 2))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Adjust font size
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width([0,1,2,3,4,5])

plt.show()
