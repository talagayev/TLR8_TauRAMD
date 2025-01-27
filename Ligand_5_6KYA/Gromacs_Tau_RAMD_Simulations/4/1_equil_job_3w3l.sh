#!/bin/bash --login
#$ -cwd
#$ -o gro_gpu.$JOB_ID.out
#$ -N gro_gpu
#$ -j y
#SBATCH --job-name=5wyx_ramd
#SBATCH -t 2-00:00
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#$ -l h_rt=720000
#$ -pe mp 2
#$ -l gpus=1

module rm ompi
module load gromacs/ramd-2.0

gmx grompp -f gromacs.mdp -c 6kya_4.gro -o 6kya0.tpr -p 6kya_4.top -maxwarn  5 -n index.ndx
gmx mdrun -s 6kya0.tpr -c confout_1st_equil.gro -x 1st_equil_run.xtc -g 1st_equil.log -ntmpi 1 -ntomp 16 -maxh 24

