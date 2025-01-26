#!/bin/bash --login
#$ -cwd
#$ -o gro_gpu.$JOB_ID.out
#$ -N mptest
#SBATCH --job-name=GDO_gaus
#SBATCH -t 2-00:00
#SBATCH --cpus-per-task=12
#$ -j y
#$ -l h_rt=172800
#$ -pe mp 12

module load g16

g16 < GD0_true_H.gau > GD0_true_H.out
