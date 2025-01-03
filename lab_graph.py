import plotly.graph_objects as go
from scipy.spatial.distance import pdist, squareform
import numpy as np


def generate_lab_3d(df, figure_title, output_file_name):

    """
    Creates a 3d plot of the provided colors based off their LAB values.

    :param df: pandas dataframe with columns "Shirt Color", "Pantone Color", "L*a*b Value", and "HEX"
    :param figure_title: Title you would like displayed on the plot
    :param output_file_name: Output file name
    :return:
    """

    # Parse the L*a*b values from the string format
    df[['L', 'a', 'b']] = df['L*a*b Value'].str.split(', ', expand=True).astype(float)

    # Create the 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=df['a'],  # a* axis (green-red)
        y=df['L'],  # L* axis (lightness)
        z=df['b'],  # b* axis (blue-yellow)
        mode='markers+text',
        text=df['Shirt Color'],
        hovertemplate=
        '<b>%{text}</b><br>' +
        'L*: %{y:.1f}<br>' +
        'a*: %{x:.1f}<br>' +
        'b*: %{z:.1f}<br>',
        marker=dict(
            size=10,
            color=['#' + hex.strip() for hex in df['HEX']],  # Use actual hex colors
            opacity=0.8
        ),
        textposition='top center'
    )])

    # Update the layout
    fig.update_layout(
        title=figure_title,
        scene=dict(
            xaxis_title='a* (green to red)',
            yaxis_title='L* (black to white)',
            zaxis_title='b* (blue to yellow)',
            # Set appropriate ranges for each axis
            xaxis=dict(range=[-128, 128]),
            yaxis=dict(range=[0, 100]),
            zaxis=dict(range=[-128, 128])
        ),
        width=1000,
        height=800,
        showlegend=False
    )

    # Add better camera angle
    fig.update_layout(scene_camera=dict(
        up=dict(x=0, y=1, z=0),
        center=dict(x=0, y=0, z=0),
        eye=dict(x=1.5, y=1.5, z=1.5)
    ))

    # Show the plot
    fig.show()

    fig.write_html(output_file_name + ".html")
    return


def generate_lab_3d_all_colors(df, figure_title, output_filename):
    # Parse the L*a*b values from the string format
    df[['L', 'a', 'b']] = df['L*a*b Value'].str.split(', ', expand=True).astype(float)

    # Create the 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=df['a'],        # a* axis (green-red)
        y=df['L'],        # L* axis (lightness)
        z=df['b'],        # b* axis (blue-yellow)
        mode='markers+text',
        text=df['Color Name'],
        hovertemplate=
            '<b>%{text}</b><br>' +
            'L*: %{y:.1f}<br>' +
            'a*: %{x:.1f}<br>' +
            'b*: %{z:.1f}<br>',
        marker=dict(
            size=3,
            color=['#' + hex.strip() for hex in df['Hex']],  # Use actual hex colors
            opacity=1.0
        ),
        textposition='top center',
        textfont=dict(
            size=8
        )
    )])

    # Update the layout
    fig.update_layout(
        template="plotly",
        title=figure_title,
        scene=dict(
            # TODO Adjust before publish
            aspectratio=dict(x=1, y=1, z=1),
            xaxis_title='a* (green to red)',
            yaxis_title='L* (black to white)',
            zaxis_title='b* (blue to yellow)',
            # Set appropriate ranges for each axis
            # Originally -128, 128
            xaxis=dict(range=[-128, 128]),
            # Originally [0, 100]
            yaxis=dict(range=[0, 100]),
            zaxis=dict(range=[-128, 128])
        ),
        #TODO Change for Export
        width=500,
        height=500,
        showlegend=False,
        margin=dict(l=1, r=1, t=1, b=1)
    )

    # Add better camera angle
    fig.update_layout(scene_camera=dict(
        up=dict(x=0, y=1, z=0),
        center=dict(x=0, y=0, z=0),
        eye=dict(x=1.5, y=1.5, z=1.5)
    ))

    # Show the plot
    fig.show()

    # Optionally save to HTML file
    #fig.write_html(output_filename + ".html")


def greedy_mdp(points, k):
    n = len(points)
    # Calculate pairwise distances
    distances = squareform(pdist(points))

    # Start with the two most distant points
    selected = set()
    i, j = np.unravel_index(np.argmax(distances), distances.shape)
    selected.add(i)
    selected.add(j)

    # Greedily add points
    while len(selected) < k:
        max_min_dist = -1
        best_point = -1

        for i in range(n):
            if i not in selected:
                # Calculate minimum distance to selected points
                min_dist = min(distances[i][j] for j in selected)
                if min_dist > max_min_dist:
                    max_min_dist = min_dist
                    best_point = i

        selected.add(best_point)

    return list(selected)