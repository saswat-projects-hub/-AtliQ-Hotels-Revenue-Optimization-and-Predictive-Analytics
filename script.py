import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load the datasets
dim_date = pd.read_csv('dim_date.csv')
dim_hotels = pd.read_csv('dim_hotels.csv')
fact_bookings = pd.read_csv('fact_aggregated_bookings.csv')

# Display basic information about the datasets
print("=== DATASET OVERVIEW ===")
print(f"Date dimension: {dim_date.shape}")
print(f"Hotels dimension: {dim_hotels.shape}")
print(f"Fact bookings: {fact_bookings.shape}")

print("\n=== DATE DIMENSION SAMPLE ===")
print(dim_date.head())

print("\n=== HOTELS DIMENSION ===")
print(dim_hotels.head())

print("\n=== BOOKINGS FACT SAMPLE ===")
print(fact_bookings.head())