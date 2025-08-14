import matplotlib.pyplot as plt

def save_plot(fig, filename):
    fig.savefig(filename, bbox_inches='tight', dpi=300)
    print(f"Plot saved as {filename}")
