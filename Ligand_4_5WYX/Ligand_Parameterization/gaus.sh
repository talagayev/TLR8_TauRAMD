#!/bin/bash --login
#$ -cwd
#$ -o gro_gpu.$JOB_ID.out
#$ -N mptest
#$ -j y
#$ -l h_rt=172800
#$ -pe mp 12

module load g09

g09 < CU8_h.gau > CU8_H.out
