# KEY CONCEPT 5: WEEK-ON-WEEK (WoW) ANALYSIS
print("=== KEY CONCEPT 5: WEEK-ON-WEEK (WoW) ANALYSIS ===")
print("Formula: WoW Change = ((Current Week - Previous Week) / Previous Week) × 100")

# Group by week and calculate weekly metrics
weekly_performance = analysis_df.groupby('week no').agg({
    'actual_revenue': 'sum',
    'potential_revenue': 'sum', 
    'successful_bookings': 'sum',
    'capacity': 'sum'
}).reset_index()

weekly_performance['occupancy_rate'] = (weekly_performance['successful_bookings'] / 
                                       weekly_performance['capacity']) * 100
weekly_performance['revenue_leakage_pct'] = ((weekly_performance['potential_revenue'] - 
                                            weekly_performance['actual_revenue']) / 
                                           weekly_performance['potential_revenue']) * 100

# Calculate WoW changes
weekly_performance['wow_revenue_change'] = weekly_performance['actual_revenue'].pct_change() * 100
weekly_performance['wow_occupancy_change'] = weekly_performance['occupancy_rate'].pct_change() * 100

print("Weekly Performance Summary:")
print("Week | Revenue(M) | Occupancy% | WoW Rev% | WoW Occ%")
print("-" * 55)
for _, row in weekly_performance.head(8).iterrows():
    revenue_m = row['actual_revenue'] / 1_000_000
    wow_rev = row['wow_revenue_change'] if not pd.isna(row['wow_revenue_change']) else 0
    wow_occ = row['wow_occupancy_change'] if not pd.isna(row['wow_occupancy_change']) else 0
    print(f"{row['week no']} | ₹{revenue_m:.1f}M | {row['occupancy_rate']:.1f}% | {wow_rev:+.1f}% | {wow_occ:+.1f}%")

# KEY CONCEPT 6: CITY-WISE PERFORMANCE ANALYSIS  
print(f"\n=== KEY CONCEPT 6: CITY-WISE REVENUE PERFORMANCE ===")
city_performance = analysis_df.groupby('city').agg({
    'actual_revenue': 'sum',
    'potential_revenue': 'sum',
    'successful_bookings': 'sum', 
    'capacity': 'sum',
    'adr': 'mean'
}).reset_index()

city_performance['occupancy_rate'] = (city_performance['successful_bookings'] / 
                                     city_performance['capacity']) * 100
city_performance['revpar'] = city_performance['actual_revenue'] / city_performance['capacity']
city_performance['revenue_leakage_pct'] = ((city_performance['potential_revenue'] - 
                                           city_performance['actual_revenue']) / 
                                          city_performance['potential_revenue']) * 100

print("City | Revenue(M) | RevPAR | Occupancy% | ADR | Rev.Leakage%")
print("-" * 65)
for _, row in city_performance.iterrows():
    revenue_m = row['actual_revenue'] / 1_000_000
    print(f"{row['city']} | ₹{revenue_m:.1f}M | ₹{row['revpar']:.0f} | {row['occupancy_rate']:.1f}% | ₹{row['adr']:.0f} | {row['revenue_leakage_pct']:.1f}%")