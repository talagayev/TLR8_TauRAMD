#!/bin/bash --login
#$ -cwd
#$ -o gro_gpu.$JOB_ID.out
#$ -N mptest
#$ -j y
#$ -l h_rt=172800
#$ -pe mp 12

module load g09

g09 < DY3_h.gau > DY3_H.out
