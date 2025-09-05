# Create a comprehensive summary of key metrics and formulas for the report
print("=== COMPREHENSIVE ANALYSIS SUMMARY ===")
print()

# Load the analysis data one more time for final calculations
df = pd.read_csv('atliq_hotels_analysis.csv')

print("KEY HOSPITALITY REVENUE MANAGEMENT CONCEPTS USED:")
print("=" * 60)
print()

print("1. OCCUPANCY RATE")
print("   Formula: (Successful Bookings ÷ Total Capacity) × 100")
print("   Purpose: Measures utilization efficiency of available rooms")
print("   Industry Benchmark: 70-80% for well-performing hotels")
print(f"   Atliq Result: {(df['successful_bookings'].sum() / df['capacity'].sum() * 100):.1f}%")
print()

print("2. AVERAGE DAILY RATE (ADR)")
print("   Formula: Total Room Revenue ÷ Number of Rooms Sold")
print("   Purpose: Measures average price achieved per occupied room")
print("   Factors: Hotel category, location, day type, seasonality")
print(f"   Atliq Average ADR: ₹{df['adr'].mean():.0f}")
print()

print("3. REVENUE PER AVAILABLE ROOM (RevPAR)")
print("   Formula 1: ADR × Occupancy Rate")
print("   Formula 2: Total Room Revenue ÷ Total Available Rooms")
print("   Purpose: Key profitability metric combining rate and occupancy")
print("   Industry Use: Primary benchmark for competitive comparison")
print(f"   Atliq Overall RevPAR: ₹{(df['actual_revenue'].sum() / df['capacity'].sum()):.0f}")
print()

print("4. REVENUE LEAKAGE")
print("   Formula: (Potential Revenue - Actual Revenue) ÷ Potential Revenue × 100")
print("   Purpose: Identifies lost revenue opportunities")
print("   Causes: Suboptimal pricing, low occupancy, operational inefficiencies")
print(f"   Atliq Revenue Leakage: {((df['potential_revenue'].sum() - df['actual_revenue'].sum()) / df['potential_revenue'].sum() * 100):.1f}%")
print()

print("5. DYNAMIC PRICING STRATEGY")
print("   Concept: Real-time rate adjustments based on demand, competition, events")
print("   Implementation: Different rates for weekends vs weekdays, seasons, market conditions")
print("   Evidence in Data: Weekend rates 20% higher than weekday rates")
print()

print("6. MARKET SEGMENTATION")
print("   Concept: Different pricing strategies for Luxury vs Business segments")
print("   Luxury Hotels: Premium positioning, higher ADR, enhanced services")
print("   Business Hotels: Value positioning, corporate focus, competitive rates")
print()

print("7. WEEK-ON-WEEK (WoW) ANALYSIS")
print("   Formula: ((Current Period - Previous Period) ÷ Previous Period) × 100")
print("   Purpose: Track performance trends and volatility")
print("   Finding: Significant volatility with revenue swings of 17-21%")
print()

# Calculate final summary metrics
total_actual = df['actual_revenue'].sum() / 1_000_000
total_potential = df['potential_revenue'].sum() / 1_000_000
total_leakage = total_potential - total_actual

print("FINAL CALCULATED RESULTS:")
print("=" * 40)
print(f"Total Actual Revenue: ₹{total_actual:.1f} million")
print(f"Total Potential Revenue: ₹{total_potential:.1f} million")
print(f"Total Revenue Leakage: ₹{total_leakage:.1f} million")
print(f"Revenue Leakage Percentage: {(total_leakage/total_potential*100):.1f}%")
print()

# Weekend vs weekday comparison
weekend_data = df[df['day_type'] == 'weekend']
weekday_data = df[df['day_type'] == 'weekeday']

weekend_occ = (weekend_data['successful_bookings'].sum() / weekend_data['capacity'].sum()) * 100
weekday_occ = (weekday_data['successful_bookings'].sum() / weekday_data['capacity'].sum()) * 100

weekend_revpar = weekend_data['actual_revenue'].sum() / weekend_data['capacity'].sum()
weekday_revpar = weekday_data['actual_revenue'].sum() / weekday_data['capacity'].sum()

print("DEMAND PATTERN ANALYSIS:")
print("=" * 30)
print(f"Weekend Occupancy: {weekend_occ:.1f}%")
print(f"Weekday Occupancy: {weekday_occ:.1f}%")
print(f"Occupancy Gap: {weekend_occ - weekday_occ:.1f} percentage points")
print(f"Weekend RevPAR: ₹{weekend_revpar:.0f}")
print(f"Weekday RevPAR: ₹{weekday_revpar:.0f}")
print(f"RevPAR Gap: {((weekend_revpar - weekday_revpar) / weekday_revpar * 100):.1f}%")
print()

# Category comparison
luxury_data = df[df['category'] == 'Luxury']
business_data = df[df['category'] == 'Business']

luxury_revpar = luxury_data['actual_revenue'].sum() / luxury_data['capacity'].sum()
business_revpar = business_data['actual_revenue'].sum() / business_data['capacity'].sum()

print("CATEGORY PERFORMANCE ANALYSIS:")
print("=" * 35)
print(f"Luxury RevPAR: ₹{luxury_revpar:.0f}")
print(f"Business RevPAR: ₹{business_revpar:.0f}")
print(f"Performance Gap: {((luxury_revpar - business_revpar) / business_revpar * 100):.1f}%")
print()

print("CODE IMPLEMENTATION SUMMARY:")
print("=" * 35)
print("• Python pandas for data manipulation and aggregation")
print("• Hospitality KPI calculations using industry-standard formulas")
print("• Time-series analysis for weekly performance tracking")
print("• Market segmentation analysis by category, city, and day type")
print("• Revenue optimization calculations and gap analysis")