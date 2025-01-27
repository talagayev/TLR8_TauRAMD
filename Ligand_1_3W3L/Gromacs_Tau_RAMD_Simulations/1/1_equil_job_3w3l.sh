#!/bin/bash --login
#$ -cwd
#$ -o gro_gpu.$JOB_ID.out
#$ -N gro_gpu
#$ -j y
#$ -l h_rt=360000
#$ -pe mp 2
#$ -l gpus=1

module rm ompi
module load gromacs/ramd-2.0

gmx grompp -f gromacs.mdp -c 3w3l.gro -o 3w3l0.tpr -p 3w3l.top -maxwarn  5 -n index.ndx
gmx mdrun -s 3w3l0.tpr -ntmpi 1 -ntomp 16 -maxh 24

