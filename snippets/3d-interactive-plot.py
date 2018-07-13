def interactive_3d_plot():
    trace1 = go.Scatter3d(
        x=[3],
        y=[4],
        z=[5],
        mode='markers',
        marker=dict(
            color='blue',
            size=12,
            symbol='circle',
            line=dict(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5
            ),
            opacity=0.6
        )
    )
    
    data = [trace1]
    
    layout = go.Layout(
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        )
    )
    
    py.offline.iplot({"data":data, "layout":layout})