def interactive_3d_plot(new_point=False, save=False):
    data = []
    
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
                    width=0.2
                ),
                opacity=0.6
            )
        )
        data.append(group)
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
    
    # To save the plot, pass in a flag and then render the plot out as a .html file:
    if save:
        file_name = "3d-interactive-plot"
        py.offline.plot({"data": data, "layout": layout}, 
                            auto_open=False, filename="output/{}.html".format(file_name))
        print("Saved the file {}".format(file_name))
    
    # Use the offline plot to see the plot:
    py.offline.iplot({"data":data, "layout":layout})