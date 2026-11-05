import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

def pseudo_potential(x, y, mu, q1, q2):
    """
    Calculates the pseudo-potential in the rotating frame of the CR3BP.

    Args:
        x (float): x-coordinate in the rotating frame.
        y (float): y-coordinate in the rotating frame.
        mu (float): Mass parameter (mass of the smaller primary).

    Returns:
        float: Pseudo-potential at the given coordinates.
    """
    r1 = np.sqrt((x + mu)**2 + y**2)
    r2 = np.sqrt((x - 1 + mu)**2 + y**2)
    return (x**2 + y**2) + 2* ((1 - mu)*q1 / r1 + mu*q2 / r2)

def zero_velocity_curves(mu, q1, q2, c_values, L_values, colors, x_range, y_range, num_points=1000):
    """
    Generates the Zero-Velocity Curves for given Jacobi constant values.

    Args:
        mu (float): Mass parameter (mass of the smaller primary).
        c_values (list or np.ndarray): List of Jacobi constant values.
        x_range (tuple): Range of x-coordinates (xmin, xmax).
        y_range (tuple): Range of y-coordinates (ymin, ymax).
        num_points (int): Number of points to use for the grid in each dimension.

    Returns:
        None: Displays the plot of the Zero-Velocity Curves.
    """
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = np.linspace(y_range[0], y_range[1], num_points)
    X, Y = np.meshgrid(x, y)
    potential = pseudo_potential(X, Y, mu, q1, q2)

    contour_levels = np.linspace(min(c_values), max(c_values), len(c_values))
    norm = mcolors.Normalize(vmin=min(c_values), vmax=max(c_values))
    sm = cm.ScalarMappable(norm=norm, cmap="viridis")
    
    for c in c_values:
        Z = 2*potential - c  # Jacobi integral: C = 2U - (x'^2 + y'^2) velocity
        con = ax.contour(X, Y, Z, levels=contour_levels, cmap="viridis", linewidths=0.5)

    # Plot the locations of the primaries
    ax.plot(-mu, 0, 'ro', markersize=6, label='Primary 1 (1-mu)')
    ax.plot(1 - mu, 0, 'go', markersize=2, label='Primary 2 (mu)')

    tit = 'Zero-Velocity Curves for μ=' + str(round(mu,3)) + ', q1=' + str(q1) + ', q2=' + str(q2)

    ax.grid(True)

    ax.tick_params(bottom=False, left=False)

    if col == 0:
        ax.set_ylabel(row_labels[row], fontsize=12, fontweight="bold", labelpad=15)
        ax.set_yticks([-1, 0, 1])
        
    if row == 4:
        ax.set_xlabel(col_labels[col], fontsize=12, fontweight="bold", labelpad=15)
        ax.set_xticks([-1, 0, 1])
        
    if col == 4 and row == 0:
        cbar = fig.colorbar(sm, ax=axes.ravel().tolist(), shrink=0.8, pad=0.04)
        cbar.set_label(r"$C_J$", fontsize=12, labelpad=15)

    # plt.show()
    

# Create a 5x5 grid of subplots
fig, axes = plt.subplots(5, 5, figsize=(10,7.5), sharex=True, sharey=True, gridspec_kw={'wspace': 0, 'hspace': 0})

# Iterate through the axes array
for row in range(5):
    for col in range(5):
        if __name__ == "__main__":
            # Define the mass parameter for the CR3BP
            mu = 1/4 

            ax = axes[row, col]
            q2 = row/4
            q1 = col/4

            col_labels = ['$q_1=0.00$', '$q_1=0.25$', '$q_1=0.50$', '$q_1=0.75$', '$q_1=1.00$']
            row_labels = ['$q_2=0.00$', '$q_2=0.25$', '$q_2=0.50$', '$q_2=0.75$', '$q_2=1.00$']

            # Choose some Jacobi constant values to visualize different curves
            # c_values_example = [2.987993197438921, 3.012151098008731, 3.1721916318646435, 3.1883775367858638]
            # c_values_example = [3.0, 3.015, 3.1721916318646435, 3.1883775367858638]
            # c_values = np.linspace(1.5, 5.0, 100)
            c_values = np.linspace(0, 6, 20)
            L_values = []
            colors = []

            # Define the range of x and y coordinates to plot
            x_range = (-1.75, 1.75)
            y_range = (-1.75, 1.75)

            zero_velocity_curves(mu, q1, q2, c_values, L_values, colors, x_range, y_range)

for spine in ax.spines.values():
    spine.set_edgecolor('black')  # Border color
    spine.set_linewidth(1.5)      # Border thickness

output_path = '/Users/sofialasky/Documents/Sanchez_Group/zvcs/zvc_1to3.png'
plt.savefig(output_path, dpi=500)

plt.show()