#!/bin/bash --login
#$ -cwd
#$ -o gro_gpu.$JOB_ID.out
#$ -N gro_gpu
#$ -j y
#$ -l h_rt=172800
#$ -pe mp 16
#$ -l gpus=2

module rm ompi
module load gromacs/ramd-2.0

gmx grompp -f gromacs_ramd_40kcal.mdp -c confout_1st_equil.gro -o 3w3l_2_Rep18_tauramd_run.tpr  -n index.ndx -p processed.top  -maxwarn  2
gmx mdrun -s 3w3l_2_Rep18_tauramd_run.tpr  -c confout_2_18_Rep_tauramd.gro -x confout_2_18_Rep_tauramd.xtc -g 2nd_tauramd.log -maxh 160 > out
