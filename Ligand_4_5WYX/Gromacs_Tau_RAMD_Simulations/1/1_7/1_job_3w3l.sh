#!/bin/bash --login
#$ -cwd
#$ -o gro_gpu.$JOB_ID.out
#$ -N gro_gpu
#$ -j y
#$ -l h_rt=576000
#$ -pe mp 16
#$ -l gpus=2

module rm ompi
module load gromacs/ramd-2.0

gmx grompp -f gromacs_ramd_40kcal.mdp -c confout_1st_equil.gro -o 5wyx_1_Rep7_tauramd_run.tpr  -n index.ndx -p 5wyx_1.top  -maxwarn  2
gmx mdrun -s 5wyx_1_Rep7_tauramd_run.tpr  -c confout_1_7_Rep_tauramd.gro -x confout_1_7_Rep_tauramd.xtc -g 2nd_tauramd.log -maxh 160 > out

