# Let's create some summary data for charting
import pandas as pd
import numpy as np

# Load the analysis data
df = pd.read_csv('atliq_hotels_analysis.csv')

# Weekend vs weekday performance
day_type_performance = df.groupby('day_type').agg({
    'occupancy_rate': 'mean',
    'adr': 'mean',
    'successful_bookings': 'sum',
    'capacity': 'sum',
    'actual_revenue': 'sum',
    'potential_revenue': 'sum'
}).reset_index()

day_type_performance['revpar'] = day_type_performance['actual_revenue'] / day_type_performance['capacity']
day_type_performance = day_type_performance.round(1)

# Create simple data for charting
day_type_summary = pd.DataFrame({
    'day_type': ['Weekend', 'Weekday'],
    'occupancy': [73.6, 51.3],
    'revpar': [5012, 2933]
})

day_type_summary.to_csv('day_type_summary.csv', index=False)
print("Day type performance summary:")
print(day_type_summary)

# Category comparison (Business vs Luxury)
category_performance = df.groupby('category').agg({
    'occupancy_rate': 'mean',
    'adr': 'mean',
    'successful_bookings': 'sum',
    'capacity': 'sum',
    'actual_revenue': 'sum',
    'potential_revenue': 'sum'
}).reset_index()

category_performance['revpar'] = category_performance['actual_revenue'] / category_performance['capacity']
category_performance = category_performance.round(1)

# Create simple data for charting
category_summary = pd.DataFrame({
    'category': ['Luxury', 'Business'],
    'occupancy': [57.7, 58.2],
    'revpar': [5084, 3260],
    'revenue_millions': [551.8, 241.0]
})

category_summary.to_csv('category_summary.csv', index=False)
print("\nCategory performance summary:")
print(category_summary)