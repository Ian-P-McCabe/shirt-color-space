import plotly.graph_objects as go


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



