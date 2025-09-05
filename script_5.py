# KEY CONCEPT 7: PROPERTY-LEVEL PERFORMANCE RANKING
print("=== KEY CONCEPT 7: PROPERTY-LEVEL PERFORMANCE ANALYSIS ===")

property_performance = analysis_df.groupby(['property_name', 'category', 'city']).agg({
    'actual_revenue': 'sum',
    'potential_revenue': 'sum',
    'successful_bookings': 'sum',
    'capacity': 'sum',
    'adr': 'mean'
}).reset_index()

property_performance['occupancy_rate'] = (property_performance['successful_bookings'] / 
                                         property_performance['capacity']) * 100
property_performance['revpar'] = property_performance['actual_revenue'] / property_performance['capacity']
property_performance['revenue_leakage_pct'] = ((property_performance['potential_revenue'] - 
                                               property_performance['actual_revenue']) / 
                                              property_performance['potential_revenue']) * 100

# Sort by RevPAR descending
property_performance = property_performance.sort_values('revpar', ascending=False)

print("TOP 10 PERFORMING PROPERTIES BY RevPAR:")
print("Property | Category | City | RevPAR | Occupancy% | Revenue(M)")
print("-" * 70)
for _, row in property_performance.head(10).iterrows():
    revenue_m = row['actual_revenue'] / 1_000_000
    print(f"{row['property_name']} | {row['category']} | {row['city']} | ₹{row['revpar']:.0f} | {row['occupancy_rate']:.1f}% | ₹{revenue_m:.1f}M")

print(f"\nBOTTOM 5 PERFORMING PROPERTIES BY RevPAR:")
print("Property | Category | City | RevPAR | Occupancy% | Revenue(M)")
print("-" * 70)
for _, row in property_performance.tail(5).iterrows():
    revenue_m = row['actual_revenue'] / 1_000_000
    print(f"{row['property_name']} | {row['category']} | {row['city']} | ₹{row['revpar']:.0f} | {row['occupancy_rate']:.1f}% | ₹{revenue_m:.1f}M")

# KEY CONCEPT 8: DEMAND PATTERN ANALYSIS
print(f"\n=== KEY CONCEPT 8: DEMAND PATTERN ANALYSIS ===")
print("Concept: Analyze booking patterns to identify peak/off-peak periods")

# Create demand heatmap data
demand_analysis = analysis_df.groupby(['week no', 'day_type']).agg({
    'occupancy_rate': 'mean',
    'successful_bookings': 'sum',
    'capacity': 'sum'
}).reset_index()

print("\nDemand Patterns by Week and Day Type:")
print("Week | Weekend Occ% | Weekday Occ% | Demand Gap")
print("-" * 50)

# Calculate demand gaps
for week in sorted(demand_analysis['week no'].unique())[:8]:
    week_data = demand_analysis[demand_analysis['week no'] == week]
    weekend_occ = week_data[week_data['day_type'] == 'weekend']['occupancy_rate'].iloc[0] if not week_data[week_data['day_type'] == 'weekend'].empty else 0
    weekday_occ = week_data[week_data['day_type'] == 'weekeday']['occupancy_rate'].iloc[0] if not week_data[week_data['day_type'] == 'weekeday'].empty else 0
    demand_gap = weekend_occ - weekday_occ
    print(f"{week} | {weekend_occ:.1f}% | {weekday_occ:.1f}% | {demand_gap:+.1f}pp")

# Save processed data for visualization
analysis_df.to_csv('atliq_hotels_analysis.csv', index=False)
city_performance.to_csv('city_performance.csv', index=False)
property_performance.to_csv('property_performance.csv', index=False)
weekly_performance.to_csv('weekly_performance.csv', index=False)

print(f"\n=== DATA EXPORTED FOR VISUALIZATION ===")
print("Files created: atliq_hotels_analysis.csv, city_performance.csv, property_performance.csv, weekly_performance.csv")