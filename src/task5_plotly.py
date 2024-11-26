import numpy as np
import pandas as pd
import plotly.express as px

def create_interactive_plotly(df):

    fig = px.scatter(
        df,
        x='x',
        y='y',
        title='Interactive Scatter Plot',
        labels={'x': 'X-Axis Label', 'y': 'Y-Axis Label'},
        color=df['y'],
        color_continuous_scale='Viridis',
        hover_data={'x': True, 'y': True}
    )

    fig.update_layout(
        title_font_size=20,
        legend_title='Color Scale',
        xaxis_title='Variable X',
        yaxis_title='Variable Y',
        template='plotly_white'
    )

    fig.show()

df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})

create_interactive_plotly(df)
