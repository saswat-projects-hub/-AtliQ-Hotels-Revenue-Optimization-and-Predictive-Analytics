# Convert check_in_date to datetime and merge datasets
fact_bookings['check_in_date'] = pd.to_datetime(fact_bookings['check_in_date'], format='%d-%b-%y')
dim_date['date'] = pd.to_datetime(dim_date['date'], format='%d-%b-%y')

# Merge all datasets
analysis_df = fact_bookings.merge(dim_hotels, on='property_id', how='left')
analysis_df = analysis_df.merge(dim_date, left_on='check_in_date', right_on='date', how='left')

print("=== MERGED DATASET SAMPLE ===")
print(analysis_df.head())

# KEY CONCEPT 1: OCCUPANCY RATE CALCULATION
print("\n=== KEY CONCEPT 1: OCCUPANCY RATE ===")
print("Formula: Occupancy Rate = (Successful Bookings / Total Capacity) × 100")

# Calculate occupancy rates
analysis_df['occupancy_rate'] = (analysis_df['successful_bookings'] / analysis_df['capacity']) * 100

# Overall occupancy statistics
overall_occupancy = (analysis_df['successful_bookings'].sum() / analysis_df['capacity'].sum()) * 100
print(f"Overall Occupancy Rate: {overall_occupancy:.1f}%")

# Occupancy by day type
occupancy_by_daytype = analysis_df.groupby('day_type').agg({
    'successful_bookings': 'sum',
    'capacity': 'sum'
}).reset_index()
occupancy_by_daytype['occupancy_rate'] = (occupancy_by_daytype['successful_bookings'] / 
                                         occupancy_by_daytype['capacity']) * 100

print("\nOccupancy by Day Type:")
for _, row in occupancy_by_daytype.iterrows():
    print(f"{row['day_type']}: {row['occupancy_rate']:.1f}%")

# Occupancy by hotel category
occupancy_by_category = analysis_df.groupby('category').agg({
    'successful_bookings': 'sum',
    'capacity': 'sum'
}).reset_index()
occupancy_by_category['occupancy_rate'] = (occupancy_by_category['successful_bookings'] / 
                                          occupancy_by_category['capacity']) * 100

print("\nOccupancy by Hotel Category:")
for _, row in occupancy_by_category.iterrows():
    print(f"{row['category']}: {row['occupancy_rate']:.1f}%")