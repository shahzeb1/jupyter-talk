def interactive_3d_plot():
    data = [None] * number_of_clusters
    
    # Marker and color info 
    marks_and_interactive = ["red", "circle"], ["blue", "diamond"]
    
    # Scatter points:
    i = 0
    for g in data_points:
        group = go.Scatter3d(
            x=g[:,0],
            y=g[:,1],
            z=g[:,2],
            mode='markers',
            name='Grouping {}'.format(i+1),
            marker=dict(
                color=marks_and_interactive[i][0],
                size=12,
                symbol=marks_and_interactive[i][1],
                line=dict(
                    color='rgba(217, 217, 217, 0.14)',
                    width=0.5
                ),
                opacity=0.6
            )
        )
        data[i] = group
        i = i + 1
    
    # The layout for the plot:
    layout = go.Layout(
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        )
    )
    
    py.offline.iplot({"data":data, "layout":layout})