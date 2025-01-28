import MDAnalysis as mda
from MDAnalysis.analysis import distances
import numpy as np
import matplotlib.pyplot as plt


# Initialize lists to store minimal distances to residues
minimal_distances_to_ex = []
minimal_distances_to_in = []

# Loop through the outer folders (1 to 5)
for folder_num in range(1, 6):  # Adjust the range if you have more folders
    # Define the GRO file based on the outer folder number
    gro_file = f"{folder_num}/{folder_num}_1/confout_1st_equil.gro"
    
    # Loop through the inner subdirectories (1_1 to 1_20, 2_1 to 2_20, etc.)
    for i in range(1, 21):  # Adjust the range if you have more files
        xtc_file = f"{folder_num}/{folder_num}_{i}/confout_{folder_num}_{i}_Rep_tauramd.xtc"
        print(f"Processing {xtc_file}")

        # Load the structure and trajectory files
        u = mda.Universe(gro_file, xtc_file)

        # Select the atoms for both residues
        residue_ex = u.select_atoms("resnum 68")
        residue_in = u.select_atoms("resnum 113")
        mol_atoms = u.select_atoms("resname MOL")

        # Initialize minimal distances for the current trajectory
        min_distance_to_ex = float('inf')
        min_distance_to_in = float('inf')

        # Loop over the last 30 frames in the trajectory
        for ts in u.trajectory[-10:]:
            # Calculate the distance arrays between MOL atoms and each residue
            dist_to_ex = distances.distance_array(residue_ex.positions, mol_atoms.positions).min()
            dist_to_in = distances.distance_array(residue_in.positions, mol_atoms.positions).min()

            # Update the minimal distances if smaller distances are found
            min_distance_to_ex = min(min_distance_to_ex, dist_to_ex)
            min_distance_to_in = min(min_distance_to_in, dist_to_in)

        if min_distance_to_ex > 20 or min_distance_to_in > 20:
            for ts in u.trajectory:
            # Calculate the distance arrays between MOL atoms and each residue
                dist_to_ex = distances.distance_array(residue_ex.positions, mol_atoms.positions).min()
                dist_to_in = distances.distance_array(residue_in.positions, mol_atoms.positions).min()

                # Update the minimal distances if smaller distances are found
                min_distance_to_ex = min(min_distance_to_ex, dist_to_ex)
                min_distance_to_in = min(min_distance_to_in, dist_to_in)

                # Store the minimal distances for this trajectory
            minimal_distances_to_ex.append(min_distance_to_ex)
            minimal_distances_to_in.append(min_distance_to_in)
            print(min_distance_to_ex)
        
        else:
            # Store the minimal distances for this trajectory
            minimal_distances_to_ex.append(min_distance_to_ex)
            minimal_distances_to_in.append(min_distance_to_in)

        print(min_distance_to_ex)
        print(min_distance_to_in)
        if min_distance_to_ex < min_distance_to_in:
            print("external path")
        else:
            print("internal path")

# Convert results to numpy arrays
minimal_distances_to_ex = np.array(minimal_distances_to_ex)
minimal_distances_to_in = np.array(minimal_distances_to_in)

# Highlighted trajectories (as provided)
highlighted_indices = [
    (1, 1), (1, 3), (1, 5), (1, 6), (1, 7),
    (1, 8), (1, 19), (1, 20), (2, 1), (2, 3),
    (2, 16), (2, 17), (2, 19), (2, 20), (3, 3),
    (3, 6), (3, 8), (3, 10), (3, 13), (3, 15),
    (3, 17), (4, 4), (4, 11), (4, 13), (4, 15),
    (4, 18), (4, 19), (4, 20), (5, 1), (5, 2),
    (5, 5), (5, 6), (5, 10), (5, 11), (5, 12),
    (5, 16), (5, 18), (5, 19), (5, 20),
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
plt.title('Unbinding Pathway Ligand 6', fontsize=20, pad=15)

plt.legend(handles=[
    plt.Line2D([0], [0], color='blue', marker='o', markersize=12, linestyle='None', label='Internal Path'),
    plt.Line2D([0], [0], color='red', marker='o', markersize=12, linestyle='None', label='External Path')],
    loc='upper center', fontsize=12)


# Save the plot as an image file
plt.savefig('scatter_7crf_final_outlier.png')

# Optional: If you don't want to display the plot, you can remove this line
plt.show()

