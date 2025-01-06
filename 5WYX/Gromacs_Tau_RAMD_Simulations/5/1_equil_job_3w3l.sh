#!/bin/bash --login
#$ -cwd
#$ -o gro_gpu.$JOB_ID.out
#$ -N gro_gpu
#$ -j y
#$ -l h_rt=720000
#$ -pe mp 2
#$ -l gpus=1

module rm ompi
module load gromacs/ramd-2.0

gmx grompp -f gromacs.mdp -c 5wyx_5.gro -o 5wyx0.tpr -p 5wyx_5.top -maxwarn  5 -n index.ndx
gmx mdrun -s 5wyx0.tpr -c confout_1st_equil.gro -x 1st_equil_run.xtc -g 1st_equil.log -ntmpi 1 -ntomp 16 -maxh 24

