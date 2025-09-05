import pandas as pd
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('city_performance.csv')

# Sort by RevPAR for better visualization
df_sorted = df.sort_values('revpar', ascending=True)

# Create RevPAR bar chart (most important KPI for hotel revenue management)
fig = go.Figure()

fig.add_trace(go.Bar(
    y=df_sorted['city'],
    x=df_sorted['revpar'],
    orientation='h',
    marker_color='#1FB8CD',
    text=[f'{val:.0f}' for val in df_sorted['revpar']],
    textposition='outside'
))

fig.update_layout(
    title='Atliq Hotels: City RevPAR Performance',
    xaxis_title='RevPAR (₹)',
    yaxis_title='City'
)

# Save the chart
fig.write_image('revpar_chart.png')
print("Chart saved successfully!")