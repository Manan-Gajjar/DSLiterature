import plotly.express as px
import plotly.graph_objects as go

def linear_plot(x, y, y_pred):

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

    return fig


def scatter_plot(data1, x1, y1, data2=None, x2=None, y2=None):
    scatter1 = go.Scatter(x=data1[x1], y=data1[y1], mode="markers", name="Data1")
    fig = go.Figure(data=[scatter1])

    if data2 is not None:
        scatter2 = go.Scatter(x=data2[x2], y=data2[y2], mode="markers", name="Data2")
        fig.add_trace(scatter2)

    fig.update_layout(
        showlegend=True,
        xaxis_title=x1,
        yaxis_title=y1,
        title=f"{x1} vs {y1}",
        margin=dict(l=0, r=0),
        autosize=False,
        width=800,
        height=600,
        template="plotly_dark"
    )

    return fig
