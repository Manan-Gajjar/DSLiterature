import plotly.express as px
import plotly.graph_objects as go


def plot_linear_plot(x, y, y_pred):

    connecting_line = []

    for i in range(len(x)):

        connecting_line.append(
            go.Scatter(
                x=[x[i], x[i]],
                y=[y[i], y_pred[i]],
                mode="lines",
                line=dict(color="gray", dash="dash"),
            )
        )

    scatter_plot = go.Scatter(x=x, y=y, mode="markers")
    line_plot = go.Scatter(x=x, y=y_pred, mode="lines")
    fig = go.Figure(data=[scatter_plot, line_plot, *connecting_line])

    fig.update_layout(
        showlegend=False,
        xaxis_title="X",
        yaxis_title="Y",
        title="Liner regression",
        margin=dict(l=0, r=0),
        autosize=False,
        width=800,
        height=400,
        template="plotly_dark"
        # paper_bgcolor="Black",
    )

    return fig.show()