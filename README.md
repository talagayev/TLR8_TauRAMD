# TLR8_TauRAMD
This repository consists out of the content used in the publication "TBD" by Valerij Talagayev, Gerhard Wolber & Ariane Nunes Alves.

![Abstract_figure](https://github.com/user-attachments/assets/4a87db62-e2c6-4f49-9e3c-cd4f67639e03)

The repository includes the data for all 6 compounds, those being the agonist 1, the cationic antagonists 2 & 3 and the neutral antagonists 4-6 used during this research.

![Figure_1_paper_modified_19_11](https://github.com/user-attachments/assets/65e12726-3650-409d-b02a-c2bf9c78a74e)

The research consisted in the identification of the internal and external unbinding pathways for the TLR8 agonists and antagonists and the frequency of the unbinding paths that the certain groups
of the compounds underwent.

![image](https://github.com/user-attachments/assets/b10c81bd-5770-438b-b0d9-211c954ae279)

The folder for each ligand consists of the following data:
  1. Amber_Simulations - Data for the Amber simulations performed for each ligand before the GROMACS simulations
  2. Gromacs_Tau_RAMD_Simulations - Data for GROMACS equilibration simulations and the 𝜏RAMD simulations. The folder has five subfolders, each representing a replicate within which the data for 20 simulations lies.
In Addition the tauRAMD.py script is present, which was used to analyze the residence times for each replicate present in the files times.dat.
  3. Ligand_Parameterization - Data containing the parameterization for each ligand, with the parameterization being performed with Gaussian.
  4. Simulation_Analysis - Contains the files for the calculation of the Ligand 1 (3W3L) dihedral angle calculation
  5. Simulation_File_Preparation - Contains the files for the preparation of the protein and ligand for the Amber simulation, with the use of Ambertools.

