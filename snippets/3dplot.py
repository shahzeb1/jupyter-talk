marks_and_colors = ["r", "o"], ["b", "^"]

def plot_3d(new_point=False):
    "Makes a 3d plot for a given dataset"
    fig = plt.figure(figsize=(16, 16)) # easy way to get bigger figures
    ax = fig.add_subplot(111, projection='3d')
    
    # Scatter points:
    i = 0
    for group in data_points:
        for point in group:
            ax.scatter(point[0], point[1], point[2], c=marks_and_colors[i][0], marker=marks_and_colors[i][1])
        i = i + 1

    # Check to see if new_point is set:
    if new_point:
        ax.scatter(new_point[0], new_point[1], new_point[2], c="g", marker="o", s=600)
        
    # Labels:
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
    
    # Save the image:
    fig.savefig('output/3d-plot.png')
    plt.close(fig)