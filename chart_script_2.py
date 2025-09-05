import pandas as pd
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('day_type_summary.csv')

# Create normalized RevPAR values for visualization (scale to 0-100 range like occupancy)
revpar_min = df['revpar'].min()
revpar_max = df['revpar'].max()
df['revpar_normalized'] = ((df['revpar'] - revpar_min) / (revpar_max - revpar_min)) * 100

# Create figure
fig = go.Figure()

# Add occupancy bars
fig.add_trace(go.Bar(
    x=df['day_type'],
    y=df['occupancy'],
    name='Occ. Rate (%)',
    text=[f"{val:.1f}%" for val in df['occupancy']],
    textposition='auto',
    marker_color='#1FB8CD',  # Strong cyan (blue-ish)
    cliponaxis=False,
    offsetgroup=1
))

# Add RevPAR bars (normalized but with original values in text)
fig.add_trace(go.Bar(
    x=df['day_type'],
    y=df['revpar_normalized'],
    name='RevPAR (₹)',
    text=[f"₹{val:,.0f}" for val in df['revpar']],
    textposition='auto',
    marker_color='#ECEBD5',  # Light green
    cliponaxis=False,
    offsetgroup=2
))

# Update layout
fig.update_layout(
    title='Weekend vs Weekday Performance Gap',
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Update y-axis 
fig.update_yaxes(
    title='Performance Index',
    showgrid=True
)

# Update x-axis
fig.update_xaxes(
    title='Day Type',
    showgrid=False
)

# Save the figure
fig.write_image('weekend_weekday_comparison.png')