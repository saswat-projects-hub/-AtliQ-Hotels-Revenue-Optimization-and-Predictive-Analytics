import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('atliq_hotels_analysis.csv')

# Group by week number and sum revenue leakage
weekly_leakage = df.groupby('week no')['revenue_leakage'].sum().reset_index()

# Convert to millions
weekly_leakage['revenue_leakage_millions'] = weekly_leakage['revenue_leakage'] / 1000000

# Create line chart with markers
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=weekly_leakage['week no'],
    y=weekly_leakage['revenue_leakage_millions'],
    mode='lines+markers+text',
    line=dict(color='#DB4545', width=3),
    marker=dict(color='#DB4545', size=8),
    text=[f'{val:.2f}m' for val in weekly_leakage['revenue_leakage_millions']],
    textposition="top center",
    textfont=dict(size=12, color='#DB4545'),
    cliponaxis=False,
    name='Revenue Leakage'
))

# Update layout
fig.update_layout(
    title="Weekly Revenue Leakage Analysis",
    showlegend=False
)

# Update axes with lighter gridlines
fig.update_xaxes(title="Week No", showgrid=True, gridcolor='lightgray', gridwidth=1)
fig.update_yaxes(title="Revenue Loss (m)", showgrid=True, gridcolor='lightgray', gridwidth=1)

# Save the chart
fig.write_image("weekly_revenue_leakage.png")