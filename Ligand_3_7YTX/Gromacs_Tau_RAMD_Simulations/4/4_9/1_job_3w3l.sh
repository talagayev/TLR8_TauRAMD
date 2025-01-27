#!/bin/bash --login
#$ -cwd
#$ -o gro_gpu.$JOB_ID.out
#$ -N gro_gpu
#$ -j y
#SBATCH --job-name=7tyx_ramd
#SBATCH -t 2-00:00
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#$ -l h_rt=576000
#$ -pe mp 16
#$ -l gpus=2

module rm ompi
module load gromacs/ramd-2.0

gmx grompp -f gromacs_ramd_40kcal.mdp -c confout_1st_equil.gro -o 7tyx_4_Rep9_tauramd_run.tpr  -n index.ndx -p 7tyx_4.top  -maxwarn  2
gmx mdrun -s 7tyx_4_Rep9_tauramd_run.tpr  -c confout_4_9_Rep_tauramd.gro -x confout_4_9_Rep_tauramd.xtc -g 2nd_tauramd.log -maxh 160 > out

