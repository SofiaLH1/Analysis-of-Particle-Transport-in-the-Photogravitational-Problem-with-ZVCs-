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

    # contour_levels = np.linspace(min(c_values), max(c_values), len(c_values))
    # norm = mcolors.Normalize(vmin=min(c_values), vmax=max(c_values))
    # sm = cm.ScalarMappable(norm=norm, cmap="PuOr")
    # plt.figure(figsize=(6, 6))
    for c in c_values:
        Z = 2*potential - c  # Jacobi integral: C = 2U - (x'^2 + y'^2) velocity
        ax.contour(X, Y, Z, levels=[c], colors=colors[c_values.index(c)], linewidths=1.25)

    # Plot the locations of the primaries
    ax.plot(-mu, 0, 'ro', markersize=6, label='Primary 1 (1-mu)')
    ax.plot(1 - mu, 0, 'go', markersize=3, label='Primary 2 (mu)')

    ax.grid(True)

    ax.tick_params(bottom=False, left=False)


    if col == 0:
        ax.set_ylabel(row_labels[row], fontsize=12, fontweight="bold", labelpad=15)
        ax.set_yticks([-1, 0, 1])

    if row == 4:
        ax.set_xlabel(col_labels[col], fontsize=12, fontweight="bold", labelpad=15)
        ax.set_xticks([-1, 0, 1])


    # plt.show()
    
# Recording the Lagrange points 
L1 = np.array([
    [1.000001000051043e-05, 0.3534103534103537, 0.4907904907904914, 0.5884705884705888, np.nan],
    [-0.1309701309701303, 0.2006902006902003, 0.2871702871702873, 0.3380103380103385, 0.3727503727503727],
    [-0.2145902145902152, 0.1404901404901402, 0.2238502238502242, 0.2740702740702741, 0.3093103093103089],
    [-0.2793302793302797, 0.1011701011701014, 0.1828701828701824, 0.2327502327502327, 0.2681902681902688],
    [np.nan, 0.07199007199007212, 0.1524101524101518, 0.2019302019302014, 0.2374302374302371],
])

L2 = np.array([
    [np.nan, np.nan, np.nan, np.nan, np.nan],
    [0.9611309611309604, 0.974850974850975, 0.9896109896109895, 1.005391005391004, 1.022191022191022],
    [1.062691062691062, 1.076451076451077, 1.090811090811091, 1.105791105791106, 1.121331121331121],
    [1.135831135831136, 1.149271149271149, 1.163151163151163, 1.177431177431178, 1.192091192091192],
    [1.194851194851195, 1.207951207951208, 1.221351221351222, 1.235071235071235, 1.249051249051249],
])

L3 = np.array([
    [np.nan, -0.7920507920507927, -0.9315109315109318, -1.030031030031029, -1.108751108751109],
    [np.nan, -0.8009308009308018, -0.9394909394909394, -1.037371037371038, -1.115611115611117],
    [np.nan, -0.8099908099908095, -0.9475309475309484, -1.044751044751045, -1.122491122491123],
    [np.nan, -0.8192108192108201, -0.955650955650956, -1.052191052191052, -1.12941112941113],
    [np.nan, -0.8285708285708289, -0.9638309638309632, -1.059631059631061, -1.136351136351136],
])

CL1 = np.array([
    [1.000002000103086e-10, 0.6102813281009822, 1.049815233506801, 1.431127038476245, np.nan],
    [0.2261037491523437, 1.022140627437619, 1.596041410680954, 2.110916382253718, 2.594347949651638],
    [0.4242965976607682, 1.356735312844849, 1.999360066747357, 2.570514663908924, 3.103211713546682],
    [0.6065683374789878, 1.661573317421406, 2.358414215939933, 2.972991913439534, 3.543299026407508],
    [np.nan, 1.948628651681768, 2.692065265997846, 3.343519161736237, 3.945570623022689],
])

CL2 = np.array([
    [np.nan, np.nan, np.nan, np.nan, np.nan],
    [1.489772303340418, 1.745942440336963, 1.999341215826674, 2.249833038386112, 2.497294819307577],
    [1.971011282663585, 2.208625550573171, 2.443881980539106, 2.676727184676258, 2.907116558324471],
    [2.355836721375539, 2.581698828377852, 2.805489942558287, 3.027185414725284, 3.246766488332951],
    [2.689854525437407, 2.907054047701251, 3.122394654651658, 3.335865068983388, 3.547458135622213],
])

CL3 = np.array([
    [np.nan, 1.354008173597315, 1.982208826512081, 2.496306690199114, 2.948832204605202],
    [np.nan, 1.467918294401165, 2.086234516127639, 2.59432405613305, 3.042525847383756],
    [np.nan, 1.581134333335148, 2.189742830300425, 2.691918988203852, 3.135858659460261],
    [np.nan, 1.693651863208046, 2.292734125833427, 2.789092734963428, 3.228832061075912],
    [np.nan, 1.805467408019495, 2.395209110841122, 2.885846720913783, 3.321447572060158],
])

# Create a 5x5 grid of subplots
fig, axes = plt.subplots(5, 5, figsize=(7.75,7.75), sharex=True, sharey=True, gridspec_kw={'wspace': 0, 'hspace': 0})

# Iterate through the axes array
for row in range(5):
    for col in range(5):
        if __name__ == "__main__":
            # Define the mass parameter for the CR3BP
            mu = 1/3 
            # Define the radiation constants for the two primaries
            ax = axes[row, col]
            q2 = row/4
            q1 = col/4

            row_labels = ['$q_2=0.00$', '$q_2=0.25$', '$q_2=0.50$', '$q_2=0.75$', '$q_2=1.00$']
            col_labels = ['$q_1=0.00$', '$q_1=0.25$', '$q_1=0.50$', '$q_1=0.75$', '$q_1=1.00$']

            # Choose some Jacobi constant values to visualize different curves
            # c_values_example = [2.987993197438921, 3.012151098008731, 3.1721916318646435, 3.1883775367858638]
            # c_values_example = [3.0, 3.015, 3.1721916318646435, 3.1883775367858638]
            # c_values = np.linspace(1.5, 5.0, 100)
            c_values = [CL1[int(row)][int(col)], CL2[int(row)][int(col)], CL3[int(row)][int(col)]]
            L_values = [L1[int(row)][int(col)], L2[int(row)][int(col)], L3[int(row)][int(col)]]
            colors = ['goldenrod', 'blue', 'firebrick']

            # Define the range of x and y coordinates to plot
            x_range = (-1.75, 1.75)
            y_range = (-1.75, 1.75)

            zero_velocity_curves(mu, q1, q2, c_values, L_values, colors, x_range, y_range)

for a in fig.axes:
    for spine in a.spines.values():
        spine.set_edgecolor('black')  # Border color
        spine.set_linewidth(1.5)      # Border thickness

output_path = '/Users/sofialasky/Documents/Sanchez_Group/zvcs/zvcs_lagrange_1to1.png'
plt.savefig(output_path, dpi=500)

plt.show()