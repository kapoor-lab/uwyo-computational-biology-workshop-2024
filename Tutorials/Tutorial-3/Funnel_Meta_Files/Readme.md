## git clone
git clone https://github.com/kapoor-lab/uwyo-computational-biology-workshop-2024.git

## Activate Environment 
#open your terminal and execute the following commands
module load miniconda3/23.11.0

conda activate /pfs/tc1/project/biocompworkshop/software/conda-envs/biocomp-day3

jupyter-notebook

## load VMD
module use /project/biocompworkshop/ukapoor/codes/packages/

module load vmd/1.9.4a57

## plumed bin 
/project/biocompworkshop/software/conda-envs/biocomp-day3/bin/plumed