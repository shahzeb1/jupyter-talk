def plot_3d():
    "Makes a 3d plot for a given dataset"
    fig = plt.figure(figsize=(16, 16))
    ax = fig.add_subplot(111, projection='3d')

    # Data points:
    xs, ys, zs = 2, 4, 6
    
    # Scatter points:
    ax.scatter(xs, ys, zs, c="r", marker="o")

    # Labels:
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()