import MDAnalysis as mda
from MDAnalysis.analysis.dihedrals import Dihedral
import numpy as np
import matplotlib.pyplot as plt


# Initialize a list to store all Chi1 angles across trajectories
all_chi1_angles_first_frames = []
all_chi1_angles_last_frames = []

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

        # Select the atoms for the residue of interest for Chi1 calculation
        residue = u.select_atoms("resnum 319")
        chi1_atoms = residue.select_atoms("name N and resid 319 and id 5038") + residue.select_atoms("name CB and resid 319 and id 5042") + \
                    residue.select_atoms("name CA and resid 319 and id 5040") + residue.select_atoms("name CG and resid 319 and id 5045")

        # Initialize the Dihedral object with Chi1 atoms
        chi1_dihedral = Dihedral([chi1_atoms])

        # Run the dihedral analysis on the entire trajectory
        chi1_dihedral.run()

        # Extract Chi1 angles for specific frames (first five and last five)
        first_five_frames = range(5)  # First five frames
        last_five_frames = range(len(u.trajectory) - 5, len(u.trajectory))  # Last five frames
        selected_frames_first = list(first_five_frames)
        selected_frames_last = list(last_five_frames)

        # Extract Chi1 angles only for the selected frames and add to the cumulative list
        selected_chi1_angles_first = [chi1_dihedral.angles[frame][0] for frame in selected_frames_first]
        print(selected_chi1_angles_first)
        # Extract Chi1 angles only for the selected frames and add to the cumulative list
        selected_chi1_angles_last = [chi1_dihedral.angles[frame][0] for frame in selected_frames_last]
        print(selected_chi1_angles_last)

        all_chi1_angles_first_frames.extend(selected_chi1_angles_first)  # Append to cumulative list
        all_chi1_angles_last_frames.extend(selected_chi1_angles_last)

# Convert the cumulative list of Chi1 angles to a NumPy array
all_chi1_angles_first = np.array(all_chi1_angles_first_frames)
print(all_chi1_angles_first)
# Convert the cumulative list of Chi1 angles to a NumPy array
all_chi1_angles_last = np.array(all_chi1_angles_last_frames)
print(all_chi1_angles_last)

# Plotting the histogram of Chi1 angles
plt.figure(figsize=(8, 6))

# Define custom bin edges (e.g., -180 to 180 with step size of 10)
bin_edges = np.arange(-180, 210, 10)  # Custom bin edges with a range of 10 degrees

# Compute histogram data for both datasets using the custom bin edges
hist_first, _ = np.histogram(all_chi1_angles_first, bins=bin_edges)
hist_last, _ = np.histogram(all_chi1_angles_last, bins=bin_edges)

# Set the width for the bars
width = 4  # Width of the bars, adjust to fit the custom bin size

# Increased shift (to make the bars further apart)
shift_factor = 0.5  # This will control the separation between the histograms

# Plot the first Chi1 angles in blue, shifted to the left
plt.bar(bin_edges[:-1] - width * shift_factor, hist_first, width=width, color='blue', edgecolor='black', alpha=0.7, label='First Frames')

# Plot the last Chi1 angles in red, shifted to the right
plt.bar(bin_edges[:-1] + width * shift_factor, hist_last, width=width, color='red', edgecolor='black', alpha=0.7, label='Last Frames')

# Adding labels and title

# Adding labels and title
plt.xlabel('Tyr353 Chi1 Angle (degrees)', fontsize=17)
plt.ylabel('Occurrence', fontsize=17)
plt.title('Occurrence of Chi1 Angles for Tyr353', fontsize=20, pad=15)

# Add a legend to describe the colors and cutoff
plt.legend(handles=[plt.Line2D([0], [0], color='blue', lw=6, label='First Five Frames'),
                    plt.Line2D([0], [0], color='red', lw=6, label='Last Five Frames ')],
           loc='upper right', fontsize=12)

plt.tight_layout()

plt.savefig("3w3l_dihedral_angles.png")

# Show the plot
plt.show()

