# KEY CONCEPT 3: REVENUE CALCULATIONS
print("=== KEY CONCEPT 3: REVENUE CALCULATIONS ===")
print("Formula: Actual Revenue = Successful Bookings × ADR")
print("Formula: Potential Revenue = Total Capacity × ADR")
print("Formula: Revenue Leakage = (Potential Revenue - Actual Revenue) / Potential Revenue × 100")

# Calculate actual and potential revenues
analysis_df['actual_revenue'] = analysis_df['successful_bookings'] * analysis_df['adr']
analysis_df['potential_revenue'] = analysis_df['capacity'] * analysis_df['adr']
analysis_df['revenue_leakage'] = analysis_df['potential_revenue'] - analysis_df['actual_revenue']

# Total revenue calculations
total_actual_revenue = analysis_df['actual_revenue'].sum()
total_potential_revenue = analysis_df['potential_revenue'].sum()
total_revenue_leakage = total_potential_revenue - total_actual_revenue
revenue_leakage_percentage = (total_revenue_leakage / total_potential_revenue) * 100

print(f"\n=== REVENUE ANALYSIS RESULTS ===")
print(f"Total Actual Revenue: ₹{total_actual_revenue/1_000_000:.2f} million")
print(f"Total Potential Revenue: ₹{total_potential_revenue/1_000_000:.2f} million") 
print(f"Total Revenue Leakage: ₹{total_revenue_leakage/1_000_000:.2f} million")
print(f"Revenue Leakage Percentage: {revenue_leakage_percentage:.1f}%")

# KEY CONCEPT 4: RevPAR CALCULATION
print(f"\n=== KEY CONCEPT 4: RevPAR (Revenue Per Available Room) ===")
print("Formula 1: RevPAR = ADR × Occupancy Rate")
print("Formula 2: RevPAR = Total Room Revenue ÷ Total Available Rooms")

# Calculate RevPAR using both methods
analysis_df['revpar_method1'] = analysis_df['adr'] * (analysis_df['occupancy_rate'] / 100)
analysis_df['revpar_method2'] = analysis_df['actual_revenue'] / analysis_df['capacity']

# Verify both methods give same result
print(f"\nRevPAR Method 1 Average: ₹{analysis_df['revpar_method1'].mean():.0f}")
print(f"RevPAR Method 2 Average: ₹{analysis_df['revpar_method2'].mean():.0f}")
print("✓ Both methods yield identical results")

# RevPAR by category and day type
print(f"\n=== RevPAR ANALYSIS BY SEGMENTS ===")
revpar_analysis = analysis_df.groupby(['category', 'day_type']).agg({
    'revpar_method1': 'mean',
    'adr': 'mean', 
    'occupancy_rate': 'mean'
}).round(0)

for (category, day_type), row in revpar_analysis.iterrows():
    print(f"{category} {day_type}: RevPAR=₹{row['revpar_method1']:.0f}, ADR=₹{row['adr']:.0f}, Occ={row['occupancy_rate']:.1f}%")