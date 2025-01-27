import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# List of Excel file names (each with a single sheet)
file_names = ['3W3L_Path.xlsx', '6TY5_Path.xlsx', '7YTX_Path.xlsx', '5WYX_Path.xlsx', '6KYA_Path.xlsx', '7CRF_Path.xlsx']


# Define pathway categories and colors
pathways = ['External', 'Internal']
colors = ['red', 'blue']

# Number of bootstrap iterations
n_bootstraps = 1000

# Function to compute percentages of each pathway type
def compute_percentages(data):
    counts = {pathway: np.count_nonzero(data == pathway) for pathway in pathways}
    total = len(data)
    return [(counts[pathway] / total) * 100 for pathway in pathways]

# Loop through each sheet, generate plot, and save
for count, file_name in enumerate(file_names, start=1):
    # Load the specific sheet
    df = pd.read_excel(file_name)
    
    # Extract pathway data from the DataFrame
    all_pathway_data = df['Pathway'].tolist()
    
    # Bootstrap sampling for confidence intervals across the entire dataset
    bootstrap_samples = []
    for _ in range(n_bootstraps):
        # Resample the entire data
        bootstrap_sample = np.random.choice(all_pathway_data, size=len(all_pathway_data), replace=True)
        # Compute percentages for the bootstrap sample
        percentages = compute_percentages(bootstrap_sample)
        bootstrap_samples.append(percentages)
    
    # Calculate standard deviation across bootstrap samples
    bootstrap_std = np.std(bootstrap_samples, axis=0)
    
    # Calculate actual percentages in the original data
    counts = {pathway: all_pathway_data.count(pathway) for pathway in pathways}
    total = len(all_pathway_data)
    percentages = [(counts[pathway] / total) * 100 for pathway in pathways]
    
    # Create the plot with specified settings
    fig, ax = plt.subplots(figsize=(24, 24))  # Larger figure size (24x24 inches)
    
    # Define error bar properties
    error_bar_settings = {'elinewidth': 8, 'capsize': 30}  # Thicker error bars
    
    # Bar plot with specified colors and error bar settings
    bars = ax.bar(pathways, percentages, yerr=bootstrap_std, color=colors, error_kw=error_bar_settings)
    
    # Set x and y labels with larger font size
    ax.set_ylabel('Path Probability', fontsize=80)
    
    # Set title with larger font size
    ax.set_title(f'Unbinding Path Ligand {count}', fontsize=80, pad=60)
    
    # Set consistent y-axis limit for all plots
    ax.set_ylim(0, 115)
    
    # Set font size for x and y ticks
    ax.tick_params(axis='x', labelsize=80)
    ax.tick_params(axis='y', labelsize=80)
    
    # Adjust layout and save the figure with specified name
    plt.tight_layout()
    plot_filename = f"{file_name.lower().split('_')[0]}_plot.png"
    plt.savefig(plot_filename, dpi=300)
