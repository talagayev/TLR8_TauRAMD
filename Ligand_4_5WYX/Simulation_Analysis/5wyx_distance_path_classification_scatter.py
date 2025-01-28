import MDAnalysis as mda
from MDAnalysis.analysis import distances
import numpy as np
import matplotlib.pyplot as plt

# Initialize lists to store minimal distances to residues
minimal_distances_to_ex = []
minimal_distances_to_in = []

# Function to calculate minimal distances
def calculate_minimal_distances(universe, residue_ex, residue_in, mol_atoms, frame_subset=None):
    min_distance_to_ex = float('inf')
    min_distance_to_in = float('inf')
    
    # Iterate through specified frames (all if frame_subset is None)
    frames = universe.trajectory if frame_subset is None else frame_subset
    for ts in frames:
        dist_to_ex = distances.distance_array(residue_ex.positions, mol_atoms.positions).min()
        dist_to_in = distances.distance_array(residue_in.positions, mol_atoms.positions).min()
        min_distance_to_ex = min(min_distance_to_ex, dist_to_ex)
        min_distance_to_in = min(min_distance_to_in, dist_to_in)
    
    return min_distance_to_ex, min_distance_to_in

# Main analysis loop
for folder_num in range(1, 6):
    gro_file = f"{folder_num}/{folder_num}_1/confout_1st_equil.gro"
    for i in range(1, 21):
        xtc_file = f"{folder_num}/{folder_num}_{i}/confout_{folder_num}_{i}_Rep_tauramd.xtc"
        print(f"Processing {xtc_file}")
        try:
            u = mda.Universe(gro_file, xtc_file)
            residue_ex = u.select_atoms("resnum 67")
            residue_in = u.select_atoms("resnum 112")
            mol_atoms = u.select_atoms("resname MOL")

            # Calculate minimal distances
            min_ex, min_in = calculate_minimal_distances(u, residue_ex, residue_in, mol_atoms, frame_subset=u.trajectory[-10:])
            if max(min_ex, min_in) > 20:
                min_ex, min_in = calculate_minimal_distances(u, residue_ex, residue_in, mol_atoms)

            minimal_distances_to_ex.append(min_ex)
            minimal_distances_to_in.append(min_in)

            print(min_ex)
            print(min_in)
            print("external path" if min_ex < min_in else "internal path")

        except Exception as e:
            print(f"Error processing {xtc_file}: {e}")

# Convert results to numpy arrays
minimal_distances_to_ex = np.array(minimal_distances_to_ex)
minimal_distances_to_in = np.array(minimal_distances_to_in)

# Highlighted trajectories (as provided)
highlighted_indices = [
    (1, 1), (1, 16), (2, 1), (2, 4), (2, 6), (2, 14), 
    (3, 3), (3, 8), (4, 2), (4, 3), (4, 9), (4, 18), 
    (4, 19), (4, 20), (5, 13), (5, 14), (5, 15), (5, 20)
]

# Convert to zero-based indices for Python lists
highlighted_indices = [(f - 1) * 20 + s - 1 for f, s in highlighted_indices]

# Determine colors for all points
colors = np.where(minimal_distances_to_ex < minimal_distances_to_in, 'red', 'blue')

# Plot
plt.figure(figsize=(6, 6))
plt.xlim(1, 26)
plt.xticks([5, 10, 15, 20, 25], fontsize=13)
plt.ylim(1, 26)
plt.yticks([5, 10, 15, 20, 25], fontsize=13)
plt.plot([0, 26], [0, 26], ls="--", c=".3")

# Plot all normal points
for idx in range(len(minimal_distances_to_ex)):
    if idx not in highlighted_indices:
        plt.scatter(
            minimal_distances_to_ex[idx], 
            minimal_distances_to_in[idx], 
            c=colors[idx], alpha=0.7
        )

# Highlight incorrect assignments with "circle-in-circle" effect
for idx in highlighted_indices:
    color = colors[idx]
    # Outer circle
    plt.scatter(
        minimal_distances_to_ex[idx], minimal_distances_to_in[idx], 
        c=color, s=200, edgecolors='none', alpha=0.9
    )
    # White buffer
    plt.scatter(
        minimal_distances_to_ex[idx], minimal_distances_to_in[idx], 
        c='white', s=150, edgecolors='none', alpha=1
    )
    # Inner circle
    plt.scatter(
        minimal_distances_to_ex[idx], minimal_distances_to_in[idx], 
        c=color, s=50, edgecolors='none', alpha=0.9
    )

# Label the axes
plt.xlabel('Minimum Distance to Phe526* (Å)', fontsize=17)
plt.ylabel('Minimum Distance to Ala571* (Å)', fontsize=17)
plt.title('Unbinding Pathway Ligand 4', fontsize=20, pad=15)

# Example legend with dots instead of lines
plt.legend(handles=[
    plt.Line2D([0], [0], color='blue', marker='o', markersize=12, linestyle='None', label='Internal Path'),
    plt.Line2D([0], [0], color='red', marker='o', markersize=12, linestyle='None', label='External Path')],
    loc='upper center', fontsize=12)

# Save the plot as an image file
plt.savefig('scatter_5wyx_final_with_outliers.png')

# Display the plot
plt.show()
