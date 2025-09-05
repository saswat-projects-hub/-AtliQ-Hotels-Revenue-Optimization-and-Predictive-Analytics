# KEY CONCEPT 2: AVERAGE DAILY RATE (ADR) ASSUMPTIONS
print("=== KEY CONCEPT 2: AVERAGE DAILY RATE (ADR) ASSUMPTIONS ===")
print("Since actual pricing data is not available, we use industry-standard assumptions:")
print("1. Luxury hotels command higher rates than Business hotels")
print("2. Room categories RT1-RT4 represent different room types (Standard to Suite)")
print("3. Mumbai > Delhi > Bangalore > Hyderabad (market premium)")
print("4. Weekend rates are 15-25% higher than weekday rates")

# Define ADR assumptions based on industry standards (in INR)
adr_base = {
    ('Luxury', 'RT1'): 4000,     # Standard Luxury Room
    ('Luxury', 'RT2'): 5500,     # Deluxe Luxury Room  
    ('Luxury', 'RT3'): 7000,     # Premium Luxury Room
    ('Luxury', 'RT4'): 9000,     # Luxury Suite
    ('Business', 'RT1'): 2500,   # Standard Business Room
    ('Business', 'RT2'): 3200,   # Deluxe Business Room
    ('Business', 'RT3'): 4000,   # Premium Business Room
    ('Business', 'RT4'): 5000    # Business Suite
}

# City multipliers
city_multipliers = {
    'Mumbai': 1.25,
    'Delhi': 1.15, 
    'Bangalore': 1.05,
    'Hyderabad': 1.00
}

# Weekend premium (20% higher on weekends)
weekend_premium = 1.20

# Create ADR calculation function
def calculate_adr(category, room_category, city, day_type):
    base_rate = adr_base.get((category, room_category), 3000)  # Default fallback
    city_adjusted = base_rate * city_multipliers.get(city, 1.0)
    
    if day_type == 'weekend':
        return city_adjusted * weekend_premium
    else:
        return city_adjusted

# Apply ADR calculation to our dataset
analysis_df['adr'] = analysis_df.apply(
    lambda row: calculate_adr(row['category'], row['room_category'], row['city'], row['day_type']), 
    axis=1
)

print("\nSample ADR calculations:")
sample_adrs = analysis_df[['property_name', 'category', 'room_category', 'city', 'day_type', 'adr']].head(10)
print(sample_adrs)