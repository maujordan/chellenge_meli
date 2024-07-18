from matplotlib.ticker import FuncFormatter

# Function to format the y-axis
def y_axis_formatter(x, pos):
    if x >= 1e6:
        return f'{x*1e-6:.0f}M'
    elif x >= 1e3:
        return f'{x*1e-3:.0f}k'
    else:
        return f'{x:.2f}'